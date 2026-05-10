# Separabilidad lineal
# Probar si una recta separa dos clases.

puntos = [
    ((1, 1), -1),
    ((1, 2), -1),
    ((3, 3), 1),
    ((4, 3), 1)
]

w = [1, 1]
b = -5

def clasificar(p):
    return 1 if w[0]*p[0] + w[1]*p[1] + b >= 0 else -1

correctos = 0
for punto, clase in puntos:
    pred = clasificar(punto)
    print(punto, "real:", clase, "pred:", pred)
    if pred == clase:
        correctos += 1

print("Todos separados correctamente:", correctos == len(puntos))
