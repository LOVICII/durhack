import pandas as pd

path = './pppmedia.xlsx'
df = pd.read_excel(path, sheet_name='Sheet1')

# drop rows where the category is NaN
df = df.dropna(subset=['category'])

# combine the category based on comptitle
category = df.groupby('comptitle')['category'].apply(list).reset_index(name="category")

# drop duplicate data
df = df.drop_duplicates(subset='comptitle', keep="last").reset_index()

# replace df category column with category list
df['category'] = category['category']
print(df.head())