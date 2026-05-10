# Texturas y sombras
# La textura se aproxima con variacion local; la sombra con baja intensidad.

imagen = [20, 22, 21, 80, 40, 42, 41, 10, 11]

variaciones = []
for i in range(1, len(imagen)):
    variaciones.append(abs(imagen[i] - imagen[i-1]))

textura_promedio = sum(variaciones) / len(variaciones)
sombras = [i for i, valor in enumerate(imagen) if valor < 25]

print("Variacion promedio de textura:", round(textura_promedio, 2))
print("Pixeles detectados como sombra:", sombras)
