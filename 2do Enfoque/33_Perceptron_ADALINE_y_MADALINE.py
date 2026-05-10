# Perceptron simple para aprender la compuerta AND.

patrones = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

pesos = [0.0, 0.0]
sesgo = 0.0
tasa = 0.2

def activar(s):
    return 1 if s >= 0 else 0

for epoca in range(10):
    errores = 0
    for x, deseado in patrones:
        suma = sesgo + pesos[0]*x[0] + pesos[1]*x[1]
        salida = activar(suma)
        error = deseado - salida
        if error != 0:
            errores += 1
        pesos[0] += tasa * error * x[0]
        pesos[1] += tasa * error * x[1]
        sesgo += tasa * error
    if errores == 0:
        break

print("Pesos finales:", pesos)
print("Sesgo final:", round(sesgo, 3))
for x, _ in patrones:
    print(x, "->", activar(sesgo + pesos[0]*x[0] + pesos[1]*x[1]))
