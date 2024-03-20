# -*- coding: utf-8 -*-
"""LVADSUSR103_Preethi_L_FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iW8RdB3ebJncJucotITqTp_cI4vgXUbI
"""

#1
#loading the dataset using pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

walmart_data = pd.read_csv('/content/drive/MyDrive/Walmart_Dataset Python_Final_Assessment.csv')
# #print(walmart_data)
df = pd.DataFrame(walmart_data)
print(df)
# getting info of dataset
print(df.info(),"\n")
print(df.describe(include = 'all').T,"\n")
print(df.columns,"\n")
print(df.head(10),"\n")
print(df.shape,"\n")
print(df.tail(7),"\n")
print(df.nunique(),"\n")
print(df.value_counts(),"\n")
categorical_cols= df.select_dtypes(include=['object']).columns
numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables: ",categorical_cols,"\n")
print("Numerical Variables: ",numerical_cols)

#2
# data cleaning
# here, We don't have null values
df.isnull() # to check if it contains any null values
df.notna() # if we check for the not-null values it returns all the values in the dataset
df.dropna() # to drop null values if any
#df.fillna() # to fill the missing values using sum(),mean(),median()
df.duplicated().sum() # there are no duplicate values as it returns output 0

#3
# descriptive statistics
# And the numerical columns are sales,quantity, profit
print("Numerical Variables: ",numerical_cols)
# Analyze measures for numerical data
# for sales column
print("Applying descriptive satistice for sales column ----------")
print("Mean of sales column is :", df['Sales'].mean())
print("Median of sales column is :", df['Sales'].median())
print("Mode of sales column is :", df['Sales'].mode())
print("Range of sales column is :", df['Sales'].max() - df['Sales'].min())
print("Variance of sales column is :", df['Sales'].var())
print("Standard Deviation of sales column is :", df['Sales'].std())
print("\n\n")
#for quantity column
print("Applying descriptive satistice for quantity column ----------")
print("Mean of quantity column is :", df['Quantity'].mean())
print("Median of qunatity column is :", df['Quantity'].median())
print("Mode of qunatity column is :", df['Quantity'].mode())
print("Range of qunatity column is :", df['Quantity'].max() - df['Quantity'].min())
print("Variance of qunatity column is :", df['Quantity'].var())
print("Standard Deviation of quantity column is :", df['Quantity'].std())
print("\n\n")

# for profit column
print("Applying descriptive satistice for profit column ----------")
print("Mean of profit column is :", df['Profit'].mean())
print("Median of profit column is :", df['Profit'].median())
print("Mode of profit column is :", df['Profit'].mode())
print("Range of profit column is :", df['Profit'].max() - df['Profit'].min())
print("Variance of profit column is :", df['Profit'].var())
print("Standard Deviation of profit column is :", df['Profit'].std())

# 4
#4
import matplotlib.pyplot as plt

#using various plots to visualize the dataset
# Histogram
df.hist(figsize=(10, 9))
plt.show()
print("\n\n\n")

# Scatter plot
plt.figure(figsize= (10,9))
plt.scatter(df['Sales'], df['Profit'])
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Sales vs Profit ')
plt.show()
print("\n\n\n")

# Box plot
plt.figure(figsize= (10,9))
df.boxplot(column=['Sales', 'Profit'])
plt.show()
print("\n\n\n")

# Bar chart
plt.figure(figsize= (10,9))
df['Category'].value_counts().plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Category Distribution of Walmart Sales Data <:)')
plt.show()
print("\n\n\n")

# Pie chart
plt.figure(figsize= (10,9))
df1 = df['Geography'].value_counts()
df1.head(10).plot(kind='pie')
plt.title('Geography Distribution of Walmart Sales Data ')
plt.legend()
plt.ylabel('')
plt.show()

#5
# Exploring correlations between different variables
correlation_matrix = df.corr()
print("The Correlation Matrix is : \n")
print(correlation_matrix)

#6
#Anamoly detection
# for to choose outliers I'll go with Box Plot
# here, I have done the same thing for sales and profit using same and different plots to variate it
import matplotlib.pyplot as plt

plt.figure(figsize= (10,9))
df.boxplot(column=['Sales', 'Profit'])
plt.title("Box plot for Anamoly Detection ")
plt.show()
print("\n\n\n")

# Box plot for Sales column
plt.figure(figsize=(7, 7))
plt.boxplot(df['Sales'])
plt.title('Box plot for Sales in Walmart Data ')
plt.ylabel('Sales')
plt.show()

# Box plot for Profit column
plt.figure(figsize=(7, 7))
plt.boxplot(df['Profit'])
plt.title('Box plot for Profit in Walmart Data ')
plt.ylabel('Profit')
plt.show()

#7
# Trend Analysis
# i
# Sales and Profit trends over the years
# using line plot we're doing this tend analysis
# here, rder Date is in object I'm converting it to date type
import datetime as dt
df['Order Date'] = pd.to_datetime(df['Order Date'])
print(df.dtypes)

df['Year'] = df['Order Date'].dt.year
sales_by_year = df.groupby('Year')['Sales'].sum()
profit_by_year = df.groupby('Year')['Profit'].sum()
# Plotting sales and profit trends
plt.plot(sales_by_year.index, sales_by_year.values, label='Sales',marker = 'o', mfc = 'black',ms = 15)
plt.plot(profit_by_year.index, profit_by_year.values, label='Profit',marker = 'o',mfc = 'black',ms = 15)
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Sales and Profit Trends over Years!')
plt.legend()
plt.show()
print("\n\n")

# ii
# Product category with the most growth in terms of sales over the years
sales_by_category = df.groupby(['Year', 'Category'])['Sales'].sum()
print(sales_by_category,"\n")
plt.figure(figsize= (10,9))
df['Category'].value_counts().plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('sales_by_category.values')
plt.show()

#7
#customer analysis
#i
# have to identify the top 5 customers based on the number of orders placed and total sales generated in walmart
top5_customers = df.groupby('EmailID').agg({'Order ID': 'count', 'Sales': 'sum'}).nlargest(5, columns='Sales')
print(top5_customers)

# ii
# Repeating the purchase behavior process
df_sort = df.sort_values(by=['EmailID', 'Order Date'])
df_sort['Time_Between_Orders'] = df_sort.groupby('EmailID')['Order Date'].diff()
average_time_between_orders = df_sort.groupby('EmailID')['Time_Between_Orders'].mean()
print(average_time_between_orders)

"""#7
#comprehensive analytics
#i
By means of supply chain, from sales velocity and order fulfillment we can increase the quantity and manage the stocks and increase the production

#ii
And the facts that contribute the geographic distribution is by sales and its mainly of the accuracy in delivery side from walmart team.
But to reach the targeted marketing strategies we need to ship the products priorly and then only it meets our suucess rate .

#iii
To enhance the customer loyalty we need to improve the product quality and make some changes to get delivered fast.And the top customers almost satisfied with our service to keep them with our eternal service we have to improve the efficacy of the products.


"""