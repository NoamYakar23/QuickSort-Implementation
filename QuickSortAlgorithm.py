import numpy as np
import random
import matplotlib.pyplot as plt
temp = 0
temp2 = 0

def generate_random_array():
    arr = []
    for i in range(10):
        x = random.randint(0,100)
        arr.append(x)
    return arr
def partition_func(array, low_val, high_val):
    pivot = array[high_val]
    i = low_val - 1
    for j in range(low_val, high_val):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high_val] = array[high_val], array[i+1]
    return i + 1

def quicksort(array, low_val, high_val):
    if low_val < high_val:
        y = partition_func(array, low_val, high_val)
        quicksort(array, low_val, high_val-1)
        quicksort(array, low_val+1, high_val)





array = generate_random_array()
print(array)
quicksort(array,0, len(array)-1)
print(array)
