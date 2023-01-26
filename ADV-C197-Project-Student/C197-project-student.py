#!/usr/bin/env python
# coding: utf-8

# In[8]:


print('Name:Ziyah // Fierce Bird ')
print('Plot a heatmap which help you visualize percentage of blood leaving the heart at each contraction of a smoking and non smoking person heart')
print('Plot a heatmap which help you visualize Percentage of blood leaving the heart at each contraction of person who died due to cardio vascular disease')


# #  Task 1 - Plot heat map to visualize percentage of blood leaving the heart at each contraction of a smoking and non smoking person

# A normal, healthy heart will never completely empty, but it will pump out 55-70 percent of the blood that’s inside it. An ejection fraction of 55-70 percent is normal; 40-55 percent is below normal. Anything less than 40 percent may indicate heart failure, and below 35 percent there’s a risk for life-threating arrhythmias

# In[43]:


#predefine code for image
from IPython.display import Image
Image(filename='heart.png') 
#predefine code end


# The right side of your heart receives oxygen-poor blood from your veins and pumps it to your lungs, where it picks up oxygen and gets rid of carbon dioxide. The left side of your heart receives oxygen-rich blood from your lungs and pumps it through your arteries to the rest of your body.

# In[2]:


# Import all the libraries and read heart_failure_clinical_records_dataset.csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataFrame= pd.read_csv('heart_failure_clinical_records_dataset.csv')
df = dataFrame.dropna()
df


# In[4]:


#Group by age and smokers and find the average ejection_fraction rate
group_smokers=df.groupby(['age','smoking'])['ejection_fraction'].mean().reset_index()
group_smokers


# In[6]:


# Plot a heatmap to show the ejection fraction rate in smokers and non smokers heart
plt.figure(figsize=(12,8))
heatmap= pd.pivot_table(values ='ejection_fraction', index ='smoking',  
                    columns ='age', data = group_smokers)
sns.heatmap(heatmap, cmap ='plasma')


# 0 are non smokers  and 1 are smokers
# 
# Conclusion - =The group from 1's ejection fraction is really low

# #  Task 2 Plot a heatmap to visualize percentage of blood leaving the heart at each contraction of people who died due to cardio vascular disease

# In[8]:


#Group by death events and ejection fraction rate and find the average ejection fraction rate
group_death = df.groupby(['age','DEATH_EVENT'])['ejection_fraction'].mean().reset_index()
group_death


# In[9]:


# Plot a heatmap to show the ejection fraction rate of people who died due to cardiovascular disease
plt.figure(figsize=(12,8))
heatmap= pd.pivot_table(values ='ejection_fraction', index ='DEATH_EVENT',  
                    columns ='age', data =group_death )
sns.heatmap(heatmap, cmap ='plasma')



# In[ ]:





# 1 are people died due to cardiovascular disease
# 
# Conclusion -many of the ones who died by cardiovascular desieses have really low ejection_fractions 

# In[ ]:




