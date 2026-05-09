# Naive Bayes para clasificar mensajes cortos.

mensajes = [
    ("gana dinero rapido", "spam"),
    ("oferta dinero premio", "spam"),
    ("reunion de proyecto", "normal"),
    ("avance del proyecto", "normal")
]

clases = ["spam", "normal"]
vocab = sorted(set(palabra for texto, _ in mensajes for palabra in texto.split()))

conteo_clase = {c: 0 for c in clases}
conteo_palabras = {c: {p: 1 for p in vocab} for c in clases}  # suavizado Laplace

for texto, clase in mensajes:
    conteo_clase[clase] += 1
    for palabra in texto.split():
        conteo_palabras[clase][palabra] += 1

def clasificar(texto):
    resultados = {}
    for clase in clases:
        prob = conteo_clase[clase] / len(mensajes)
        total_palabras = sum(conteo_palabras[clase].values())
        for palabra in texto.split():
            if palabra in vocab:
                prob *= conteo_palabras[clase][palabra] / total_palabras
        resultados[clase] = prob
    return max(resultados, key=resultados.get), resultados

mensaje = "dinero premio"
clase, puntajes = clasificar(mensaje)
print("Mensaje:", mensaje)
print("Puntajes:", puntajes)
print("Clase asignada:", clase)
