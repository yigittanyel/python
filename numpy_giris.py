import numpy as np
a=np.array([[1,2,3],[4,5,6]]) #array oluşturma işlemi
print(a)
print(a.dtype) #data tipini verir
print(a.ndim) #arrayin boyutunu verir
 

#%% SLICING
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) #2 4
print(arr[::2])   # 1 3 5 7

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
#%% VERİ TÜRÜ DÖNÜŞÜMÜ
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#%% DİZİLERİ DÜZLEŞTİRME / YENİDEN BOYUTLANDIRMA
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)
print("---------------------")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1) #bilinmeyen boyut.
print(newarr)
#%% RESHAPE SHAPE
a1=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
a1=a1.reshape(3,5)
print(a1)

print("--------------")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2) #2 tane 3 satır 2 sutun dizi yap 3 boyutlu.
print(newarr)

#%%MATRİSİ DÜZ HALE GETİRME - 

a2=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
a=a2.ravel()
print(a)
#ESKİ HAL -> a3=a.reshape(3,3)
#%% FOR İLE DİZİLERİ GÖRÜNTÜLEMEK
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

print("---------------")
for x in arr:
    for y in x:
        print(y)
        
#Bu da iç içe döngünün aynısını yapar:
arr4 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr4):
  print(x)
  
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# for x in np.nditer(arr[:, ::2]):
#   print(x)  BURASI DA BİRLEŞTİRİR nditer ile ondan sonra da çıktı olarak 1 3 5 7 döner.

#NUMARALANDIRILMIŞ YİNELEME
arr5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr5): #(0, 0) 1 (0,1) 2 vs.
  print(idx, x)


#%% COPY / VİEW
#view yapılan değişiklikten etkilenirken copy etkilenmez.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
b=arr.view()
arr[0] = 42

print(arr) # [42  2  3  4  5]
print(x)   # [1 2 3 4 5]
print(b)   #[42  2  3  4  5]
print("--------------------")
print(x.base) #copy
print(b.base) #view
#EĞER NONE DONERSE COPY DİZİNİN KENDİSİ DONERSE VİEW'dir.


#%% ARANGE LİNSPACE
a2=np.arange(0,20,5) #0 5 10 15 20 DAHİL DEĞİL!
print(a2)
a2=np.linspace(11,30, 14)
print(a2)

#%% RANDOM
a3=np.random.randint(12,size=15) #max 12 olacak şekilde 15 random sayı
print(a3)

a4=np.random.random((3,2)) #3 satır 2 sutun
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
a4=np.zeros((2,3)) #0 0 0
print(a4)
print("-----------")
a5=np.ones((2,3)) #1 1 1 
print(a5)
print("-----------")
a6=np.eye(3) #birim matris
print(a6)

#%%CONCANATE BİRLEŞTİRME
a7=np.array([[1,2,3],
            [4,5,6]])

a8=np.array([[7,8,9],
            [10,11,12]])

a9=np.concatenate([a7,a8]) #,axis=1 yaparsak yan yana birleştirir.
print(a9)

#%%   ARRAY BİRLEŞTİRME
a1=np.array([[1,2,3],
            [4,5,6]])
a2=np.array([[7,8,9],
             [10,11,12]])

a3=np.vstack((a1,a2)) #VERTICAL(DIKEY)   #axis=0 gibi işlem görür.
a4=np.hstack((a1,a2)) #HORIZONTAL(YATAY) #axis=1 gibi işlem görür.
print(a3)
print("--------------------------")
print(a4)
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
#%%KAYDETMEK
a1=np.array([[1,2,3],
            [4,5,6]])
np.save("save",a1)
#%% SPLIT ile diziyi bölme
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 5)

print(newarr)  #  [array([1, 2]), array([3, 4]), array([5]), array([6])]

#%% WHERE KOMUTU
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0) #1 3 5 7

print(x)

        
#%% SEARCH SORTED ile sıralamada nereye gelmesi gerektiği.
import numpy as np

arr = np.array([6, 2, 9, 7])

x = np.searchsorted(arr, 7) #2

print(x)

#%% SORT KOMUTU İLE SIRALAMA
import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr2 = np.array([True, False, True])

print(np.sort(arr2)) #FALSE TRUE TRUE

#%%KOŞULLAR
a1=np.array([[1,2,3],
            [4,5,6]])
kosul=a1>3
print(kosul)
hangileri_buyuk=a1[a1>3]
print(hangileri_buyuk)

#%% FILTRE
import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = []
for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print("---------------------------")

arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []

for element in arr2:
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr2[filter_arr]

print(filter_arr)
print(newarr)
print("-------------------")

arr3 = np.array([41, 42, 43, 44])

filter_arr = arr3 > 42

newarr = arr3[filter_arr]

print(filter_arr)
print(newarr)







