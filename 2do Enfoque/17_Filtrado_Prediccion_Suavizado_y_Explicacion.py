# Filtrado, prediccion, suavizado y explicacion
# Ejemplo compacto con un sistema de clima oculto y observaciones.

estados = ["Soleado", "Lluvia"]
trans = {
    "Soleado": {"Soleado": 0.8, "Lluvia": 0.2},
    "Lluvia": {"Soleado": 0.3, "Lluvia": 0.7}
}
sensor = {
    "Soleado": {"paraguas": 0.1, "sin_paraguas": 0.9},
    "Lluvia": {"paraguas": 0.8, "sin_paraguas": 0.2}
}

def normalizar(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}

def filtrar(creencia, obs):
    pred = {e2: sum(creencia[e1] * trans[e1][e2] for e1 in estados) for e2 in estados}
    corregida = {e: pred[e] * sensor[e][obs] for e in estados}
    return normalizar(corregida)

creencia = {"Soleado": 0.5, "Lluvia": 0.5}
observaciones = ["paraguas", "paraguas", "sin_paraguas"]

for obs in observaciones:
    creencia = filtrar(creencia, obs)

prediccion_manana = {e2: sum(creencia[e1] * trans[e1][e2] for e1 in estados) for e2 in estados}
explicacion = max(creencia, key=creencia.get)

print("Filtrado actual:", creencia)
print("Prediccion siguiente paso:", prediccion_manana)
print("Explicacion mas probable del estado actual:", explicacion)
