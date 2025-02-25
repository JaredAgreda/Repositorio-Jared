# matriz bidimensional (3x3)
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i, fila in enumerate(matriz):
        if valor in fila:
            return f"El valor {valor} fue encontrado en la posición ({i}, {fila.index(valor)})."
    return f"El valor {valor} no fue encontrado en la matriz."


valor_a_buscar = 50

# Llamamos a la función y mostramos el resultado
print(buscar_valor(matriz, valor_a_buscar))