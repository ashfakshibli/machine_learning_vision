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
