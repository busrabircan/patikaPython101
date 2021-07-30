""" 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı 
listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]"""

data=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = []
def flatten_list(data):
    for element in data:
        if type(element) == list:
             flatten_list(element)
        else:
             flat_list.append(element)
flatten_list(data)
print(flat_list)
       



""""2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
 Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]"""
boyut=int(input("Listenin boyutunu giriniz"))
for i in range(boyut):
    lst[i]=input("Elemanları giriniz:")
def Ters(lst): 
    lst.reverse() 
    return lst      
print(Ters(lst)) 
lst2=[[1, 2], [3, 4], [5, 6, 7]]
print(Ters(lst2))
