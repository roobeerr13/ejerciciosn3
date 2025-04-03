def mover_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover piedra de {origen} a {destino}")
    else:
        mover_hanoi(n - 1, origen, destino, auxiliar)
        print(f"Mover piedra de {origen} a {destino}")
        mover_hanoi(n - 1, auxiliar, origen, destino)

def mover_hanoi_resumen(n, origen, auxiliar, destino, contador, limite=10):
    total_movimientos = (2**n) - 1  # Total de movimientos necesarios
    if n == 1:
        contador[0] += 1
        if contador[0] <= limite or contador[0] > total_movimientos - limite:
            print(f"Movimiento {contador[0]}: Mover piedra de {origen} a {destino}")
    else:
        mover_hanoi_resumen(n - 1, origen, destino, auxiliar, contador, limite)
        contador[0] += 1
        if contador[0] <= limite or contador[0] > total_movimientos - limite:
            print(f"Movimiento {contador[0]}: Mover piedra de {origen} a {destino}")
        mover_hanoi_resumen(n - 1, auxiliar, origen, destino, contador, limite)