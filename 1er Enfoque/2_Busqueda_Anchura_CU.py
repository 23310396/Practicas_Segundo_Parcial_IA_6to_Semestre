"""
BÚSQUEDA EN ANCHURA DE COSTO UNIFORME (Uniform Cost Search - UCS)
A diferencia de la búsqueda en anchura tradicional, UCS considera el costo acumulado 
para llegar a cada nodo.
Busca el nodo que contiene un valor específico, explorando los nodos con menor costo acumulado
"""

import heapq


def busqueda_costo_uniforme_valor(grafo, valores_nodos, inicio, valor_objetivo):
    """
    Busca el nodo que contiene un VALOR específico usando UCS.
    """
    cola_prioridad = [(0, inicio)]  # (costo_acumulado, nodo)
    costo_minimo = {inicio: 0}
    padre = {inicio: None}
    explorados = set()

    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual in explorados:
            continue

        explorados.add(nodo_actual)

        # Si este nodo tiene el valor que buscamos
        if valores_nodos[nodo_actual] == valor_objetivo:
            camino = []
            actual = nodo_actual
            while actual is not None:
                camino.append(actual)
                actual = padre[actual]
            return True, camino[::-1], costo_actual, list(explorados), nodo_actual

        for vecino, costo_arista in grafo[nodo_actual]:
            costo_nuevo = costo_actual + costo_arista

            if vecino not in costo_minimo or costo_nuevo < costo_minimo[vecino]:
                costo_minimo[vecino] = costo_nuevo
                padre[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (costo_nuevo, vecino))

    return False, [], 0, list(explorados), None


# ====== EJEMPLO======

if __name__ == "__main__":
    grafo = {
        1: [(2, 1), (3, 10)],     # Nodo 1 conecta con 2 (costo 1) y 3 (costo 10)
        2: [(1, 1), (4, 1)],      # Nodo 2 conecta con 1 (costo 1) y 4 (costo 1)
        3: [(1, 10), (5, 5)],     # Nodo 3 conecta con 1 (costo 10) y 5 (costo 5)
        4: [(2, 1)],               # Nodo 4 conecta con 2 (costo 1)
        5: [(3, 5), (6, 1)],      # Nodo 5 conecta con 3 (costo 5) y 6 (costo 1)
        6: [(5, 1)]                # Nodo 6 conecta con 5 (costo 1)
    }

    valores_nodos = {
        1: 10,   
        2: 20,   
        3: 30,   
        4: 40,  
        5: 50,   
        6: 100   
    }

    print("=" * 70)
    print("GRAFO CON NODOS NUMÉRICOS Y VALORES:")
    print("=" * 70)
    for nodo, conexiones in grafo.items():
        valor = valores_nodos[nodo]
        print(f"  Nodo {nodo} -> conexiones: {conexiones} | VALOR: {valor}")

    print("\n" + "=" * 70)
    print("BUSCANDO VALOR NUMÉRICO EN LOS NODOS:")
    print("=" * 70)

    valor_buscado = 100

    encontrado, camino, costo_total, explorados, nodo_encontrado = busqueda_costo_uniforme_valor(
        grafo, valores_nodos, 1, valor_buscado)

    if encontrado:
        print(f"VALOR {valor_buscado} ENCONTRADO")
        print(f"  Está en el nodo: {nodo_encontrado}")
        print(f"  Camino para llegar: {' → '.join(map(str, camino))}")
        print(f"  Costo total del camino: {costo_total}")
        print(f"  Nodos que exploró: {explorados}")
    else:
        print(f"El valor {valor_buscado} no existe en ningún nodo")