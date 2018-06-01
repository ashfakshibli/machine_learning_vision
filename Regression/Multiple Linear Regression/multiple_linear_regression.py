"""
Created on Thu May 31 16:11:34 2018

@author: Ashfak Md. Shibli
"""
# Multiple Linear Regression

#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values #Matrix
y = dataset.iloc[:,4].values #Vector


# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3]) # Encoding fourth column

onehotencoder = OneHotEncoder(categorical_features = [3]) # ctrl + i for inspect class
X = onehotencoder.fit_transform(X).toarray() # Encode dummy variables


# Avoiding the dummy variable trap
X = X[:,1:]

#splitting dataset into training and test data set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train) """


# Fitting Multiple Linear Regression to the Training set

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1) # Added column of ones in front of X
X_opt = X[:, [0, 3]] # Written all columns explicitly becuase we will remove one by one
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() # Ordinary Least Squares. Step 2 (fit)
regressor_OLS.summary() # Check step 3
























