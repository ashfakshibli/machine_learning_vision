# Regression Template

#import dataset

dataset = read.csv('Position_Salaries.csv')
dataset = dataset[,2:3]

#splitting dataset into training and test data set
#install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Purchased, SplitRatio = 0.8) #for training set split TRUE means observation goes to training set. False means test set
# training_set = subset(dataset, split== TRUE)
# test_set = subset(dataset, split== FALSE)

# Feature scaling
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])


# Fitting Polynomial Regression to the dataset
#Create your own regressor



# Predicting a new result 
y_pred = predict(regressor, data.frame(Level = 6.5))


# Visualizing the Regression Model results
# install.packages('ggplot2')
library(ggplot2)

x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
  
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  # geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
  #           color = 'blue') +
  ggtitle('Truth or Bluff (Regression Model)') +
  xlab('Level') +
  ylab('Salary')




