## Comparison Among Models #

# R Squared #

SSres = SUM(y_i = y)^2
SStot = SUM(y_i = y_avg)^2

R^2 = 1 - SSres/SStot

R^2 shows how much your model fits with the dataset

# Adjusted R^2 #

R^2 bigger is better.

Problem when variable increases.

R^2 - Goodness of fit

If variable increases R^2 never will increase.

That's why adjusted R^2 comes in  business.

Adj R^2 = 1 - (1- R^2)*(n-1)/(n-p-1)

Adj R^2 increased then model fit more efficiently.

# Understanding Co-effiecients #

If positive co-related to dependent variable (Profit).

Don't give conclusion with magnitude of Co-effiecients. Can say with per unit(same unit)