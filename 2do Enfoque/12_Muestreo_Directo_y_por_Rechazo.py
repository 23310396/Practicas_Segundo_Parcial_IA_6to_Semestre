# Muestreo directo y por rechazo
# Estimar P(Lluvia | CespedMojado=True)

import random

random.seed(12)

def elegir(prob_true):
    return random.random() < prob_true

def muestra_red():
    lluvia = elegir(0.30)
    riego = elegir(0.40)
    tabla_mojado = {
        (True, True): 0.99,
        (True, False): 0.80,
        (False, True): 0.90,
        (False, False): 0.05
    }
    mojado = elegir(tabla_mojado[(lluvia, riego)])
    return lluvia, riego, mojado

aceptadas = 0
lluvia_y_mojado = 0

for _ in range(10000):
    lluvia, riego, mojado = muestra_red()
    if mojado:
        aceptadas += 1
        if lluvia:
            lluvia_y_mojado += 1

estimacion = lluvia_y_mojado / aceptadas
print("Muestras aceptadas:", aceptadas)
print(f"P(Lluvia | Mojado=True) aproximada = {estimacion:.3f}")
