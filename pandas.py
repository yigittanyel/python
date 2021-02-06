import pandas as pd
dict={"Name":["Ali","Veli","Efe","Mert","Alp","Ege"],
      "Age":[14,15,18,22,37,45],
      "Salary":[100,120,354,740,340,678]}
dataFr=pd.DataFrame(dict)

head=dataFr.head() #İLK 5
tail=dataFr.tail() #SON 5

print("Columns: \n",dataFr.columns)
print("Info: \n",dataFr.info())
print("Data types: \n",dataFr.dtypes)
print("Describe: \n",dataFr.describe())

#%% YENİ FEATURE EKLEME VE INDEXİNG-SLICING
dataFr["yeni_eklenen"]=[-1,-2,-3,-4,-5,-6]
print(dataFr.Age)
print(dataFr.loc[:3,"Name":"Salary"]) #loc: location
print("Salary:\n",dataFr.iloc[:,2]) #iloc: integer location

#NOT: 0:3 yazdığımızda Numpy'de 3 dahil değil,pandas'da 3 dahil yani inclusive

#%%
dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

print(dataFrame1.loc[3, ["AGE","NAME"]]) #age 33 name hilal 

#FILTERING / KOSULLAR
a=dataFr.Salary>200 
b= dataFr.Age<25
print("Filtrelenmiş data:\n",dataFr[a & b])


#%%ORTALAMA
import numpy as np
print("Ortalama maas: ",dataFr.Salary.mean())
print("Numpy ile: ",np.mean(dataFr.Salary))

#%%  List Comprehension
ort_maas=dataFr.SALARY.mean()
dataFr["maas_seviyesi"]=["yuksek" if ort_maas<each else "dusuk" for each in dataFr.SALARY]
dataFr.columns=[each.upper() for each in dataFr.columns]
dataFr["arada bosluk"]=[1,4,7,8,6,8]
#ARADA BOSLUK OLAN DEGELER İCİN:
dataFr.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFr.columns]


#%% DROP VE CONCATENATE
dataFr.columns=[each.lower() for each in dataFr.columns]
#dataFr.drop(["maas_seviyesi"],axis=1,inplace=True)
#dataFr.drop(["arada_bosluk"],axis=1,inplace=True)

data1 = dataFr.head()
data2 = dataFr.tail()

# vertical
data_concat = pd.concat([data1,data2],axis=0)


# horizontal

salary = dataFr.salary
age = dataFr.age

data_h_concat = pd.concat([salary,age],axis=1)


#%%TRANSFORMING DATA
dataFr.columns=[each.lower() for each in dataFr.columns]
dataFr["apply"]=[each*2 for each in dataFr.age]

def Multiply(age):
    return age*2
dataFr["apply metodu"]=dataFr.age.apply(Multiply)

