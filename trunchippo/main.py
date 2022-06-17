import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
import glob
import os

#Building a path variable to the data in my personal C: drive.
#To play with the Harvard Dataverse numerical data yourself, you'll have to cater the path
#variable to wherever you place this folder in your computer.
path = r'C:/fMRI/trunchippoL/data'

#Building a dataframe based on a pandas.read_csv method.
#Takes files ending in csv from your specified path, so be sure to have nothing but the data you want to look at.
dfs = [pd.read_csv(filename, index_col=None, header=0) for filename in os.listdir(path)]

#Concatenates or fuses the two data tables into a single dataframe.
df = pd.concat(dfs, axis=0, ignore_index=True)

#Allows you to view rows of your dataframe beyond the default of 5.
df.head()

#Useful print function for displaying dataframe
print(df.describe)

#Useful print function for displaying column names
print(df.columns)

#Here, we import sk.learn cluster to build our k-means clusters.
import sklearn.cluster as cluster

#Fit the axes to a cluster of value n.
kmeans = cluster.KMeans(n_clusters=3, init="k-means++")
kmeans = kmeans.fit(df[['Degree', 'GlobalEfficiency']])

#Adds a Clusters column to the dataframe.
df['Clusters'] = kmeans.labels_

#Assigns the cluster-clad dataframe its own csv file.
df.to_csv('DegreeEfficiencyClusters.csv', index=False)

#Plot
sns.scatterplot(x="Degree", y="GlobalEfficiency", hue='Clusters', data=df)
plt.show()