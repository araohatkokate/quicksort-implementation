import sys
import random
import time
import matplotlib.pyplot as plt

# Increase recursion limit
sys.setrecursionlimit(10000)

# Iterative version of quicksort (non-random pivot)
def quicksort_iterative(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = arr[end]
        left = start
        right = end - 1

        while left <= right:
            if arr[left] <= pivot:
                left += 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1

        arr[left], arr[end] = arr[end], arr[left]

        stack.append((start, left - 1))
        stack.append((left + 1, end))

    return arr

# Helper functions to generate best, worst, and average cases
def generate_best_case(n):
    return list(range(n))

def generate_worst_case(n):
    return list(range(n, 0, -1))

def generate_average_case(n):
    return [random.randint(0, n) for _ in range(n)]

# Benchmarking function
def benchmark_quicksort():
    input_sizes = [100, 500, 1000, 5000]
    best_case_times = []
    worst_case_times = []
    average_case_times = []
    
    for n in input_sizes:
        # Best case (already sorted)
        best_case = generate_best_case(n)
        start_time = time.time()
        quicksort_iterative(best_case)
        best_case_times.append(time.time() - start_time)
        
        # Worst case (reverse sorted)
        worst_case = generate_worst_case(n)
        start_time = time.time()
        quicksort_iterative(worst_case)
        worst_case_times.append(time.time() - start_time)
        
        # Average case (random inputs)
        average_case = generate_average_case(n)
        start_time = time.time()
        quicksort_iterative(average_case)
        average_case_times.append(time.time() - start_time)
    
    # Plotting the results
    plt.plot(input_sizes, best_case_times, label='Best Case')
    plt.plot(input_sizes, worst_case_times, label='Worst Case')
    plt.plot(input_sizes, average_case_times, label='Average Case')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Quicksort Non-Random Pivot Performance (Iterative)')
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig('quicksort_benchmark.png')  # You can specify the path here
    plt.show()

# Run benchmark
benchmark_quicksort()
