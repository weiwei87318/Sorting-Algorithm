from random import randint

data = []

for i in range(10):
    value = randint(0,100)
    data.append(value)
print("Unsorted:",data)

def partition(start, end, data):
    pivot_index = start
    pivot = data[pivot_index]
    while start < end:
        #Increment the start pointer till it finds an element greater than pivot
        while start < len(data) and data[start] <= pivot:
            start += 1
        #Decrement the end pointer till it finds an element less than pivot
        while data[end] > pivot:
            end -= 1
        #If start and end have not crossed each other , swap the numbers
        if(start < end):
            data[start], data[end] = data[end], data[start]
    data[end], data[pivot_index] = data[pivot_index], data[end]
    return end

def QuickSort(start, end, data):
    if(start < end):
        pivot = partition(start, end, data) # returns the end pointer to divide the array into 2
        #Sort the elements before partition and after partition
        QuickSort(start, pivot - 1, data)
        QuickSort(pivot + 1, end, data)
        

QuickSort(0, len(data) - 1, data)
print("Sorted:",data)    
