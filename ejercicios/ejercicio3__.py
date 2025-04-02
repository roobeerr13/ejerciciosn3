naves = [
    {"nombre": "Cometa Veloz", "longitud": 20, "tripulacion": 5, "pasajeros": 12},
    {"nombre": "Titán del Cosmos", "longitud": 50, "tripulacion": 20, "pasajeros": 80},
    {"nombre": "GX300", "longitud": 10, "tripulacion": 3, "pasajeros": 6},
    {"nombre": "GX400", "longitud": 15, "tripulacion": 4, "pasajeros": 10},
]

def analizar_naves():
    naves_ordenadas = sorted(naves, key=lambda x: (x['nombre'], -x['longitud']))
    print("Lista ordenada por nombre y longitud:", naves_ordenadas)

    for nave in naves:
        if nave["nombre"] in ["Cometa Veloz", "Titán del Cosmos"]:
            print("Información específica:", nave)

    top_5_pasajeros = sorted(naves, key=lambda x: -x['pasajeros'])[:5]
    print("Top 5 naves con mayor pasajeros:", top_5_pasajeros)

    nave_tripulacion = max(naves, key=lambda x: x["tripulacion"])
    print("Nave con mayor tripulación:", nave_tripulacion)

    gx_naves = [nave for nave in naves if nave["nombre"].startswith("GX")]
    print("Naves que comienzan con 'GX':", gx_naves)

    seis_o_mas = [nave for nave in naves if nave["pasajeros"] >= 6]
    print("Naves con seis o más pasajeros:", seis_o_mas)

    mas_pequena = min(naves, key=lambda x: x["longitud"])
    mas_grande = max(naves, key=lambda x: x["longitud"])
    print("Nave más pequeña:", mas_pequena)
    print("Nave más grande:", mas_grande)
