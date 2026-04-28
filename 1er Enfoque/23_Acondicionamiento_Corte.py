from itertools import product


def es_valido(variable, valor, asignacion, vecinos):
    """
    Verifica si una variable puede tomar un valor
    sin violar las restricciones con sus vecinos.
    """
    for vecino in vecinos[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False

    return True


def busqueda_vuelta_atras(variables, dominios, vecinos, asignacion):
    """
    Resuelve el problema restante usando búsqueda de vuelta atrás.
    """

    # Caso base: todas las variables tienen valor
    if len(asignacion) == len(variables):
        return asignacion.copy()

    # Elegir la primera variable sin asignar
    variable_actual = None

    for variable in variables:
        if variable not in asignacion:
            variable_actual = variable
            break

    # Probar cada valor posible
    for valor in dominios[variable_actual]:

        if es_valido(variable_actual, valor, asignacion, vecinos):

            asignacion[variable_actual] = valor

            resultado = busqueda_vuelta_atras(
                variables,
                dominios,
                vecinos,
                asignacion
            )

            if resultado is not None:
                return resultado

            # Si no funcionó, se deshace la asignación
            del asignacion[variable_actual]

    return None


def acondicionamiento_de_corte(variables, dominios, vecinos, conjunto_corte):
    """
    Algoritmo de acondicionamiento de corte.

    Primero se asignan valores a las variables del conjunto de corte.
    Después se resuelve el resto del problema con búsqueda de vuelta atrás.
    """

    # Obtener los dominios de las variables del conjunto de corte
    dominios_corte = []

    for variable in conjunto_corte:
        dominios_corte.append(dominios[variable])

    # Probar todas las combinaciones posibles del conjunto de corte
    for valores in product(*dominios_corte):

        asignacion = {}

        for i in range(len(conjunto_corte)):
            asignacion[conjunto_corte[i]] = valores[i]

        # Revisar si la asignación del conjunto de corte es válida
        asignacion_valida = True

        for variable in conjunto_corte:
            valor = asignacion[variable]

            if not es_valido(variable, valor, asignacion, vecinos):
                asignacion_valida = False
                break

        if asignacion_valida:

            print("Probando conjunto de corte:")
            for variable in conjunto_corte:
                print(f"Región {variable}: {asignacion[variable]}")

            print()

            resultado = busqueda_vuelta_atras(
                variables,
                dominios,
                vecinos,
                asignacion
            )

            if resultado is not None:
                return resultado

    return None


# Variables: regiones del mapa
variables = ["A", "B", "C", "D"]

# Colores disponibles
colores = ["Rojo", "Verde", "Azul"]

# Dominio de cada variable
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

# Conjunto de corte
# Se elige A para asignarla primero y simplificar el problema restante
conjunto_corte = ["A"]

# Ejecutar algoritmo
solucion = acondicionamiento_de_corte(
    variables,
    dominios,
    vecinos,
    conjunto_corte
)

# Mostrar resultado
if solucion is not None:
    print("Solución encontrada:")

    for variable, valor in solucion.items():
        print(f"Región {variable}: {valor}")

else:
    print("No se encontró solución.")