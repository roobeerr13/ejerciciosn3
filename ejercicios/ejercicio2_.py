import numpy as np

def determinante_recursivo(matriz):
    if len(matriz) == 1:
        return matriz[0][0]
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    det = 0
    for i in range(len(matriz)):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        det += ((-1) ** i) * matriz[0][i] * determinante_recursivo(submatriz)
    return det

def determinante_iterativo(matriz):
    matriz_np = np.array(matriz)
    return round(np.linalg.det(matriz_np), 2)
