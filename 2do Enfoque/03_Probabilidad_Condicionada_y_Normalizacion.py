# Probabilidad condicionada y normalizacion
# Ejemplo: sensor que detecta falla en una maquina.

prior = {
    "normal": 0.80,
    "falla": 0.20
}

# P(sensor_alerta | estado)
verosimilitud = {
    "normal": 0.10,
    "falla": 0.85
}

sin_normalizar = {}
for estado in prior:
    sin_normalizar[estado] = prior[estado] * verosimilitud[estado]

total = sum(sin_normalizar.values())
posterior = {}
for estado in sin_normalizar:
    posterior[estado] = sin_normalizar[estado] / total

print("Probabilidades despues de observar sensor_alerta:")
for estado, p in posterior.items():
    print(f"P({estado} | alerta) = {p:.3f}")
