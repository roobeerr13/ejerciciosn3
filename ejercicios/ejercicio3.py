naves = [
    {"nombre": "Cometa Veloz", "longitud": 20, "tripulacion": 5, "pasajeros": 12},
    {"nombre": "Titán del Cosmos", "longitud": 50, "tripulacion": 20, "pasajeros": 80},
    {"nombre": "GX300", "longitud": 10, "tripulacion": 3, "pasajeros": 6},
    {"nombre": "GX400", "longitud": 15, "tripulacion": 4, "pasajeros": 10},
]

def analizar_naves():
    naves_ordenadas = sorted(naves, key=lambda x: (x['nombre'], -x['longitud']))
    print("\nLista ordenada por nombre y longitud:")
    for nave in naves_ordenadas:
        print(f"  - {nave}")

    print("\nInformación específica:")
    for nave in naves:
        if nave["nombre"] in ["Cometa Veloz", "Titán del Cosmos"]:
            print(f"  - {nave}")

    top_5_pasajeros = sorted(naves, key=lambda x: -x['pasajeros'])[:5]
    print("\nTop 5 naves con mayor pasajeros:")
    for nave in top_5_pasajeros:
        print(f"  - {nave}")

    nave_tripulacion = max(naves, key=lambda x: x["tripulacion"])
    print("\nNave con mayor tripulación:")
    print(f"  - {nave_tripulacion}")

    gx_naves = [nave for nave in naves if nave["nombre"].startswith("GX")]
    print("\nNaves que comienzan con 'GX':")
    for nave in gx_naves:
        print(f"  - {nave}")

    seis_o_mas = [nave for nave in naves if nave["pasajeros"] >= 6]
    print("\nNaves con seis o más pasajeros:")
    for nave in seis_o_mas:
        print(f"  - {nave}")

    mas_pequena = min(naves, key=lambda x: x["longitud"])
    mas_grande = max(naves, key=lambda x: x["longitud"])
    print("\nNave más pequeña:")
    print(f"  - {mas_pequena}")
    print("\nNave más grande:")
    print(f"  - {mas_grande}")