def calcular_utilidad_esperada(creencia, recompensas, accion):
    """
    Calcula la utilidad esperada de una acción
    usando la creencia actual del agente.
    """
    utilidad = 0

    for estado in creencia:
        utilidad += creencia[estado] * recompensas[accion][estado]

    return utilidad


def actualizar_creencia(creencia, transiciones, observaciones, accion, observacion_recibida):
    """
    Actualiza la creencia del agente después de realizar una acción
    y recibir una observación del sensor.
    """

    nueva_creencia = {}

    # Paso 1: calcular la predicción después de la acción
    prediccion = {}

    for estado_siguiente in creencia:
        prediccion[estado_siguiente] = 0

        for estado_actual in creencia:
            probabilidad_transicion = transiciones[accion][estado_actual][estado_siguiente]
            prediccion[estado_siguiente] += creencia[estado_actual] * probabilidad_transicion

    # Paso 2: ajustar la predicción usando la observación recibida
    total = 0

    for estado in prediccion:
        probabilidad_observacion = observaciones[estado][observacion_recibida]
        nueva_creencia[estado] = prediccion[estado] * probabilidad_observacion
        total += nueva_creencia[estado]

    # Paso 3: normalizar para que las probabilidades sumen 1
    for estado in nueva_creencia:
        nueva_creencia[estado] = nueva_creencia[estado] / total

    return nueva_creencia


# Estados reales posibles
estados = ["Seguro", "Peligroso"]

# Creencia inicial del robot
# El robot cree que hay 70% de probabilidad de estar seguro
# y 30% de probabilidad de estar en peligro
creencia = {
    "Seguro": 0.70,
    "Peligroso": 0.30
}

# Acciones disponibles
acciones = ["avanzar", "retirarse"]

# Recompensas de cada acción según el estado real
recompensas = {
    "avanzar": {
        "Seguro": 8,
        "Peligroso": -10
    },
    "retirarse": {
        "Seguro": 2,
        "Peligroso": 2
    }
}

# Modelo de transición
# Indica cómo cambia el estado después de cada acción
transiciones = {
    "avanzar": {
        "Seguro": {
            "Seguro": 0.80,
            "Peligroso": 0.20
        },
        "Peligroso": {
            "Seguro": 0.30,
            "Peligroso": 0.70
        }
    },

    "retirarse": {
        "Seguro": {
            "Seguro": 1.00,
            "Peligroso": 0.00
        },
        "Peligroso": {
            "Seguro": 0.60,
            "Peligroso": 0.40
        }
    }
}

# Modelo de observación
# El sensor no es perfecto
observaciones = {
    "Seguro": {
        "sensor_seguro": 0.85,
        "sensor_peligro": 0.15
    },
    "Peligroso": {
        "sensor_seguro": 0.25,
        "sensor_peligro": 0.75
    }
}

# Calcular la utilidad esperada de cada acción con la creencia inicial
print("Creencia inicial:")
for estado, probabilidad in creencia.items():
    print(f"{estado}: {probabilidad:.2f}")

print("\nUtilidad esperada inicial:")

utilidades = {}

for accion in acciones:
    utilidad = calcular_utilidad_esperada(creencia, recompensas, accion)
    utilidades[accion] = utilidad
    print(f"{accion}: {utilidad:.2f}")

mejor_accion = max(utilidades, key=utilidades.get)

print("\nMejor acción inicial:")
print(mejor_accion)

# Supongamos que el robot avanza y el sensor detecta peligro
observacion_recibida = "sensor_peligro"

creencia_actualizada = actualizar_creencia(
    creencia,
    transiciones,
    observaciones,
    "avanzar",
    observacion_recibida
)

print("\nObservación recibida:")
print(observacion_recibida)

print("\nCreencia actualizada:")
for estado, probabilidad in creencia_actualizada.items():
    print(f"{estado}: {probabilidad:.2f}")

# Decidir nuevamente con la creencia actualizada
print("\nUtilidad esperada después de actualizar la creencia:")

nuevas_utilidades = {}

for accion in acciones:
    utilidad = calcular_utilidad_esperada(creencia_actualizada, recompensas, accion)
    nuevas_utilidades[accion] = utilidad
    print(f"{accion}: {utilidad:.2f}")

nueva_mejor_accion = max(nuevas_utilidades, key=nuevas_utilidades.get)

print("\nNueva mejor acción:")
print(nueva_mejor_accion)