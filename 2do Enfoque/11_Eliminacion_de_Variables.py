# Eliminacion de variables
# Mismo ejemplo del cesped mojado, eliminando la variable Riego por suma.

p_lluvia = {True: 0.30, False: 0.70}
p_riego = {True: 0.40, False: 0.60}
p_mojado = {
    (True, True): 0.99,
    (True, False): 0.80,
    (False, True): 0.90,
    (False, False): 0.05
}

factor_lluvia = {}
for lluvia in [True, False]:
    suma_sobre_riego = 0
    for riego in [True, False]:
        suma_sobre_riego += p_riego[riego] * p_mojado[(lluvia, riego)]
    factor_lluvia[lluvia] = p_lluvia[lluvia] * suma_sobre_riego

normalizador = sum(factor_lluvia.values())
posterior = {valor: factor_lluvia[valor] / normalizador for valor in factor_lluvia}

print("Resultado despues de eliminar Riego:")
print(posterior)
