#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset  [TMDb movie data]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# # <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# >his data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.
# 
# 
# 
# 
# ### Question(s) for Analysis
# ###### 1. which genres are most produced over years?
# ###### 2. what is the relation between movie duration and rate?
# ###### 3. which year has the bigest number of movies?
# ###### 4. what is the madian budgat for movies?
# ###### 5.is people prefer old movies?
# ###### 6.What is the most used keywords of the TMDb data set?
# 

# In[50]:


#  import statements for all of used packages 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from datetime import datetime
from wordcloud import WordCloud


# <a id='wrangling'></a>
# ## Data Wrangling

# In[51]:


#Load your data and print out a few lines.
df= pd.read_csv('tmdb-movies.csv')
df.head()


# In[52]:


# display  dataframe summary for each column
df.info()


# 
# ### Data Cleaning
# 

# #### 1. clean unwanted items

# In[53]:


removed_data = ['id', 'imdb_id', 'homepage','tagline', 'overview']

df.drop(removed_data, axis=1, inplace=True)
df.head()


# #### 2.solve duplication problem  

# In[54]:


#check duplication 
df.duplicated().sum()


# In[55]:


#remove duplicated items
df.drop_duplicates(inplace=True)
#check duplication
df.duplicated().sum()


# #### 3. solve data type problem

# In[56]:


# convert release_date column to datetime
df['release_date'] = pd.to_datetime(df['release_date'])


# #### 4. remove non rows

# In[57]:


df = df.replace(0, np.nan)
df = df.dropna()
df.info()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 
# 
# ### Research Question 1 (Which genres are most produced over years?)

# In[58]:


# function generate dummy matrix
def dum (column1):
    return column1.str.get_dummies(sep='|')

genres_dum = dum(df['genres'])
# Bar Chart 
genres_dum.sum().sort_values(ascending=False).plot.bar(figsize = (20,10))
plt.title('Most produced Genre', fontsize =20)
plt.xlabel('Genres', fontsize = 20)
plt.ylabel('Number Of Movies', fontsize = 20)
plt.xticks(rotation =0);


# the most produced genres is drama

# ### Research Question 2  (what is the relation between movie duration and rate?)

# In[60]:


# using scatter plot to describe the relation between duration and rate 
plt.scatter(df['runtime'], df['vote_average'])
plt.title('All Movies Run time', fontsize = 24)
plt.xlabel('duration minutes', fontsize = 12)
plt.ylabel('rate', fontsize = 12);


# long movies have high rate

# ### Research Question 3  ( which year has the bigest number of movies?)

# In[61]:


plt.figure(figsize=(50,30))
sns.countplot(df['release_year'])
plt.title('Number of Movies per Year', fontsize = 40)
plt.xlabel('Year', fontsize = 30)
plt.ylabel('Number Of Movies', fontsize = 30)
plt.xticks(rotation = 90);


#  year 2011 has the maximum number of movies

# ### Research Question 4  ( what is the madian budgat for movies?)

# In[62]:


plt.hist(df['budget'] , bins=50)
plt.title('Movies VS. Budget', fontsize = 24)
plt.xlabel('budget', fontsize = 12)
plt.ylabel('Number Of Movies', fontsize = 12);


# madian of budget is10e8

# ### Research Question 5 (is people prefer old movies ?)

# In[63]:


avg= df.groupby("release_year")["vote_average"].mean()
avg.plot(kind='line',title='Average Rating VS Years',figsize = (10,5))
plt.xlabel('Years')
plt.ylabel('Vote Average Rating');


# the rate of old movies is higher

# ### Research Question 6 (What is the most used keywords of the TMDb data set?)

# In[64]:


text = ','.join(df['keywords'].str.cat(sep='|').split('|'))

wordcloud = WordCloud(max_words=100, background_color = 'white').generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off");


# <a id='conclusions'></a>
# ## Conclusions
# 1. the most produced genres is drama
# 2. long movies have high rate
# 3. year 2011 has the maximum number of movies
# 4. madian of budget is10e8
# 5. the rate of old movies is higher
# 
# ## The limitations 
# • NAN values
# • zeros values
# • Duplicates 
# • Inccorect datatype
# 
# ## Submitting your Project 

# In[65]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:





# In[ ]:




