def normalizar(distribucion):
    """
    Normaliza una distribución de probabilidad
    para que la suma total sea 1.
    """
    total = sum(distribucion.values())

    for estado in distribucion:
        distribucion[estado] = distribucion[estado] / total

    return distribucion


def actualizar_creencia(creencia, transicion, sensor, observacion, estados):
    """
    Actualiza la probabilidad de cada estado usando:
    1. Modelo de transición
    2. Modelo de observación
    """

    # Paso 1: predicción del nuevo estado
    prediccion = {}

    for estado_siguiente in estados:
        prediccion[estado_siguiente] = 0

        for estado_actual in estados:
            prediccion[estado_siguiente] += (
                creencia[estado_actual] *
                transicion[estado_actual][estado_siguiente]
            )

    # Paso 2: corrección usando la observación del sensor
    nueva_creencia = {}

    for estado in estados:
        nueva_creencia[estado] = (
            prediccion[estado] *
            sensor[estado][observacion]
        )

    # Paso 3: normalizar probabilidades
    nueva_creencia = normalizar(nueva_creencia)

    return nueva_creencia


# Estados posibles de la máquina
estados = ["Normal", "Falla"]

# Creencia inicial
creencia = {
    "Normal": 0.80,
    "Falla": 0.20
}

# Modelo de transición
# Probabilidad de pasar de un estado actual a un estado siguiente
transicion = {
    "Normal": {
        "Normal": 0.85,
        "Falla": 0.15
    },
    "Falla": {
        "Normal": 0.30,
        "Falla": 0.70
    }
}

# Modelo de observación
# Probabilidad de observar cierto sensor dependiendo del estado real
sensor = {
    "Normal": {
        "sensor_ok": 0.90,
        "sensor_alerta": 0.10
    },
    "Falla": {
        "sensor_ok": 0.20,
        "sensor_alerta": 0.80
    }
}

# Observaciones recibidas con el paso del tiempo
observaciones = [
    "sensor_ok",
    "sensor_alerta",
    "sensor_alerta",
    "sensor_ok"
]

print("Creencia inicial:")
for estado, probabilidad in creencia.items():
    print(f"{estado}: {probabilidad:.2f}")

# Actualizar la creencia en cada tiempo
for tiempo, observacion in enumerate(observaciones, start=1):

    creencia = actualizar_creencia(
        creencia,
        transicion,
        sensor,
        observacion,
        estados
    )

    print(f"\nTiempo {tiempo}")
    print("Observación recibida:", observacion)

    for estado, probabilidad in creencia.items():
        print(f"{estado}: {probabilidad:.2f}")