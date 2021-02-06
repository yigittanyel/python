import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv")
print(df.columns)
print(df.Species.unique()) # Tekrarsız verileri(eşsiz-unique) döndürür.
setosa=df[df.Species=="Iris-setosa"]
vert=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]
print("------------------------------------")
print(setosa.describe())
print(vert.describe())
print(virginica.describe())

df1=df.drop(["Id"],axis=1) #Id'ler görselleştirmede işimize yaramayacağı için drop edildi.

#%% LINE PLOT
plt.plot(setosa.Id,setosa.PetalLengthCm,color="blue",label="Setosa-PetalLengthCm")
plt.legend()
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()

df1.plot(grid=True,linestyle=":",alpha=0.5)
plt.show()

#%% SCATTER PLOT
setosa=df[df.Species=="Iris-setosa"]
vert=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="Setosa")
plt.scatter(vert.PetalLengthCm,vert.PetalWidthCm,color="green",label="Setosa")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="Setosa")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()

#%% HISTOGRAM

plt.hist(setosa.SepalLengthCm,bins=20)
plt.show()

#%% BAR PLOT
import numpy as np

a=np.array([1,2,3,4,5])
ulke=np.array(["france","usa","turkey","denmark","england"])
b=a*2+5

plt.bar(ulke,b)
plt.xlabel("Ulke")
plt.ylabel("Degerler")
plt.title(("Bar Plot"))
plt.legend()
plt.show()

















