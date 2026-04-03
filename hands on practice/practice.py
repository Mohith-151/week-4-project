#===============================================================================
#       # Week 4: Data Visualization & Your First Complete Project
#===============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df  = pd.read_csv('hands on practice\sales_data.csv')
# print(df.head())
# print(df.shape)

#===============================================================================
#to print a Bar chart for the sales according to the product.

# products = df['Product'].unique()
# print(products)

#the product list: ['Phone', 'Headphones', 'Laptop', 'Tablet', 'Monitor']
df1 = df.copy(deep=True)
x = df1['Product']
y = df1['Total_Sales']

plt.bar(x,y)
# plt.show()
#===============================================================================

#adding  title for the same bar chart.
plt.title('Total sales by product.')
# plt.show()