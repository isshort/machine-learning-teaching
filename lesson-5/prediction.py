#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 22:06:22 2023

@author: nematullah
"""

import numpy as np
import pandas as pd


data=pd.read_csv('sales.csv')



x=data.iloc[:,:1].values

y=data.iloc[:,1:].values


from sklearn.model_selection import train_test_split 


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


from sklearn.preprocessing import StandardScaler


sc=StandardScaler()

x_train_sc=sc.fit_transform(x_train)
x_test_sc=sc.fit_transform(x_test)

y_train_sc=sc.fit_transform(y_train)
y_test_sc=sc.fit_transform(y_test)



from sklearn.linear_model import LinearRegression

le=LinearRegression()

le.fit(x_train, y_train)

predict=le.predict(x_test)



import matplotlib.pyplot as plt


plt.scatter(x_train,y_train)

plt.plot(x_test,predict,'r')













