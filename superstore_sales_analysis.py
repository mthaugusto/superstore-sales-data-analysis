# -*- coding: utf-8 -*-
"""Superstore_sales_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rElhNrBS7tTo1RRyM3uk4B0U2x7w1vYv

# Superstore Sales Analysis

## 1 - Problem Statement

•	The Superstore dataset provides sales and profit data for a variety of products across different categories and regions.


•	The goal of this project is to analyze the data and identify insights that can help the company improve its business performance.


•	Specifically, we aim to answer questions such as: which product categories are the most profitable? Which regions have the highest sales and profit? What are the most profitable products?


•	By answering these questions, we hope to provide recommendations for the company on how to optimize its product offerings and improve its revenue and profitability.

## 2 - Research questions

We’re interested in understanding which factors contribute to high sales in the superstore.

•	Which product categories have the highest profit margins in the Super Store?

•	Are there any significant differences in sales between the East region and other regions?

•	How do sales vary by product category during different months of the year?

•	What is the rate of returned products for orders with same-day shipping compared to other shipping options?

•	How do sales and profit vary by product category on weekdays compared to weekends?

## 3 - Formulate hypotheses

•	Hypothesis 1: Technology products have the highest profit margin compared to other product categories.

•	Hypothesis 2: The East region has the highest sales compared to other regions.

•	Hypothesis 3: Sales are higher during certain months of the year.

•	Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products.

•	Hypothesis 5: The Company’s profit is more on weekdays than on weekends.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.float_format', lambda x: '%.3f' % x)

import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('superstore_dataset2011-2015.csv', sep=',', encoding='ISO-8859-1')

"""# Explore the data

### 1. Display Top 5 Rows of The Dataset
"""

data.head()

data.columns

"""### 2. Check The Last 5 Rows of The Dataset"""

data.tail()

"""### 3. Find Shape of Our Dataset (numbers of rows and number of lines)"""

data.shape

print(f'Number of rows: {data.shape[0]}')
print(f'Number of lines: {data.shape[1]}')

"""### 4. Get information about our dataset like total number of rows, columns, datatypes of each column and memory requirement"""

data.info()

"""### 5. Check null values available in our dataset"""

data.isnull()

data.isnull().sum()

"""### 6. Check for duplicate data and drop them"""

data.duplicated().any()

# In case duplicated().any() returned true, we could use data.duplicated().sum() to check and
# duplicated_rows = data[data.duplicated()] ---> print(duplicated_rows) to see exactly which ones are the duplicated rows

"""### 7. Get overall statistics about the dataset"""

data.describe()

"""### 8. Drop unnecessary columns

"""

data.columns

data = data.drop(['Row ID', 'Order ID', 'Customer ID', 'Postal Code'], axis=1)

# axis = 1 to specify we're removing our columns

data.columns

"""### Hypothesis 1: Technology products have the highest profit margin compared to other product categories."""

data.columns

cat_profit=data.groupby('Category')['Profit'].sum()

cat_profit

cat_profit.plot(kind='bar ')
plt.title('Profit by Category')
plt.xlabel('Category')
plt.ylabel('Total Profit')
plt.show()

"""### Conclusion: The hypothesis is supported as technology products have the highest profit margin of the three categories.

### Hyphotesis 2: The East region has the highest sales compared to other regions.
"""

data.columns

reg_sales = data.groupby('Region')['Sales'].sum()

reg_sales

reg_sales.plot(kind='bar')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

"""### Conclusion: The hypothesis 2 is not supported as the central region has the highest sales.

### Hypothesis 3: Sales are higher during certain months of the year
"""

data.columns

data['Order Month'] = pd.DatetimeIndex(data['Order Date']).month

data.head()

month_sales = data.groupby('Order Month')['Sales'].sum()

month_sales

month_sales.plot(kind='line')
plt.title("Total Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

"""### Conclusion: Out hypothesis is supported as sales are higher during certain months of the year.

### Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products.
"""

data.columns

total_orders_by_shipping_mode = data.groupby('Ship Mode').size()

total_orders_by_shipping_mode

returned_orders_by_shipping_mode = data[data['Profit']<0].groupby('Ship Mode').size()

returned_orders_by_shipping_mode

returned_per_by_shipping_mode = (returned_orders_by_shipping_mode/total_orders_by_shipping_mode)*100

returned_per_by_shipping_mode

returned_per_by_shipping_mode.plot(kind='bar')
plt.title('Return % By Shipping Mode')
plt.xlabel('Shipping Mode')
plt.ylabel('Return Per')
plt.show()

"""### Conclusion: Our hypothesis is supported as orders with same day shipping have the lowest rate of returned products.

### Hypothesis 5: The company's profit is more on weekdays than on weekends
"""

data.columns

data['Order Day'] = pd.DatetimeIndex(data['Order Date']).day_name()

data.head()

day_profit = data.groupby('Order Day')['Profit'].sum()

day_profit

day_profit.plot(kind='bar')
plt.title('Total Profit by Day Of The Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Profit')
plt.show()

"""### Conclusion: Our hypothesis is supported as company's profit is higher on weekdays compared to weekends

# CONCLUSIONS

**Hypothesis 1: Technology products have the highest profit margin compared to other product categories.**

This hypothesis is supported. The data shows that technology products have the highest profit margin compared to other product categories.

**Hypothesis 2: The East region has the highest sales compared to other regions.**

This hypothesis is not supported. The data shows that the East region does not have the highest sales compared to other regions.

**Hypothesis 3: Sales are higher during certain months of the year.**

This hypothesis is supported. The data shows that sales are higher during certain months of the year.

**Hypothesis 4: Orders with same-day shipping have the lowest rate of returned products.**

This hypothesis is supported. The data shows that orders with same-day shipping have the lowest rate of returned products.

**Hypothesis 5: The Company's profit is more on weekdays than on weekends.**

This hypothesis is supported. The data shows that the company's profit is more on weekdays than on weekends.

# RESULTS

Based on the analysis, it can be concluded that technology products have the highest profit margin compared to other product categories.

The company's profit is higher on weekdays than on weekends. Sales are higher during certain months of the year.

Orders with same-day shipping have the lowest rate of returned products. However, the hypothesis that the East region has the highest sales compared to other regions is not supported by the data.

These conclusions provide valuable insights into the company's performance and can guide future decision-making processes.

**It is important to note that further investigation may be required to fully understand the underlying factors influencing these observations.**

# SUGGESTIONS

The company should focus on developing and promoting technology products to increase its profits. They could also consider reducing the production and promotion of products with lower profit margins.

Central region has the highest sales compared to other regions; the company could consider increasing its focus on this region. then the company should re-evaluate its marketing and sales strategies in other regions.

The company should focus on maximizing sales during the months of November and December. This could involve increasing the inventory of popular products during this time, running targeted marketing campaigns, and offering promotions or discounts to customers. However, the company should also consider strategies to maintain sales during other months, such as introducing new products or services or offering promotions and discounts during slower months.

The company could consider offering more same-day shipping options to customers. This might involve optimizing inventory and supply chain processes to ensure that products can be shipped quickly and efficiently.

The company could consider focusing on different types of promotions or sales during the weekends to increase sales. For example, the company could offer weekend-only promotions or discounts or run targeted marketing campaigns aimed at weekend shoppers. The company could also consider offering special events or activities in-store on weekends to attract customers and increase sales. Additionally, the company could focus on offering products and services that are particularly popular among weekend shoppers, such as home entertainment or outdoor products.
"""