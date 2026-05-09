# Aprendizaje profundo simplificado
# Red pequena con una capa oculta, solo pase hacia adelante.

import math

entrada = [0.8, 0.4]

pesos_oculta = [
    [0.5, -0.3],
    [0.2, 0.7]
]
sesgos_oculta = [0.1, -0.2]

pesos_salida = [0.6, -0.4]
sesgo_salida = 0.05

def relu(x):
    return max(0, x)

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

oculta = []
for neurona in range(2):
    z = sesgos_oculta[neurona]
    for i in range(2):
        z += entrada[i] * pesos_oculta[neurona][i]
    oculta.append(relu(z))

z_salida = sesgo_salida + sum(oculta[i] * pesos_salida[i] for i in range(2))
salida = sigmoide(z_salida)

print("Activaciones ocultas:", [round(x, 3) for x in oculta])
print(f"Salida de la red: {salida:.3f}")
