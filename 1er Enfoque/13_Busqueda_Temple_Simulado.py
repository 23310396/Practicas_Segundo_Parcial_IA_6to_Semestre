import math
import random

random.seed(0)

def evaluar(x, y):
    """
    Función a maximizar: -((x-3)^2 + (y-2)^2) + 10
    Máximo global en (3, 2) con valor 10.
    """
    return -(math.pow(x - 3, 2) + math.pow(y - 2, 2)) + 10


def generar_vecino(x, y, paso=0.33):
    """Genera un vecino aleatorio cercano."""
    dx = random.choice([-paso, 0, paso])
    dy = random.choice([-paso, 0, paso])
    # Evitar quedarse en el mismo punto
    if dx == 0 and dy == 0:
        dx = paso
    return round(x + dx, 2), round(y + dy, 2)


def temple_simulado(x_inicial, y_inicial, temperatura_inicial=10.0, tasa_enfriamiento=0.95, iteraciones_max=100):
    """
    Algoritmo de Temple Simulado (Simulated Annealing).

    - Comienza con una solución inicial.
    - Genera un vecino aleatorio.
    - Si es mejor, lo acepta.
    - Si es peor, lo acepta con probabilidad exp((delta)/T).
    - Enfriamos la temperatura T en cada iteración.
    """
    x_actual, y_actual = x_inicial, y_inicial
    valor_actual = evaluar(x_actual, y_actual)

    x_mejor, y_mejor = x_actual, y_actual
    valor_mejor = valor_actual

    historial = [(x_actual, y_actual, valor_actual)]
    temperatura = temperatura_inicial

    for i in range(iteraciones_max):
        vecino = generar_vecino(x_actual, y_actual)
        valor_vecino = evaluar(*vecino)

        delta = valor_vecino - valor_actual
        if delta > 0:
            aceptar = True
        else:
            probabilidad = math.exp(delta / temperatura)
            aceptar = random.random() < probabilidad

        if aceptar:
            x_actual, y_actual = vecino
            valor_actual = valor_vecino
            historial.append((x_actual, y_actual, valor_actual))

        if valor_actual > valor_mejor:
            x_mejor, y_mejor = x_actual, y_actual
            valor_mejor = valor_actual

        temperatura *= tasa_enfriamiento
        if temperatura < 1e-6:
            break

    return (x_mejor, y_mejor), valor_mejor, iteraciones_max, historial


def resolver_temple(x_inicial, y_inicial, temperatura_inicial=10.0, tasa_enfriamiento=0.95):
    print(f"Inicio: x={x_inicial:.2f}, y={y_inicial:.2f}")
    print(f"Valor inicial: {evaluar(x_inicial, y_inicial):.4f}\n")

    (x_final, y_final), valor_final, iteraciones, historial = temple_simulado(
        x_inicial,
        y_inicial,
        temperatura_inicial=temperatura_inicial,
        tasa_enfriamiento=tasa_enfriamiento,
        iteraciones_max=100
    )

    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Mejor solución encontrada: x={x_final:.2f}, y={y_final:.2f}")
    print(f"Valor final: {valor_final:.4f}\n")
    print("Historial (primeros 10 pasos):")
    for i, (x, y, valor) in enumerate(historial[:10]):
        print(f"  Paso {i}: x={x:.2f}, y={y:.2f}, valor={valor:.4f}")
    if len(historial) > 10:
        print(f"  ... ({len(historial) - 10} pasos más)")
    print(f"\nOptimal global: x=3.00, y=2.00, valor=10.0000")


if __name__ == "__main__":
    print("=== BÚSQUEDA DE TEMPLE SIMULADO ===\n")

    print("CASO 1: Inicio CERCANO (2.5, 1.8)")
    print("-" * 50)
    resolver_temple(2.5, 1.8)
    print("\n" + "=" * 50 + "\n")

    print("CASO 2: Inicio LEJANO (-2, -2)")
    print("-" * 50)
    resolver_temple(-2, -2)
