#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt


# In[7]:


def my_central_diff(y, h):
    # y : compute function
    # h : step size
    
    n = len(y)
    d = np.zeros(n)                          #creat a zero matrix which the len is y
    
    for i in range(1, n - 1):              
        d[i] = (y[i+1] - y[i-1]) / (2 * h)   # f'(xi) = (f(xj+1) - f(xj-1))/2h
        
    return d


# In[8]:


# step size
h = 0.1
# define grid
x = np.arange(0, 2*np.pi, h)
# compute function
y = np.sin(x)
# compute vector of forward differences
central_diff = my_central_diff(y, h)[1:-1]
# compute corresponding grid
x_diff = x[1:-1]
# compute exact solution
exact_solution = np.cos(x_diff)

# Plot solution
plt.figure(figsize = (12, 8))
plt.plot(x_diff, central_diff, "-", label = "Finite difference approximation", lw=8)
plt.plot(x_diff, exact_solution, label = "Exact solution", lw=4)
plt.legend()
plt.show()

# Compute max error between
# numerical derivative and exact solution
max_error = max(abs(exact_solution - central_diff))
print('The maximum error is', max_error)


# ### ---Bonus---

# In[9]:


# define step size
h = 1
# define number of iterations to perform
iterations = 15
# list to store our step sizes
step_size = []
# list to store max error for each step size
max_error = []


for i in range(iterations):
    # halve the step size
    h /= 2
    # ...to be continued
    # define grid
    x = np.arange(0, 2*np.pi, h)
    # compute function
    y = np.sin(x)
    # compute vector of forward differences
    central_diff = my_central_diff(y, h)[1:-1]
    # compute corresponding grid
    x_diff = x[1:-1]
    # compute exact solution
    exact_solution = np.cos(x_diff)
    step_size.append(h)
    max_error.append(max(abs(exact_solution - central_diff)))   # define the max error between exact sol and central sol

# produce log-log plot of max error versus step size
plt.figure(figsize = (12, 8))
plt.loglog(step_size, max_error, "v", markersize=14)
plt.xlabel('step size', fontsize=20)
plt.ylabel('max error', fontsize=20)
plt.show()


# In[ ]:





# In[ ]:




