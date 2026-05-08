# Reconocimiento del habla simplificado
# Se compara una senal contra plantillas usando distancia absoluta.

plantillas = {
    "hola": [1, 2, 3, 2, 1],
    "adios": [3, 2, 1, 2, 3],
    "si": [1, 1, 2, 1, 1]
}

entrada = [1, 2, 2.8, 2.1, 1]

def distancia(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))

puntajes = {}
for palabra, patron in plantillas.items():
    puntajes[palabra] = distancia(entrada, patron)

reconocida = min(puntajes, key=puntajes.get)
print("Distancias:", puntajes)
print("Palabra reconocida:", reconocida)
