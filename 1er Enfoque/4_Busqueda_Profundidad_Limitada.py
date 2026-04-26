"""
BÚSQUEDA EN PROFUNDIDAD LIMITADA

Busca un valor específico en el grafo, pero con límite de profundidad.
Se detiene cuando encuentra el valor o llega al límite máximo.
"""


def buscar_valor_limitado(grafo, valores_nodos, inicio, valor_objetivo, max_profundidad):
    visitados = set()
    pila = [(inicio, [inicio], 0)]  # (nodo, camino, profundidad)

    while pila:
        nodo_actual, camino, profundidad = pila.pop()
        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        if valores_nodos[nodo_actual] == valor_objetivo:
            return True, camino, list(visitados), nodo_actual

        if profundidad < max_profundidad:
            for vecino in reversed(grafo.get(nodo_actual, [])):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino], profundidad + 1))

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
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
        6: 60
    }

    print("Grafo para DFS limitada:")
    for nodo, vecinos in grafo.items():
        print(f"  {nodo} -> {vecinos}")
    
    
    valor_buscado = 50
    max_prof = 2
    print(f"Buscar {valor_buscado} con una profundidad de {max_prof}")

    encontrado, camino, explorados, nodo_encontrado = buscar_valor_limitado(
        grafo, valores_nodos, 1, valor_buscado, max_prof)

    if encontrado:
        print(f"  Valor {valor_buscado} está en el nodo: {nodo_encontrado}")
        print(f"  Camino seguido: {' → '.join(map(str, camino))}")
        print(f"  Nodos explorados: {explorados}")
        print(f"  Profundidad máxima usada: {len(camino) - 1}")
    else:
        print(f"Valor {valor_buscado} no encontrado dentro del límite de profundidad {max_prof}")

