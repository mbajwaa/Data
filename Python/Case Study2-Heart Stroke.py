#!/usr/bin/env python
# coding: utf-8

# In[63]:


######## IMPORTING LIBRARIES
import pandas as pd #Missing values## used Shape,Info,Describe Funations
import seaborn as sb #graohical data
import matplotlib as mp
import matplotlib.pyplot as plt #Graphical data
import numpy as np #Mathematic Caluculations


# In[3]:


####HOW TO IMPORT DATASET
heartstroke = pd.read_csv('hs.csv')


# In[6]:


heartstroke#


# In[7]:


heartstroke.head()
heartstroke.head(10)


# In[24]:


heartstroke.tail()


# In[5]:


heartstroke.info()


# In[6]:


heartstroke.shape


# In[27]:


###STATISTICAL MEASURE OF  DIFFERENT ATTRIBUTES
heartstroke.describe()


# In[37]:


heartstroke.columns


# In[38]:


heartstroke.shape


# In[39]:


print("Shape of imported DataSet: R*C are: " , heartstroke.shape)


# In[41]:


##HOW TO SEPARTES COLUMINS IN DATASET
age= heartstroke.iloc[:,2]
print(age)


# In[8]:


heartstroke.info()


# In[10]:


heartstroke.describe()


# In[ ]:


##HOW TO SEPERATE COLUMNS IN DATA SET TO FINDOUT WHICH COLUMNS YOU WANT TO SHOWS


# In[ ]:





# In[15]:


age = heartstroke.iloc[:, 2]
print (age)


# In[30]:


age=list(heartstroke.iloc[:, 2])
print("Age of all Patients in DataSet are :" , age)
np_age =np.array(age)
avg_age=np.mean(np_age)##AVERAGE AGE 
print("Average ago of Patients in DataSet is :", avg_age, "\n")
st_age=np.std(np_age)
print("Standard Derivations of Patients in Dataset is :" ,st_age,  "\n")


# In[ ]:


## CHECKNG AND REMOVING MISSING VALUES IN DATA SET


# In[37]:


#CHECKING 
heartstroke.isnull().sum()
print("DataSet information Before Removal of Null Values: ", "\n", heartstroke.isnull().sum(), "\n")


# In[38]:


#REMOVINF OF MISSING VLAUES IN DATA SET
heartstroke.dropna(inplace=True)
print("DataSet information after Removal of Null Values: ", "\n", heartstroke.isnull().sum(), "\n")
print("SHAPE OF DataSet information after Removal of Null/Missing Values are : ", "\n", heartstroke.shape,"\n")


# In[19]:


##ATTRIBUTE #1-STROKE

stroke_counts = heartstroke["stroke"].value_counts()
print(stroke_counts)
plt.figure(figsize=(8,6 ))
sb.countplot(x="stroke", data=heartstroke)
plt.title("STROKE")
plt.show()


# In[ ]:


##ATTRIBUTE #2 -AGE DISTRIBUTION


# In[14]:


sb.set()
plt.figure(figsize=(6,6 ))
sb.displot(heartstroke["age"])
plt.title("Age Distribution")
plt.show()


# In[ ]:


##ATTRIBUTE #3 -STATUS OF SMOKING


# In[16]:


plt.figure(figsize=(8,6 ))
sb.countplot(x="smoking_status", data=heartstroke)
plt.title("Smoker")
plt.show()


# In[20]:


##ATTRIBUTE #5-WORK TYPE

heartstroke["work_type"].value_counts()
plt.figure(figsize=(8,6 ))
sb.countplot(x="work_type", data=heartstroke)
plt.title("WORK TYPE")
plt.show()


# In[25]:


##ATTRIBUTE # RESIDENCE TYPE
heartstroke["Residence_type"].value_counts()
plt.figure(figsize=(8,6 ))
sb.countplot(x="Residence_type", data=heartstroke)
plt.title("RESIDENCE TYPE")
plt.show()


# In[28]:


##ATTRIBUTE #7 HEART DISEASEE
heartstroke["heart_disease"].value_counts()
plt.figure(figsize=(8,6 ))
sb.countplot(x="heart_disease", data=heartstroke)
plt.title("HEART DISEASE")
plt.show()


# In[45]:


##FOUR GRAPHS SHOWS IN SINGLE GRAPH
cat_var = ["gender","ever_married","work_type","Residence_type"]

fig,axs = plt.subplots(nrows=2,ncols=2,figsize=(15,10))
axs=axs.flatten()

for i,var in enumerate(cat_var):
    sb.countplot(x=var,hue="stroke",data=heartstroke,ax=axs[i])
    axs[i].set_xticklabels(axs[i].get_xticklabels(),rotation=90)
    
fig.tight_layout()
plt.show()


# In[54]:


##FOUR GRAPHS SHOWS IN SINGLE GRAPH-Numerical
num_vars=["age","hypertension","heart_disease","avg_glucose_level","bmi","stroke"]

fig,axs = plt.subplots(nrows=2,ncols=3,figsize=(20,10))
axs = axs.flatten()

for i,var in enumerate(num_vars):
  sb.boxplot(x=var,data=heartstroke,ax=axs[i])
    
fig.tight_layout()
plt.show()


# In[ ]:





# In[ ]:




