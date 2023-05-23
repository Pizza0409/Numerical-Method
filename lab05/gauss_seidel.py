#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from copy import deepcopy


# ##### Write the function for check the matrix is diagonally dominant

# In[10]:


def check_diagonally(a):
    # Find diagonal coefficients
    # diag = ...
    diag = np.diag(np.abs(a))                         #|aii|
    
    # Find row sum without diagonal coefficients
    # off_diag = ...
    off_diag = np.sum(np.abs(a), axis = 1) - diag     #axis = 1 -> row, sum of row of each rows

    if np.all(diag > off_diag):
        print("matrix is diagonally dominant")
    else:
        print("NOT diagonally dominant")


# ##### Wirte the funtion for Gauss-Seidel method

# In[16]:


def Gauss_Seidel(a, x, y, it, epsilon):
    converged = False
    x_old = np.zeros(a.shape[0])
    print("Iteration results") 
    print(" k,    x1,      x2,       x3 ")
    # You should to do...
    # Use the for loop to complete the iterative process
        # check if it is smaller than threshold 
        # assign the latest x value to the old value
    for i in range(it):                                                 #the most iteration number
        for j in range(a.shape[0]):                                     #how many rows
            sum = 0
            for k in range(a.shape[1]):                                 #how many cols
                if k != j:                                              #avoid diagonal elements
                    sum += a[j][k] * x[k]                               #Gauss–Seidel method
            x[j] = (y[j] - sum) / a[j][j]
        print(f" {i + 1}, {x[0]:.4f}, {x[1]:.4f}, {x[2]:.4f}")     
        if np.linalg.norm(x - x_old) < epsilon:                         #check if it is convergent
            converged = True
            break
        x_old = x.copy()                                                # assign the latest x value to the old value
              
    if converged:
        print('Converged')
    else:
        print("Didn't converged" )
        

    return x


# # Sample 1

# In[17]:


a = np.array([[5, -1, -3], [2, 9, 3], [2, 4, 8]])

check_diagonally(a)


# In[18]:


a = np.array([[5, -1, -3], [2, 9, 3], [2, 4, 8]])
x = np.zeros(a.shape[0])
y = np.array([14, 5, -8])

x = Gauss_Seidel(a, x, y, it=50, epsilon=0.0001)
print('')
print('Check')
print('my solve:',x)
x = np.linalg.solve(a, y)
print('np solve:',x)


# # Sample 2

# In[14]:


a = np.array([[12, 3, -5, 2], [1, 7, 3, 1], [3, 7, 13, -2], [-2, 2, 5, 20]])

check_diagonally(a)


# In[15]:


a = np.array([[12, 3, -5, 2], [1, 7, 3, 1], [3, 7, 13, -2], [-2, 2, 5, 20]])
x = np.zeros(a.shape[0])
y = np.array([10, 6, 3, 2])

x = Gauss_Seidel(a, x, y, it=50, epsilon=0.0001)
print('')
print('Check')
print('my solve:',x)
x = np.linalg.solve(a, y)
print('np solve:',x)


# In[ ]:





# In[ ]:




