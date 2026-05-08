# Modelo Oculto de Markov
# Algoritmo de Viterbi para encontrar la secuencia de estados mas probable.

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
observaciones = ["paraguas", "paraguas", "normal"]

rutas = {e: (inicial[e] * emision[e][observaciones[0]], [e]) for e in estados}

for obs in observaciones[1:]:
    nuevas = {}
    for estado in estados:
        mejor_prob = -1
        mejor_ruta = None
        for anterior in estados:
            prob = rutas[anterior][0] * trans[anterior][estado] * emision[estado][obs]
            if prob > mejor_prob:
                mejor_prob = prob
                mejor_ruta = rutas[anterior][1] + [estado]
        nuevas[estado] = (mejor_prob, mejor_ruta)
    rutas = nuevas

prob, ruta = max(rutas.values(), key=lambda x: x[0])
print("Secuencia mas probable:", ruta)
print(f"Probabilidad: {prob:.5f}")
