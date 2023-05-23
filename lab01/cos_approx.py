#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


x = float(input('Please input x '))


# In[3]:


N = 2
cos = 1
sign = 1
while(N <= 24):
    sign = -sign
    cos += sign * x**N / math.factorial(N)
    N += 2

print(cos)


# In[ ]:




