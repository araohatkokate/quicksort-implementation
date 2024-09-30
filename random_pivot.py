import random

from non_random_pivot import partition_non_random

def quicksort_random(arr, low, high):
    if low < high:
        pi = partition_random(arr, low, high)
        quicksort_random(arr, low, pi - 1)
        quicksort_random(arr, pi + 1, high)

def partition_random(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[rand_pivot], arr[high] = arr[high], arr[rand_pivot]
    return partition_non_random(arr, low, high)
