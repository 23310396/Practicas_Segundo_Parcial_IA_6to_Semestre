# Utilidad y toma de decisiones
# Subtema: Teoría de Juegos - Equilibrios y mecanismos
# Ejemplo: Equilibrio de Nash entre dos empresas

def obtener_pago(matriz_pagos, accion_empresa_1, accion_empresa_2):
    """
    Obtiene el pago de ambas empresas según sus decisiones.
    """
    return matriz_pagos[(accion_empresa_1, accion_empresa_2)]


def es_equilibrio_nash(matriz_pagos, acciones_empresa_1, acciones_empresa_2, accion_1, accion_2):
    """
    Verifica si una combinación de acciones es equilibrio de Nash.

    Un equilibrio de Nash ocurre cuando ningún jugador puede mejorar
    su pago cambiando su acción de manera individual.
    """

    pago_actual_empresa_1, pago_actual_empresa_2 = obtener_pago(
        matriz_pagos,
        accion_1,
        accion_2
    )

    # Revisar si la empresa 1 puede mejorar cambiando solo su acción
    for nueva_accion_1 in acciones_empresa_1:
        nuevo_pago_empresa_1, _ = obtener_pago(
            matriz_pagos,
            nueva_accion_1,
            accion_2
        )

        if nuevo_pago_empresa_1 > pago_actual_empresa_1:
            return False

    # Revisar si la empresa 2 puede mejorar cambiando solo su acción
    for nueva_accion_2 in acciones_empresa_2:
        _, nuevo_pago_empresa_2 = obtener_pago(
            matriz_pagos,
            accion_1,
            nueva_accion_2
        )

        if nuevo_pago_empresa_2 > pago_actual_empresa_2:
            return False

    return True


# Acciones disponibles para cada empresa
acciones_empresa_1 = ["Mantener precio", "Bajar precio"]
acciones_empresa_2 = ["Mantener precio", "Bajar precio"]

# Matriz de pagos
# Formato:
# (acción empresa 1, acción empresa 2): (pago empresa 1, pago empresa 2)
matriz_pagos = {
    ("Mantener precio", "Mantener precio"): (8, 8),
    ("Mantener precio", "Bajar precio"): (3, 10),
    ("Bajar precio", "Mantener precio"): (10, 3),
    ("Bajar precio", "Bajar precio"): (5, 5)
}

# Buscar equilibrios de Nash
equilibrios = []

for accion_1 in acciones_empresa_1:
    for accion_2 in acciones_empresa_2:

        if es_equilibrio_nash(
            matriz_pagos,
            acciones_empresa_1,
            acciones_empresa_2,
            accion_1,
            accion_2
        ):
            equilibrios.append((accion_1, accion_2, matriz_pagos[(accion_1, accion_2)]))


# Mostrar matriz de pagos
print("Matriz de pagos:\n")

for combinacion, pagos in matriz_pagos.items():
    print(f"{combinacion}: Empresa 1 = {pagos[0]}, Empresa 2 = {pagos[1]}")

# Mostrar equilibrios encontrados
print("\nEquilibrios de Nash encontrados:\n")

if equilibrios:
    for equilibrio in equilibrios:
        accion_1, accion_2, pagos = equilibrio

        print("Decisión Empresa 1:", accion_1)
        print("Decisión Empresa 2:", accion_2)
        print("Pago Empresa 1:", pagos[0])
        print("Pago Empresa 2:", pagos[1])
        print()
else:
    print("No se encontró equilibrio de Nash.")