import os
from ejercicios.ejercicio1 import mover_hanoi, mover_hanoi_resumen
from ejercicios.ejercicio2_ import determinante_recursivo
from ejercicios.ejercicio3__ import analizar_naves
from ejercicios.ejercicio4___ import restar_polinomios, dividir_polinomios

def limpiar_pantalla():
    """Limpia la consola para mostrar solo el menú principal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """Muestra el menú principal y devuelve la opción seleccionada."""
    print("=== Menú Principal ===")
    print("1. Ejercicio 1: Puzzle de la Pirámide de Piedras Preciosas")
    print("2. Ejercicio 2: El Secreto de la Cifra Mágica")
    print("3. Ejercicio 3: El Gran Rally Espacial")
    print("4. Ejercicio 4: La Matemática de los Encantamientos")
    print("5. Salir")
    opcion = input("Selecciona una opción (1-5): ").strip()
    return opcion

def ejecutar_ejercicio(opcion):
    """Ejecuta el ejercicio seleccionado por el usuario."""
    if opcion == "1":
        n = 74  # Número de piedras
        print(f"\nResolviendo el problema de las Torres de Hanói con {n} piedras...\n")
        
        mostrar_todo = input("¿Deseas ver todos los movimientos? (s/n): ").strip().lower()
        if mostrar_todo == "s":
            mover_hanoi(n, "Columna 1", "Columna 2", "Columna 3")
        else:
            contador = [0]  # Contador para rastrear los movimientos
            limite = 10  # Número de movimientos a mostrar al inicio y al final
            mover_hanoi_resumen(n, "Columna 1", "Columna 2", "Columna 3", contador, limite)
            print(f"\nTotal de movimientos realizados: {contador[0]}")
        
        # Conclusión del Ejercicio 1
        print("\n¡Felicidades! Has resuelto el Puzzle de la Pirámide de Piedras Preciosas.")
        print("El antiguo tesoro escondido ha sido descubierto.")
    elif opcion == "2":
        matriz_3x3 = [[2, 4, 1], [3, 1, 5], [0, 2, 3]]
        print(f"Determinante (Recursivo): {determinante_recursivo(matriz_3x3)}")
    elif opcion == "3":
        analizar_naves()
    elif opcion == "4":
        polinomio1 = {2: 3, 1: 2, 0: -1}
        polinomio2 = {1: 5, 0: 3}
        print("Resultado de la resta:", restar_polinomios(polinomio1, polinomio2))
        print("Resultado de la división:", dividir_polinomios(polinomio1, polinomio2))
    elif opcion == "5":
        print("¡Hasta luego!")
        exit()
    else:
        print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    while True:
        limpiar_pantalla()  # Limpia la consola antes de mostrar el menú
        opcion = menu_principal()
        ejecutar_ejercicio(opcion)
        input("\nPresiona Enter para continuar...")  # Pausa antes de limpiar la pantalla