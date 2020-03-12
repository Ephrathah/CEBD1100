import pandas as pd

pd.options.display.float_format = '{:2f}'.format
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)


dataset = pd.read_csv("50000 Sales records.csv")
dataset = pd.read_csv("50000 Sales records.csv",)
print(dataset)

print(dataset.keys())
dataset.colums = datset.colums.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', ‘’)
print(dataset.keys())

print(dataset.unit_price.describe())
print(dataset.country.describe())
Print(dataset.unit_price.max())
Print(dataset.unit_price.min())
Print(dataset.unit_price.mean())

print(dataset.describe())   # value type listed only here
print(dataset.describe(include=object)) #non value types listed here.

print(dataset.groupby('region'))
dataset.groupby('region')['units_sold'].sum()

dataset.groupby('region')['units_sold'].sum()
#sum for europe
dataset.groupby('region')['units_sold'].sum()[Europe'])

a = dataset.groupby('region')['units_sold'].sum()['Europe'])






print(dataset.region.value_counts())

print(dataset.region.unique()) # we could use this for homework

print(dataset.region.values)
