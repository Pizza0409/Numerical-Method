#!/usr/bin/env python
# coding: utf-8

# ### import the module you need first

# In[17]:


import numpy as np


# ## step1. 
# #### Construct a numpy array represent the equations.
# #### the coefficients,answers and augmented matrix of each equation need to be stored separately.

# In[18]:


"""
example:
 
5y-7z = 7        | 0 5 -7 7 |
4x-z = 8      -> | 4 0 -1 8 |
x-y+z = 9        | 1 -1 -1 9 |
"""

coe = np.array([[0, 5, -7], [4, 0, -1], [1, -1, -1]])          #係數
ans = np.array([7, 8, 9])                                      #答案

augmented_matrix = np.column_stack((coe, ans)).astype(float)  #增廣矩陣，且有可能是float

for i, row in enumerate(augmented_matrix):                    #列出矩陣
    equation = "  ".join([f"{coe[i][j]}{var}" for j, var in enumerate(["x", "y", "z"]) if coe[i][j] != 0])
    print(f"{equation} = {ans[i]}  |  {row}")


# ## step2. 
# ### Before doing gauss elimination,
# ### we need to check if the first element([0,0]) of the augmented matrix is zero or not.
# ### If the first element is zero,
# ### we need to find another row whose first element isn't zero,and change them.

# In[ ]:





# In[19]:


#test:step2
#print the new augment matrix

if augmented_matrix[0][0] == 0:                  # check if the first element([0,0]) of the augmented matrix is zero or not.
    for i in range(1, len(augmented_matrix)):    # find the first element in row != 0
        if augmented_matrix[i][0] != 0:
            augmented_matrix[[0, i]] = augmented_matrix[[i, 0]]    #swap
            break

print("The new augmented matrix:")
for i in augmented_matrix:
    print(i)


# ## step3. gauss elimination
# 
# #### print the matrix after  gauss elimination

# In[ ]:





# In[20]:


nrows, ncols = augmented_matrix.shape

for i in range(nrows):
    pivot = augmented_matrix[i][i]                           #即將要被消除=0的主對角線的數
    for j in range(i+1, nrows):
        factor = augmented_matrix[j][i] / pivot              #找出它跟前幾列的factor  
        augmented_matrix[j] -= factor * augmented_matrix[i]  
        

print(augmented_matrix)


# ## step4. LU decomposition(bonus)
# 
# ## if you don't want to submit bouns,you don't need to do  step4 and step5

# In[ ]:





# In[21]:


#print L and U

n = coe.shape[0]      #n = how many rows
L = np.zeros((n, n))
U = np.zeros((n, n))
P = np.eye(n)

for i in range(n):
    pivot_row = i + np.argmax(np.abs(coe[i:, i])) #Find pivot
    coe[[i, pivot_row]] = coe[[pivot_row, i]]     #Swap rows
    L[[i, pivot_row]] = L[[pivot_row, i]]
    P[[i, pivot_row]] = P[[pivot_row, i]]
    L[i][i] = 1                                   #diagonal elements = 1 in L
    for j in range(i, n):                         #Doolittle Algorithm
        U[i][j] = coe[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
    for j in range(i+1, n):
        L[j][i] = (coe[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
        
print(L)
print(U)


# ## step5. check the ansewer of LU(bonus)
# 
# please use the function in scipy.linalg to check your answer
# 
# the documentatin of scipy.linalg :
# https://docs.scipy.org/doc/scipy/reference/linalg.html

# In[22]:


import scipy.linalg as la


# In[23]:


P, L, U = la.lu(coe)
print(L)
print(U)


# In[ ]:




