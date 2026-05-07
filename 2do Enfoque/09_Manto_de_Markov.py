# Manto de Markov
# En una red bayesiana, el manto de un nodo son sus padres, hijos y otros padres de sus hijos.

grafo = {
    "Nube": ["Lluvia"],
    "Riego": ["CespedMojado"],
    "Lluvia": ["CespedMojado", "Trafico"],
    "CespedMojado": [],
    "Trafico": []
}

def padres(nodo):
    encontrados = []
    for posible_padre, hijos in grafo.items():
        if nodo in hijos:
            encontrados.append(posible_padre)
    return encontrados

def manto_markov(nodo):
    manto = set(padres(nodo))
    hijos = grafo[nodo]
    manto.update(hijos)
    for hijo in hijos:
        manto.update(padres(hijo))
    manto.discard(nodo)
    return sorted(manto)

nodo = "Lluvia"
print("Nodo:", nodo)
print("Manto de Markov:", manto_markov(nodo))
