# Algoritmo hacia delante-atras en un HMM pequeno.

estados = ["Soleado", "Lluvia"]
inicial = {"Soleado": 0.6, "Lluvia": 0.4}
trans = {
    "Soleado": {"Soleado": 0.7, "Lluvia": 0.3},
    "Lluvia": {"Soleado": 0.4, "Lluvia": 0.6}
}
emision = {
    "Soleado": {"normal": 0.8, "paraguas": 0.2},
    "Lluvia": {"normal": 0.1, "paraguas": 0.9}
}
obs = ["paraguas", "normal", "paraguas"]

def normalizar(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}

adelante = []
alpha = normalizar({e: inicial[e] * emision[e][obs[0]] for e in estados})
adelante.append(alpha)
for t in range(1, len(obs)):
    alpha = normalizar({e2: emision[e2][obs[t]] * sum(alpha[e1] * trans[e1][e2] for e1 in estados) for e2 in estados})
    adelante.append(alpha)

atras = [{e: 1.0 for e in estados}]
beta = atras[0]
for t in range(len(obs) - 2, -1, -1):
    beta = normalizar({e1: sum(trans[e1][e2] * emision[e2][obs[t+1]] * beta[e2] for e2 in estados) for e1 in estados})
    atras.insert(0, beta)

suavizado = []
for t in range(len(obs)):
    combinado = {e: adelante[t][e] * atras[t][e] for e in estados}
    suavizado.append(normalizar(combinado))

for i, dist in enumerate(suavizado, start=1):
    print(f"Tiempo {i}:", dist)
