"""
BÚSQUEDA EN PROFUNDIDAD (DFS - Depth-First Search)

La búsqueda en profundidad recorre un grafo siguiendo un camino
hasta llegar al final, y sólo entonces retrocede para explorar
otros caminos.
"""


def busqueda_profundidad(grafo, inicio, visitados=None, orden=None):
    if visitados is None:
        visitados = set()
    if orden is None:
        orden = []

    visitados.add(inicio)
    orden.append(inicio)

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            busqueda_profundidad(grafo, vecino, visitados, orden)

    return orden


def buscar_valor_profundidad(grafo, valores_nodos, inicio, valor_objetivo):
    visitados = set()
    pila = [(inicio, [inicio])]

    while pila:
        nodo_actual, camino = pila.pop()
        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)
        if valores_nodos[nodo_actual] == valor_objetivo:
            return True, camino, list(visitados), nodo_actual

        for vecino in reversed(grafo.get(nodo_actual, [])):
            if vecino not in visitados:
                pila.append((vecino, camino + [vecino]))

    return False, [], list(visitados), None


# ====== EJEMPLO ======

if __name__ == "__main__":
    grafo = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: []
    }

    valores_nodos = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6
    }

    print("Grafo para DFS:")
    for nodo, vecinos in grafo.items():
        print(f"  {nodo} -> {vecinos}")

    recorrido = busqueda_profundidad(grafo, 1)
    print(f"\nRecorrido DFS desde 1: {recorrido}")

    print("\nBuscar valor 50 en los nodos usando DFS:")
    valor_buscado = 5
    encontrado, camino, explorados, nodo_encontrado = buscar_valor_profundidad(
        grafo, valores_nodos, 1, valor_buscado)

    if encontrado:
        print(f"Valor {valor_buscado} encontrado en nodo {nodo_encontrado}")
        print(f"  Camino seguido: {camino}")
        print(f"  Nodos explorados: {explorados}")
    else:
        print(f"Valor {valor_buscado} no encontrado")
