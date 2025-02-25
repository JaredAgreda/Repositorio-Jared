# Definición de la matriz bidimensional (3x3)
matriz = [
    [30, 10, 20],
    [60, 50, 40],
    [90, 70, 80]
]

# Función para ordenar una fila usando Bubble Sort
def ordenar_fila(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar elementos
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Función para ordenar todas las filas de la matriz
def ordenar_matriz(matriz):
    for fila in matriz:
        ordenar_fila(fila)

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la matriz
ordenar_matriz(matriz)

# Mostrar la matriz ordenada
print("\nMatriz ordenada :")
for fila in matriz:
    print(fila)