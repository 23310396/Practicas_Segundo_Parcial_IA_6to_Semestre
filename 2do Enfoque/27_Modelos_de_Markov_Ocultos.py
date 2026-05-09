# Modelos de Markov Ocultos
# Calcular probabilidad de una secuencia de observaciones con el algoritmo forward.

estados = ["Alta", "Baja"]
inicial = {"Alta": 0.5, "Baja": 0.5}
trans = {
    "Alta": {"Alta": 0.7, "Baja": 0.3},
    "Baja": {"Alta": 0.4, "Baja": 0.6}
}
emision = {
    "Alta": {"compra": 0.8, "no_compra": 0.2},
    "Baja": {"compra": 0.3, "no_compra": 0.7}
}
obs = ["compra", "compra", "no_compra"]

alpha = {e: inicial[e] * emision[e][obs[0]] for e in estados}
for o in obs[1:]:
    alpha = {e2: emision[e2][o] * sum(alpha[e1] * trans[e1][e2] for e1 in estados) for e2 in estados}

print("Probabilidad de la secuencia:", round(sum(alpha.values()), 5))
print("Valores finales forward:", alpha)
