from collections import deque, defaultdict
import heapq

class BusquedaNoInformada:
    def __init__(self, grafo, valores_nodos=None):
        self.grafo = grafo
        self.valores_nodos = valores_nodos or {}

    def bfs(self, inicio, objetivo=None):
        visitados = set()
        cola = deque([inicio])
        padres = {inicio: None}
        visitados.add(inicio)

        while cola:
            nodo = cola.popleft()
            if objetivo is not None:
                if isinstance(objetivo, int) and self.valores_nodos.get(nodo) == objetivo:
                    return self._reconstruir_camino(padres, nodo)
                elif nodo == objetivo:
                    return self._reconstruir_camino(padres, nodo)

            for vecino in self.grafo.get(nodo, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
                    padres[vecino] = nodo

        return None if objetivo is not None else list(visitados)

    def dfs(self, inicio, objetivo=None):
        visitados = set()
        pila = [inicio]
        padres = {inicio: None}

        while pila:
            nodo = pila.pop()
            if nodo not in visitados:
                visitados.add(nodo)
                if objetivo is not None:
                    if isinstance(objetivo, int) and self.valores_nodos.get(nodo) == objetivo:
                        return self._reconstruir_camino(padres, nodo)
                    elif nodo == objetivo:
                        return self._reconstruir_camino(padres, nodo)

                for vecino in reversed(self.grafo.get(nodo, [])):
                    if vecino not in visitados:
                        pila.append(vecino)
                        padres[vecino] = nodo

        return None if objetivo is not None else list(visitados)

    def ucs(self, inicio, objetivo=None):
        # Para simplicidad, asumimos costo 1 por arista
        costos = {nodo: float('inf') for nodo in self.grafo}
        costos[inicio] = 0
        padres = {inicio: None}
        cola_prioridad = [(0, inicio)]  # (costo, nodo)

        while cola_prioridad:
            costo_actual, nodo = heapq.heappop(cola_prioridad)

            if costo_actual > costos[nodo]:
                continue

            if objetivo is not None:
                if isinstance(objetivo, int) and self.valores_nodos.get(nodo) == objetivo:
                    return self._reconstruir_camino(padres, nodo), costo_actual
                elif nodo == objetivo:
                    return self._reconstruir_camino(padres, nodo), costo_actual

            for vecino in self.grafo.get(nodo, []):
                nuevo_costo = costo_actual + 1  # costo por defecto
                if nuevo_costo < costos[vecino]:
                    costos[vecino] = nuevo_costo
                    padres[vecino] = nodo
                    heapq.heappush(cola_prioridad, (nuevo_costo, vecino))

        return None if objetivo is not None else (list(costos.keys()), costos)

    def dfs_limitada(self, inicio, limite_profundidad, objetivo=None):
        visitados = set()
        pila = [(inicio, 0)]  # (nodo, profundidad)
        padres = {inicio: None}

        while pila:
            nodo, profundidad = pila.pop()
            if nodo not in visitados and profundidad <= limite_profundidad:
                visitados.add(nodo)
                if objetivo is not None:
                    if isinstance(objetivo, int) and self.valores_nodos.get(nodo) == objetivo:
                        return self._reconstruir_camino(padres, nodo)
                    elif nodo == objetivo:
                        return self._reconstruir_camino(padres, nodo)

                if profundidad < limite_profundidad:
                    for vecino in reversed(self.grafo.get(nodo, [])):
                        if vecino not in visitados:
                            pila.append((vecino, profundidad + 1))
                            padres[vecino] = nodo

        return None if objetivo is not None else list(visitados)

    def iddfs(self, inicio, objetivo=None, max_profundidad=10):
        for limite in range(max_profundidad + 1):
            resultado = self.dfs_limitada(inicio, limite, objetivo)
            if resultado is not None:
                return resultado
        return None

    def busqueda_bidireccional(self, inicio, objetivo):
        if inicio == objetivo:
            return [inicio]

        # Grafo inverso
        grafo_inv = defaultdict(list)
        for nodo, vecinos in self.grafo.items():
            for vecino in vecinos:
                grafo_inv[vecino].append(nodo)

        visitados_inicio = set([inicio])
        visitados_objetivo = set([objetivo])
        cola_inicio = deque([inicio])
        cola_objetivo = deque([objetivo])
        padres_inicio = {inicio: None}
        padres_objetivo = {objetivo: None}

        while cola_inicio and cola_objetivo:
            # Expansión desde inicio
            nodo_inicio = cola_inicio.popleft()
            for vecino in self.grafo.get(nodo_inicio, []):
                if vecino not in visitados_inicio:
                    visitados_inicio.add(vecino)
                    cola_inicio.append(vecino)
                    padres_inicio[vecino] = nodo_inicio
                    if vecino in visitados_objetivo:
                        return self._reconstruir_camino_bidireccional(padres_inicio, padres_objetivo, vecino)

            # Expansión desde objetivo
            nodo_objetivo = cola_objetivo.popleft()
            for vecino in grafo_inv.get(nodo_objetivo, []):
                if vecino not in visitados_objetivo:
                    visitados_objetivo.add(vecino)
                    cola_objetivo.append(vecino)
                    padres_objetivo[vecino] = nodo_objetivo
                    if vecino in visitados_inicio:
                        return self._reconstruir_camino_bidireccional(padres_inicio, padres_objetivo, vecino)

        return None

    def _reconstruir_camino(self, padres, nodo):
        camino = []
        while nodo is not None:
            camino.append(nodo)
            nodo = padres[nodo]
        camino.reverse()
        return camino

    def _reconstruir_camino_bidireccional(self, padres_inicio, padres_objetivo, encuentro):
        camino1 = self._reconstruir_camino(padres_inicio, encuentro)
        camino2 = self._reconstruir_camino(padres_objetivo, encuentro)
        camino2.reverse()
        return camino1 + camino2[1:]  # Evitar duplicar el nodo de encuentro

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo de ejemplo
    grafo = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [],
        6: [7],
        7: [8],
        8: [9],
        9: []
    }
    valores = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}

    busqueda = BusquedaNoInformada(grafo, valores)

    print("BFS desde 1 buscando valor 90:")
    resultado = busqueda.bfs(1, 90)
    print("Camino:", resultado)

    print("\nDFS desde 1 buscando nodo 9:")
    resultado = busqueda.dfs(1, 9)
    print("Camino:", resultado)

    print("\nUCS desde 1 buscando valor 60:")
    resultado, costo = busqueda.ucs(1, 60)
    print("Camino:", resultado, "Costo:", costo)

    print("\nDFS Limitada desde 1 con limite 3 buscando valor 50:")
    resultado = busqueda.dfs_limitada(1, 3, 50)
    print("Camino:", resultado)

    print("\nIDDFS desde 1 buscando valor 90:")
    resultado = busqueda.iddfs(1, 90)
    print("Camino:", resultado)

    print("\nBusqueda Bidireccional entre 1 y 9:")
    resultado = busqueda.busqueda_bidireccional(1, 9)
    print("Camino:", resultado)