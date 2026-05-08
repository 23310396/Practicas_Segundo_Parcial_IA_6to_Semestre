# Filtrado de particulas
# Estimar posicion de un robot en una linea.

import random

random.seed(21)

N = 500
particulas = [random.uniform(0, 10) for _ in range(N)]
mediciones = [2.0, 3.1, 4.0, 5.2]

def peso(particula, medicion):
    error = abs(particula - medicion)
    return 1 / (1 + error)

def remuestrear(particulas, pesos):
    total = sum(pesos)
    pesos = [p / total for p in pesos]
    acumuladas = []
    s = 0
    for p in pesos:
        s += p
        acumuladas.append(s)

    nuevas = []
    for _ in particulas:
        r = random.random()
        for i, limite in enumerate(acumuladas):
            if r <= limite:
                nuevas.append(particulas[i])
                break
    return nuevas

for medicion in mediciones:
    particulas = [p + random.uniform(0.7, 1.3) for p in particulas]
    pesos = [peso(p, medicion) for p in particulas]
    particulas = remuestrear(particulas, pesos)
    estimacion = sum(particulas) / len(particulas)
    print(f"Medicion={medicion:.1f}, posicion estimada={estimacion:.2f}")
