#!/usr/bin/env python
# coding: utf-8

# In[1]:


# define parameter for plt
linewidths = [0.5, 1.0, 2.0, 4.0]
linestyles = ['-', '--', '-.', ':']
markers = ['+', 'o', '*', 's', '.', '1', '2', '3', '4']
markersizecolors = [(4, "white"), (8, "red"), (12, "yellow"), (16, "lightgreen")] #tuple in list


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 5)
y = np.ones_like(x)                                        # return an array of 1 with the same shape and type as x. 
def axes_settings(fig, ax, title, ymax):
    ax.set_xticks([])                                      # No xticks
    ax.set_yticks([])                                      # No yticks
    ax.set_ylim(0, ymax+1)
    ax.set_title(title)

fig, axes = plt.subplots(1, 4, figsize=(16,3))             # create a figure with 1 row X 4 columns subfig 
# Line width
for n, linewidth in enumerate(linewidths):                 # enumerate returns index and value
    axes[0].plot(x, y + n, color="blue", linewidth=linewidth)  #線粗為題目定義的  
axes_settings(fig, axes[0], "linewidth", len(linewidths))

# Line style
for n, linestyle in enumerate(linestyles):
    axes[1].plot(x, y + n, color =  "blue", linewidth = 3, linestyle = linestyles[n])     #線粗自訂，線的形式則為題目規定的
axes_settings(fig, axes[1], "linestyle", len(linestyles))    


# Marker
for n, marker in enumerate(markers):
    axes[2].plot(x, y + n, color =  "blue", linewidth = 0, markersize = 4, marker = markers[n])     #不需要線所以linewidth = 0，makersize自訂，maker則為題目定義
axes_settings(fig, axes[2], "makers", len(markers))

# marker size/color
for n, (size, color) in enumerate(markersizecolors):
    axes[3].plot(x, y + n, color =  "blue", marker = 'o', linewidth = 0, markersize = size, markerfacecolor = color)    #不需要線所以linewidth = 0，maker範例裡用 o，makersize與makerfacecolor則為題目定義
axes_settings(fig, axes[3], "markersizecolors", len(markersizecolors))    
    


# In[ ]:





# In[ ]:




