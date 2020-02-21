import pandas as pd

df = pd.read_csv("/Users/akashpatel/Documents/Clairvoyant/Spark-Training/WorldWealth.csv")

print(df.describe())

print(df.columns)

print(df["Country"])

print(df.Country)

df["ones"] = 1

df["twos"] = 2

print(df.head())


# Apply function
# df ['x1x2'] = df.apply(lambda row: row['x1'] * row['x2'], axis =1)
#
# def get_interaction(row):
#   retunr row['x1'] * row['x2']
# df['x1x2'] = df.apply(get_interaction, axis = 1)

df = df.rename(columns={'Wealth ($B)': 'Wealth'})

print(df.columns)

print(df.head())

# df['cleanWealth'] = df.apply(lambda x: str(x['Wealth']).replace('$', ''))

# df['wealth2'] = df.apply(lambda row: (df['Wealth ($B)']))
print("-------------------")

print(df.info())

df.Region = df.Region.astype(str)

df.Wealth = df.Wealth.astype(str)


print("-------------------")

print(df.info())

df['cname'] = df['Region'].apply(lambda x: x.strip().capitalize())
df["w"] = df['Wealth'].apply((lambda x: x.replace('$', '')))
df['FinalWealth'] = df['w'].apply(lambda x: x.replace(',', ''))

print(df.info())

print(df.head())