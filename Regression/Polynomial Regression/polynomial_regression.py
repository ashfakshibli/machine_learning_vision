# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:05:45 2018

@author: Ashfak Md. Shibli
"""

# Polynomial Regression

# Polynomial regression is still a linear regression because the coefficients can be expressed linearly.

# Here regressors are not linear regressor.

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values # Is a matrix
y = dataset.iloc[:,2].values  #is a vector

"""
#splitting dataset into training and test data set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""

#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train) """


