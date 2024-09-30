def quicksort_non_random(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        return quicksort_non_random(left) + [pivot] + quicksort_non_random(right)

# Test
'''if __name__ == "__main__":
    arr = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", arr)
    print("Sorted array with non-random pivot:", quicksort_non_random(arr))'''

