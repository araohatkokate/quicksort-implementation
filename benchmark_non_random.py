import random
import time
import matplotlib.pyplot as plt

def quicksort_fixed(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition_fixed(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def partition_fixed(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def benchmark_quicksort_fixed(array_sizes):
    best_case_times = []
    worst_case_times = []
    average_case_times = []

    for n in array_sizes:
        best_case_input = list(range(n))
        start_time = time.perf_counter()
        quicksort_fixed(best_case_input)
        best_case_times.append(time.perf_counter() - start_time)

        worst_case_input = list(range(n))  
        start_time = time.perf_counter()
        quicksort_fixed(worst_case_input)
        worst_case_times.append(time.perf_counter() - start_time)

        avg_times = []
        for _ in range(5):  
            average_case_input = [random.randint(0, n) for _ in range(n)]
            start_time = time.perf_counter()
            quicksort_fixed(average_case_input)
            avg_times.append(time.perf_counter() - start_time)
        average_case_times.append(sum(avg_times) / len(avg_times))

    print("\nFinal Benchmark Results:")
    print(f"{'Array Size':<12}{'Best Case Time (s)':<20}{'Worst Case Time (s)':<22}{'Average Case Time (s)'}")
    for i, n in enumerate(array_sizes):
        print(f"{n:<12}{best_case_times[i]:<20.6f}{worst_case_times[i]:<22.6f}{average_case_times[i]:<20.6f}")
    
    return best_case_times, worst_case_times, average_case_times


if __name__ == "__main__":
    array_sizes = [2000, 4000, 6000, 8000, 10000]
    best_case_times, worst_case_times, average_case_times = benchmark_quicksort_fixed(array_sizes)
    plt.plot(array_sizes, best_case_times, label='Best Case', marker='o')
    plt.plot(array_sizes, worst_case_times, label='Worst Case', marker='o')
    plt.plot(array_sizes, average_case_times, label='Average Case', marker='o')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Quicksort (Fixed Pivot) Benchmark - Iterative Version')
    plt.legend()
    plt.grid(True)
    plt.savefig('quicksort_benchmark_fixed_pivot.png')
