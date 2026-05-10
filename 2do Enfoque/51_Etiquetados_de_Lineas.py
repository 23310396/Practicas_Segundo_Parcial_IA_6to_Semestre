# Etiquetado de lineas
# Se etiquetan segmentos como borde vertical, horizontal o diagonal.

lineas = [
    ((0, 0), (0, 5)),
    ((1, 1), (6, 1)),
    ((2, 2), (5, 5))
]

def etiquetar(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0:
        return "vertical"
    if dy == 0:
        return "horizontal"
    return "diagonal"

for linea in lineas:
    print(linea, "->", etiquetar(*linea))
