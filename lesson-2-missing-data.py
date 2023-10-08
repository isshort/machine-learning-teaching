#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:21:07 2023

@author: nematullah
"""


import numpy as np
import pandas as pd


mising_data=pd.read_csv('mising_data.csv')

from sklearn.impute import SimpleImputer

impute=SimpleImputer(missing_values=np.nan, strategy='mean')

age=mising_data.iloc[:,1:4].values

imputer=impute.fit(age)

age=imputer.transform(age)

print(age)

gender=mising_data.iloc[:3,4:5]

print(gender)


basket_data=pd.read_csv('bread basket.csv')
print(basket_data)

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
3. Convert categorical data to numerical data by label encoder
4. Convert categorical data to numerical data by One Hot encoder

'''

