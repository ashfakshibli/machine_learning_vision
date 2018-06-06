# Polynomial Regression
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

# Fitting Linear Regression to the dataset
lin_reg = lm(formula = Salary ~ .,
             data = dataset)

# Fitting Polynomial Regression to the dataset
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,
              data = dataset)


# Visualizing the linear Regression results
# install.packages('ggplot2')
library(ggplot2)

ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff (Linear Regression)') +
  xlab('Level') +
  ylab('Salary')

  

# Visualizing the Polynomial Regression results


ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff (Polynomial Regression)') +
  xlab('Level') +
  ylab('Salary')
