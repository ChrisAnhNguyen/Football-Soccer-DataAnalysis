#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar




# In[4]:


df= pd.read_csv('RadarFix.csv')


# In[6]:


df.head()


# In[12]:


#get parameters
params=list(df.columns)
params=params[1:]
params


# In[13]:


#add ranges to list of tuple pairs
ranges = []
a_values = []
b_values = []

for x in params:
    a = min(df[params][x])
    a = a - (a*.25)
    
    b = max(df[params][x])
    b = b + (b*.25)
    
    ranges.append((a,b))
    
for x in range(len(df['Player'])):
    if df['Player'][x] == 'Declan Rice':
        a_values = df.iloc[x].values.tolist()
    if df['Player'][x] == 'Aurélien Tchouaméni':
        b_values = df.iloc[x].values.tolist()
        
a_values = a_values[1:]
b_values = b_values[1:]

values = [a_values,b_values]


# In[36]:


#title 


title = dict(
    title_name='Declan Rice',
    title_color = 'red',
    subtitle_name = 'West Ham United',
    subtitle_color = 'red',
    title_name_2='Aurélien Tchouaméni',
    title_color_2 = 'blue',
    subtitle_name_2 = 'AS Monaco',
    subtitle_color_2 = 'blue',
    title_fontsize = 18,
    subtitle_fontsize=15
)

endnote = 'Chris Anh Nguyen\ndata via FBREF / Statsbomb'
endnote='inspired by @mckayjohns/visualisation made by Chris Anh Nguyen/Data from Fbref'


# In[38]:


radar = Radar()

fig,ax1 = radar.plot_radar(ranges=ranges,params=params,values=values,
                         radar_color=['red','blue'],
                         alphas=[.75,.6],title=title,endnote=endnote,
                         compare=True)
plt.savefig("fig,ax1.png")


# SAME CODE FOR COMPARING RICE VS HAIDARA AND TCHOUAMENI VS HAIDARA

# In[20]:


#add ranges to list of tuple pairs
ranges = []
a_values = []
c_values = []

for x in params:
    a = min(df[params][x])
    a = a - (a*.25)
    
    c = max(df[params][x])
    c = c + (c*.25)
    
    ranges.append((a,c))
    
for x in range(len(df['Player'])):
    if df['Player'][x] == 'Declan Rice':
        a_values = df.iloc[x].values.tolist()
    if df['Player'][x] == 'Amadou Haidara':
        c_values = df.iloc[x].values.tolist()
        
a_values = a_values[1:]
c_values = c_values[1:]

values = [a_values,c_values]


# In[34]:


#title 


title = dict(
    title_name='Declan Rice',
    title_color = 'red',
    subtitle_name = 'West Ham United',
    subtitle_color = 'red',
    title_name_2='Amadou Haidara',
    title_color_2 = 'yellow',
    subtitle_name_2 = 'RB Leipzig',
    subtitle_color_2 = 'yellow',
    title_fontsize = 18,
    subtitle_fontsize=15
)

endnote = 'Chris Anh Nguyen\ndata via FBREF / Statsbomb'
endnote='inspired by @mckayjohns/visualisation made by Chris Anh Nguyen/Data from Fbref'

radar = Radar()

fig,ax2 = radar.plot_radar(ranges=ranges,params=params,values=values,
                         radar_color=['red','yellow'],
                         alphas=[.75,.6],title=title,endnote=endnote,
                         compare=True)
plt.savefig("fig,ax2.png")


# In[25]:



 #add ranges to list of tuple pairs
ranges = []
b_values = []
c_values = []

for x in params:
    b = min(df[params][x])
    b = b - (b*.30)
    
    c = max(df[params][x])
    c = c + (c*.30)
    
    ranges.append((b,c))
    
for x in range(len(df['Player'])):
    if df['Player'][x] == 'Aurélien Tchouaméni':
        b_values = df.iloc[x].values.tolist()
    if df['Player'][x] == 'Amadou Haidara':
        c_values = df.iloc[x].values.tolist()
        
b_values = b_values[1:]
c_values = c_values[1:]

values = [b_values,c_values] 


# In[35]:


#title 


title = dict(
    title_name='Aurélien Tchouaméni',
    title_color = 'blue',
    subtitle_name = 'AS Monaco',
    subtitle_color = 'blue',
    title_name_2='Amadou Haidara',
    title_color_2 = 'brown',
    subtitle_name_2 = 'RB Leipzig',
    subtitle_color_2 = 'brown',
    title_fontsize = 18,
    subtitle_fontsize=15
)

endnote = 'Chris Anh Nguyen\ndata via FBREF / Statsbomb'
endnote='inspired by @mckayjohns/visualisation made by Chris Anh Nguyen/Data from Fbref'

radar = Radar()

fig,ax3 = radar.plot_radar(ranges=ranges,params=params,values=values,
                         radar_color=['blue','brown'],
                         alphas=[.75,.6],title=title,endnote=endnote,
                         compare=True)
plt.savefig("fig,ax3.png")

