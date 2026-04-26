"""
BÚSQUEDA BIDIRECCIONAL

Busca desde dos direcciones simultáneamente:
- Desde el nodo inicial hacia el objetivo
- Desde el objetivo hacia el nodo inicial

Se encuentran en el medio, reduciendo el espacio de búsqueda.
Mucho más eficiente que buscar desde una sola dirección.
"""


def busqueda_bidireccional(grafo, inicio, objetivo):
    
    if inicio == objetivo:
        return True, [inicio]

    # Colas para ambas direcciones
    cola_inicio = [inicio]
    cola_objetivo = [objetivo]

    # Diccionarios para rastrear padres
    padre_inicio = {inicio: None}
    padre_objetivo = {objetivo: None}

    # Visitados en cada dirección
    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}

    while cola_inicio or cola_objetivo:
        # Expandir desde la dirección del inicio
        if cola_inicio:
            nodo = cola_inicio.pop(0)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados_inicio:
                    visitados_inicio.add(vecino)
                    padre_inicio[vecino] = nodo
                    cola_inicio.append(vecino)

                    # Verificar si se encontró con la búsqueda del objetivo
                    if vecino in visitados_objetivo:
                        camino_inicio = []
                        actual = vecino
                        while actual is not None:
                            camino_inicio.append(actual)
                            actual = padre_inicio[actual]
                        camino_inicio.reverse()

                        camino_objetivo = []
                        actual = vecino
                        while actual is not None:
                            camino_objetivo.append(actual)
                            actual = padre_objetivo[actual]

                        camino_completo = camino_inicio + camino_objetivo[1:]
                        return True, camino_completo

        # Expandir desde la dirección del objetivo
        if cola_objetivo:
            nodo = cola_objetivo.pop(0)
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados_objetivo:
                    visitados_objetivo.add(vecino)
                    padre_objetivo[vecino] = nodo
                    cola_objetivo.append(vecino)

                    # Verificar si se encontró con la búsqueda del inicio
                    if vecino in visitados_inicio:
                        camino_inicio = []
                        actual = vecino
                        while actual is not None:
                            camino_inicio.append(actual)
                            actual = padre_inicio[actual]
                        camino_inicio.reverse()

                        camino_objetivo = []
                        actual = vecino
                        while actual is not None:
                            camino_objetivo.append(actual)
                            actual = padre_objetivo[actual]

                        camino_completo = camino_inicio + camino_objetivo[1:]
                        return True, camino_completo

    return False, []


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

    print("Grafo para búsqueda bidireccional:")
    for nodo, vecinos in grafo.items():
        print(f"  {nodo} -> {vecinos}")

    print("\n" + "=" * 70)
    nodo_inicio = 1
    nodo_objetivo = 9
    print(f"Buscar camino de {nodo_inicio} a {nodo_objetivo} (búsqueda bidireccional):")
    print("=" * 70)

    encontrado, camino = busqueda_bidireccional(grafo, nodo_inicio, nodo_objetivo)

    if encontrado:
        print(f"CAMINO ENCONTRADO")
        print(f"  De {nodo_inicio} a {nodo_objetivo}")
        print(f"  Camino: {' → '.join(map(str, camino))}")
        print(f"  Longitud del camino: {len(camino) - 1} pasos")

    else:
        print(f"No hay camino entre {nodo_inicio} y {nodo_objetivo}")