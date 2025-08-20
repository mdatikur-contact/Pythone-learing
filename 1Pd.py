import pandas as pd
myDataSet = {
    'car':['BMD', 'Marchendis', 'Toyota'],
    'passing': [7,7,2]
}
myVar = pd.DataFrame(myDataSet)
print(myVar)