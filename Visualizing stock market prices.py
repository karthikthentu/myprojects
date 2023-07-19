#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda  install plotly


# In[2]:


pip install cufflinks


# In[3]:


conda  install plotly


# In[4]:


import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader.data as web

import matplotlib as mpl
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly.offline as plyo
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()


# In[5]:


start=dt.datetime(2022,1,1)
end=dt.datetime(2022,9,1)
df=web.DataReader('AAPL','yahoo',start,end)
df


# In[8]:


plt.plot(df['Adj Close'])


# In[10]:


plt.plot(df['Close'],'orange')


# In[35]:


plt.figure(figsize=(10,6))
plt.plot(df['Close'],'darkgreen', lw=1.5,label='AAPL Close Price')
plt.plot(df['Open'],'navy', lw=1.5,label='AAPL Close Price')
plt.legend(loc=0)
plt.xlabel('Date')
plt.ylabel('price($)')
plt.ylim(100,200)
plt.grid(True)


# In[38]:


plt.figure(figsize=(10,6))
plt.plot(df['Close'],'darkgreen', lw=1.5,label='Close')
plt.plot(df['Volume'],'navy', lw=1.5,label='Volume')
plt.legend(loc=0)
plt.xlabel('Date')
plt.ylabel('price($)')
plt.title('A simple plot of prices')
plt.grid(True)


# In[42]:


fig,ax1= plt.subplots(figsize=(10,6))
ax1.plot(df['Close'],'darkgreen', lw=1.5,label='Close')
plt.ylabel('Price')
plt.xlabel('Date')
plt.grid(True)

ax2=ax1.twinx()
ax2.plot(df['Volume'],'navy', lw=1.5,label='Volume')
plt.ylabel('Volume')


# In[48]:


plt.figure(figsize=(10,6))
plt.subplot(211)
plt.plot(df['Close'],'darkgreen', lw=1.5,label='Close')
plt.ylabel('Price')
plt.grid(True)

plt.figure(figsize=(10,6))
plt.subplot(212)
#in 212 the first 2 numbers denotes the dimensions and the next number denotes the location
#2 X 1 grid and 2nd Position
plt.plot(df['Volume'],'navy', lw=1.5,label='Volume')
plt.ylabel('Volume')
plt.xlabel('Date')
plt.grid(True)


# In[49]:


df['Close'].plot()


# In[51]:


fig, axes = plt.subplots(nrows=2,ncols=1)
df['Close'].plot(figsize=(10,6),'navy',ax=axes[0])
axes[0].set_xlabel('')
axes[1].set_xticklabels('')
df['Volume'].plot(ax=axes[1])


# In[53]:


aapl= web.DataReader('AAPL','yahoo',start,end)['Adj Close']
googl=web.DataReader('Googl','yahoo',start,end)['Adj Close']
msft=web.DataReader('MSFT','yahoo',start,end)['Adj Close']


# In[57]:


df_sample=web.DataReader(['AAPL','GOOGL','MSFT','NFLX'],'yahoo',start,end)
df_sample


# In[ ]:





# In[ ]:





# In[55]:


d1=pd.merge(aapl,googl,on='Date',how='left')
stocks=pd.merge(d1,msft,on='Date',how='left')
stocks.columns=['AAPL','Googl','MSFT']
stocks


# In[59]:


returns=stocks.pct_change()
returns


# In[60]:


log_returns=np.log(stocks/stocks.shift(1))
log_returns


# In[61]:


log_returns.plot(figsize=(10,6))


# In[63]:


log_returns.cumsum().plot(figsize=(10,6))


# In[67]:


returns.loc['2022-8-1':'2022-9-1'].plot(figsize=(18,6), kind='bar')


# In[70]:


returns.plot(figsize=(10,6),kind='scatter', x='AAPL',y='GOOGL')


# In[73]:


ax=returns.plot(figsize=(10,6),kind='bar',color='blue',x='AAPL',y='GOOGL')
returns.plot(figsize=(10,6),kind='bar',color='red',x='AAPL',y='MSFT',ax=ax)
ax.set(ylabel='GOOGL(blue)','MSFT(red)')


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




