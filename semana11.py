def ordenar_fila(matriz, fila):

    for i in range(len(matriz[fila])):
        for j in range(len(matriz[fila]) - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]


matriz = [[9, 11, 10],
    [12, 14, 13],
    [8, 6, 7]]

print("Matriz original:")
for fila in matriz:
    print(fila)
fila_a_ordenar = 1

ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)