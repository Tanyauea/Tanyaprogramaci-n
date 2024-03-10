
# Definir una matriz pequeña (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimir la matriz
print("Matriz original:")
for fila in matriz:
    print(fila)

# Calcular la suma de todos los elementos de la matriz
suma_total = sum(sum(fila) for fila in matriz)

# Imprimir la suma total
print("\nLa suma de todos los elementos de la matriz es:", suma_total)
# Encontrar la posicion 4
print("laposicion 4",matriz[2],[2])








