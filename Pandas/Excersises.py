import numpy as np

import pandas as pd
x = pd.read_csv("/Users/akashpatel/Documents/Clairvoyant/Spark-Training/WorldWealth.csv", header = None)

print(x.info())

print(x.shape)

print(type(x))

print(x.head(5))

print(x[0])     # works when the header sets None
# print(x['Country']) # when the header is available

print(type(x[0]))

print(x.iloc[1])

print(x[[0,2]])

print(x[0] == 'Japan')

print(x[x[0] == 'Japan'])