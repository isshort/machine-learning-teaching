#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 22:15:03 2023

@author: nematullah
"""

import pandas as pd


#y=ax+b





data=pd.read_csv('data.csv')


x=data.iloc[:,1:4].values
y=data.iloc[:,4:].values

from sklearn.model_selection import train_test_split

# 0 1  0.33  %33
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=0)





