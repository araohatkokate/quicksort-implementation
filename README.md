# Quicksort Implementation Benchmark

This project implements an iterative version of the Quicksort algorithm using a **non-random pivot** (the last element) for partitioning. The code benchmarks the performance of Quicksort for three different cases:
- **Best Case**: The input array is already sorted.
- **Worst Case**: The input array is also sorted, but since the last element is used as the pivot, this results in highly unbalanced partitions, leading to the worst-case performance.
- **Average Case**: The input array consists of randomly generated elements, representing the typical performance of Quicksort.

The benchmark runs multiple input sizes and measures the time taken to sort the arrays for each case. Results are printed in tabular format and plotted as a graph, which is saved as a PNG file.

## Running the Benchmark

To run the benchmark and generate the results:

1. Clone this repository and navigate to the directory:
  
2. Run the benchmark script:

3. After the script runs, you will see the timing results printed in the terminal, and a PNG file named `quicksort_benchmark_fixed_pivot.png` will be saved in the current directory.


The graph generated for this benchmark is saved as `quicksort_benchmark_fixed_pivot.png`.

## Quicksort Complexity Analysis

### Mathematical Derivation of Average Runtime Complexity (Non-Random Pivot)

The **average time complexity** of the Quicksort algorithm with a **non-random pivot** (i.e., the last element is always used as the pivot) is derived as follows:

1. **Partitioning Step**:
   Each time Quicksort runs, it selects a pivot and divides the array into two parts: elements less than or equal to the pivot, and elements greater than the pivot. This process requires \(O(n)\) comparisons because each element is compared to the pivot once.

2. **Recursive Depth**:
   In the **average case**, the pivot splits the array into two roughly equal halves. On average, the partitioning divides the array such that approximately half the elements are on either side of the pivot. This creates a recursion tree with depth \(O(\log n)\).

3. **Total Work**:
   At each level of recursion, the algorithm makes \(O(n)\) comparisons. Since the recursion depth is \(O(log n)\), the total time complexity for the average case is:

   \[
   T(n) = O(n log n)
   \]

### Worst Case Complexity

The **worst-case time complexity** occurs when the pivot does not split the array evenly, and instead, one of the partitions is nearly empty. For example, in a sorted array, the last element (pivot) will always result in one partition containing \(n - 1\) elements, and the other partition containing zero elements. This leads to a recursion tree with \(n\) levels, each doing \(O(n)\) work, resulting in a total time complexity of:

\[
T(n) = O(n^2)
\]

### Best Case Complexity

In the **best case**, the pivot perfectly splits the array into two equal halves at each level of recursion. This results in a balanced recursion tree with \(O(\log n)\) levels, and each level requires \(O(n)\) work for partitioning. Therefore, the best-case time complexity is:

\[
T(n) = O(n log n)
\]

## Further Considerations

- **Space Complexity**: The iterative version of Quicksort implemented here has a space complexity of \(O(log n)\) due to the stack used to keep track of the subarray boundaries.
- **Improvements**: In real-world applications, randomizing the pivot selection (instead of using the last element) can help mitigate the worst-case performance and ensure that the algorithm runs in \(O(n log n)\) time for most inputs.



