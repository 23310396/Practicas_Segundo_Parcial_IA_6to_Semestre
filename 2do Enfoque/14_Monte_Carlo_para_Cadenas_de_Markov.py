# Monte Carlo para Cadenas de Markov
# Una caminata aleatoria con dos estados: Normal y Falla.

import random

random.seed(14)

transicion = {
    "Normal": [("Normal", 0.85), ("Falla", 0.15)],
    "Falla": [("Normal", 0.25), ("Falla", 0.75)]
}

def siguiente_estado(estado):
    r = random.random()
    acumulado = 0
    for nuevo, p in transicion[estado]:
        acumulado += p
        if r <= acumulado:
            return nuevo
    return transicion[estado][-1][0]

estado = "Normal"
conteo = {"Normal": 0, "Falla": 0}

for _ in range(20000):
    estado = siguiente_estado(estado)
    conteo[estado] += 1

total = sum(conteo.values())
print("Distribucion aproximada despues de simular la cadena:")
for estado, c in conteo.items():
    print(f"{estado}: {c / total:.3f}")
