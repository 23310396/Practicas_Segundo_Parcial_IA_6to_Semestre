import heapq
import math

def heuristica(nodo, objetivo, posiciones):
    """
    Función heurística: distancia euclidiana entre dos nodos.
    posiciones: diccionario {nodo: (x, y)}
    """
    if nodo in posiciones and objetivo in posiciones:
        x1, y1 = posiciones[nodo]
        x2, y2 = posiciones[objetivo]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return 0  # Heurística trivial

def a_star(grafo, posiciones, inicio, objetivo):
    """
    Algoritmo A* (A estrella).
    grafo: {nodo: [(vecino, costo)]}
    posiciones: {nodo: (x, y)} para heurística
    Retorna: (camino, costo_total) o None si no hay camino
    """
    if inicio not in grafo or objetivo not in grafo:
        return None

    # Cola de prioridad: (f_score, g_score, nodo)
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0 + heuristica(inicio, objetivo, posiciones), 0, inicio))

    g_score = {nodo: float('inf') for nodo in grafo}
    g_score[inicio] = 0

    padres = {inicio: None}

    while cola_prioridad:
        f_score, g_actual, nodo = heapq.heappop(cola_prioridad)

        if nodo == objetivo:
            # Reconstruir camino
            camino = []
            actual = nodo
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino, g_score[nodo]

        for vecino, costo in grafo.get(nodo, []):
            g_tentativo = g_actual + costo
            if g_tentativo < g_score.get(vecino, float('inf')):
                g_score[vecino] = g_tentativo
                f_score_nuevo = g_tentativo + heuristica(vecino, objetivo, posiciones)
                heapq.heappush(cola_prioridad, (f_score_nuevo, g_tentativo, vecino))
                padres[vecino] = nodo

    return None

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo con costos en aristas
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1), ('E', 3)],
        'E': [('D', 3)]
    }

    # Posiciones para heurística
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
        print("Camino encontrado:", camino)
        print("Costo total:", costo)
    else:
        print("No se encontró camino")