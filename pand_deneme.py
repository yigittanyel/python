import pandas as pd
dict={"Name":["Yiğit","Semih","Yusuf","Ayşe","Fatma"],
      "Age":[21,9,5,27,34],
      "Salary":[100,50,75,145,300]}
dataFr=pd.DataFrame(dict,index=["1. Kişi ","2. Kişi ","3. Kişi","4. Kişi","5. Kişi"])
#print(dataFr.iloc[0])
#maaşı 200den az yaşı 20 den büyük olanlar
a=dataFr.Salary<200
b=dataFr.Age>20
#print(dataFr[a&b])

#print(dataFr.describe())
dataFr.columns=[each.lower() for each in dataFr.columns]
ort_maas=dataFr.salary.mean()
dataFr["Maas_Durumu"]=["yuksek" if ort_maas<each else "dusuk" for each in dataFr.salary]
ort_yas=dataFr.age.mean()
dataFr["Yas_Durumu"]=["Yaslı" if ort_yas<each else "genc" for each in dataFr.age]
dataFr.drop(["Yas_Durumu"],axis=1,inplace=True)












