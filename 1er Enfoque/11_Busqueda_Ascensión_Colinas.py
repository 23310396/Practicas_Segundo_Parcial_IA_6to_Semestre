import random
import math

def evaluar(x, y):
    """
    Función a maximizar (representa la "altura" de la colina).
    Esta es una función de ejemplo: -((x-3)^2 + (y-2)^2) + 10
    Máximo en (3, 2) con valor 10
    """
    return -(math.pow(x - 3, 2) + math.pow(y - 2, 2)) + 10

def generar_vecinos(x, y, paso=0.5):
    """
    Genera 4 vecinos (movimientos posibles): arriba, abajo, izquierda, derecha.
    Cada movimiento cambia x o y por 'paso'
    """
    vecinos = [
        (x + paso, y),      # Derecha
        (x - paso, y),      # Izquierda
        (x, y + paso),      # Arriba
        (x, y - paso)       # Abajo
    ]
    return vecinos

def hill_climbing(x_inicial, y_inicial, iteraciones_max=100):
    """
    Algoritmo de Ascensión de Colinas (Hill Climbing).
    
    Partiendo de (x_inicial, y_inicial):
    1. Evalúa la posición actual
    2. Genera vecinos (soluciones cercanas)
    3. Elige el vecino con mayor valor (greedy)
    4. Si mejora, se mueve allá. Si no, se detiene.
    
    Retorna: (solución_final, valor_final, iteraciones_realizadas, historial)
    """
    x_actual = x_inicial
    y_actual = y_inicial
    valor_actual = evaluar(x_actual, y_actual)
    
    historial = [(x_actual, y_actual, valor_actual)]
    mejoro = True
    iteraciones = 0
    
    while mejoro and iteraciones < iteraciones_max:
        mejoro = False
        iteraciones += 1
        
        # Generar vecinos
        vecinos = generar_vecinos(x_actual, y_actual)
        mejor_vecino = None
        mejor_valor = valor_actual
        
        # Evaluar todos los vecinos
        for x_vecino, y_vecino in vecinos:
            valor_vecino = evaluar(x_vecino, y_vecino)
            
            # Si es mejor que el actual, lo guardamos
            if valor_vecino > mejor_valor:
                mejor_valor = valor_vecino
                mejor_vecino = (x_vecino, y_vecino)
                mejoro = True
        
        # Si encontramos mejora, nos movemos
        if mejoro:
            x_actual, y_actual = mejor_vecino
            valor_actual = mejor_valor
            historial.append((x_actual, y_actual, valor_actual))
    
    return (x_actual, y_actual), valor_actual, iteraciones, historial

def resolver_problema(x_inicial, y_inicial):
    """Resuelve el problema usando Hill Climbing y muestra resultados."""
    print(f"Inicio: x={x_inicial:.2f}, y={y_inicial:.2f}")
    print(f"Valor inicial: {evaluar(x_inicial, y_inicial):.4f}\n")
    
    (x_final, y_final), valor_final, iteraciones, historial = hill_climbing(x_inicial, y_inicial)
    
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Solución encontrada: x={x_final:.2f}, y={y_final:.2f}")
    print(f"Valor final: {valor_final:.4f}")
    print(f"\nHistorial (primeros 10 pasos):")
    for i, (x, y, valor) in enumerate(historial[:10]):
        print(f"  Paso {i}: x={x:.2f}, y={y:.2f}, valor={valor:.4f}")
    
    if len(historial) > 10:
        print(f"  ... ({len(historial) - 10} pasos más)")
    
    print(f"\nOptimal global: x=3.00, y=2.00, valor=10.0000")
    return x_final, y_final, valor_final

# Ejemplo de uso
if __name__ == "__main__":
    print("=== BÚSQUEDA DE ASCENSIÓN DE COLINAS ===\n")
    
    # Caso 1: Inicio cercano al óptimo
    print("CASO 1: Inicio CERCANO al óptimo (2.5, 1.8)")
    print("-" * 50)
    resolver_problema(x_inicial=2.5, y_inicial=1.8)
    
    print("\n" + "="*50 + "\n")
    
    # Caso 2: Inicio lejano del óptimo
    print("CASO 2: Inicio LEJANO del óptimo (-2, -2)")
    print("-" * 50)
    resolver_problema(x_inicial=-2, y_inicial=-2)
