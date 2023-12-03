from Punto2.src.Moda import divide_y_venceras_moda
import random

def test_divide_y_venceras_moda(array_size):
    arr = [random.randint(1, 10) for _ in range(array_size)]
    print(f"Arreglo: {arr}")
    modas = divide_y_venceras_moda(arr)
    print(f"Moda(s): {modas}")
    print()

# Realizar pruebas con arreglos aleatorios de diferentes tamaños
test_divide_y_venceras_moda(10)
test_divide_y_venceras_moda(100)
test_divide_y_venceras_moda(1000)
test_divide_y_venceras_moda(10000)