def calcular_utilidad(caracteristicas, pesos):
    """
    Calcula la utilidad total de una opción.

    La utilidad se obtiene multiplicando cada característica
    por su peso de importancia.
    """

    utilidad = 0

    for criterio in pesos:
        utilidad += caracteristicas[criterio] * pesos[criterio]

    return utilidad


# Opciones disponibles
# Escala de 1 a 10:
# En precio, un valor más alto significa que es más conveniente o barato.
opciones = {
    "Laptop económica": {
        "precio": 9,
        "rendimiento": 6,
        "durabilidad": 5
    },
    "Laptop intermedia": {
        "precio": 7,
        "rendimiento": 8,
        "durabilidad": 8
    },
    "Laptop gamer": {
        "precio": 4,
        "rendimiento": 10,
        "durabilidad": 7
    }
}

# Pesos de importancia de cada criterio
# La suma de los pesos debe ser 1.0
pesos = {
    "precio": 0.40,
    "rendimiento": 0.35,
    "durabilidad": 0.25
}

# Calcular utilidad de cada opción
resultados = {}

for opcion, caracteristicas in opciones.items():
    utilidad = calcular_utilidad(caracteristicas, pesos)
    resultados[opcion] = utilidad

# Mostrar resultados
print("Resultados de utilidad:")

for opcion, utilidad in resultados.items():
    print(f"{opcion}: {utilidad:.2f}")

# Elegir la opción con mayor utilidad
mejor_opcion = max(resultados, key=resultados.get)

print("\nMejor decisión:")
print(mejor_opcion)
print("Utilidad:", round(resultados[mejor_opcion], 2))