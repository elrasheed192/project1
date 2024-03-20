#!/usr/bin/env python
# coding: utf-8

# In[138]:


# Importing the important library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


# read the file from a specific folder path
df= pd.read_csv("D:\TRAININGS\DATA ANALYTICS\Projects Data Analysis\Ask A Manager Salary Survey 2021 (Responses) - Form Responses 1.csv")
df


# In[3]:


# To check the header 
df.head()


# In[4]:


# To check the footer 
df.tail()


# In[5]:


# to check the file column and row number 
df.shape


# In[40]:


# To describe the data 
df.describe ()


# In[44]:


# Find missing values in the DataFrame
missing_values = df.isnull()
missing_values


# In[48]:


Timestamp = 'Timestamp'
missing_values_in_column = df[Timestamp].isnull()
missing_values_in_column


# In[49]:


df.dropna(subset=[Timestamp], inplace=True)


# In[50]:


Timestamp


# In[53]:


df[Timestamp].info()


# In[54]:


df['Timestamp'] = pd.to_datetime(df['Timestamp'])


# In[55]:


df[Timestamp]


# In[57]:


df['How old are you?']


# In[82]:


# Rename the column
df.rename(columns={"What is your annual salary? (You'll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)": 'What is your salary'}, inplace=True)


# In[83]:





# In[64]:


df.info()


# In[136]:


# Remove non-numeric characters from the column
df['What is your salary'] = df['What is your salary'].str.replace(r'[^\d]+', '', regex=True)


# In[140]:


# Convert the column to integer type
df['What is your salary'] = pd.to_numeric(df['What is your salary'], errors='coerce')

df['How many years of professional work experience do you have overall?'] = pd.to_numeric(df['How many years of professional work experience do you have overall?'], errors='coerce')

df['How many years of professional work experience do you have in your field?'] = pd.to_numeric(df['How many years of professional work experience do you have in your field?'], errors='coerce')


# In[87]:


# Group by industry and calculate average salary
avg_salary_by_industry = df.groupby('What industry do you work in?')['What is your salary'].mean().sort_values(ascending=False)


# In[88]:


avg_salary_by_industry


# In[109]:


avg_salary_by_industry


# In[158]:


avg_salary_by_industry.max()


# In[115]:


# Visualize average salaries across industries
avg_salary_by_industry.plot(kind='bar', figsize=(20, 12), color='black', edgecolor='black')
plt.title('Average Salary by Industry')
plt.xlabel('Industry')
plt.ylabel('Average Salary')
plt.xticks(rotation=90)
plt.show()


# In[111]:


# Group the data by years of experience and calculate average salary
avg_salary_by_experience = df.groupby('How many years of professional work experience do you have overall?')['What is your salary'].mean()


# In[112]:


avg_salary_by_experience


# In[113]:


# Create a line chart to visualize salary growth with years of experience
plt.figure(figsize=(10, 6))
plt.plot(avg_salary_by_experience.index, avg_salary_by_experience.values, marker='o', linestyle='-')
plt.xlabel('How many years of professional work experience do you have overall?')
plt.ylabel('Average Salary')
plt.title('Salary Growth with Years of Experience')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[159]:


# Group the data by location and calculate average salary
avg_salary_by_location = df.groupby('What country do you work in?')['What is your salary'].sum().sort_values()
avg_salary_by_location


# In[160]:


avg_salary_by_location.max()


# In[124]:


# Create a bar chart to visualize regional salary differences
plt.figure(figsize=(10, 6))
avg_salary_by_location.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('avg_salary_by_location?')
plt.ylabel('What is your salary')
plt.title('Regional Salary Differences')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[127]:


# Create a box plot to visualize salary differences based on gender and years of experience
plt.figure(figsize=(10, 6))
sns.boxplot(x='What is your gender?', y='What is your salary', hue='How many years of professional work experience do you have overall?', data=df, palette='muted')
plt.xlabel('What is your gender?')
plt.ylabel('What is your salary')
plt.title('Salary Differences Based on Gender and Experience')
plt.legend(title='Years of Experience', loc='upper right')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[129]:


# Create a pairplot to visualize the relationships between variables
sns.pairplot(df, hue='What is your race? (Choose all that apply.)', palette='muted')
plt.show()


# In[130]:


# Calculate correlation matrix
correlation_matrix = df.corr()

# Plot correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()


# In[156]:


# Calculate the balance between total work experience and field-specific experience
df['Balance'] = df['How many years of professional work experience do you have overall?'] - df['How many years of professional work experience do you have in your field?']


# In[157]:


# Create a scatter plot to visualize the relationship between balance and salary
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Balance', y='What is your salary', data=df, hue='What is your salary', palette='coolwarm', alpha=0.7)
plt.xlabel('Balance (How many years of professional work experience do you have overall? - How many years of professional work experience do you have in your field?)')
plt.ylabel('What is your salary')
plt.title('Balance vs. What is your salary')
plt.legend(title='Salary')
plt.show()


# In[145]:


# Calculate correlation coefficients
correlation_matrix = df[['Balance', 'What is your salary']].corr()
correlation_matrix


# In[ ]:




