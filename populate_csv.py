# importing csv
import csv, random, string, pandas as pd

def randomword():
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(5))

df = pd.DataFrame()

for x in range(100):
    df = pd.concat([df, pd.DataFrame([{
        "title": randomword(),
        "amzn_id": random.randint(0, 1000),
        "store_id": random.randint(0, 1000),
        "amzn_price": random.randint(0,300),
        "store_price": random.randint(0,300),
        "sales_rank": random.randint(0, 1000)
    }])], ignore_index=True)

df.to_csv('products.csv')
