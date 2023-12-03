import random
import time
from Punto3.src.QuickSort import quicksort
from Punto3.src.InsertionSort import insertion_sort
from Punto3.src.MergeSort import merge_sort
# Función para realizar la comparación
def compare_algorithms(array_sizes):
    results = []

    for size in array_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]

        # QuickSort
        start_time = time.time()
        quicksort(arr.copy())
        quicksort_time = time.time() - start_time

        # Insertion-Sort
        start_time = time.time()
        insertion_sort(arr.copy())
        insertion_sort_time = time.time() - start_time

        # Merge-Sort
        start_time = time.time()
        merge_sort(arr.copy())
        merge_sort_time = time.time() - start_time

        results.append((size, quicksort_time, insertion_sort_time, merge_sort_time))

    return results

# Realizar la comparación con diferentes tamaños de entrada
array_sizes = [10,50, 100, 500, 1000, 2000, 5000, 10000]
comparison_results = compare_algorithms(array_sizes)

# Imprimir los resultados en forma de tabla
print("{:<10} {:<15} {:<15} {:<15}".format("Size", "QuickSort", "Insertion-Sort", "Merge-Sort"))
for result in comparison_results:
    size, quicksort_time, insertion_sort_time, merge_sort_time = result
    print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(size, quicksort_time, insertion_sort_time, merge_sort_time))