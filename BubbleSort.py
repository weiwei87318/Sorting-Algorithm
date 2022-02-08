from dataclasses import dataclass
from random import seed
from random import randint
 
seed(1)
data = []

for i in range(10):
    value = randint(0,100)
    data.append(value)
print("Unsorted:",data)

def BubbleSort(data):
    n = len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

BubbleSort(data)
print("Sorted:",data)
