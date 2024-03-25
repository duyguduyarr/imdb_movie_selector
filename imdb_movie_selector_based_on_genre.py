#!/usr/bin/env python
# coding: utf-8

# In[14]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load
# importing easygui module
from easygui import *
import pandas as pd
import numpy as np
import random

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

data = pd.read_csv(r'E:\İndirilenler\archive\imdb_top_1000.csv')
data.head()

selected_columns = ['Series_Title', 'Genre']
subset_df = data[selected_columns]

# Display the DataFrame
#getting drama movies
drama_movies=subset_df[subset_df['Genre'].str.contains('Drama', case=False, na=False)]
war_movies=subset_df[subset_df['Genre'].str.contains('Drama', case=False, na=False)]
comedy_movies=subset_df[subset_df['Genre'].str.contains('Comedy', case=False, na=False)]
crime_movies=subset_df[subset_df['Genre'].str.contains('Crime', case=False, na=False)]
romance_movies=subset_df[subset_df['Genre'].str.contains('Romance', case=False, na=False)]
mystery_movies=subset_df[subset_df['Genre'].str.contains('Mystery', case=False, na=False)]
action_movies=subset_df[subset_df['Genre'].str.contains('Action', case=False, na=False)]


# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# message to be displayed
text = "What kind of movie do you want to watch?"

# window title
title = "MOVIE SELECTING APP"

# item choices
choices = ["Drama", "Action", "Crime", "Comedy","Romance", "War","Mystery"]

# creating a button box
output = choicebox(text, title, choices)

if output == "Drama":
    movie = random.choice(drama_movies['Series_Title'].tolist())
    final = msgbox("Your movie based on genre is: "+str(movie))
elif output == "Action":
    movie = random.choice(action_movies['Series_Title'].tolist())
    final = msgbox("Your movie based on genre is: "+str(movie)) # doesnt work without "+"
elif output == "Crime":
    movie = random.choice(crime_movies['Series_Title'].tolist())
    final = msgbox("Your movie based on genre is: "+str(movie))
elif output == "Comedy":
    movie = random.choice(comedy_movies['Series_Title'].tolist())
    final = msgbox("Your movie based on genre is: "+str(movie))
elif output == "Romance":
    movie = random.choice(romance_movies['Series_Title'].tolist())
    final = msgbox("Your movie based on genre is: "+str(movie))
elif output == "War":
    movie = random.choice(war_movies['Series_Title'].tolist())
    final = msgbox("Your movie based on genre is: "+str(movie))
elif output == "Mystery":
    movie = random.choice(mystery_movies['Series_Title'].tolist())
    final = msgbox("Your movie based on genre is: "+str(movie))

