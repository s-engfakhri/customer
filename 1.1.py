
import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv("Mall_Customers.csv")
print(data.head(10))
print("null:",data.isnull().sum())
###age median
data["Age"].fillna(data["Age"].mean(), inplace=True)
###annual income and spending score fill with mean
data["Annual Income (k$)"].fillna(data["Annual Income (k$)"].mean(), inplace=True)
data["Spending Score (1-100)"].fillna(data["Spending Score (1-100)"].mean(), inplace=True)
print(data.isnull().sum())
print("duplicated:",data.duplicated())
print("type:",data.dtypes)
data.dict={"Genre":data["Genre"].value_counts(),
           "Age":data["Age"].value_counts(),
           "Annual Income (k$)":data["Annual Income (k$)"].value_counts(),
           "Spending Score (1-100)":data["Spending Score (1-100)"].value_counts()}
print(data.dict)
data.rename(columns={"Annual Income (k$)":"annual income","Spending Score (1-100)":"spending amount"}, inplace=True)
data.drop(columns=["CustomerID"], inplace=True)

print("columns names:",data.columns)

