# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

cars1 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars1.csv")
cars2 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/05_Merge/Auto_MPG/cars2.csv")

# COMMAND ----------

print(cars1.head())
print(cars2.head())

# COMMAND ----------

cars1.to_csv("cars1.csv", index=False)
cars2.to_csv("cars2.csv", index=False)

# COMMAND ----------

cars1 = cars1.loc[:, "mpg":"car"]
cars1.head()

# COMMAND ----------

print(cars1.shape)
print(cars2.shape)

# COMMAND ----------

cars = cars1.append(cars2)
cars

# COMMAND ----------

 nr_owners= np.random.randint(15000, high=73001, size=398, dtype='I')
 nr_owners

# COMMAND ----------

cars = pd.concat([cars1, cars2])
display(cars)

# COMMAND ----------

cars['owners'] = nr_owners
cars.tail()

# COMMAND ----------

