# Databricks notebook source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
sns.set(style="ticks")


# COMMAND ----------

path = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Online_Retail/Online_Retail.csv"

online_rt = pd.read_csv(path, encoding='latin1')

online_rt.head()

# COMMAND ----------

countries = online_rt.groupby("Country").sum(numeric_only=True)
top_countries = countries.sort_values(by="Quantity", ascending=False)[1:11]
colors = plt.cm.tab10.colors  # 10 distinct colors from matplotlib's colormap

# Plotting
top_countries["Quantity"].plot(kind="bar", figsize=(10, 6) , color=colors)
plt.xlabel("Countries")
plt.ylabel("Quantity")
plt.title("Top 10 Countries with Most Orders (by Quantity)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# COMMAND ----------

online_rt = online_rt[online_rt.Quantity > 0]
online_rt.head()

# COMMAND ----------

customers = online_rt.groupby(['CustomerID','Country']).sum()
customers = customers[customers.UnitPrice > 0]
customers['Contry'] = customers.index.get_level_values(1)
top_contries = ['Netherlands', 'EIRE', 'Germany', 'France', 'Spain']
customers = customers[customers['Contry'].isin(top_contries)]


# COMMAND ----------

g = sns.FactGrid(customers, col="Country")
g = map(plt.scatter,"Quantity", "UnitPrice",)

# COMMAND ----------

 