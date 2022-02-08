from random import randint

data = []

for i in range(10):
    value = randint(0,100)
    data.append(value)
print("Unsorted:",data)

def InsertionSort(data):
    n = len(data)
    for i in range(1,n):
        current = data[i]
        j = i - 1
        while j >= 0 and current < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = current

InsertionSort(data)
print("Sorted:", data)