# Reconocimiento de objetos por plantilla sencilla.

plantillas = {
    "cuadro": [1, 1, 1, 1],
    "linea": [0, 1, 1, 0],
    "punto": [0, 0, 1, 0]
}

objeto = [1, 1, 1, 0.8]

def error(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))

errores = {nombre: error(objeto, patron) for nombre, patron in plantillas.items()}
reconocido = min(errores, key=errores.get)

print("Errores:", errores)
print("Objeto reconocido:", reconocido)
