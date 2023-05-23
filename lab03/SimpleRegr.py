#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def least_squares_fit(x, y):
    x_ave = np.mean(x) 
    y_ave = np.mean(y) # np.mean() return mean value of given array
    # [hint] np.dot: inner product for 1D array; matrix multiplication for 2D array
    num = np.sum((x - x_ave) * (y - y_ave))   #分子 = (xi - x_avg)(yi - y_avg)
    den = np.sum((x - x_ave) ** 2)            #分母 = (x - x_avg ^ 2)
    beta1 = num / den
    beta0 = y_ave - beta1 * x_ave
    
    return beta0, beta1
    
    pass


# In[6]:


#for testing your function of computing beta

#report beta0 and beta1
X = np.array([1, 2, 3, 4])
Y = np.array([9, 13, 14, 18])
beta0, beta1 = least_squares_fit(X, Y)
print('From home-made linear regression model')
print('beta0 =', beta0)
print('beta1 =', beta1)


# In[38]:


#plot the line with matplotlib

import matplotlib.pyplot as plt

#1. [hint]plot points by plt.scatter (parameter setting: c=marker color='blue', s=marker size=20) 
plt.scatter(X, Y, c = 'blue', s = 20)        #散布圖
#2. [hint]plot line by plt.plot(parameter setting: lw=linewidth=3)
n = len(X)
x_fit = np.arange(X.min(), Y.min(), n)
y_fit = beta0 + beta1 * x_fit
plt.plot(x_fit, y_fit, linewidth = 3, color = 'red', markersize = 20)       #Fitting line

plt.show()


# In[ ]:




