# Hipotesis de Markov
# El siguiente estado depende del estado actual, no de todo el historial.

import random

random.seed(16)

transicion = {
    "A": {"A": 0.2, "B": 0.8},
    "B": {"A": 0.6, "B": 0.4}
}

def avanzar(estado):
    r = random.random()
    acumulado = 0
    for nuevo, p in transicion[estado].items():
        acumulado += p
        if r <= acumulado:
            return nuevo
    return estado

estado = "A"
historial = [estado]
for _ in range(10):
    estado = avanzar(estado)
    historial.append(estado)

print("Historial simulado:")
print(" -> ".join(historial))
