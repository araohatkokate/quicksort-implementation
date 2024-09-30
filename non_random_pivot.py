import time
import matplotlib.pyplot as plt

# Non-random pivot quicksort (last element as pivot)
def quicksort_non_random(arr, low, high):
    if low < high:
        pi = partition_non_random(arr, low, high)
        quicksort_non_random(arr, low, pi - 1)
        quicksort_non_random(arr, pi + 1, high)

def partition_non_random(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
