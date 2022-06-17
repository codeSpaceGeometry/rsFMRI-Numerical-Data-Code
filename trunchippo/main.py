import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
import glob
import os

path = r'C:/fMRI/trunchippo/data'

os.listdir(path)

dfs = [pd.read_csv(filename, index_col=None, header=0) for filename in os.listdir(path)]


df = pd.concat(dfs, axis=0, ignore_index=True)

df.head(22)

print(df.describe)

print(df.columns)

sns.pairplot(data=df, vars=['Degree', 'GlobalEfficiency'], hue="Degree")

plt.show()

import sklearn.cluster as cluster

kmeans = cluster.KMeans(n_clusters=3, init="k-means++")
kmeans = kmeans.fit(df[['Degree', 'GlobalEfficiency']])

print(kmeans.cluster_centers_)

df['Clusters'] = kmeans.labels_

print(df.head(22))

print(df['Clusters'].value_counts())

df.to_csv('DegreeEfficiencyClusters.csv', index=False)

sns.scatterplot(x="Degree", y="GlobalEfficiency", hue='Clusters', data=df)
#plt.show()

