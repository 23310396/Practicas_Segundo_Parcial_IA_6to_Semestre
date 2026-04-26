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
    return 0

def greedy_best_first(grafo, posiciones, inicio, objetivo):
    """
    Greedy Best-First Search (Búsqueda Voraz Primero el Mejor).
    
    Solo usa la heurística, no considera el costo real acumulado.
    Siempre elige el nodo que parece más cercano al objetivo (según heurística).
    Retorna: (camino, costo_total) o None
    """
    if inicio not in grafo or objetivo not in grafo:
        return None

    # Cola de prioridad: (heuristica, nodo)
    # Solo priorizamos por heurística, NO por costo real
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (heuristica(inicio, objetivo, posiciones), inicio))

    visitados = set()
    padres = {inicio: None}
    costos = {inicio: 0}  # Rastrear el costo acumulado

    while cola_prioridad:
        h_actual, nodo = heapq.heappop(cola_prioridad)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == objetivo:
            # Reconstruir camino
            camino = []
            actual = nodo
            while actual is not None:
                camino.append(actual)
                actual = padres[actual]
            camino.reverse()
            return camino, costos[nodo]

        # Expandir vecinos
        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                costo_nuevo = costos[nodo] + costo
                if vecino not in costos or costo_nuevo < costos[vecino]:
                    costos[vecino] = costo_nuevo
                    heapq.heappush(cola_prioridad, (heuristica(vecino, objetivo, posiciones), vecino))
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

    resultado = greedy_best_first(grafo, posiciones, 'A', 'E')
    if resultado:
        camino, costo = resultado
        print("Camino encontrado:", camino)
        print("Costo total:", costo)
    else:
        print("No se encontró camino")
