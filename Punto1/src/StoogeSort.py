import random

def stooge_sort(arr, i, j):
    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
    if i + 1 >= j:
        return
    k = (j - i + 1) // 3
    stooge_sort(arr, i, j - k)
    stooge_sort(arr, i + k, j)
    stooge_sort(arr, i, j - k)