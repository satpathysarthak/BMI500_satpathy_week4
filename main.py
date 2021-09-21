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


