import math

def evaluar(x, y):
    """
    Función a maximizar: -((x-3)^2 + (y-2)^2) + 10
    Máximo global en (3, 2) con valor 10
    """
    return -(math.pow(x - 3, 2) + math.pow(y - 2, 2)) + 10

def generar_vecinos(x, y, paso=0.5):
    """Genera 4 vecinos: arriba, abajo, izquierda, derecha."""
    vecinos = [
        (x + paso, y),      # Derecha
        (x - paso, y),      # Izquierda
        (x, y + paso),      # Arriba
        (x, y - paso)       # Abajo
    ]
    return vecinos

def tabu_search(x_inicial, y_inicial, iteraciones_max=100, tamaño_lista_tabu=5):
    """
    Algoritmo de Búsqueda Tabú (Tabu Search).
    
    Diferencia con Hill Climbing:
    - Recuerda movimientos RECIENTES en una lista tabú
    - Permite movimientos MALOS para escapar de óptimos locales
    - Evita volver a los mismos lugares durante un tiempo
    
    tamaño_lista_tabu: Cuántos movimientos recientes recordar
    """
    x_actual = x_inicial
    y_actual = y_inicial
    valor_actual = evaluar(x_actual, y_actual)
    
    # La lista tabú: recuerda los últimos movimientos
    lista_tabu = []
    
    # Mejor solución encontrada hasta ahora
    mejor_x = x_actual
    mejor_y = y_actual
    mejor_valor = valor_actual
    
    historial = [(x_actual, y_actual, valor_actual)]
    iteraciones = 0
    
    while iteraciones < iteraciones_max:
        iteraciones += 1
        
        # Generar vecinos
        vecinos = generar_vecinos(x_actual, y_actual)
        mejor_vecino = None
        mejor_valor_vecino = float('-inf')
        
        # Evaluar todos los vecinos (incluso los MALOS)
        for x_vecino, y_vecino in vecinos:
            # Redondear para evitar errores de precisión
            x_vecino = round(x_vecino, 2)
            y_vecino = round(y_vecino, 2)
            
            valor_vecino = evaluar(x_vecino, y_vecino)
            
            # Si NO está en lista tabú, considerarlo
            if (x_vecino, y_vecino) not in lista_tabu:
                if valor_vecino > mejor_valor_vecino:
                    mejor_valor_vecino = valor_vecino
                    mejor_vecino = (x_vecino, y_vecino)
        
        # Si no encontramos vecino permitido, salir
        if mejor_vecino is None:
            break
        
        # Moverse al mejor vecino (aunque sea peor que actual)
        x_actual, y_actual = mejor_vecino
        valor_actual = mejor_valor_vecino
        
        # Agregar movimiento a lista tabú
        lista_tabu.append((x_actual, y_actual))
        
        # Mantener lista tabú con tamaño máximo
        if len(lista_tabu) > tamaño_lista_tabu:
            lista_tabu.pop(0)  # Quitar el más antiguo
        
        # Actualizar mejor solución encontrada
        if valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_x = x_actual
            mejor_y = y_actual
        
        historial.append((x_actual, y_actual, valor_actual))
    
    return (mejor_x, mejor_y), mejor_valor, iteraciones, historial

def resolver_problema_tabu(x_inicial, y_inicial, tamaño_tabu=5):
    """Resuelve el problema usando Tabu Search y muestra resultados."""
    print(f"Inicio: x={x_inicial:.2f}, y={y_inicial:.2f}")
    print(f"Valor inicial: {evaluar(x_inicial, y_inicial):.4f}")
    print(f"Tamaño de lista tabú: {tamaño_tabu}\n")
    
    (x_final, y_final), valor_final, iteraciones, historial = tabu_search(x_inicial, y_inicial, tamaño_lista_tabu=tamaño_tabu)
    
    print(f"Iteraciones realizadas: {iteraciones}")
    print(f"Mejor solución encontrada: x={x_final:.2f}, y={y_final:.2f}")
    print(f"Valor final: {valor_final:.4f}")
    print(f"\nHistorial (primeros 15 pasos):")
    for i, (x, y, valor) in enumerate(historial[:15]):
        print(f"  Paso {i}: x={x:.2f}, y={y:.2f}, valor={valor:.4f}")
    
    if len(historial) > 15:
        print(f"  ... ({len(historial) - 15} pasos más)")
    
    print(f"\nOptimal global: x=3.00, y=2.00, valor=10.0000")
    return x_final, y_final, valor_final

# Ejemplo de uso
if __name__ == "__main__":
    print("=== BÚSQUEDA TABÚ (TABU SEARCH) ===\n")
    
    # Caso 1: Inicio cercano (mismo del Hill Climbing)
    print("CASO 1: Inicio CERCANO (2.5, 1.8)")
    print("-" * 50)
    resolver_problema_tabu(x_inicial=2.5, y_inicial=1.8, tamaño_tabu=5)
    
    print("\n" + "="*50 + "\n")
    
    # Caso 2: Inicio lejano (mismo del Hill Climbing)
    print("CASO 2: Inicio LEJANO (-2, -2)")
    print("-" * 50)
    resolver_problema_tabu(x_inicial=-2, y_inicial=-2, tamaño_tabu=5)
