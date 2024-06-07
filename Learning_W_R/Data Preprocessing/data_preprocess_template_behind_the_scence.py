import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

#Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values #Features Independent Variables [Except Purachased column]
y = dataset.iloc[:,3].values #Dependent Variable. [Purachased column]

#What about missing data

from sklearn.preprocessing import Imputer  # Imputer class used to take care of missing data

imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0) # If axis=0, then impute along columns.
imputer.fit(X[:, 1:3]) # X[rows, column]. column = 1:3 column 1 to 2 (upper bound excluded) 
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # Encoding first column

onehotencoder = OneHotEncoder(categorical_features = [0]) # ctrl + i for inspect class
X = onehotencoder.fit_transform(X).toarray() # Encode dummy variables


#for dependent variable OneHot not needed. Beacause model will know it's categorical not weight
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


#splitting dataset into training and test data set
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


#feature scaling  Age and Salary is not having same scale. It will cause problem. Because of eclidean distance is dominated by salary.
# for scaling 1. Standarization 2. Normalization

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train) # first fitted with X_train then same transformation for X_test
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train) 

# do we need to apply on dependent variable?
#It's a classification problem (categorical variable). For regression dependent variable will need scaling as huge.
