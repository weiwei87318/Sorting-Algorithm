from random import randint

data = []

for i in range(10):
    value = randint(0,100)
    data.append(value)
print("Unsorted:",data)

def SelectionSort(data):
    n = len(data)
    for i in range(n-1): 
        min_index = i
        for j in range(i+1,n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

SelectionSort(data)
print("Sorted:", data)