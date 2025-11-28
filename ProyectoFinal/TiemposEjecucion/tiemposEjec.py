import random
import time

# ------------------------------
# Bubble Sort
# ------------------------------
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# ------------------------------
# Selection Sort
# ------------------------------
def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# ------------------------------
# Merge Sort
# ------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    resultado = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

# ------------------------------
# Stupid Sort (Bogo Sort)
# ------------------------------
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def stupid_sort(arr):
    #import random
    a = arr.copy()
    while not is_sorted(a):
        random.shuffle(a)
    return a

# ------------------------------
# Medición de tiempos
# ------------------------------
def medir_tiempo(func, lista):
    inicio = time.perf_counter()
    func(lista)
    fin = time.perf_counter()
    return fin - inicio

# ==============================
# PROGRAMA PRINCIPAL
# ==============================
n = 1

for i in range(5):
    n*=10
    lista = [random.randint(0, 10000) for _ in range(n)]
    print("N =", n)
    print("Midiendo tiempos...\n")

    print(f"Merge Sort:      {medir_tiempo(merge_sort, lista):.6f} segundos")
    print(f"Selection Sort:  {medir_tiempo(selection_sort, lista):.6f} segundos")
    print(f"Bubble Sort:     {medir_tiempo(bubble_sort, lista):.6f} segundos")

    # Stupid sort solo funciona con listas MUY pequeñas
    lista_pequena = [random.randint(0, 20) for _ in range(6)]
    print(f"Stupid Sort (6 elementos): {medir_tiempo(stupid_sort, lista_pequena):.6f} segundos")

    print("================================================================\n")
