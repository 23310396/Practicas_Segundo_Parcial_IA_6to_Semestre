import math
import random

random.seed(0)

def evaluar(x, y):
    """
    Función a maximizar: -((x-3)^2 + (y-2)^2) + 10
    Máximo global en (3, 2) con valor 10.
    """
    return -(math.pow(x - 3, 2) + math.pow(y - 2, 2)) + 10


def generar_vecinos(x, y, paso=0.5):
    """Genera 4 vecinos inmediatos: derecha, izquierda, arriba y abajo."""
    return [
        (round(x + paso, 2), y),
        (round(x - paso, 2), y),
        (x, round(y + paso, 2)),
        (x, round(y - paso, 2))
    ]


def haz_local(k=3, iteraciones_max=20, paso=0.5, rango_inicial=5.0):
    """
    Búsqueda de Haz Local (Local Beam Search).

    - Genera k estados iniciales aleatorios.
    - En cada iteración, expande los k estados y toma los mejores k vecinos.
    - Repite hasta terminar.
    """
    haz = []
    for _ in range(k):
        x = round(random.uniform(-rango_inicial, rango_inicial), 2)
        y = round(random.uniform(-rango_inicial, rango_inicial), 2)
        haz.append((x, y, evaluar(x, y)))

    historial = [list(haz)]

    for i in range(iteraciones_max):
        candidatos = []
        for x, y, valor in haz:
            vecinos = generar_vecinos(x, y, paso=paso)
            for x_vecino, y_vecino in vecinos:
                candidatos.append((x_vecino, y_vecino, evaluar(x_vecino, y_vecino)))
        candidatos.sort(key=lambda item: item[2], reverse=True)
        haz = candidatos[:k]
        historial.append(list(haz))

    mejor = max(haz, key=lambda item: item[2])
    return mejor, historial


def imprimir_resultados(mejor, historial):
    (x_mejor, y_mejor, valor_mejor) = mejor
    print(f"Mejor solución encontrada: x={x_mejor:.2f}, y={y_mejor:.2f}, valor={valor_mejor:.4f}")
    print("\nEstados del haz por iteración:")
    for i, estado in enumerate(historial):
        lineas = [f"({x:.2f},{y:.2f})={valor:.4f}" for x, y, valor in estado]
        print(f"  Iteración {i}: {', '.join(lineas)}")
    print("\nÓptimo global: x=3.00, y=2.00, valor=10.0000")


if __name__ == "__main__":
    print("=== BÚSQUEDA DE HAZ LOCAL ===\n")
    print("Parámetros: k=3, iteraciones=15, paso=0.5")
    print("-" * 50)
    mejor, historial = haz_local(k=3, iteraciones_max=15, paso=0.5, rango_inicial=5.0)
    imprimir_resultados(mejor, historial)
