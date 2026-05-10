# Deteccion de aristas y segmentacion en una imagen 1D.

imagen = [10, 12, 11, 80, 85, 83, 20, 18]

aristas = []
for i in range(1, len(imagen)):
    cambio = abs(imagen[i] - imagen[i-1])
    if cambio > 30:
        aristas.append(i)

segmentacion = ["objeto" if valor > 50 else "fondo" for valor in imagen]

print("Imagen 1D:", imagen)
print("Aristas detectadas en indices:", aristas)
print("Segmentacion:", segmentacion)
