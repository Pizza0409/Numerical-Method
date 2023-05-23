#!/usr/bin/env python
# coding: utf-8

# In[53]:


import random
from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.nrows = nrows
        self.ncols = ncols
        
        self.matrix = [] 
        
        for i in range(nrows):
            r = []
            for j in range(ncols):
                r.append(random.randint(0, 10))                   #random int from 0-10所以用randint
                
            self.matrix.append(r)
        pass
    
    def add(self, m):
        """return a new Matrix object after summation"""
        # Check two matrix are in the same size
        
        if(self.nrows != m.nrows or self.ncols != m.ncols):
            print('Error')
            return None
        
        # add self.matrix with m.matrix
        result = deepcopy(self)                                   #copy result form self
        
        for i in range(self.nrows):
            for j in range(self.ncols):
                result.matrix[i][j] += m.matrix[i][j]             #每一個元素相加
        
        pass
        
        return result

    def sub(self, m):
        """return a new Matrix object after substraction"""
        # Check two matrix are in the same size
        
        if(self.nrows != m.nrows or self.ncols != m.ncols):
            print('Error')
            return None
        
        # substraction self.matrix from m.matrix
        result = deepcopy(self)                                   #copy result form self
        
        for i in range(self.nrows):
            for j in range(self.ncols):
                result.matrix[i][j] -= m.matrix[i][j]             #每一個元素相減
                
        pass
    
        return result

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        # Check if the nrows of m is the same as ncols of self
        
        if(self.ncols != m.nrows):
            print('Error')
            return None
        
        # Multiply self.matrix and m.matrix
        result = Matrix(self.nrows, m.ncols)
        pass
    
        for i in range(self.nrows):
            for j in range(m.ncols):
                temp = 0                                           #定義一個要暫存的值的變數且每輪要重設
                for k in range(m.ncols):
                    temp = self.matrix[i][k] * m.matrix[k][j]      #將乘完的值丟進temp暫存
                result.matrix[i][j] = temp                         #將temp的值丟進result中
    
        return result

    def transpose(self):
        """return a new Matrix object after transpose"""
        # Tranpose
        result = Matrix(self.nrows, self.ncols)                    #此處的self = mul的result所以不用再算一次mul
        pass
        
        for i in range(self.nrows):
            for j in range(self.ncols):
                result.matrix[j][i] = self.matrix[i][j]            #row col互換
        
        return result
    
    def display(self):
        """Display the content in the matrix"""
        
        for i in self.matrix:                                      #將整個矩陣print出來
            print(i)
                
        pass


# In[54]:


a_rows = int(input("Enter A matrix's rows:"))
a_cols = int(input("Enter A matrix's cols:"))
print("Matrix A({}, {}):".format(a_rows, a_cols))
A = Matrix(a_rows, a_cols)
A.display()
    
b_rows = int(input("Enter B matrix's rows:"))
b_cols = int(input("Enter B matrix's cols:"))
print("Matrix B({}, {}):".format(b_rows, b_cols))
B = Matrix(b_rows, b_cols)
B.display()
    
print("="*10, 'A + B', "="*10)
result = A.add(B)
if result is not None:
    result.display()
    
print("="*10, 'A - B', "="*10)
result = A.sub(B)
if result is not None:
    result.display()

print("="*10, 'A * B', "="*10)
result = A.mul(B)
if result is not None:
    result.display()

print("="*5, "the transpose of A*B", "="*5)
result = result.transpose()
if result is not None:
    result.display()


# 

# In[ ]:





# In[ ]:




