import pandas as pd
a= {
    'colors':[700,800,900],
    'duration': [1,5,7]
}

arr =pd.DataFrame(a)
print(arr.loc[[0,2]])

df= pd.read_csv('academicStress.csv')
print(df.to_string())