#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import folium


# In[2]:


dataset = pd.read_excel("Covid-red-orange-green-zones.xlsx")


# In[3]:


dataset.head(20)


# In[4]:


dataset.info()


# In[5]:


dataset.columns


# In[6]:


dir = dataset[ ['Latitude', 'Longitude'] ]


# In[7]:


dir = dir.values.tolist()


# In[8]:


type(dir)


# In[9]:


name = dataset["District"]


# In[10]:


zones = dataset[['greenzone', 'orangezone', 'redzone']]


# In[11]:


zones = pd.get_dummies(zones )


# In[12]:


zones.columns


# In[13]:


zones = zones.drop('greenzone_Green Zone' , axis = 1)


# In[14]:


zones.head(15)


# In[15]:


zones = zones.values.tolist()


# In[16]:


type(zones)


# In[25]:





# In[27]:


#Code for red , orange , green hotspot zones in India
rog_map = folium.Map(zoom_starts = 12)
def dis(i,color):
    folium.Marker(
        location = point,
        popup = dataset['District'][i],
        icon = folium.Icon(color = color, icon = 'tint', icon_color = 'white')
    ).add_to(rog_map)

i = 0 
for point in dir:
    if zones[i][0] == 1:
        dis(i , 'orange')
    elif zones[i][1] == 1:
        dis(i , 'darkred')      
    else:
        dis(i , 'green')
    i+=1


# In[28]:


rog_map


# In[29]:


#Code for red hotspot zones in India
red_map = folium.Map(zoom_starts = 12)
def dis(i,color):
    folium.Marker(
        location = point,
        popup = dataset['District'][i],
        icon = folium.Icon(color = color, icon = 'tint', icon_color = 'white')
    ).add_to(red_map)

i = 0 
for point in dir:
    if zones[i][1] == 1:
        dis(i , 'darkred')      
    i+=1


# In[30]:


red_map


# In[31]:


#Code for orange hotspot zones in India
orange_map = folium.Map(zoom_starts = 12)
def dis(i,color):
    folium.Marker(
        location = point,
        popup = dataset['District'][i],
        icon = folium.Icon(color = color, icon = 'tint', icon_color = 'white')
    ).add_to(orange_map)

i = 0 
for point in dir:
    if zones[i][0] == 1:
        dis(i , 'orange')
    i+=1


# In[32]:


orange_map


# In[36]:


#Code for green hotspot zones in India
green_map = folium.Map(zoom_starts = 12)
def dis(i,color):
    folium.Marker(
        location = point,
        popup = dataset['District'][i],
        icon = folium.Icon(color = color, icon = 'tint', icon_color = 'white')
    ).add_to(green_map)

i = 0 
for point in dir:
    if zones[i][0] == 1:
        pass
    elif zones[i][1] == 1:
        pass      
    else:
        dis(i , 'green')
    i+=1


# In[37]:


green_map


# In[ ]:




