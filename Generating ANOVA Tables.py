#!/usr/bin/env python
# coding: utf-8

# In[21]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

from sklearn import linear_model


# In[3]:


data = pd.read_csv(r'Desktop/PlantGrowth.csv')


# In[4]:


data.boxplot('weight', by='group')


# In[15]:


mod = ols('weight ~ group', data=data).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)


# In[16]:


# GoodReads Regression ANOVA Table Using statsmodel


# In[17]:


data = pd.read_excel(r'Desktop/GoodReads_Reddit_And_Site_Data.xlsx')


# In[20]:


mod = ols('GoodReadsScore ~ RedditPostPerception + CommentCount + UpvoteRatio + GoodReadsPositivityRatio', data=data).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)


# In[22]:


# GoodReads Regression ANOVA Table Using sklearn


# In[25]:


df = pd.read_excel(r'Desktop/GoodReads_Reddit_And_Site_Data.xlsx')


# In[26]:


X = df[['RedditPostPerception','CommentCount', 'UpvoteRatio', 'GoodReadsPositivityRatio']]
Y = df['GoodReadsScore']


# In[27]:


regr = linear_model.LinearRegression()
regr.fit(X, Y)


# In[28]:


print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


# In[29]:


New_RedditPostPerception = 1
New_CommentCount = 16
New_UpvoteRatio = 0.85
New_GoodReadsPositivityRatio = 0.93
print('Predicted GoodReads Score: \n', regr.predict([[New_RedditPostPerception, New_CommentCount, New_UpvoteRatio, New_GoodReadsPositivityRatio]]))


# In[30]:


X = sm.add_constant(X)


# In[31]:


model = sm.OLS(Y, X).fit()
predictions = model.predict(X)


# In[32]:


print_model = model.summary()
print(print_model)


# In[33]:


# sklearn provides a more similar output to STATA -- might be best to use as a default 


# In[34]:


# as expected, comment count is statistically insignificant


# In[ ]:


# from here, would need to rerun and compare AIC/BIC (or R-Square, because it is the same model type) ...
# ... in order to determine which model best firts the data

