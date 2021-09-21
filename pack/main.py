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

# Using sklearn GMM to fit
nclusters = 5 # set the desired number of clusters here
gmm = GaussianMixture(n_components=nclusters)
gmm.fit(X_pca)

# predict the cluster for each data point
y_cluster_gmm = gmm.predict(X_pca)
# y_cluster_gmm

# Changing the categorical labels PRAD, BRCA, KIRC, LUAD, COAD into arbitrary integers
y_id = pd.Categorical(labels['Class']).codes # these nodes would be different from 

score = adjusted_rand_score(y_id, y_cluster_gmm)
print(score)


# To visualize the results and store clusters
df_plot = X_pca.copy() # copies the PCA columns
df_plot['ClusterGMMs'] = y_cluster_gmm # adds the GMM clusters 
df_plot['Class'] = y_id # adds actual labels as reference

# this is the result from the analysis which stores the PCs and cluster/predicted and original labels
df_plot.to_csv('./output/labels_classes.csv',index=False)
df_plot['Cancer'] = y

# plot: original with labels
fig=plt.figure()
fig, ax = plt.subplots()
groups = df_plot.groupby('Cancer')
for name, group in groups:
    ax.plot(group.PC1, group.PC2, marker='o', linestyle='', ms=3, 
label=name)
ax.legend(numpoints=1)
#ax.set_ylim((0, 500000))
plt.draw()
plt.savefig('./TCGA_plot_Class.png', dpi=300, bbox_inches='tight')

# plot: predicted with clusters

fig=plt.figure()
fig, ax = plt.subplots()
groups = df_plot.groupby('ClusterGMMs')
for name, group in groups:
    ax.plot(group.PC1, group.PC2, marker='o', linestyle='', ms=3, 
label=name)
ax.legend(numpoints=1)
#ax.set_ylim((0, 500000))
plt.draw()
plt.savefig('./TCGA_plot_GMMs.png', dpi=300, bbox_inches='tight')
        
        
