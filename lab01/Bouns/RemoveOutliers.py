#!/usr/bin/env python
# coding: utf-8

# In[25]:


move = int(input('Enter the number of the largest and smallest to remove '))


# In[26]:


x = list()


# In[27]:


while True:
    val = input('Enter the value : ')
    
    if(val == 'q' or val == 'Q'):
        break
        
    x.append(val)


# In[28]:


for i in range(0, len(x)):
    x[i] = int(x[i])
print('The original list is ', x)


# In[29]:


# bubble sort
l = len(x)
for i in range(l - 1):
    for j in range(l - i -1):
        if(x[j] > x[j + 1]):
            temp = x[j + 1]
            x[j + 1] = x[j]
            x[j] = temp
            
y = x

temp = -move

item = list()
for i in range(0, move):
    item.append(y[i])

a = -1    

while(-1 >= temp):

    item.append(y[a])
    a -= 1
    temp += 1


# In[31]:


del x[0:move]

temp = -move

while(-1 >= temp):
    del x[-1]
    temp += 1

print('The data with the outliers removed : ', x)


# 

# In[32]:


print('The outliers : ', item)


# In[ ]:





# In[ ]:




