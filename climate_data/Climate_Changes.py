#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#date formatting
import matplotlib.dates as mdates
get_ipython().run_line_magic('matplotlib', 'inline')

#data collected from https://www7.ncdc.noaa.gov/CDO/cdoselect.cmd?datasetabbv=GSOD&countryabbv&georegionabbv


# In[2]:


# This data is only 6 days out of the month; the website keeps crashing. Code should work, but we can get
# more data when I find a workaround later. This is daily mean temp. 
climate_data = pd.read_csv("jonkoping_climate_data.txt",  delimiter = ",")
climate_clean = climate_data.drop(['STN---', 'WBAN ','  ', '   DEWP', '  .1', '  SLP  ', '  .2', '  STP  ', 
                                   '  .3', ' VISIB', '  .4', '  WDSP', '  .5', ' MXSPD', '  GUST', '   MAX  ', 
                                   '  MIN  ', 'PRCP  ', 'SNDP ', ' FRSHTT', 'Unnamed: 22'], 
                                  axis = 1)
climate_clean.columns = ['date', 'temp']

print(climate_clean.head(10), '\n', climate_clean.shape)


# In[3]:


# Extracting year from date column 
year = np.zeros(climate_clean.shape[0])
index = 0
for i in climate_clean['date']:
    curr_year = int(i/10000)
    year[index] = int(curr_year)
    index = index+1

print(year)


# In[4]:


# Extracting month from date Column
month = np.zeros(climate_clean.shape[0])
index = 0
for i in climate_clean['date']:
    curr_month = int((i/100)%100)
    month[index] = int(curr_month)
    index = index+1

print(month)


# In[5]:


# inputting month and year into main df, dropping date
climate_clean['year'] =  year
climate_clean['month'] =  month 
climate_clean = climate_clean.drop('date', axis = 1)

print(climate_clean.head(10), '\n', climate_clean.shape)


# In[8]:


# Extracting monthly average temperature 
years = np.arange(np.min(climate_clean['year']),2020)
months = np.arange(1,13)
index = 0 
df_length = int(climate_clean.shape[0] / 6) 
monthly_avg_temp = np.zeros((df_length,3))
for y in years:
    for m in months:
        temp_temp = climate_clean[(climate_clean['month'] == m) & (climate_clean['year'] == y)]['temp'] 
        monthly_avg_temp[index, 0] = y
        monthly_avg_temp[index, 1] = m 
        monthly_avg_temp[index, 2] = np.mean(temp_temp)
        index =  index + 1
        
monthly_avg_temp = pd.DataFrame(monthly_avg_temp).dropna()
monthly_avg_temp.columns =  ['year', 'month', 'mean temp']
monthly_avg_temp.head(7)


# In[25]:



Column1 = monthly_avg_temp['year']
Column2= np.ones(len(Column1))
A = np.column_stack((Column1, Column2))
columnC = np.array(monthly_avg_temp['mean temp'])
C = np.transpose(columnC)

ps = np.linalg.lstsq(A, C, rcond=None)[0]
p1 = ps[0]
p2 = ps[1]

# Create predicted y values for a range of x values
xhat = np.arange(min(monthly_avg_temp['year']), 
                 max(monthly_avg_temp['year'])+1)
yhat = p1*xhat + p2


# In[ ]:





# In[28]:




fig = plt.figure(figsize = (8,8))

ax = fig.add_subplot(111)
ax.set(title = 'Mean Temperature over Time',
       xlabel = 'Year',
       ylabel = 'Temperature',
       xlim = [1977,2020])

ax.scatter(monthly_avg_temp['year'], 
           monthly_avg_temp['mean temp'])

ax.plot(xhat, yhat, color="red")

plt.legend()
plt.show()


# In[ ]:




