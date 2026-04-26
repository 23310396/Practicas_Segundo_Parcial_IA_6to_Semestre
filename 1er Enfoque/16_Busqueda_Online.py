import random
from collections import deque

random.seed(0)

class BusquedaOnline:
    def __init__(self, grafo, valores=None):
        """
        grafo: {nodo: [vecinos]}
        valores: {nodo: valor} para búsqueda de metas
        """
        self.grafo = grafo
        self.valores = valores or {}
        self.visitados = set()
        self.padres = {}

    def buscar(self, inicio, objetivo=None, max_pasos=100):
        """
        Búsqueda online simple.
        - Explora paso a paso.
        - Puede usar la información del nodo actual.
        - No conoce todo el grafo desde el inicio.
        """
        self.visitados = set()
        self.padres = {inicio: None}
        actual = inicio
        pasos = 0

        while pasos < max_pasos:
            pasos += 1
            self.visitados.add(actual)

            if objetivo is not None and actual == objetivo:
                return self._reconstruir_camino(actual), pasos

            if objetivo is not None and self.valores.get(actual) == objetivo:
                return self._reconstruir_camino(actual), pasos

            vecinos = [v for v in self.grafo.get(actual, []) if v not in self.visitados]
            if not vecinos:
                break

            # Elegir vecino usando heurística local simple: mejor valor conocido
            siguiente = self._mejor_vecino(vecinos, objetivo)
            self.padres[siguiente] = actual
            actual = siguiente

        return None, pasos

    def _mejor_vecino(self, vecinos, objetivo):
        """Selecciona el vecino con mejor valor local o el primero disponible."""
        if objetivo is not None:
            vecinos_objetivo = [v for v in vecinos if self.valores.get(v) == objetivo]
            if vecinos_objetivo:
                return vecinos_objetivo[0]

        vecinos_ordenados = sorted(vecinos, key=lambda v: self.valores.get(v, 0), reverse=True)
        return vecinos_ordenados[0]

    def _reconstruir_camino(self, nodo):
        camino = []
        while nodo is not None:
            camino.append(nodo)
            nodo = self.padres.get(nodo)
        camino.reverse()
        return camino


if __name__ == "__main__":
    print("=== BÚSQUEDA ONLINE ===\n")

    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H'],
        'E': [],
        'F': [],
        'G': ['I'],
        'H': [],
        'I': []
    }

    valores = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 5,
        'E': 4,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9
    }

    busqueda = BusquedaOnline(grafo, valores)

    print("Ejemplo 1: encontrar el nodo 'I' desde A")
    camino, pasos = busqueda.buscar('A', objetivo='I')
    print("Camino:", camino)
    print("Pasos:", pasos)

    print("\nEjemplo 2: encontrar nodo de valor 6 desde A")
    camino, pasos = busqueda.buscar('A', objetivo=6)
    print("Camino:", camino)
    print("Pasos:", pasos)
