import random
from collections import Counter


def divide_y_venceras_moda(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_part = arr[:mid]
    right_part = arr[mid:]

    moda_izquierda = divide_y_venceras_moda(left_part)
    moda_derecha = divide_y_venceras_moda(right_part)

    if moda_izquierda == moda_derecha:
        return moda_izquierda

    else:
        frecuencias = Counter(arr)
        max_frecuencia = max(frecuencias.values())
        modas = [elemento for elemento, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
        return modas