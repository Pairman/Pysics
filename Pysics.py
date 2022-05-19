import decimal as decimal_module

def decimal(number=0):
    """
    Convert a number from number type to decimal.Decimal type.
    :param number: (number) The number to convert.
    :return: (decimal.Decimal) The number in decimal.Decimal form.
    """
    return number if type(number) is decimal_module.Decimal else decimal_module.Decimal(str(number))

def t_factor(number,precision=0):
    """
    Return the t factor at 0.683 probability for given degree of freedom and precision.
    :param number: (number) Degree of freedom starting from 2.
    :param precision: (number) The precision level. 0 by default for all set to 1 when number>=6, or 1 for t factor with 2 digits, or 2 for t factor with 5 digits.
    :return: (decimal.Decimal) The t factor for given degree of freedom and precision.
    """
    t_factors=[[0,0,1.84,1.32,1.20,1.14,1,1,1,1,1,1,1],[0,0,1.84,1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.05,1.03],[0,0,1.83741,1.32132,1.19691,1.14165,1.11053,1.09059,1.07674,1.06655,1.05875,1.05259,1.04759]]
    return decimal(t_factors[precision][number])
    
def minimum_correlation(number):
    """
    Return the minimum correlation for given degree of freedom.
    :param number: (number) Degree of freedom ranging from 3 to 20.
    :return: (decimal.Decimal) The minimum correlation for given degree of freedom and precision.
    """
    minimum_correlations=[0,0,0,1,0.99,0.959,0.917,0.874,0.834,0.798,0.765,0.735,0.708,0.684,0.661,0.641,0.623,0.606,0.59,0.575,0.561]
    return decimal(minimum_correlations[number])

class Dataset:
    """
    Dataset with multiple variables.
    :attr m: The number of variables.
    :attr n: The number of data pairs.
    :attr variables: Names of variables.
    :attr dataset: Variables as keys with its data as values.
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
    """
    def __init__(self):
        self.m,self.n,self.variables,self.dataset=0,0,list(),dict()
    def list(self):
        """
        Print all variable names and its values.
        """
        print([[self.m,self.variables],self.n])
        for variable,values in self.dataset.items():
            print("'{}' [{}".format(variable,values[0]),end='')
            for i in range(1,len(values)):
                print(',',values[i],end='')
            print(']')
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
        Remove an existing variable.
        :param variable: (str) Name of an existing variable.
        """
        self.dataset.pop(variable)
        self.m-=1
        self.variables=[self.dataset.keys()]
    def pop(self,*numbers):
        """
        Remove the number-th (starting from 1) data from all existing variables.
        :param numbers: (tuple(number,...)) Indexes of the data to remove.
        """
        numbers=tuple(number-1 for number in numbers)
        for variable in self.dataset.keys():
            self.dataset[variable]=[value for i,value in enumerate(self.dataset[variable]) if i not in numbers]
        self.n-=len(numbers)
    def pop_bad_data(self,variable,t_factor=decimal(1)):
        """
        Remove the bad data depending on an existing variable and t factor. Returns the indexes of the removed data.
        :param variable: (str) Name of an existing variable.
        :param t_factor: (number|decimal.Decimal) the t factor for converting sample standard deviation to population standard deviation.
        :return: (list(number,...)) Indexes of the removed data. 
        """
        sample_standard_deviation=self.sample_standard_deviation(variable)/t_factor
        absolute_deviation=[abs(value) for value in self.absolute_deviation(variable)]
        dataset=[self.dataset[variable][i] if absolute_deviation[i]<=3*sample_standard_deviation else None for i in range(self.n)]
        indexes_to_remove=[i for i,value in enumerate(dataset) if value==None]
        self.pop(*tuple(index+1 for index in indexes_to_remove))
        return [index+1 for index in indexes_to_remove]
    def update(self,variable,values):
        """
        Add a list of values of a new variable with the same length n.
        :param variable: (str) Name of the new variable.
        :param values: (list(decimal.Decimal|number,...)) Values of the variable.
        """
        if not self.n:
            self.n=len(values)
        self.dataset[variable]=[decimal(value) for value in values]
        self.m+=1
        self.variables=list(self.dataset.keys())
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
        if self.n==1:
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
        Return the slope of the line plotted by two existing variables using least square func.
        :param avariable: (str) Name of an existing variable as the independent variable.
        :param bvariable: (str) Name of an existing variable as the dependent variable.
        :return: (decimal.Decimal) The slope of the line plotted by the given variables.
        """
        return (self.product_mean(ivariable,dvariable)-self.arithmic_mean(ivariable)*self.arithmic_mean(dvariable))/(self.square_sum_mean(ivariable)-self.arithmic_mean(ivariable)*self.arithmic_mean(ivariable))
    def least_square_bias(self,ivariable,dvariable):
        
        """
        Return the bias of the line plotted by two existing variables using least square func.
        :param avariable: (str) Name of an existing variable as the independent variable.
        :param bvariable: (str) Name of an existing variable as the dependent variable.
        :return: (decimal.Decimal) The bias of the line plotted by the given variables.
        """
        return self.arithmic_mean(dvariable)-self.arithmic_mean(ivariable)*self.least_square_slope(ivariable,dvariable)
