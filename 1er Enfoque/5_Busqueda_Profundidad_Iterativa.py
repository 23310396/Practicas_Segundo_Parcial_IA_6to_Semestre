"""
BÚSQUEDA EN PROFUNDIDAD ITERATIVA (IDDFS - Iterative Deepening DFS)

Esta técnica combina BFS y DFS:
- Usa DFS limitada por profundidad
- Aumenta gradualmente el límite de profundidad
- Garantiza encontrar el camino más corto en términos de profundidad
- Evita los problemas de memoria de DFS normal
"""


def buscar_valor_iterativo(grafo, valores_nodos, inicio, valor_objetivo, max_profundidad_total=10):
    for profundidad in range(max_profundidad_total + 1):
        visitados = set()
        pila = [(inicio, [inicio], 0)]  # (nodo, camino, profundidad_actual)

        while pila:
            nodo_actual, camino, prof_actual = pila.pop()

            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            if valores_nodos[nodo_actual] == valor_objetivo:
                return True, camino, list(visitados), nodo_actual, profundidad

            if prof_actual < profundidad:
                for vecino in reversed(grafo.get(nodo_actual, [])):
                    if vecino not in visitados:
                        pila.append((vecino, camino + [vecino], prof_actual + 1))

    return False, [], [], None, max_profundidad_total


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

    print("Grafo para IDDFS:")
    for nodo, vecinos in grafo.items():
        print(f"  {nodo} -> {vecinos}")

    valor_buscado = 60
    print(f"\nBuscar {valor_buscado} usando IDDFS:")
    

    encontrado, camino, explorados, nodo_encontrado, profundidad_usada = buscar_valor_iterativo(
        grafo, valores_nodos, 1, valor_buscado, 2) # Limitar a profundidad 2 para encontrar el valor 50

    if encontrado:
        print(f"  Valor {valor_buscado} está en el nodo: {nodo_encontrado}")
        print(f"  Camino más corto: {' → '.join(map(str, camino))}")
        print(f"  Profundidad necesaria: {profundidad_usada}")
        print(f"  Nodos explorados: {explorados}")

    else:
        print(f"Valor {valor_buscado} no encontrado")
