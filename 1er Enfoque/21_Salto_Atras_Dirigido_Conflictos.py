def es_consistente(variable, valor, asignacion, restricciones):
    """
    Verifica si asignar un valor a una variable genera conflicto.
    Si hay conflicto, regresa también la variable que lo causó.
    """

    for var1, var2 in restricciones:

        if variable == var1 and var2 in asignacion:
            if asignacion[var2] == valor:
                return False, var2

        if variable == var2 and var1 in asignacion:
            if asignacion[var1] == valor:
                return False, var1

    return True, None


def salto_atras_dirigido(variables, dominios, restricciones, asignacion, indice):
    """
    Algoritmo de salto atrás dirigido por conflictos.

    Si una variable no puede tomar ningún valor válido,
    el algoritmo identifica qué variable anterior causó el conflicto
    y salta directamente hacia ella.
    """

    # Caso base: todas las variables tienen valor
    if indice == len(variables):
        return asignacion, None

    variable_actual = variables[indice]
    conjunto_conflictos = set()

    # Probar cada valor posible
    for valor in dominios[variable_actual]:

        consistente, variable_conflicto = es_consistente(
            variable_actual,
            valor,
            asignacion,
            restricciones
        )

        if consistente:
            # Asignar valor temporalmente
            asignacion[variable_actual] = valor

            # Continuar con la siguiente variable
            resultado, salto = salto_atras_dirigido(
                variables,
                dominios,
                restricciones,
                asignacion,
                indice + 1
            )

            # Si se encontró solución, se devuelve
            if resultado is not None:
                return resultado, None

            # Si no funcionó, se elimina la asignación
            del asignacion[variable_actual]

            # Si el conflicto pertenece a otra variable,
            # se sigue saltando hacia atrás
            if salto is not None:
                if salto != variable_actual:
                    return None, salto

        else:
            # Guardar la variable que causó el conflicto
            conjunto_conflictos.add(variable_conflicto)

    # Si ningún valor funcionó, elegir hacia qué variable saltar
    if conjunto_conflictos:
        indices = {}

        for i in range(len(variables)):
            indices[variables[i]] = i

        # Se salta a la variable conflictiva más reciente
        variable_salto = max(conjunto_conflictos, key=lambda v: indices[v])

        return None, variable_salto

    return None, variable_actual


# Variables: regiones del mapa
variables = ["A", "B", "C", "D"]

# Dominio: colores disponibles
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

# Ejecutar algoritmo
solucion, _ = salto_atras_dirigido(
    variables,
    dominios,
    restricciones,
    {},
    0
)

# Mostrar resultado
if solucion is not None:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"Región {variable}: {valor}")
else:
    print("No se encontró solución.")