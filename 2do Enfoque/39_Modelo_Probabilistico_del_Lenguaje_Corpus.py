# Modelo probabilistico del lenguaje usando corpus
# Se calculan probabilidades de palabras por frecuencia.

corpus = "el robot aprende el robot decide el sistema aprende"
palabras = corpus.split()
conteo = {}
for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1

total = len(palabras)
probabilidades = {p: c / total for p, c in conteo.items()}

print("Probabilidades de palabras:")
for palabra, prob in sorted(probabilidades.items()):
    print(f"P({palabra}) = {prob:.3f}")
