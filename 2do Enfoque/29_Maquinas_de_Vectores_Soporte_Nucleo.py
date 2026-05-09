# Maquinas de Vectores Soporte con nucleo RBF simplificado
# Se clasifica por similitud contra ejemplos de soporte.

import math

soportes = [
    ((1, 1), -1, 0.8),
    ((2, 1), -1, 0.6),
    ((5, 5), 1, 0.7),
    ((6, 5), 1, 0.9)
]

def rbf(a, b, gamma=0.2):
    d2 = (a[0]-b[0])**2 + (a[1]-b[1])**2
    return math.exp(-gamma * d2)

def clasificar(x):
    score = 0
    for punto, etiqueta, alpha in soportes:
        score += alpha * etiqueta * rbf(x, punto)
    return 1 if score >= 0 else -1, score

punto = (5.2, 4.8)
clase, valor = clasificar(punto)
print("Punto:", punto)
print(f"Funcion de decision: {valor:.3f}")
print("Clase:", clase)
