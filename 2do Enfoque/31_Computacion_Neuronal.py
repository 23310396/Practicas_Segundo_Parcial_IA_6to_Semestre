# Computacion neuronal
# Una neurona calcula suma ponderada y aplica una funcion escalon.

entradas = [1, 0, 1]
pesos = [0.7, -0.4, 0.5]
sesgo = -0.8

suma = sesgo
for x, w in zip(entradas, pesos):
    suma += x * w

salida = 1 if suma >= 0 else 0

print("Suma ponderada:", round(suma, 3))
print("Salida de la neurona:", salida)
