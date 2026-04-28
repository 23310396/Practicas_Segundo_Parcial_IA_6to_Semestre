def es_consistente(variable, valor, asignacion, restricciones):
    """
    Verifica que la asignación actual no viole restricciones
    con las variables que ya tienen valor.
    """
    for var1, var2 in restricciones:
        if variable == var1 and var2 in asignacion:
            if asignacion[var2] == valor:
                return False

        if variable == var2 and var1 in asignacion:
            if asignacion[var1] == valor:
                return False

    return True


def comprobacion_hacia_adelante(variables, dominios, restricciones, asignacion):
    """
    Algoritmo de comprobación hacia adelante.
    Asigna valores y elimina opciones inválidas de los dominios futuros.
    """

    # Caso base: si todas las variables tienen valor, ya hay solución
    if len(asignacion) == len(variables):
        return asignacion

    # Seleccionar la primera variable que aún no tenga valor
    variable_actual = None
    for variable in variables:
        if variable not in asignacion:
            variable_actual = variable
            break

    # Probar cada valor posible del dominio de la variable actual
    for valor in dominios[variable_actual]:

        if es_consistente(variable_actual, valor, asignacion, restricciones):

            # Crear copias para no modificar directamente los datos originales
            nueva_asignacion = asignacion.copy()
            nuevos_dominios = {v: dominios[v][:] for v in dominios}

            # Asignar valor
            nueva_asignacion[variable_actual] = valor

            fallo = False

            # Comprobación hacia adelante:
            # eliminar el valor usado del dominio de los vecinos no asignados
            for var1, var2 in restricciones:

                vecino = None

                if variable_actual == var1 and var2 not in nueva_asignacion:
                    vecino = var2
                elif variable_actual == var2 and var1 not in nueva_asignacion:
                    vecino = var1

                if vecino is not None:
                    if valor in nuevos_dominios[vecino]:
                        nuevos_dominios[vecino].remove(valor)

                    # Si un vecino se queda sin valores, esta rama falla
                    if len(nuevos_dominios[vecino]) == 0:
                        fallo = True
                        break

            # Si no hubo fallo, continuar recursivamente
            if not fallo:
                resultado = comprobacion_hacia_adelante(
                    variables,
                    nuevos_dominios,
                    restricciones,
                    nueva_asignacion
                )

                if resultado is not None:
                    return resultado

    # Si ningún valor funciona, no hay solución en esta rama
    return None


# Variables: regiones del mapa
variables = ["A", "B", "C", "D"]

# Dominio: colores disponibles para cada región
dominios = {
    "A": ["Rojo", "Verde", "Azul"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"],
    "D": ["Rojo", "Verde", "Azul"]
}

# Restricciones: regiones vecinas no pueden tener el mismo color
restricciones = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D")
]

# Ejecutar el algoritmo
solucion = comprobacion_hacia_adelante(variables, dominios, restricciones, {})

# Mostrar resultado
if solucion is not None:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"Región {variable}: {valor}")
else:
    print("No se encontró solución.")