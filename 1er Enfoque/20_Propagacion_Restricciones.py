from collections import deque


def revisar(variable_actual, variable_vecina, dominios):
    """
    Revisa si los valores del dominio de variable_actual
    son compatibles con los valores del dominio de variable_vecina.

    En este problema, la restricción es:
    dos regiones vecinas no pueden tener el mismo color.
    """

    hubo_cambio = False

    for valor_actual in dominios[variable_actual][:]:

        # Verificar si existe al menos un valor diferente en la variable vecina
        existe_valor_valido = False

        for valor_vecino in dominios[variable_vecina]:
            if valor_actual != valor_vecino:
                existe_valor_valido = True
                break

        # Si no existe ningún valor válido, se elimina del dominio
        if not existe_valor_valido:
            dominios[variable_actual].remove(valor_actual)
            hubo_cambio = True

    return hubo_cambio


def propagacion_restricciones(variables, dominios, restricciones):
    """
    Algoritmo AC-3 para propagación de restricciones.
    Reduce los dominios eliminando valores que no cumplen las restricciones.
    """

    cola = deque(restricciones)

    while cola:

        variable_actual, variable_vecina = cola.popleft()

        if revisar(variable_actual, variable_vecina, dominios):

            # Si una variable se queda sin valores posibles, no hay solución
            if len(dominios[variable_actual]) == 0:
                return False

            # Si hubo cambios, se vuelven a revisar las restricciones relacionadas
            for var1, var2 in restricciones:
                if var2 == variable_actual and var1 != variable_vecina:
                    cola.append((var1, variable_actual))

    return True


# Variables: regiones del mapa
variables = ["A", "B", "C", "D"]

# Dominios iniciales
# Aquí A ya tiene asignado el color Rojo
dominios = {
    "A": ["Rojo"],
    "B": ["Rojo", "Verde", "Azul"],
    "C": ["Rojo", "Verde", "Azul"],
    "D": ["Rojo", "Verde", "Azul"]
}

# Vecinos de cada región
vecinos = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Restricciones en ambos sentidos
restricciones = []

for region in vecinos:
    for vecino in vecinos[region]:
        restricciones.append((region, vecino))


# Ejecutar propagación de restricciones
resultado = propagacion_restricciones(variables, dominios, restricciones)

# Mostrar resultado
if resultado:
    print("Propagación realizada correctamente.")
    print("Dominios después de aplicar restricciones:")

    for variable in variables:
        print(f"Región {variable}: {dominios[variable]}")

else:
    print("No hay solución posible.")