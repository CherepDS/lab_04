import sys
import random

sys.setrecursionlimit(10**5)

# Сортировка вставками
def insertion_sort(arr):
    res = arr.copy()
    for i in range(1, len(res)):
        key = res[i]
        j = i-1
        while (j >= 0 and res[j] > key):
            res[j+1] = res[j]
            j -= 1
        res[j+1] = key
    return res

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr)//2]

        equal = []
        less = []
        greater = []

        for item in arr:
            if item < pivot:
                less.append(item)
            elif item > pivot:
                greater.append(item)
            else:
                equal.append(item)

        return quick_sort(less) + [pivot] + quick_sort(greater)