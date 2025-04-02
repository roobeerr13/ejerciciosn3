def mover_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover piedra de {origen} a {destino}")
    else:
        mover_hanoi(n - 1, origen, destino, auxiliar)
        print(f"Mover piedra de {origen} a {destino}")
        mover_hanoi(n - 1, auxiliar, origen, destino)