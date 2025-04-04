import numpy as np

def determinante_recursivo(matriz, nivel=0):
    indent = "  " * nivel  
    print(f"{indent}Calculando determinante de la matriz:")
    for fila in matriz:
        print(f"{indent}{fila}")

    if len(matriz) == 1:
        print(f"{indent}Determinante de matriz 1x1: {matriz[0][0]}")
        return matriz[0][0]
    if len(matriz) == 2:
        det = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        print(f"{indent}Determinante de matriz 2x2: {det}")
        return det

    det = 0
    for i in range(len(matriz)):
        submatriz = [fila[:i] + fila[i+1:] for fila in matriz[1:]]
        print(f"{indent}Expandiendo por el elemento {matriz[0][i]} en la columna {i}:")
        for subfila in submatriz:
            print(f"{indent}  {subfila}")
        subdet = determinante_recursivo(submatriz, nivel + 1)
        det += ((-1) ** i) * matriz[0][i] * subdet
        print(f"{indent}Contribución del elemento {matriz[0][i]}: {((-1) ** i) * matriz[0][i] * subdet}")
    print(f"{indent}Determinante calculado: {det}")
    return det

def determinante_iterativo(matriz):
    matriz_np = np.array(matriz)
    return round(np.linalg.det(matriz_np), 2)