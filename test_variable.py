
#With otomatik olarak resource allocation'unu bırakır
# örn. normalde File open yaptıktan sonra File close yapmamız gerekir.
#Yada file open yaptıktan sonra exceğti



#-------------------------
# Generators comprehensions
#Eğer milyarlık bir değişken setimiz var ise, bunu oluşturup memory'de gereksiz yer işgal etmek istemeyiz
#bu sebeple her iterasyonda generate etmek daha mantıklı (stream etmek gibi ama değil)

values = (x * 2 for x in range(10))
print(values) #bize bisey donmez, sadece generator oldugunu soyler print cıktısında

#ama loop edersek değerleri ekrana basar
for x in values:
    print(x)

#get size of generator
from sys import getsizeof

values = (x * 2 for x in range(10000))
print("gen:", getsizeof(values))
# **** list comprehension kullansaysdık hayvan gibi memory siserdi
values = [x * 2 for x in range(10000)]
print("gen:", getsizeof(values))

print(len(values)) #hata verir alamayız dezavantajı bu

#-------------------------



#-------------------------
# List comprehensions

#Standary yontem
values = []
for x in range(5):
    values.append(x*2)

#Standart yomtemin daha guzel hali 
# [expression for item in items] -- > pattern bu aslında
#expression ne yapmak istiyorsın
#gerisi for loop'u doldurma

#List olarak tanımlamak istersek
values = [x*2 for x in range(5)]
print(values)

#Set olarak tanımlamak istersek
values = {x*2 for x in range(5)}
print(values)

#Dictionary olarak tanımlamak istersek
values = {x: x*2 for x in range(5)}
print(values)


#Tuple olarak tanımlamak istersek ???
#values = {x: x*2 for x in range(5)}
#print(values)

#-------------------------



#-------------------------
#Dictionary

sample_dict = {"x":1,"y":2} #dictionary tanımlama
sample_dict = dict(x=1,y=2) #dictionary tanımlama

#Dictionary'lere key ile access ederiz.
sample_dict["x"] = 10
sample_dict["z"] = 20 # dictionary'ye yeni eleman ekleme
print(sample_dict)

#Hata almamak için bu sekilde search ediyoruz dictionary'i
if "a" in sample_dict:
    print(sample_dict["a"])

#Yada bu sekilde ararız, bulamazsa None doner
print(sample_dict.get("a"))
#Yada bu sekilde ararız, bulamazsa 0 doner
print(sample_dict.get(("a"),0 ))

#delete item
del sample_dict["x"]
print(sample_dict)

#Loop dictionary v1
for key in sample_dict:
    print(key, sample_dict[key])

#Loop dictionary v2
for x in sample_dict.items():
    print(x)
    print(x[0],"-",x[1])

#Loop dictionary v2.1 bence boyle daha guzel
for key, value in sample_dict.items():
    print(key, value)

#-------------------------

#-------------------------
#Queue kullanımı: FIFO islemlerinde list'in ilk elemanını çıkartman
# sonraki elemanların sırasını bir adım ilerletmek cok maliyetli
#Bu sebepten queue kullanmalıyız

from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft() # ilk sıradakini alir ve queueden siler
print(queue)
if not queue:
    print(empty)

#-------------------------


#-------------------------
#Complex List Sorting
items = [ 
            ("Product1", 10),
            ("Product2", 9),
            ("Product3", 12)
        ]

items.sort(key=lambda item: item[1])
print(items)
#-------------------------


#-------------------------
#Get values into a list from Complex List
#** Map function ile daha guzel yapabiliriz.

items = [ 
            ("Product1", 10),
            ("Product2", 9),
            ("Product3", 12)
        ]

prices = [] 
for item in items:
    prices.append(item[1])   
print(prices)    
#-------------------------


#-------------------------
#Get values into a list from Complex List by Mapping and Lambda
items = [ 
            ("Product1", 10),
            ("Product2", 9),
            ("Product3", 12)
        ]


prices = list(map(lambda item: item[1], items))
print(prices)
#yada bu şekilde List comprehension olarak ta yazılabilir
prices = [item[1] for item in items]
print(prices)
#-------------------------


#-------------------------
#Get item values bigger than 10 with lambda and Filter method
items = [ 
            ("Product1", 10),
            ("Product2", 9),
            ("Product3", 12)
        ]

filtered = list(filter(lambda item: item[1] >= 10, items ))
print(filtered)
#yada bu şekilde List comprehension olarak ta yazılabilir
filtered = [item for item in items if item[1] >= 10]
print(filtered)

#-------------------------

#-------------------------
#Get item values bigger than 10 with lambda and Filter method
items = [ 
            ("Product1", 10),
            ("Product2", 9),
            ("Product3", 12)
        ]

filtered = list(filter(lambda item: item[1] >= 10, items ))
print(filtered)
#-------------------------

#-------------------------
#Combine multiple list objects side by side
list1 = [ 1,2,3]
list2 = [10,20,30]

print(list(zip("abc",list1,list2)))
#-------------------------

#-------------------------
#Sorting Lists
numbers = [3,65,6,4]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#Orjinal liste kalsın ancak yeni bir liste olarak sort olsun dersek
print(sorted(numbers))

#-------------------------------
#Check if an item in list !!!! if the value is not in list we get exception 
letters = ["a","b","c","f",",t","c","e"]
print(letters.index["w"]) #exceptipn atar, boyle aramamalıyız

    #Yontem 1
if "w" in letters:
    print(letters.index("d"))

    #Yontem 2
print(letters.count("w"))
#-------------------------------

#-------------------------------
#remove a specific value (single value) from a list
letters = ["a","b","c","f",",t","c","e"]

letters.remove("c") #removes first item found in list
print(letters)
#-------------------------------


#-------------------------------
#remove a range of items in list by index
letters = ["a","b","c","f",",t","c","e"]
del letters[0:3]
print(letters)
#-------------------------------

#Multiply array of numbers
"""
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(1,2,3))
"""


#Globl Value issue
"""
global counter
counter = 0

def changeMessage():
   global counter +=1

changeMessage()

print(counter)
"""