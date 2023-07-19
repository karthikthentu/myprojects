#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pokemon_data= pd.read_csv('pokemon_data.csv')


# In[3]:


poke=pokemon_data


# In[4]:


print(poke.head(5))


# In[5]:


print(poke['Name'])


# In[6]:


print(poke[['Name','Type 1','HP']])


# In[7]:


print(poke.head(4))


# In[8]:


print(poke.iloc[1])


# In[9]:


print(poke.iloc[21])


# In[10]:


print(poke.iloc[0,1])


# In[11]:


poke.dtypes


# In[12]:


poke.axes


# In[13]:


poke.iterrows()


# In[14]:


poke.loc[poke['Type 1']=='Grass']


# In[15]:


poke.sort_values(['Type 1','HP'],ascending=[0,1])


# In[16]:


poke['Total']= poke['HP']+poke['Attack']+poke['Defense']+poke['Sp. Atk']+poke['Sp. Def']+poke['Speed']


# In[17]:


poke.drop(columns=['Total'])


# In[18]:


poke_total=poke.iloc[:,4:10].sum(axis=1)


# In[19]:


poke


# In[20]:


cols=list(poke.columns)
cols


# In[21]:


poke.drop(columns='Total')
poke.head(5)


# In[22]:


cols=list(poke.columns.values)
cols


# In[23]:


poke['Total']=poke.iloc[:,4:10].sum(axis=1)


# In[24]:


poke=poke[cols[0:4]+[cols[-1]]+cols[4:12]]
poke


# In[25]:


poke.to_csv('Modified.csv')


# In[26]:


import re

poke.loc[poke['Name'].str.contains('Mega',regex=True)]

poke.loc[poke['Type 1'].str.contains('grass',flags=re.I,regex=True)]


# In[27]:


poke.loc[poke['Name'].str.contains('^pi[a-z]',flags=re.I,regex=True)]


# In[28]:


poke.loc[poke['Name'].str.contains('bul',flags=re.I,regex=True)]


# In[29]:


poke.head()


# In[31]:


df=poke


# In[51]:


df.loc[df['Type 1']=='Grass']
       


# In[49]:


df.loc[df['Type 2']=='Poison']


# In[55]:


df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)]


# In[75]:


new_df=df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison')& 
              (df['HP']>70)]
new_df=new_df.reset_index()
new_df


# In[76]:


new_df.reset_index(drop=True,inplace=True)


# In[78]:


new_df=new_df.reset_index(drop=True)


# In[79]:


new_df


# In[88]:


df.loc[df['Type 1']=='Flamer','Type 1']='Fire'
df


# In[89]:


df.loc[df['Type 1']=='Fire','legendary']= True


# In[90]:


df


# In[91]:


df=pd.read_csv('modified.csv')


# In[92]:


df


# In[94]:


df.loc[df['Total']>500, ['legendary','generation']] = ['TEST 1','TEST 2']
df


# In[95]:


df=pd.read_csv('modified.csv')
df


# In[101]:


df.groupby(['Type 1']).mean()


# In[105]:


df=df.drop(columns=['Unnamed: 0'])
df


# In[107]:


df.groupby(['Legendary']).mean()


# In[115]:


df.groupby(['Type 1']).count().sort_values('HP',ascending=False)


# In[121]:


a=[10,20,30]
total=0
for x in a:
    total=total+x
    print(total)


# In[123]:


f=['ab',1,2]


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




