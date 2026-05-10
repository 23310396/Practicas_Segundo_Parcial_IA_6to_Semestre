# Reconocimiento de escritura simple
# Se clasifican digitos dibujados como vectores pequenos.

plantillas = {
    "0": [1, 1, 1, 1, 0, 1, 1, 1, 1],
    "1": [0, 1, 0, 0, 1, 0, 0, 1, 0]
}

entrada = [0, 1, 0, 0, 1, 0, 0, 1, 0]

def distancia(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))

puntajes = {digito: distancia(entrada, patron) for digito, patron in plantillas.items()}
print("Puntajes:", puntajes)
print("Digito reconocido:", min(puntajes, key=puntajes.get))
