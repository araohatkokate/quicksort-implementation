# Quicksort Implementation Benchmark

This project implements an iterative version of the Quicksort algorithm using a **fixed pivot** (the last element) for partitioning. The code benchmarks the performance of Quicksort for three different cases:
- **Best Case**: The input array is already sorted.
- **Worst Case**: The input array is also sorted, but since the last element is used as the pivot, this results in highly unbalanced partitions, leading to the worst-case performance.
- **Average Case**: The input array consists of randomly generated elements, representing the typical performance of Quicksort.

The benchmark runs multiple input sizes and measures the time taken to sort the arrays for each case. Results are printed in tabular format and plotted as a graph, which is saved as a PNG file.

## Running the Benchmark

To run the benchmark and generate the results:

1. Clone this repository and navigate to the directory:
  
2. Run the benchmark script:

3. After the script runs, you will see the timing results printed in the terminal, and a PNG file named `quicksort_benchmark_fixed_pivot.png` will be saved in the current directory.

