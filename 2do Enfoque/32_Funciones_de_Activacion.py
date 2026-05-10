# Funciones de activacion comunes.

import math

valores = [-2, -1, 0, 1, 2]

def escalon(x):
    return 1 if x >= 0 else 0

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

print("x\tescalon\tsigmoide\trelu")
for x in valores:
    print(f"{x}\t{escalon(x)}\t{sigmoide(x):.3f}\t\t{relu(x)}")
