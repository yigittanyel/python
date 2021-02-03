import numpy as np
a=np.array([[1,2,3],[4,5,6]]) #array oluşturma işlemi
print(a)
print(a.dtype) #data tipini verir
print(a.ndim) #arrayin boyutunu verir
 

#%% RESHAPE SHAPE
print(a.shape) #2,3 yazar.
a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
a1=a1.reshape(3,5)
print(a1)

#%% ARANGE LİNSPACE
a2=np.arange(0,20,5)
print(a2)
a2=np.linspace(11,30, 14)
print(a2)

#%% RANDOM
a3=np.random.randint(10,size=15)
print(a3)

a4=np.random.random((3,2))
print(a4)

#%% SATIR - SÜTUN ELEMANLARA ERİŞME
birinci_satir=a1[0]
ikinci_satir=a1[1]
ilk_iki_satir=a1[0:2]
print(ilk_iki_satir)

print("-------")

birinci_sutun=a1[:,0]
ikinci_sutun=a1[:,1]
ilk_iki_sutun=a1[:,0:2]
print(ilk_iki_sutun)

#%%ZEROS-ONES  - EYE(BİRİM)
a4=np.zeros((2,3))
print(a4)
print("-----------")
a5=np.ones((2,3))
print(a5)
print("-----------")
a6=np.eye(3)
print(a6)

#%%CONCANATE BİRLEŞTİRME
a7=np.array([[1,2,3],
            [4,5,6]])

a8=np.array([[7,8,9],
            [10,11,12]])

a9=np.concatenate([a7,a8]) #,axis=1 yaparsak yan yana birleştirir.
print(a9)

#%%MAX MİN SUM MEAN(ORT) STANDART SAPMA VARYANS EXP
a1=np.array([[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15]])
print(a1.max())
print(a1.min())
print(a1.sum())
print("Ortalama: ",a1.mean())
satirların_toplamı=a1.sum(axis=1);
sutunların_toplamı=a1.sum(axis=0)
print(satirların_toplamı)
print(sutunların_toplamı)

print("Varyans: ",a1.var())
print("Standart Sapma",a1.std())

islem=np.sin(a1)
islem2=np.cos(a1)
islem3=np.sqrt(a1)
islem4=a1[1]+2
islem5=np.exp(a1) # e üzeri işlem
islem6=np.log(a1)
islem7=np.square(a1)
print("Sin: ",islem)
print("Cos: ",islem2)
print("Karekök: ",islem3)
print("Matrise 2 ekleme: \n",islem4)
print("E üzeri işlem: \n",islem5)
print("10 tabanında log: \n",islem6)
print("Karesi: \n",islem7)
#%% MATRİS ÇARPIMI TRANSPOZ ALMA
#transpoz: sutunlar satır satırlar sutun olur.
a1=np.array([[1,2,3],
            [4,5,6]])
a2=np.array([[7,8],
             [9,10],
             [11,12]])
carpim=np.dot(a1,a2) #a.dot(b.T) de olurdu.
transpoz=a1.T
print(carpim)
print(transpoz)

#%%KOŞULLAR
a1=np.array([[1,2,3],
            [4,5,6]])
kosul=a1>3
print(kosul)
hangileri_buyuk=a1[a1>3]
print(hangileri_buyuk)

#%%KAYDETMEK
a1=np.array([[1,2,3],
            [4,5,6]])
np.save("save",a1)

#%% INDEXING SLICING REVERSE ARRAY
a1=np.array([1,2,3,4,5,6,7])
print(a1[0:3])

a2=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

reverse_array=a1[::-1]
print(reverse_array)

print("Yaz: \n",a2[:,0:2]) #satırların hepsi sutunlardan ılk ikisi

#SON SATIR -> print(-1,:)
#SON SUTUN -> print(:,-1)

#%%MATRİSİ DÜZ HALE GETİRME - 

a2=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
a=a2.ravel()
print(a)
#ESKİ HAL -> a3=a.reshape(3,3)

#%%   ARRAY BİRLEŞTİRME
a1=np.array([[1,2,3],
            [4,5,6]])
a2=np.array([[7,8,9],
             [10,11,12]])

a3=np.vstack((a1,a2)) #VERTICAL(DIKEY)
a4=np.hstack((a1,a2)) #HORIZONTAL(YATAY)
print(a3)
print(a4)














