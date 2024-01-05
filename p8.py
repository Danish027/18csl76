from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris_dataset = load_iris()
targets = iris_dataset.target_names

# Print class labels with their corresponding numerical value
print("Class : number")
for i in range(len(targets)):
    print(targets[i], ':', i)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"])

# Initialize the KNeighborsClassifier with 1 neighbor
kn = KNeighborsClassifier(1)

# Train the classifier
kn.fit(X_train, y_train)

# Predictions and evaluation
for i in range(len(X_test)):
    x_new = np.array([X_test[i]])  # Get the test instance
    prediction = kn.predict(x_new)  # Predict the class

    # Print actual and predicted classes
    print("Actual:[{0}] [{1}], Predicted:{2} {3}".format(y_test[i], targets[y_test[i]], prediction, targets[prediction]))

# Print accuracy of the model on the test data
print("\nAccuracy: ", kn.score(X_test, y_test))
