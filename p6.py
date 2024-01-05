import pandas as pd
import numpy as np

# Load the dataset
mush = pd.read_csv("data/mushrooms.csv")
mush = mush.replace('?', np.nan)  # Replace '?' with NaN
mush.dropna(axis=1, inplace=True)  # Drop columns with NaN values

# Define target (class) and features
target = 'class'
features = mush.columns[mush.columns != target]
target_classes = mush[target].unique()

# Splitting the data into training and test sets
test = mush.sample(frac=.3)  # 30% data for testing
mush = mush.drop(test.index)  # Remaining 70% for training

# Calculating conditional probabilities
cond_probs = {}
target_class_prob = {}
for t in target_classes:
    mush_t = mush[mush[target] == t][features]
    target_class_prob[t] = float(len(mush_t) / len(mush))
    class_prob = {}
    
    for col in mush_t.columns:
        col_prob = {}
        for val, cnt in mush_t[col].value_counts().iteritems():
            pr = cnt / len(mush_t)
            col_prob[val] = pr
        class_prob[col] = col_prob
    cond_probs[t] = class_prob

# Function to calculate probabilities for each class
def calc_probs(x):
    probs = {}
    for t in target_classes:
        p = target_class_prob[t]
        for col, val in x.iteritems():
            try:
                p *= cond_probs[t][col][val]
            except KeyError:
                p = 0
        probs[t] = p
    return probs

# Function to classify a single instance
def classify(x):
    probs = calc_probs(x)
    max_prob = max(probs.values())
    max_class = max(probs, key=probs.get)
    return max_class

# Evaluating the classifier on training data
correct_predictions = [classify(mush.loc[i, features]) == mush.loc[i, target] for i in mush.index]
print(sum(correct_predictions), "correct of", len(mush))
print("Training Accuracy:", sum(correct_predictions) / len(mush))

# Evaluating the classifier on test data
correct_predictions_test = [classify(test.loc[i, features]) == test.loc[i, target] for i in test.index]
print(sum(correct_predictions_test), "correct of", len(test))
print("Test Accuracy:", sum(correct_predictions_test) / len(test))
