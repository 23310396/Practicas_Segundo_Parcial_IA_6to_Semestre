def utilidad_esperada(resultados):
    """
    Calcula la utilidad esperada de una decisión.

    Fórmula:
    Utilidad esperada = suma(probabilidad * utilidad)
    """

    total = 0

    for resultado in resultados:
        probabilidad = resultado["probabilidad"]
        utilidad = resultado["utilidad"]

        total += probabilidad * utilidad

    return total


# Red de decisión
# Cada decisión tiene posibles resultados con su probabilidad y utilidad
red_decision = {
    "Invertir en publicidad": [
        {
            "evento": "Ventas altas",
            "probabilidad": 0.70,
            "utilidad": 12000
        },
        {
            "evento": "Ventas bajas",
            "probabilidad": 0.30,
            "utilidad": -3000
        }
    ],

    "No invertir en publicidad": [
        {
            "evento": "Ventas altas",
            "probabilidad": 0.40,
            "utilidad": 7000
        },
        {
            "evento": "Ventas bajas",
            "probabilidad": 0.60,
            "utilidad": 2000
        }
    ]
}

# Calcular utilidad esperada para cada decisión
resultados = {}

for decision, eventos in red_decision.items():
    resultados[decision] = utilidad_esperada(eventos)

# Mostrar resultados
print("Utilidad esperada de cada decisión:\n")

for decision, utilidad in resultados.items():
    print(f"{decision}: ${utilidad:.2f}")

# Elegir la mejor decisión
mejor_decision = max(resultados, key=resultados.get)

print("\nMejor decisión:")
print(mejor_decision)
print("Utilidad esperada:", f"${resultados[mejor_decision]:.2f}")