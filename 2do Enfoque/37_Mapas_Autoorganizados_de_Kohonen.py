# Mapa autoorganizado de Kohonen simplificado
# Dos neuronas compiten por representar puntos 2D.

import random

random.seed(37)
datos = [(0.1, 0.2), (0.2, 0.1), (0.9, 0.8), (0.8, 0.9)]
neuronas = [(random.random(), random.random()) for _ in range(2)]

def distancia(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

for _ in range(20):
    for x in datos:
        ganadora = min(range(2), key=lambda i: distancia(x, neuronas[i]))
        wx, wy = neuronas[ganadora]
        tasa = 0.3
        neuronas[ganadora] = (wx + tasa*(x[0]-wx), wy + tasa*(x[1]-wy))

print("Neuronas finales:")
for n in neuronas:
    print(tuple(round(v, 3) for v in n))
