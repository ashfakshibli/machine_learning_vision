# Data Preprocessing Template
#import dataset

dataset = read.csv('Data.csv')
# dataset = dataset[,2:3]

#splitting dataset into training and test data set
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8) #for training set split TRUE means observation goes to training set. False means test set
training_set = subset(dataset, split== TRUE)
test_set = subset(dataset, split== FALSE)

# Feature scaling
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])