import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values #Features Independent Variables [Except Purachased column]
y = dataset.iloc[:,3].values #Dependent Variable. [Purachased column]