from Punto1.src.StoogeSort import stooge_sort
import random

def test_stooge_sort(array_size):
    arr = [random.randint(1, 1000) for _ in range(array_size)]
    print(f"Original array: {arr}")
    stooge_sort(arr, 0, len(arr) - 1)
    print(f"Sorted array: {arr}")
    print()

# Realizar pruebas con arreglos aleatorios de diferentes tamaños
test_stooge_sort(10)
test_stooge_sort(100)
test_stooge_sort(1000)
test_stooge_sort(10000)