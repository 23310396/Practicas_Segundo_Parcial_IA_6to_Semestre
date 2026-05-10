# Traduccion automatica estadistica simplificada
# Se elige la traduccion palabra por palabra con mayor probabilidad.

tabla = {
    "el": {"the": 0.9, "a": 0.1},
    "robot": {"robot": 0.95, "machine": 0.05},
    "aprende": {"learns": 0.8, "studies": 0.2}
}

frase = "el robot aprende"
traduccion = []
prob_total = 1.0

for palabra in frase.split():
    opciones = tabla[palabra]
    mejor = max(opciones, key=opciones.get)
    traduccion.append(mejor)
    prob_total *= opciones[mejor]

print("Frase original:", frase)
print("Traduccion:", " ".join(traduccion))
print(f"Probabilidad aproximada = {prob_total:.3f}")
