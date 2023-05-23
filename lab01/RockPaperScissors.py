#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


cmp = random.randint(1, 3)


# In[3]:


if(cmp == 1):
    cmp = 'r'
elif(cmp == 2):
    cmp = 'p'
else:
    cmp = 's'


# In[4]:


l = 0
w = 0
t = 0


# In[5]:


print('Welocome to ROCK, PAPER, SCISSORS game!')


# In[6]:


while True:
    player = input('Enter your move: (r)ock (p)aper (s)cissors')
    if(player == cmp):
        print('It is a tie!')
        t += 1
    elif(player == 'r'):
        if(cmp == 'p'):
            print('You lose!')
            l += 1
        else:
            print('You Win!')
            w += 1
    elif(player == 'p'):
        if(cmp == 's'):
            print('You lose!')
            l += 1
        else:
            print('You Win!')
            w += 1
    elif(player == 's'):
        if(cmp == 'r'):
            print('You lose!')
            l += 1
        else:
            print('You Win!') 
            w += 1
    
    if(w == 1):
        break
    else:    
        print('You have ', t,' ties and ' , l, 'losses' )
    


# In[ ]:





# In[ ]:





# In[ ]:




