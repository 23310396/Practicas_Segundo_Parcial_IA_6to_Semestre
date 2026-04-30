def utilidad_esperada(resultados):
    """
    Calcula la utilidad esperada.
    Fórmula:
    utilidad esperada = suma(probabilidad * utilidad)
    """
    total = 0

    for resultado in resultados:
        total += resultado["probabilidad"] * resultado["utilidad"]

    return total


# Decisiones sin información perfecta
decisiones = {
    "Comprar mucho inventario": [
        {
            "evento": "Demanda alta",
            "probabilidad": 0.60,
            "utilidad": 15000
        },
        {
            "evento": "Demanda baja",
            "probabilidad": 0.40,
            "utilidad": -4000
        }
    ],

    "Comprar poco inventario": [
        {
            "evento": "Demanda alta",
            "probabilidad": 0.60,
            "utilidad": 8000
        },
        {
            "evento": "Demanda baja",
            "probabilidad": 0.40,
            "utilidad": 4000
        }
    ]
}

# Calcular utilidad esperada sin información perfecta
resultados = {}

for decision, eventos in decisiones.items():
    resultados[decision] = utilidad_esperada(eventos)

print("Utilidad esperada sin información perfecta:\n")

for decision, utilidad in resultados.items():
    print(f"{decision}: ${utilidad:.2f}")

# Mejor decisión sin información perfecta
mejor_decision = max(resultados, key=resultados.get)
mejor_utilidad_sin_info = resultados[mejor_decision]

print("\nMejor decisión sin información perfecta:")
print(mejor_decision)
print("Utilidad esperada:", f"${mejor_utilidad_sin_info:.2f}")


# Utilidad esperada con información perfecta
# Si se sabe que la demanda será alta, conviene comprar mucho inventario.
# Si se sabe que la demanda será baja, conviene comprar poco inventario.

utilidad_con_info_perfecta = (0.60 * 15000) + (0.40 * 4000)

print("\nUtilidad esperada con información perfecta:")
print(f"${utilidad_con_info_perfecta:.2f}")


# Valor de la información perfecta
valor_informacion = utilidad_con_info_perfecta - mejor_utilidad_sin_info

print("\nValor de la información:")
print(f"${valor_informacion:.2f}")