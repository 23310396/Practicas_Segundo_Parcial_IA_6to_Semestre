import random


def contar_conflictos(variable, valor, asignacion, vecinos):
    """
    Cuenta cuántos conflictos tendría una variable
    si se le asigna cierto valor.
    """
    conflictos = 0

    for vecino in vecinos[variable]:
        if asignacion.get(vecino) == valor:
            conflictos += 1

    return conflictos


def total_conflictos(asignacion, vecinos):
    """
    Cuenta el número total de conflictos en toda la asignación.
    Se divide entre 2 porque cada conflicto se cuenta dos veces.
    """
    total = 0

    for variable in asignacion:
        total += contar_conflictos(
            variable,
            asignacion[variable],
            asignacion,
            vecinos
        )

    return total // 2


def busqueda_minimos_conflictos(variables, dominios, vecinos, max_iteraciones=1000):
    """
    Algoritmo de búsqueda local por mínimos conflictos.

    1. Genera una asignación inicial aleatoria.
    2. Busca variables que están en conflicto.
    3. Cambia el valor de una variable conflictiva por el valor
       que produzca menos conflictos.
    4. Repite hasta encontrar una solución.
    """

    # Crear asignación inicial aleatoria
    asignacion = {}

    for variable in variables:
        asignacion[variable] = random.choice(dominios[variable])

    print("Asignación inicial:")
    for variable, valor in asignacion.items():
        print(f"Región {variable}: {valor}")

    print("\nConflictos iniciales:", total_conflictos(asignacion, vecinos))

    # Proceso de búsqueda local
    for iteracion in range(max_iteraciones):

        # Si ya no hay conflictos, se encontró solución
        if total_conflictos(asignacion, vecinos) == 0:
            return asignacion, iteracion

        # Buscar variables que tienen conflicto
        variables_conflictivas = []

        for variable in variables:
            conflictos = contar_conflictos(
                variable,
                asignacion[variable],
                asignacion,
                vecinos
            )

            if conflictos > 0:
                variables_conflictivas.append(variable)

        # Elegir una variable conflictiva al azar
        variable_actual = random.choice(variables_conflictivas)

        mejor_valor = None
        menor_numero_conflictos = float("inf")

        # Probar los valores posibles y elegir el que genere menos conflictos
        for valor in dominios[variable_actual]:

            conflictos = contar_conflictos(
                variable_actual,
                valor,
                asignacion,
                vecinos
            )

            if conflictos < menor_numero_conflictos:
                menor_numero_conflictos = conflictos
                mejor_valor = valor

        # Cambiar el valor de la variable conflictiva
        asignacion[variable_actual] = mejor_valor

    # Si no se encuentra solución en el límite de iteraciones
    return None, max_iteraciones


# Para que el resultado sea repetible
random.seed(7)

# Variables: regiones del mapa
variables = ["A", "B", "C", "D"]

# Colores disponibles
colores = ["Rojo", "Verde", "Azul"]

# Dominio de cada región
dominios = {
    "A": colores[:],
    "B": colores[:],
    "C": colores[:],
    "D": colores[:]
}

# Vecinos de cada región
vecinos = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Ejecutar algoritmo
solucion, iteraciones = busqueda_minimos_conflictos(
    variables,
    dominios,
    vecinos
)

# Mostrar resultado final
if solucion is not None:
    print("\nSolución encontrada:")
    for variable, valor in solucion.items():
        print(f"Región {variable}: {valor}")

    print("\nIteraciones realizadas:", iteraciones)
    print("Conflictos finales:", total_conflictos(solucion, vecinos))

else:
    print("\nNo se encontró solución.")