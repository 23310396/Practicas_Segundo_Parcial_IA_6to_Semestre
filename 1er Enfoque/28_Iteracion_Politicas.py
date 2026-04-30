# Estados posibles
estados = ["A", "B", "C", "Meta"]

# Acciones disponibles en cada estado
acciones = {
    "A": ["ir_B", "ir_C"],
    "B": ["ir_Meta", "ir_C"],
    "C": ["ir_Meta"],
    "Meta": []
}

# Transiciones:
# (estado, accion): (siguiente_estado, recompensa)
transiciones = {
    ("A", "ir_B"): ("B", -1),
    ("A", "ir_C"): ("C", -2),
    ("B", "ir_Meta"): ("Meta", 10),
    ("B", "ir_C"): ("C", -1),
    ("C", "ir_Meta"): ("Meta", 5)
}

# Factor de descuento
gamma = 0.9

# Política inicial
# Es una primera decisión para cada estado
politica = {
    "A": "ir_C",
    "B": "ir_C",
    "C": "ir_Meta",
    "Meta": None
}

# Valores iniciales de los estados
valores = {}

for estado in estados:
    valores[estado] = 0


def evaluar_politica(estados, politica, transiciones, valores, gamma):
    """
    Evalúa la política actual.
    Calcula qué valor tiene cada estado siguiendo esa política.
    """

    for _ in range(20):
        nuevos_valores = valores.copy()

        for estado in estados:

            if estado == "Meta":
                nuevos_valores[estado] = 0
                continue

            accion = politica[estado]
            siguiente_estado, recompensa = transiciones[(estado, accion)]

            nuevos_valores[estado] = recompensa + gamma * valores[siguiente_estado]

        valores = nuevos_valores

    return valores


def mejorar_politica(estados, acciones, transiciones, valores, politica, gamma):
    """
    Mejora la política actual.
    Para cada estado, busca la acción con mayor valor esperado.
    """

    politica_estable = True

    for estado in estados:

        if estado == "Meta":
            continue

        accion_anterior = politica[estado]

        mejor_accion = None
        mejor_valor = float("-inf")

        for accion in acciones[estado]:

            siguiente_estado, recompensa = transiciones[(estado, accion)]

            valor_accion = recompensa + gamma * valores[siguiente_estado]

            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = accion

        politica[estado] = mejor_accion

        if accion_anterior != mejor_accion:
            politica_estable = False

    return politica, politica_estable


# Algoritmo de iteración de políticas
iteracion = 0

while True:
    iteracion += 1

    # Paso 1: evaluar la política actual
    valores = evaluar_politica(
        estados,
        politica,
        transiciones,
        valores,
        gamma
    )

    # Paso 2: mejorar la política
    politica, estable = mejorar_politica(
        estados,
        acciones,
        transiciones,
        valores,
        politica,
        gamma
    )

    # Si la política ya no cambia, se encontró la mejor
    if estable:
        break


# Mostrar resultados
print("Iteraciones realizadas:", iteracion)

print("\nValores finales de cada estado:")
for estado in estados:
    print(f"Estado {estado}: {valores[estado]:.2f}")

print("\nPolítica óptima encontrada:")
for estado in estados:
    if politica[estado] is not None:
        print(f"En el estado {estado}, conviene hacer: {politica[estado]}")
    else:
        print(f"En el estado {estado}, no se necesita acción.")