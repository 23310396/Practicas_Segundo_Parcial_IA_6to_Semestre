import heapq
import math

# ==================== A* ====================

def heuristica(nodo, objetivo, posiciones):
    """Distancia euclidiana como heurística."""
    if nodo in posiciones and objetivo in posiciones:
        x1, y1 = posiciones[nodo]
        x2, y2 = posiciones[objetivo]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return 0

def a_star(grafo, posiciones, inicio, objetivo):
    """
    A* algorithm.
    grafo: {nodo: [(vecino, costo)]}
    Retorna: (camino, costo_total) o None
    """
    if inicio not in grafo or objetivo not in grafo:
        return None

    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0 + heuristica(inicio, objetivo, posiciones), 0, inicio))

    g_score = {nodo: float('inf') for nodo in grafo}
    g_score[inicio] = 0
    padres = {inicio: None}

    while cola_prioridad:
        f_score, g_actual, nodo = heapq.heappop(cola_prioridad)

        if nodo == objetivo:
            camino = []
            actual = nodo
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino, g_score[nodo]

        for vecino, costo in grafo.get(nodo, []):
            g_tentativo = g_actual + costo
            if g_tentativo < g_score[vecino]:
                g_score[vecino] = g_tentativo
                f_score_nuevo = g_tentativo + heuristica(vecino, objetivo, posiciones)
                heapq.heappush(cola_prioridad, (f_score_nuevo, g_tentativo, vecino))
                padres[vecino] = nodo

    return None

# ==================== AO* ====================

def ao_star(grafo_and_or, inicio, objetivo):
    """
    AO* algorithm para grafos AND-OR.
    """
    g_score = {nodo: float('inf') for nodo in grafo_and_or}
    g_score[inicio] = 0
    
    padres = {inicio: None}
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        costo_actual, nodo = heapq.heappop(cola_prioridad)
        
        if nodo == objetivo:
            # Reconstruir camino
            camino = []
            actual = nodo
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino, g_score[nodo]
        
        if nodo in grafo_and_or:
            tipo_nodo = grafo_and_or[nodo]['tipo']
            vecinos = grafo_and_or[nodo]['vecinos']
            
            if tipo_nodo == 'OR':
                # Nodos OR: elige el vecino con menor costo
                for vecino, costo in vecinos:
                    nuevo_costo = g_score[nodo] + costo
                    if nuevo_costo < g_score[vecino]:
                        g_score[vecino] = nuevo_costo
                        padres[vecino] = nodo
                        heapq.heappush(cola_prioridad, (nuevo_costo, vecino))
            
            elif tipo_nodo == 'AND':
                # Nodos AND: deben cumplirse TODOS los vecinos
                for vecino, costo in vecinos:
                    nuevo_costo = g_score[nodo] + costo
                    if nuevo_costo < g_score[vecino]:
                        g_score[vecino] = nuevo_costo
                        padres[vecino] = nodo
                        heapq.heappush(cola_prioridad, (nuevo_costo, vecino))
    
    return None

# ===========Ejemplo==========

if __name__ == "__main__":
    # Ejemplo 1: A* (grafo simple)
    print("=== A* ===")
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1), ('E', 3)],
        'E': [('D', 3)]
    }
    
    posiciones = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (4, 0),
        'D': (4, 3),
        'E': (7, 3)
    }
    
    resultado = a_star(grafo, posiciones, 'A', 'E')
    if resultado:
        camino, costo = resultado
        print("Camino A*:", camino)
        print("Costo total:", costo)
    else:
        print("No se encontró camino con A*")
    
    # Ejemplo 2: AO* (grafo AND-OR)
    print("\n=== AO* ===")
    grafo_and_or = {
        'A': {'tipo': 'OR', 'vecinos': [('B', 2), ('C', 3)]},
        'B': {'tipo': 'AND', 'vecinos': [('D', 1), ('E', 1)]},
        'C': {'tipo': 'OR', 'vecinos': [('D', 2), ('F', 4)]},
        'D': {'tipo': 'OR', 'vecinos': [('G', 1)]},
        'E': {'tipo': 'OR', 'vecinos': [('G', 2)]},
        'F': {'tipo': 'OR', 'vecinos': [('G', 1)]},
        'G': {'tipo': 'OR', 'vecinos': []}  # Nodo objetivo
    }
    
    resultado_ao = ao_star(grafo_and_or, 'A', 'G')
    if resultado_ao:
        camino, costo = resultado_ao
        print("Camino AO*:", camino)
        print("Costo total:", costo)
    else:
        print("No se encontró camino con AO*")
