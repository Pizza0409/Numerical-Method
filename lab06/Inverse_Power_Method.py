#!/usr/bin/env python
# coding: utf-8

# In[84]:


import numpy as np
from numpy.linalg import eig
from numpy.linalg import inv


# In[85]:


def inverse_normalize(x):
    # factor fac is the maximum absoulute value of x
    fac = abs(x).max()
    if fac == abs(x.min()):          #check if x最大的絕對值是否在x中是負數
        fac = fac * -1
    x_n = x / fac
    
    return fac, x_n


# In[86]:


def inverse_power_method(a, x):
    # The subtraction of the lambda_0 and the lambda_1 must be less than 1e-30
    lambda_0 = 1
    a_inv = inv(a)                             # define a_inv is the inverse of the matrix a
    iter = 1000                                # iteration time
    y = 0
    
    for i in range(iter):
        x = np.dot(a_inv, x)                   #A^-1 dot x0
        lambda_1, x = inverse_normalize(x)
        if(abs(lambda_0 - lambda_1) < 10 ** (-30)):
            break
    lambda_1 = 1 / lambda_1
    
    return lambda_1, x


# ### Sample 1

# In[87]:


x = np.array([1, 1])
a = np.array([[0, 2],[2, 3]])
lambda_1, x = inverse_power_method(a, x)
print("The Minimum Eigenvalue:", lambda_1)
print("Eigenvector:", x)


# In[88]:


# compare with numpy

a = np.array([[0, 2],[2, 3]])

value, vector = eig(a)
print("E-value:", value)
print("E-vector:\n", vector)


# ### Sample 2

# In[89]:


x = np.array([1, 1, 1])
a = np.array([[1, 5, 2],[2, 4, 3],[2, 1, 6]])
lambda_1, x = inverse_power_method(a, x)
print("The Minimum Eigenvalue:", lambda_1)
print("Eigenvector:", x)


# In[90]:


# compare with numpy

a = np.array([[1, 5, 2],[2, 4, 3],[2, 1, 6]])

value, vector = eig(a)
print("E-value:", value)
print("E-vector:\n", vector)


# In[ ]:





# In[ ]:




