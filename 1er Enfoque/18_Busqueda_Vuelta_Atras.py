def es_valido(region, color, asignacion, vecinos):
    """
    Verifica si se puede asignar un color a una región
    sin romper las restricciones.
    """
    for vecino in vecinos[region]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True


def busqueda_vuelta_atras(regiones, colores, vecinos, asignacion):
    """
    Algoritmo de búsqueda de vuelta atrás.
    Intenta asignar colores a todas las regiones respetando restricciones.
    """

    # Caso base: si todas las regiones ya tienen color, se encontró solución
    if len(asignacion) == len(regiones):
        return asignacion

    # Elegir una región que todavía no tenga color asignado
    region_actual = None
    for region in regiones:
        if region not in asignacion:
            region_actual = region
            break

    # Probar cada color disponible
    for color in colores:
        if es_valido(region_actual, color, asignacion, vecinos):
            # Asignar color temporalmente
            asignacion[region_actual] = color

            # Llamada recursiva para continuar con las demás regiones
            resultado = busqueda_vuelta_atras(regiones, colores, vecinos, asignacion)

            # Si se encontró una solución, se regresa
            if resultado is not None:
                return resultado

            # Si no funcionó, se deshace la asignación
            del asignacion[region_actual]

    # Si ningún color funciona, se regresa None
    return None


# Regiones del mapa
regiones = ["A", "B", "C", "D"]

# Colores disponibles
colores = ["Rojo", "Verde", "Azul"]

# Vecinos de cada región
vecinos = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Ejecutar el algoritmo
solucion = busqueda_vuelta_atras(regiones, colores, vecinos, {})

# Mostrar resultado
if solucion is not None:
    print("Solución encontrada:")
    for region, color in solucion.items():
        print(f"Región {region}: {color}")
else:
    print("No se encontró solución.")