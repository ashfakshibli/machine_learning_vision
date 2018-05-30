# @author: Ashfak Md. Shibli

# Simple Linear Regression

#import dataset

dataset = read.csv('Salary_Data.csv')
# dataset = dataset[,2:3]

#splitting dataset into training and test data set
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3) #for training set split TRUE means observation goes to training set. False means test set
training_set = subset(dataset, split== TRUE)
test_set = subset(dataset, split== FALSE)

# Feature scaling
# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

# Fitting Simple Linear Regression to the Training Set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

#summary(regressor) at console to see regressor

# lm(formula = Salary ~ YearsExperience, data = training_set)
# 
# Residuals:
#   Min      1Q  Median      3Q     Max 
# -7325.1 -3814.4   427.7  3559.7  8884.6 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept)        25592       2646   9.672 1.49e-08 ***
#   YearsExperience     9365        421  22.245 1.52e-14 ***  (meaning high statistical significance)
#   ---
#   Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
# 
# Residual standard error: 5391 on 18 degrees of freedom
# Multiple R-squared:  0.9649,	Adjusted R-squared:  0.963 
# F-statistic: 494.8 on 1 and 18 DF,  p-value: 1.524e-14 (lower the p value indepent variable is more significant. less than 5% is a threshold)


# Predicting the Test set results
y_pred = predict(regressor, newdata = test_set)

#Visualize the Training set results
install.packages('ggplot2')
#library(caTools)
ggplot() +
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             color = 'red') +
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            color = 'blue') +
  ggtitle('Salary vs Experience (Training Set)') +
  xlab('Years of experience') +
  ylab('Salary')
  

