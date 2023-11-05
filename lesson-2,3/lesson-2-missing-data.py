#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:21:07 2023

@author: nematullah
"""


# library import 
import numpy as np
import pandas as pd

# data pre
mising_data=pd.read_csv('mising_data.csv')

from sklearn.impute import SimpleImputer

impute=SimpleImputer(missing_values=np.nan, strategy='mean')

age=mising_data.iloc[:,1:4].values

imputer=impute.fit(age)

age=imputer.transform(age)

print(age)

gender=mising_data.iloc[:3,4:5]

print(gender)

 
country=mising_data.iloc[:,0:1].values

print(country)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

country[:,0] = le.fit_transform(mising_data.iloc[:,0])

print(country)

ohe = preprocessing.OneHotEncoder()
country = ohe.fit_transform(country).toarray()
print(country)

print(list(range(22)))

result = pd.DataFrame(data=country, index = range(22), columns = ['af','usa','uk'])
print(result)

result2 = pd.DataFrame(data=age, index = range(22), columns = ['height','weight','age'])
print(result2)


gender=mising_data.iloc[:,-1].values
print(gender)

result3 = pd.DataFrame(data = gender, index = range(22), columns = ['gender'])
print(result3)


r1=pd.concat([result,result2], axis=1)
print(r1)

r2=pd.concat([r1,result3], axis=1)
print(r2)


'''
Ali =3 
Taheri = 6 
 3*6=18
 3+6 =9  
 Result = 9*18 = 162 * name
 Result= 162*3= 486. count of data
  
 Get the data after 
 9+18 = 27 
 Starting form 27’th row 
   	
Analysis this 

1. Get average of time 
2.  Find the most frequent time in the interval  

nematullahwahidi@hotmail.com


3. Convert categorical data to numerical data by label encoder
4. Convert categorical data to numerical data by One Hot encoder

'''

