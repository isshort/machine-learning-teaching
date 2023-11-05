
import pandas as pd
import numpy as np1


 
missing_data=pd.read_csv('mising_data.csv')

print(missing_data)


age=missing_data.iloc[:,1:4].values


from sklearn.impute import SimpleImputer

impute=SimpleImputer(strategy='mean',missing_values=np1.nan)



impute=impute.fit(age) 

age=impute.transform(age)


 
from sklearn import preprocessing 

# label encoder af=0 ,usa=2, uk=1
le=preprocessing.LabelEncoder()


country=missing_data.iloc[:,0:1].values



ohe=preprocessing.OneHotEncoder()


country=ohe.fit_transform(country).toarray()

print(country)
 

gender=missing_data.iloc[:,-1].values
print(len(gender))

country_result=pd.DataFrame(data=country,index=range(22),columns=['af','usa','uk'])

age_weight_height_result=pd.DataFrame(data=age,index=range(22),columns=['weight','height','age'])

print(age_weight_height_result)


gender_result=pd.DataFrame(data=gender,index=range(22),columns=['gender'])



numrical_result=pd.concat([country_result,age_weight_height_result],axis=1)


final_result=pd.concat([numrical_result,gender_result],axis=1)





