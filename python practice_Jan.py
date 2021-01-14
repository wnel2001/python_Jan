#!/usr/bin/env python
# coding: utf-8

# In[2]:


#7. Pandas


# In[3]:


import pandas as pd


# In[5]:


X1=pd.Series([0.1, 0.2, 0.3, 0.4], index=['a','b','c','d']) # can provide index on vector which is different with numpy
print(X1)


# In[8]:


print(X1.index) #series' index
print(X1.values) #series' value


# In[9]:


print(X1['a':'c']) # materials' slicing - index slicing from a to c
print(X1[0:3])     # materials' slicing - index slicing from line  0~2     


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




