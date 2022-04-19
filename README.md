# Pysics
Statistic tools for calculating data from physical experiments, in Python.

# Functions
## decimal()
Convert a number from number type to decimal.Decimal type.

# Classes
## Dataset
Dataset with multiple variables.
### Attributions
:attr m: The number of variables.
:attr n: The number of data pairs.
:attr variables: Names of variables.
:attr dataset: Variables as keys with its data as values.
### Methods
:method list(): Print all variable names and its values.
:method rename(): Rename an existing variable.
:method remove(): Remove and return an existing variable.
:method update(): Add a list of values of a new variable with the same length n.
:method maximum(): Return the minimum of an existing variable.
:method minimum(): Return the minimum of an existing variable.
:method range(): Return the range of an existing variable.
:method sum(): Return the sum of an existing variable.
:method square_sum(): Return the square sum of an existing variable.
:method product(): Return a list of the product of two existing variables.
:method continued_product(): Return the product of an existing variable.
:method median(): Return the median of an existing variable.
:method arithmic_mean(): Return the arithmic mean of an existing variable.
:method geometric_mean(): Return the geometric mean of an existing variable.
:method square_sum_mean(): Return the square sum mean of an existing variable.
:method product_mean(): Return the product mean of two existing variables.
:method successive_minus(): Return the successive minus of an existing variable.
:method sample_variance(): Return the sample variance of an existing variable.
:method population_variance(): Return the population variance of an existing variable.
:method covariance(): Return the covariance of two existing variables.
:method absolute_deviation(): Return the absolute variance of an existing variable.
:method relative_deviation(): Return the relative variance of an existing variable.
:method sample_standard_deviation(): Return the sample standard deviation of an existing variable.
:method population_standard_deviation(): Return the population standard deviation of an existing variable.
:method correlation(): Return the correlation of two existing variables.
:method least_square_slope(): Return the slope of the line plotted by two existing variables using least square method.
:method least_square_bias(): Return the bias of the line plotted by two existing variables using least square method.
