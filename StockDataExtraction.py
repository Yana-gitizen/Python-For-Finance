#!/usr/bin/env python
# coding: utf-8

# In[3]:


import yfinance as yf


# In[4]:


import os


# In[5]:


tickers = ["TATASTEEL.NS", "GAIL.NS"]


# In[6]:


output_folder = "D:/Python for Finance"


# In[7]:


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# In[8]:


for ticker in tickers:
    stock_data = yf.download(ticker, start="2020-01-01", end="2025-01-01")
    file_path = os.path.join(output_folder, f"{ticker}.csv")
    stock_data.to_csv(file_path)
print(f"Saved data for {ticker} to {file_path}")


# In[ ]:




