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
# Sirve para darle importancia a las recompensas futuras
gamma = 0.9

# Inicializar valores de cada estado en 0
valores = {}

for estado in estados:
    valores[estado] = 0

# Guardar la mejor acción para cada estado
politica = {}

for estado in estados:
    politica[estado] = None

# Número de iteraciones
numero_iteraciones = 20

# Algoritmo de iteración de valores
for iteracion in range(numero_iteraciones):

    nuevos_valores = valores.copy()

    for estado in estados:

        # La meta no necesita acción
        if estado == "Meta":
            nuevos_valores[estado] = 0
            continue

        mejor_valor = float("-inf")
        mejor_accion = None

        # Probar cada acción posible
        for accion in acciones[estado]:

            siguiente_estado, recompensa = transiciones[(estado, accion)]

            # Fórmula de iteración de valores
            valor_accion = recompensa + gamma * valores[siguiente_estado]

            if valor_accion > mejor_valor:
                mejor_valor = valor_accion
                mejor_accion = accion

        nuevos_valores[estado] = mejor_valor
        politica[estado] = mejor_accion

    valores = nuevos_valores

# Mostrar resultados
print("Valores finales de cada estado:\n")

for estado in estados:
    print(f"Estado {estado}: {valores[estado]:.2f}")

print("\nMejor política encontrada:\n")

for estado in estados:
    if politica[estado] is not None:
        print(f"En el estado {estado}, conviene hacer: {politica[estado]}")
    else:
        print(f"En el estado {estado}, no se necesita acción.")