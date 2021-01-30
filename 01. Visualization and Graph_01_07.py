#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 01) visualization and graph
# 01 The purpose
# 02 Practices


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[10]:


df = pd.read_csv('E:/2021/DataScientist/DS/3. Data Analysis and visualization/broadcast.csv', index_col = 0)
df


# In[11]:


df.plot()


# In[12]:


df.plot(kind='line')


# In[13]:


df.plot(y='KBS')


# In[14]:


df.plot(y=['KBS', 'JTBC'])


# In[15]:


df[['KBS', 'JTBC']]


# In[16]:


df[['KBS', 'JTBC']].plot()


# In[17]:


df['KBS']


# In[18]:


df[['KBS']]


# In[20]:


df['KBS'].plot()


# In[ ]:


# 03  Project : Economic growth according to the countries

# With Given data, draw the GDP's graphes for South Korea, America, UK, Germany, China, Japan


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd

df = pd.read_csv('E:/2021/DataScientist/DS/3. Data Analysis and visualization/GDP/gdp.csv', index_col=0)

df[['Korea_Rep', 'United_States', 'United_Kingdom', 'Germany', 'France', 'China', 'Japan']].plot()


# In[ ]:





# In[ ]:


# 04. growth analysis 
#    Among the countries shown in the graph, China is the largest growth rate, also US and Korea showed the largest gap 


# In[9]:


# 05. Bar chart
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd

df = pd.read_csv('E:/2021/DataScientist/DS/3. Data Analysis and visualization/sports.csv', index_col=0)
df


# In[10]:


df.plot()


# In[11]:


df.plot(kind='bar')


# In[12]:


df.plot(kind ='barh')  #h: horizontal 


# In[13]:


df.plot(kind= 'bar', stacked = True) #stack : accumulate (쌓아 올리다) 


# In[14]:


df['Female']


# In[18]:


df['Female'].plot(kind='bar', color=['red', 'blue', 'purple', 'green', 'lavender','orange'])   # showing only for Female data


# In[ ]:





# In[12]:


# 06. What kind of people work in Silicon valley?  
# There are Job_title, race_ethnicity, gender, count and percentage factors. 
# Draw the bar graph of the race distribution about male (managers). 

get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
df = pd.read_csv('E:/2021/DataScientist/DS/3. Data Analysis and visualization/silicon_valley_summary1.csv', index_col=0)
data = df[(df['Job_title']== 'Managers') & (df['gender'] =='Male') & (df['race_ethnicity'] != 'All')]
data.plot(kind='bar', x='race_ethnicity', y='count', color=['lavender', 'black', 'Yellow', 'Brown'])


# In[ ]:


# 07. pie graph


# In[43]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
df = pd.read_csv('E:/2021/DataScientist/DS/3. Data Analysis and visualization/broadcast.csv', index_col=0)
df


# In[44]:


df.loc[2017]


# In[47]:


df.loc[2017].plot(kind ='pie', autopct='%1.1f%%') # %1.1f%% means ?


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




