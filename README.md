# Pysics
Statistic tools for calculating data from physical experiments, in Python.
This module uses the `decimal` module.
Open source under GPU/GPL v3 license.

# Functions
## decimal()
Convert a number from number type to decimal.Decimal type.
## t_factor()
Return the t factor at 0.683 probability for given degree of freedom and precision.
## minimum_correlation()
Return the minimum correlation for given degree of freedom.

# Classes

## Dataset
Dataset with multiple variables.

### Attributions
:attr m: The number of variables.

:attr n: The number of data pairs.

:attr variables: Names of variables.

:attr dataset: Variables as keys with its data as values.

### Methods
:func list(): Print all variable names and its values.

:func rename(): Rename an existing variable.

:func remove(): Remove an existing variable.

:func pop(): Remove the number-th (starting from 1) data from all existing variables.

:func pop_bad_data(): Remove the bad data depending on an existing variable and t factor. Returns the indexes of the removed data.

:func update(): Add a list of values of a new variable with the same length n.

:func maximum(): Return the minimum of an existing variable.

:func minimum(): Return the minimum of an existing variable.

:func range(): Return the range of an existing variable.

:func sum(): Return the sum of an existing variable.

:func square_sum(): Return the square sum of an existing variable.

:func product(): Return a list of the product of two existing variables.

:func continued_product(): Return the product of an existing variable.

:func median(): Return the median of an existing variable.

:func arithmic_mean(): Return the arithmic mean of an existing variable.

:func geometric_mean(): Return the geometric mean of an existing variable.

:func square_sum_mean(): Return the square sum mean of an existing variable.

:func product_mean(): Return the product mean of two existing variables.

:func successive_minus(): Return the successive minus of an existing variable.

:func sample_variance(): Return the sample variance of an existing variable.

:func population_variance(): Return the population variance of an existing variable.

:func covariance(): Return the covariance of two existing variables.

:func absolute_deviation(): Return the absolute variance of an existing variable.

:func relative_deviation(): Return the relative variance of an existing variable.

:func sample_standard_deviation(): Return the sample standard deviation of an existing variable.

:func population_standard_deviation(): Return the population standard deviation of an existing variable.

:func correlation(): Return the correlation of two existing variables.

:func least_square_slope(): Return the slope of the line plotted by two existing variables using least square func.

:func least_square_bias(): Return the bias of the line plotted by two existing variables using least square func.
