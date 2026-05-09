# Agrupamiento no supervisado
# Se agrupan puntos segun cercania a dos centroides.

puntos = [(1, 2), (1, 1), (2, 1), (8, 8), (9, 8), (8, 9)]
centroides = [(1, 1), (9, 9)]

def distancia(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

for _ in range(5):
    grupos = {0: [], 1: []}
    for p in puntos:
        indice = min(range(2), key=lambda i: distancia(p, centroides[i]))
        grupos[indice].append(p)
    centroides = []
    for i in range(2):
        xs = [p[0] for p in grupos[i]]
        ys = [p[1] for p in grupos[i]]
        centroides.append((sum(xs)/len(xs), sum(ys)/len(ys)))

print("Grupos finales:")
print(grupos)
print("Centroides:", centroides)
