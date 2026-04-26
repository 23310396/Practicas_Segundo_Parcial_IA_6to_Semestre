"""
BÚSQUEDA EN ANCHURA (BFS - Breadth-First Search)

Busca un número específico en el grafo, explorando nivel por nivel.
Se detiene cuando lo encuentra.
"""

from collections import deque


def buscar_numero(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([inicio])
    padre = {inicio: None}
    nodos_explorados = []
    
    visitados.add(inicio)
    
    while cola:
        nodo = cola.popleft()
        nodos_explorados.append(nodo)
        
        # Si encontramos el objetivo, reconstruimos el camino
        if nodo == objetivo:
            camino = []
            actual = objetivo
            while actual is not None:
                camino.append(actual)
                actual = padre[actual]
            return True, camino[::-1], nodos_explorados
        
        # Explora los vecinos
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                padre[vecino] = nodo
                cola.append(vecino)
    
    return False, [], nodos_explorados


# ====== EJEMPLO ======

if __name__ == "__main__":
    grafo = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5, 7],
        7: [6, 8],
        8: [7, 9],
        9: [8]
    }
    
    print("Grafo:")
    for nodo, vecinos in grafo.items():
        print(f"  {nodo} -> {vecinos}")
    
    """En esta linea podemos cambiar el valor del numero a buscar para observar
       como se comporta la busqueda en anchura
    """
    numero_buscado = 5
    
    print(f"\nBuscando el número: {numero_buscado}")
    encontrado, camino, explorados = buscar_numero(grafo, 1, numero_buscado)
    
    if encontrado:
        print(f"El número {numero_buscado} fue encontrado en el grafo.")
        print(f"  Camino: {' → '.join(map(str, camino))}")
        print(f"  Nodos que tuvo que explorar: {explorados}")
    else:
        print(f"El número {numero_buscado} no está en el grafo")
