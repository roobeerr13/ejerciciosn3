def restar_polinomios(p1, p2):
    return {k: p1.get(k, 0) - p2.get(k, 0) for k in set(p1) | set(p2)}

def dividir_polinomios(p1, p2):
    if not p2:
        raise ValueError("No se puede dividir por un polinomio vacío.")
    grado_p1 = max(p1.keys())
    grado_p2 = max(p2.keys())
    return grado_p1 - grado_p2  # Simplificación de división

def eliminar_termino(p, termino):
    if termino in p:
        del p[termino]

def existe_termino(p, termino):
    return termino in p

# Ejemplo
polinomio1 = {2: 3, 1: 2, 0: -1}
polinomio2 = {1: 5, 0: 3}

print("Resta de polinomios:", restar_polinomios(polinomio1, polinomio2))
print("División de polinomios (simplificada):", dividir_polinomios(polinomio1, polinomio2))
eliminar_termino(polinomio1, 2)
print("Polinomio después de eliminar el término 2:", polinomio1)
print("¿Existe el término 1 en el polinomio1?", existe_termino(polinomio1, 1))
