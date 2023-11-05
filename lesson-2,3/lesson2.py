

 

import pandas as pd


data=pd.read_csv('data.csv') 
print(data)

print(data.info())

print(data.head(5))

first_5=data.head(5)


height_column=data['height']

height_age=data[['height', 'age']]



