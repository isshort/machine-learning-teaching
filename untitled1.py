 


import matplotlib.pyplot as plt
#Library 
import numpy as np
import pandas as pd

#Cod
#Data import

data=pd.read_csv('mising_data.csv')
 
 

country1=data.iloc[:,0:1].values
 

from sklearn import preprocessing

 

ohe=preprocessing.OneHotEncoder()


country1=ohe.fit_transform(country1).toarray()


result=pd.DataFrame(data=country1,index=range(22),columns=['af','usa','uk'])
print(result)
