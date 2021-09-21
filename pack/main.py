# import some libraries
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# The pancancer dataset in the datsets directory
# tar gunzip the tar.gz file 
data = pd.read_csv('./datasets/TCGA-PANCAN-HiSeq-801x20531/data.csv')
labels = pd.read_csv('./datasets/TCGA-PANCAN-HiSeq-801x20531/labels.csv')

# preparing the dataset 
data = data.drop('ID', axis=1) # removing the ID column and keeping gene expression. Each gene is a variable.
X = data # X stores the matrix of gene expression data 
y = labels["Class"] # y stores the labels associated with that (PRAD, BRCA, KIRC, LUAD, COAD)

# scaling the datasets by columns to avoid 
scalefn = preprocessing.StandardScaler()
scalefn.fit(X)
X_scaled_array = scalefn.transform(X) # the values are transformed to a scaled value
X_scaled = pd.DataFrame(X_scaled_array, columns = X.columns)  

# Dimension Reduction
ndimensions = 5 # enter the number of Principle components that you want
seed = 0 # seed set to 0 
pca = PCA(n_components=ndimensions, random_state=seed)
pca.fit(X_scaled)
X_pca_array = pca.transform(X_scaled) # this array stores the 
#X_pca = pd.DataFrame(X_pca_array, columns=['PC1','PC2']) 
X_pca = pd.DataFrame(X_pca_array, columns=['PC1','PC2','PC3','PC4','PC5']) # Add the column names according to the ndimensions

