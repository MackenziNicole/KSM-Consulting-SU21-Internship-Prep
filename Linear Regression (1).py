#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.linear_model import LinearRegression


# In[2]:


x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])


# In[3]:


print(x)


# In[4]:


print(y)


# In[5]:


model = LinearRegression()


# In[6]:


model.fit(x, y)


# In[7]:


model = LinearRegression().fit(x, y)


# In[8]:


r_sq = model.score(x, y)


# In[9]:


print('coefficient of determination:', r_sq)


# In[10]:


print('intercept:', model.intercept_)


# In[11]:


print('slope:', model.coef_)


# In[12]:


new_model = LinearRegression().fit(x, y.reshape((-1, 1)))


# In[13]:


print('intercept:', new_model.intercept_)


# In[14]:


print('slope:', new_model.coef_)


# In[15]:


y_pred = model.predict(x)


# In[16]:


print('predicted response:', y_pred, sep='\n')


# In[17]:


y_pred = model.intercept_ + model.coef_ * x


# In[18]:


print('predicted response:', y_pred, sep='\n')


# In[19]:


x_new = np.arange(5).reshape((-1, 1))


# In[20]:


print(x_new)


# In[21]:


y_new = model.predict(x_new)


# In[22]:


print(y_new)


# In[23]:


# Multiple Regression


# In[24]:


x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)


# In[25]:


print(x)


# In[26]:


print(y)


# In[27]:


model = LinearRegression().fit(x, y)


# In[28]:


r_sq = model.score(x, y)


# In[29]:


print('coefficient of determination:', r_sq)


# In[30]:


print('intercept:', model.intercept_)


# In[31]:


print('slope:', model.coef_)


# In[32]:


y_pred = model.predict(x)


# In[33]:


print('predicted response:', y_pred, sep='\n')


# In[34]:


y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1)


# In[35]:


print('predicted response:', y_pred, sep='\n')


# In[36]:


x_new = np.arange(10).reshape((-1, 2))


# In[37]:


print(x_new)


# In[38]:


y_new = model.predict(x_new)


# In[39]:


print(y_new)

