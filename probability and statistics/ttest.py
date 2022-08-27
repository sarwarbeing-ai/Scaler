# Importing Required Libraries
from math import sqrt
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from scipy.stats import sem
from scipy.stats import t
import numpy as np
def independent_ttest(data1, data2):
    '''
    input:
    data1 -> contains a python list signifying first data distribution
    data2 -> contains a python list signifying second data distribution
    output:
    t_stat -> a float value signifying the t_stat value
    p -> a float value signifying the p value
    '''
    t_stat = 0.0
    p = 0.0
    # YOUR CODE GOES HERE
    m1=mean(data1)
    m2=mean(data2)
    s1=np.std(data1,ddof=1)
    s2=np.std(data2,ddof=1)
    t_stat=(m1-m2)/sqrt(s1**2/len(data1)+s2**2/len(data2))
    df=len(data1)+len(data2)-2
    p=t.cdf(t_stat,df)*2
    # Your code ends here
    return t_stat, p
