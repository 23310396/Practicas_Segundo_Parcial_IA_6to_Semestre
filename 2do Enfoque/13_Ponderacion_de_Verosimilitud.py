# Ponderacion de verosimilitud
# La evidencia CespedMojado=True no se rechaza; se usa como peso.

import random

random.seed(13)

def elegir(prob_true):
    return random.random() < prob_true

p_mojado = {
    (True, True): 0.99,
    (True, False): 0.80,
    (False, True): 0.90,
    (False, False): 0.05
}

pesos = {True: 0.0, False: 0.0}

for _ in range(10000):
    lluvia = elegir(0.30)
    riego = elegir(0.40)
    peso = p_mojado[(lluvia, riego)]  # evidencia: mojado=True
    pesos[lluvia] += peso

total = pesos[True] + pesos[False]
posterior = {k: pesos[k] / total for k in pesos}

print("P(Lluvia | Mojado=True) con ponderacion:")
print(posterior)
