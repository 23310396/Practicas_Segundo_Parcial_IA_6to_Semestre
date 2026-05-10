# Graficos por computador
# Dibujar una linea en una matriz de caracteres.

ancho, alto = 12, 7
pantalla = [["." for _ in range(ancho)] for _ in range(alto)]

for x in range(ancho):
    y = int((alto - 1) * x / (ancho - 1))
    pantalla[y][x] = "#"

print("Linea dibujada:")
for fila in pantalla:
    print("".join(fila))
