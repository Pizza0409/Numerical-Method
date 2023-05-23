#!/usr/bin/env python
# coding: utf-8

# In[65]:


class Map:
    def __init__(self, n, p):
        """
        initialize by n
        """
        self.n = n
        self.p = p
        
        if p == 1:
            """
            construct square inside the Map
            """
            self.matrix = [['*'] * n for i in range(n)]      #先全部放*
            for i in range(1, n-1):                          #第一跟最後都是***填滿，但中間是*ooo*之類的，所以range start from 1
                self.matrix[i][1:-1] = ['o'] * (n - 2)
        else:
            self.matrix = [[' '] * n for j in range(n)]
                
    def display(self):
        """
        display the map
        """
        for i in self.matrix:
            print(i)
        


# In[68]:


my_map = Map(5, 1)
my_map.display()


# In[ ]:





# In[ ]:




