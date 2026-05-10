# Retropropagacion del error en una neurona sigmoide.

import math

x = [1.0, 0.5]
y_real = 1.0
pesos = [0.2, -0.1]
sesgo = 0.0
tasa = 0.5

def sigmoide(z):
    return 1 / (1 + math.exp(-z))

for epoca in range(20):
    z = sesgo + sum(xi*wi for xi, wi in zip(x, pesos))
    y = sigmoide(z)
    error = y_real - y
    grad = error * y * (1 - y)
    for i in range(len(pesos)):
        pesos[i] += tasa * grad * x[i]
    sesgo += tasa * grad

print("Salida final:", round(y, 3))
print("Pesos:", [round(w, 3) for w in pesos])
print("Sesgo:", round(sesgo, 3))
