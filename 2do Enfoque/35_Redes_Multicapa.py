# Red multicapa pequena para resolver XOR con pesos ya ajustados.

import math

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def red_xor(x1, x2):
    h1 = sigmoide(20*x1 + 20*x2 - 10)   # OR
    h2 = sigmoide(-20*x1 - 20*x2 + 30)  # NAND
    y = sigmoide(20*h1 + 20*h2 - 30)    # AND entre h1 y h2
    return y

for x1 in [0, 1]:
    for x2 in [0, 1]:
        salida = red_xor(x1, x2)
        print(f"{x1} XOR {x2} = {round(salida)} ({salida:.3f})")
