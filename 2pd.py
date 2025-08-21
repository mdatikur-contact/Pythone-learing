import pandas as pd
df = pd.read_csv('data.csv')
# df.dropna(inplace= True)
x= df['Maxpulse'].median()
df.fillna({'Maxpulse':x}, inplace= True)
print(df.to_string())