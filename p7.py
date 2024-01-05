import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

# Reading data from CSV file
data = pd.read_csv('data/ex.csv')
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))  # Combining the two features into a 2D array

# Displaying the whole dataset
print("x: ", X)
print('Graph for whole dataset')
plt.scatter(f1, f2, c='black')
plt.show()

# K-Means Clustering
kmeans = KMeans(2)  # Initializing KMeans with 2 clusters
labels = kmeans.fit(X).predict(X)  # Fitting the model and predicting labels
print("labels for kmeans:", labels)
print('Graph using Kmeans Algorithm')
plt.scatter(f1, f2, c=labels)  # Plotting the clusters
centroids = kmeans.cluster_centers_  # Getting the centroids
print("centroids:", centroids)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='red')  # Plotting the centroids
plt.show()

# Gaussian Mixture Model (EM Algorithm)
gmm = GaussianMixture(2)  # Initializing GMM with 2 components
labels = gmm.fit(X).predict(X)  # Fitting the model and predicting labels
print("Labels for GMM: ", labels)
print('Graph using EM Algorithm')
plt.scatter(f1, f2, c=labels)  # Plotting the clusters
plt.show()
