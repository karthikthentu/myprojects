#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[2]:





# In[10]:


df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/housing.csv')


# In[30]:


df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv')
df


# In[14]:


few_cols=['diagnosis','radius_mean','texture_mean','perimeter_mean','area_mean']


# In[19]:


new_df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv',usecols=few_cols)
new_df


# In[17]:


few_cols


# In[20]:


new_df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv',header=None)
new_df


# In[21]:


new_names=['abc','def']


# In[22]:


new_df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv',header=None,names=new_names)


# In[28]:


new_df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv',skiprows=2)


# In[29]:


new_df


# In[31]:


df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv')


# In[44]:


df=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv',nrows=100,usecols=['id','diagnosis','radius_mean','texture_mean'])
df


# In[48]:


print(df.shape)


# In[49]:


df2=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv')
df2


# In[53]:


for x in ["Unnamed: 32"]:
    df2[x].fillna("Remote", inplace=True)
    


# In[54]:


df2


# In[55]:


for x in ["Unnamed: 32"]:
    df2[x].fillna("NaN",inplace=True)


# In[56]:


df2


# In[57]:


df1=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv')
df1


# In[58]:


df1=pd.read_csv('C:/Users/sidda/OneDrive/Desktop/data.csv',header=None)
df1


# In[60]:


df2=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data2.csv",header=None)
df2[]


# In[68]:


column_names=['id','diagnosis','radius_mean','texture_mean','perimeter_mean','area_mean']


# In[67]:


df2=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data.csv",nrows=100)
df2


# In[80]:


df2=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data.csv")
df2


# In[81]:


df2.head()


# In[84]:


df2.shape


# In[87]:


df2.isna()


# In[88]:


df2.isna().sum()


# In[96]:


Total_nan=df2['Unnamed: 32'].isna().sum()
Total_nan


# In[101]:


print("The total number of Not available entries in the df2 dataframe are:",Total_nan)


# In[105]:


df2.head()


# In[109]:


df2=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data.csv")
df2


# In[111]:


df2.loc[df2['radius_mean']>20, 'radius_mean']='Good'
df2


# In[115]:


df2=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data.csv")
df2


# In[117]:


df2.loc[df2['radius_mean']<15,'radius_mean']='Bad'
df2


# In[118]:


df2=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data.csv")
df2


# In[119]:


df2.loc[(df2['radius_mean']>10)&(df2['radius_mean']<20),'radius_mean']='Good'
df2


# In[127]:


df2['radius_mean'].value_counts()['Good']


# In[132]:


import pandas as pd


# In[133]:


import matplotlib as plt


# In[137]:


df2.plot()


# In[140]:


df2.plot.bar()


# In[141]:


df2.plot.hist()


# In[142]:





# In[143]:


df2=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data.csv")
df2


# In[151]:


df2['diagnosis_values']=pd.Series(['Red'if category=='M' else 'Green'if category=='B' else 'Blue' 
                                   for category in df2['diagnosis']],index=df2.index)


# In[152]:


df2['radius_mean_values']=pd.Series(['Pass'if score>20 else 'low' for score in df2['radius_mean']],index=df2.index)


# In[147]:


df2.columns.tolist()


# In[156]:


df2.isna()['Unnamed: 32']


# In[163]:


df2['Unnamed: 32'].isna().sum()


# In[198]:


df3=df2


# In[166]:


df3


# In[168]:


df3['Unnamed: 32'].fillna(100,inplace=True)
df3


# In[169]:


import numpy as np


# In[170]:


df3['Unnamed: 32'].replace(100,np.nan,inplace=True)


# In[172]:


df3.head()


# In[174]:


df3['Unnamed: 32'].fillna(100,inplace=True)
df3.head()


# In[175]:


df3['Unnamed: 32'].replace(100,np.nan,inplace=True)
df3


# In[178]:


df3['index']=df3.index
df3.drop('index',axis=1,inplace=True)


# In[189]:


#Adding index as a column
df3['Index']=df3.index
df3.head()


# In[190]:


#Dropping column
df3.drop('Index',axis=1,inplace=True)


# In[191]:


df3.head()


# In[192]:


#reset index
df3.reset_index(inplace=True)


# In[197]:


df3.head()


# In[194]:


df3.drop('index',axis=1,inplace=True)
df3.head()


# In[199]:


df3.reset_index(inplace=True)


# In[200]:


df3


# In[201]:


df3.drop(['level_0','index'],axis=1,inplace=True)


# In[202]:


df3.head()


# In[203]:


df3.reset_index(inplace=True)


# In[204]:


df3.head()


# In[205]:


df3.reset_index(inplace=True)
df3.head()


# In[207]:


df3.drop(['level_0','index'],axis=1,inplace=True)


# In[208]:


df3.head()


# In[209]:


df3.reset_index(inplace=True)
df3.head()


# In[210]:


#read all data except one column
df4=df3.loc[:,df3.columns!='index']
df4.head()


# In[211]:


df3.reset_index(inplace=True)
df3.head()


# In[215]:



df4=df3.loc[:,df3.columns!='level_0']
df4.head()


# In[219]:


df4.head()


# In[221]:


df5=df4.loc[:,df4.columns!='level_0']
df5.head()


# In[222]:


df5=pd.read_csv("C:/Users/sidda/OneDrive/Desktop/data.csv",na_values=missing_value)
df5


# In[223]:


df5['Empty_column']=None
df5


# In[224]:


df5.drop('Empty_column',axis=1,inplace=True)
df5.head()


# In[225]:


df5['Empty_column']=" "
df5


# In[226]:


df5.head()


# In[228]:


df5['Empty_column2']=np.nan
df5.head()


# In[235]:


df5.head()


# In[ ]:





# In[ ]:





# In[ ]:




