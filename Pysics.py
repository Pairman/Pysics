import decimal as decimal_module
from random import sample

def decimal(number=0):
    """
    Convert a number from number type to decimal.Decimal type.
    :param number: (number) The number to convert.
    :return: (decimal.Decimal) The number in decimal.Decimal form.
    """
    if type(number) is decimal_module.Decimal:
        return number
    return decimal_module.Decimal(str(number))

class Dataset:
    """
    Dataset with multiple variables.
    :attr m: The number of variables.
    :attr n: The number of data pairs.
    :attr variables: Names of variables.
    :attr dataset: Variables as keys with its data as values.
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
    """
    def __init__(self):
        self.m,self.n,self.variables,self.dataset=0,0,list(),dict()
        for variable in self.variables:
            self.dataset.update({variable:list()})
    def list(self):
        """
        Print all variable names and its values.
        """
        for i in range(self.m):
            print(self.variables[i],'    ',self.dataset[self.variables[i]])
    def rename(self,ovariable,nvariable):
        """
        Rename an existing variable.
        :param ovariable: (str) Name of an existing variable.
        :param nvariable: (str) Name of the new variable name.
        """
        self.dataset[nvariable]=self.dataset.pop(ovariable)
        self.variables=[self.dataset.keys()]
    def remove(self,variable):
        """
        Remove and return an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (list(decimal.Decimal,...)) The removed variable with its values.
        """
        self.dataset.pop(variable)
        self.m-=1
    def update(self,variable,values):
        """
        Add a list of values of a new variable with the same length n.
        :param variable: (str) Name of the new variable.
        :values: (list(decimal.Decimal|number,...)) Values of the variable.
        """
        if not self.n:
            self.n=len(values)
        self.dataset[variable]=[decimal(value) for value in values]
        self.m+=1
        self.variables=[self.dataset.keys()]
    def maximum(self,variable):
        """
        Return the maximum of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) Maximum of the given variable.
        """
        return decimal(max(self.dataset[variable]))
    def minimum(self,variable):
        """
        Return the minimum of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) Minimum of the given variable.
        """
        return decimal(min(self.dataset[variable]))
    def range(self,variable):
        """
        Return the range of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (tuple(decimal.Decimal,decimal.Decimal)) The range of the given variable.
        """
        return self.minimum(variable),self.maximum(variable)
    def sum(self,variable):
        """
        Return the sum of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The sum of the given variable.
        """
        return decimal(sum(self.dataset[variable]))
    def square_sum(self,variable):
        """
        Return the square sum of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The square sum of the given variable.
        """
        return decimal()+sum([decimal(value)*decimal(value) for value in self.dataset[variable]])
    def product(self,avariable,bvariable):
        """
        Return a list of the product of two existing variables.
        :param avariable: (str) Name of an existing variable.
        :param bvariable: (str) Name of an existing variable.
        :return: (list(decimal.Decimal,...)) The product of the given variables.
        """
        return [decimal(avalue)*decimal(bvalue) for avalue,bvalue in zip(self.dataset[avariable],self.dataset[bvariable])]
    def continued_product(self,variable):
        """
        Return the product of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The product of the given variable.
        """
        product=decimal(1)
        for value in self.dataset[variable]:
            product*=decimal(value)
        return product
    def median(self,variable):
        """
        Return the median of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The median of the given variable.
        """
        return decimal(sorted(self.dataset[variable])[(self.n-1)//2]) if self.n%2 else decimal(sorted(self.dataset[variable])[self.n//2]+sorted(self.dataset[variable])[(self.n//2)-1])/decimal(2)
    def arithmic_mean(self,variable):
        """
        Return the arithmic mean of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The arithmic mean of the given variable.
        """
        return self.sum(variable)/decimal(self.n)
    def geometric_mean(self,variable):
        """
        Return the geometric mean of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The geometric mean of the given variable.
        """
        continued_product=self.continued_product(variable)
        return continued_product.__pow__(1/decimal(self.n))
    def square_sum_mean(self,variable):
        """
        Return the square sum mean of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The square mean of the given variable.
        """
        return self.square_sum(variable)/decimal(self.n)
    def product_mean(self,avariable,bvariable):
        """
        Return the product mean of two existing variables.
        :param avariable: (str) Name of an existing variable.
        :param bvariable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The product mean of the given variables.
        """
        return sum(self.product(avariable,bvariable))/decimal(self.n)
    def successive_minus(self,variable):
        """
        Return the successive minus of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The successive minus of the given variable.
        """
        if self.n is 1:
            return decimal()
        return decimal(sum(self.dataset[variable][2+self.n//2:])-sum(self.dataset[variable][:self.n//2]))/decimal((self.n//2)*(self.n//2)) if self.n%2 else decimal(sum(self.dataset[variable][self.n//2:])-sum(self.dataset[variable][:self.n//2]))/decimal((self.n//2)*(self.n//2))
    def sample_variance(self,variable):
        """
        Return the sample variance of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The sample variance of the given variable.
        """
        if self.n<=1:
            return decimal(0)
        return (self.square_sum(variable)-(self.sum(variable)*self.sum(variable))/decimal(self.n))/decimal(self.n-1)
    def population_variance(self,variable):
        """
        Return the population variance of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The population variance of the given variable.
        """
        return (self.square_sum(variable)-(self.sum(variable)*self.sum(variable))/decimal(self.n))/decimal(self.n)
    def covariance(self,avariable,bvariable):
        """
        Return the covariance of two existing variables.
        :param avariable: (str) Name of an existing variable as the independent variable.
        :param bvariable: (str) Name of an existing variable as the dependent variable.
        :return: (decimal.Decimal) The covariance of the given variables.
        """
        return sum([avalue*bvalue for avalue,bvalue in zip(self.absolute_deviation(avariable),self.absolute_deviation(bvariable))])/decimal(self.n)
    def absolute_deviation(self,variable):
        """
        Return the absolute variance of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return : (list(decimal.Decimal,...)) List of the absolute variance of the given variable.
        """
        return [decimal(value)-self.arithmic_mean(variable) for value in self.dataset[variable]]
    def relative_deviation(self,variable):
        """
        Return the relative variance of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return : (list(decimal.Decimal,...)) List of the relative variance of the given variable.
        """
        return [value/decimal(self.n) for value in self.absolute_deviation(variable)]
    def sample_standard_deviation(self,variable):
        """
        Return the sample standard deviation of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The sample standard deviation variance of the given variable.
        """
        sample_variance=self.sample_variance(variable)
        return sample_variance.__pow__(decimal(0.5))
    def population_standard_deviation(self,variable):
        """
        Return the population standard deviation of an existing variable.
        :param variable: (str) Name of an existing variable.
        :return: (decimal.Decimal) The population standard deviation of the given variable.
        """
        population_variance=self.population_variance(variable)
        return population_variance.__pow__(decimal(0.5))
    def correlation(self,ivariable,dvariable):
        """
        Return the correlation of two existing variables.
        :param variable: (str) Name of two existing variables.
        :return: (decimal.Decimal) The correlation of the given variables.
        """
        return self.covariance(ivariable,dvariable)/(self.population_standard_deviation(ivariable)*self.population_standard_deviation(dvariable))
    def least_square_slope(self,ivariable,dvariable):
        """
        Return the slope of the line plotted by two existing variables using least square method.
        :param avariable: (str) Name of an existing variable as the independent variable.
        :param bvariable: (str) Name of an existing variable as the dependent variable.
        :return: (decimal.Decimal) The slope of the line plotted by the given variables.
        """
        return (self.product_mean(ivariable,dvariable)-self.arithmic_mean(ivariable)*self.arithmic_mean(dvariable))/(self.square_sum_mean(ivariable)-self.arithmic_mean(ivariable)*self.arithmic_mean(ivariable))
    def least_square_bias(self,ivariable,dvariable):
        
        """
        Return the bias of the line plotted by two existing variables using least square method.
        :param avariable: (str) Name of an existing variable as the independent variable.
        :param bvariable: (str) Name of an existing variable as the dependent variable.
        :return: (decimal.Decimal) The bias of the line plotted by the given variables.
        """
        return self.arithmic_mean(dvariable)-self.arithmic_mean(ivariable)*self.least_square_slope(ivariable,dvariable)
