from ejercicios.ejercicio1 import mover_hanoi
from ejercicios.ejercicio2_ import determinante_recursivo
from ejercicios.ejercicio3__ import analizar_naves
from ejercicios.ejercicio4___ import restar_polinomios, dividir_polinomios

def menu_principal():
    print("=== Menú Principal ===")
    print("1. Ejercicio 1: Puzzle de la Pirámide de Piedras Preciosas")
    print("2. Ejercicio 2: El Secreto de la Cifra Mágica")
    print("3. Ejercicio 3: El Gran Rally Espacial")
    print("4. Ejercicio 4: La Matemática de los Encantamientos")
    print("5. Salir")
    opcion = input("Selecciona una opción (1-5): ").strip() 
    return opcion

def ejecutar_ejercicio(opcion):
    if opcion == "1":
        n = 3  
        mover_hanoi(n, "Columna 1", "Columna 2", "Columna 3")
    elif opcion == "2":
        matriz_3x3 = [[2, 4, 1], [3, 1, 5], [0, 2, 3]]
        determinante_recursivo(matriz_3x3)
    elif opcion == "3":
        analizar_naves()
    elif opcion == "4":
        polinomio1 = {2: 3, 1: 2, 0: -1}
        polinomio2 = {1: 5, 0: 3}
        restar_polinomios(polinomio1, polinomio2)
        dividir_polinomios(polinomio1, polinomio2)
    elif opcion == "5":
        exit()

if __name__ == "__main__":
    while True:
        opcion = menu_principal()
        ejecutar_ejercicio(opcion)