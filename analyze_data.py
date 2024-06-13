import pandas as pd

df = pd.read_csv('data.csv')
df = df.reset_index()  # make sure indexes pair with number of rows

unsalable_df = df[df.amzn_price <= df.store_price]

unsalable_df.pop('amzn_price')
unsalable_df.pop('store_price')
unsalable_df.pop('sales_rank')

df = df[df.amzn_price > df.store_price]

for index, row in df.iterrows():
	df.loc[index, 'markup_%'] = row['amzn_price'] / row['store_price']
	df.loc[index, 'price_dif'] = row['amzn_price'] - row['store_price']


print(unsalable_df)

unsalable_df.to_csv('unsalable_products.csv')