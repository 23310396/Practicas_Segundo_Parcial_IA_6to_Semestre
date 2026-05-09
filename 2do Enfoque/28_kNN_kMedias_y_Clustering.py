# k-NN, k-Medias y clustering en un ejemplo pequeno.

puntos = [(1, 1, "A"), (2, 1, "A"), (8, 8, "B"), (9, 8, "B")]
nuevo = (2, 2)

def dist2(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

# k-NN
vecinos = sorted(puntos, key=lambda p: dist2(p, nuevo))[:3]
votos = {}
for _, _, etiqueta in vecinos:
    votos[etiqueta] = votos.get(etiqueta, 0) + 1
print("k-NN clasifica como:", max(votos, key=votos.get))

# k-medias rapido sin etiquetas
sin_etiqueta = [(x, y) for x, y, _ in puntos]
centros = [(1, 1), (9, 9)]
for _ in range(3):
    grupos = {0: [], 1: []}
    for p in sin_etiqueta:
        i = min([0, 1], key=lambda c: dist2(p, centros[c]))
        grupos[i].append(p)
    centros = [(sum(x for x, y in grupos[i])/len(grupos[i]), sum(y for x, y in grupos[i])/len(grupos[i])) for i in [0, 1]]
print("Centros de k-medias:", centros)
