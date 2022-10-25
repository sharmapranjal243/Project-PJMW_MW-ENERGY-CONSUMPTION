#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore") 


# In[14]:


model=pickle.load(open('regresser.pkl',"rb"))
data=pd.read_csv("C:\\Users\\nehas\\PJMW_MW.csv")
last_7days=pd.read_csv('last_7days.csv',header=None)


# In[21]:


st.title("Forecast power consumption data")
st.sidebar.subheader('Select the number of days to forecast from 2018-aug-4')
days=st.sidebar.number_input('Days',min_value=1,step=1)


# In[25]:


z=last_7days
z=np.array(z[0].tail(7))

for i in range(0,days):
    r=z[-7:]
    r=np.array([r])
    ranf_f=model.predict(r)
    z=np.append(z,ranf_f)
    i=+1
future_pred=z[-days:]


# In[28]:


future=pd.date_range(start='4/8/2018',periods=days,tz=None,freq='D')
future_df=pd.DataFrame(index=future)
future_df['future_energy']=future_pred.tolist()
future_df


# In[29]:


st.sidebar.write(f"Power consumption for{days}th day")
st.sidebar.write(future_df[-1:])
st.write(f"Power consumption  dorecasted till {days}")

st.write(future_df)


# In[ ]:





# In[ ]:





# In[ ]:




