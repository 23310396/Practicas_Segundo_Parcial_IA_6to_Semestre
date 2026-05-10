# Extraccion de informacion
# Se extraen datos simples de frases con un patron.

textos = [
    "sensor temperatura valor 35",
    "sensor presion valor 120",
    "robot estado activo"
]

extraidos = []
for linea in textos:
    partes = linea.split()
    if len(partes) == 4 and partes[0] == "sensor" and partes[2] == "valor":
        extraidos.append({"sensor": partes[1], "valor": float(partes[3])})

print("Informacion extraida:")
for item in extraidos:
    print(item)
