# Estados posibles
estados = ["Inicio", "Intermedio", "Meta"]

# Acciones disponibles por estado
acciones = {
    "Inicio": ["avanzar", "esperar"],
    "Intermedio": ["avanzar", "regresar"],
    "Meta": []
}

# Transiciones del MDP
# Formato:
# estado -> accion -> lista de posibles resultados
# Cada resultado tiene: siguiente estado, probabilidad y recompensa

transiciones = {
    "Inicio": {
        "avanzar": [
            ("Intermedio", 0.80, 5),
            ("Inicio", 0.20, -1)
        ],
        "esperar": [
            ("Inicio", 1.00, 0)
        ]
    },

    "Intermedio": {
        "avanzar": [
            ("Meta", 0.70, 10),
            ("Intermedio", 0.30, -2)
        ],
        "regresar": [
            ("Inicio", 1.00, -3)
        ]
    },

    "Meta": {}
}

# Factor de descuento
gamma = 0.9

# Inicializar valores de los estados
valores = {}

for estado in estados:
    valores[estado] = 0

# Guardar la mejor política
politica = {}

for estado in estados:
    politica[estado] = None

# Número de iteraciones
numero_iteraciones = 20

# Resolver el MDP usando iteración de valores
for iteracion in range(numero_iteraciones):

    nuevos_valores = valores.copy()

    for estado in estados:

        if estado == "Meta":
            nuevos_valores[estado] = 0
            continue

        mejor_valor = float("-inf")
        mejor_accion = None

        for accion in acciones[estado]:

            valor_accion = 0

            for siguiente_estado, probabilidad, recompensa in transiciones[estado][accion]:

                valor_accion += probabilidad * (
                    recompensa + gamma * valores[siguiente_estado]
                )

            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = accion

        nuevos_valores[estado] = mejor_valor
        politica[estado] = mejor_accion

    valores = nuevos_valores


# Mostrar resultados
print("Valores finales de los estados:\n")

for estado in estados:
    print(f"{estado}: {valores[estado]:.2f}")

print("\nPolítica óptima encontrada:\n")

for estado in estados:
    if politica[estado] is not None:
        print(f"En {estado}, conviene hacer: {politica[estado]}")
    else:
        print(f"En {estado}, no se necesita acción.")