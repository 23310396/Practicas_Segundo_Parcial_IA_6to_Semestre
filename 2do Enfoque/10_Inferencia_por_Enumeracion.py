# Inferencia por enumeracion
# Calcular P(Lluvia | CespedMojado=True)

p_lluvia = {True: 0.30, False: 0.70}
p_riego = {True: 0.40, False: 0.60}

p_mojado = {
    (True, True): 0.99,
    (True, False): 0.80,
    (False, True): 0.90,
    (False, False): 0.05
}

def probabilidad(lluvia, riego, mojado):
    p = p_lluvia[lluvia] * p_riego[riego]
    p *= p_mojado[(lluvia, riego)] if mojado else 1 - p_mojado[(lluvia, riego)]
    return p

resultado = {}
for lluvia in [True, False]:
    total = 0
    for riego in [True, False]:
        total += probabilidad(lluvia, riego, True)
    resultado[lluvia] = total

normalizador = sum(resultado.values())
for lluvia in resultado:
    resultado[lluvia] /= normalizador

print("P(Lluvia | CespedMojado=True):")
print(resultado)
