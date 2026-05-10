# Movimiento
# Detectar movimiento comparando dos cuadros sencillos.

cuadro_1 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

cuadro_2 = [
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
]

cambios = []
for y in range(len(cuadro_1)):
    for x in range(len(cuadro_1[0])):
        if cuadro_1[y][x] != cuadro_2[y][x]:
            cambios.append((x, y))

print("Pixeles con cambio:", cambios)
print("Hubo movimiento:", len(cambios) > 0)
