def mover_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover piedra de {origen} a {destino}")
    else:
        mover_hanoi(n - 1, origen, destino, auxiliar)  # Mueve n-1 discos al auxiliar
        print(f"Mover piedra de {origen} a {destino}")  # Mueve el disco más grande al destino
        mover_hanoi(n - 1, auxiliar, origen, destino)  # Mueve n-1 discos al destino