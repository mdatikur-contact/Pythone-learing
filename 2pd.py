import pandas as pd
df = pd.read_csv('data.csv')
df.dropna(inplace= True)
# df_np= df.fillna(200, inplace= True)
print(df.to_string())