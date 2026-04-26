import math
import random

random.seed(0)

def evaluar(x, y):
    """
    Función a maximizar: -((x-3)^2 + (y-2)^2) + 10
    Máximo global en (3, 2) con valor 10.
    """
    return -(math.pow(x - 3, 2) + math.pow(y - 2, 2)) + 10


def inicializar_poblacion(tamaño, rango=5.0):
    poblacion = []
    for _ in range(tamaño):
        x = round(random.uniform(-rango, rango), 2)
        y = round(random.uniform(-rango, rango), 2)
        poblacion.append((x, y))
    return poblacion


def evaluar_poblacion(poblacion):
    return [(ind, evaluar(*ind)) for ind in poblacion]


def seleccion_torneo(poblacion, puntajes, k=3):
    """Selecciona un individuo usando torneo de tamaño k."""
    participantes = random.sample(list(zip(poblacion, puntajes)), k)
    mejor = max(participantes, key=lambda item: item[1])
    return mejor[0]


def crossover_promedio(padre1, padre2):
    """Crossover aritmético simple entre dos padres."""
    x = round((padre1[0] + padre2[0]) / 2, 2)
    y = round((padre1[1] + padre2[1]) / 2, 2)
    return (x, y)


def mutacion_gaussiana(individuo, tasa_mutacion=0.2, sigma=0.5):
    """Aplica mutación gaussiana a un individuo con cierta probabilidad."""
    x, y = individuo
    if random.random() < tasa_mutacion:
        x = round(x + random.gauss(0, sigma), 2)
    if random.random() < tasa_mutacion:
        y = round(y + random.gauss(0, sigma), 2)
    return (x, y)


def algoritmo_genetico(tamaño_poblacion=10, generaciones=20, tasa_cruce=0.7, tasa_mutacion=0.2, sigma=0.5):
    poblacion = inicializar_poblacion(tamaño_poblacion)
    historial = []

    for generacion in range(generaciones):
        evaluados = evaluar_poblacion(poblacion)
        evaluados.sort(key=lambda item: item[1], reverse=True)

        mejor_individuo, mejor_valor = evaluados[0]
        historial.append((generacion, mejor_individuo, mejor_valor))

        nueva_poblacion = [mejor_individuo]  # elitismo: mantener el mejor

        while len(nueva_poblacion) < tamaño_poblacion:
            padre1 = seleccion_torneo(poblacion, [evaluar(*ind) for ind in poblacion])
            padre2 = seleccion_torneo(poblacion, [evaluar(*ind) for ind in poblacion])

            if random.random() < tasa_cruce:
                hijo = crossover_promedio(padre1, padre2)
            else:
                hijo = padre1

            hijo = mutacion_gaussiana(hijo, tasa_mutacion=tasa_mutacion, sigma=sigma)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    evaluados = evaluar_poblacion(poblacion)
    mejor_individuo, mejor_valor = max(evaluados, key=lambda item: item[1])
    historial.append((generaciones, mejor_individuo, mejor_valor))
    return mejor_individuo, mejor_valor, historial


def imprimir_resultados(mejor_individuo, mejor_valor, historial):
    print(f"Mejor solución encontrada: x={mejor_individuo[0]:.2f}, y={mejor_individuo[1]:.2f}, valor={mejor_valor:.4f}")
    print("\nMejor individuo por generación:")
    for gen, indiv, valor in historial:
        print(f"  Generación {gen}: ({indiv[0]:.2f}, {indiv[1]:.2f}) = {valor:.4f}")
    print("\nÓptimo global: x=3.00, y=2.00, valor=10.0000")


if __name__ == "__main__":
    print("=== ALGORITMO GENÉTICO ===\n")
    mejor_individuo, mejor_valor, historial = algoritmo_genetico(tamaño_poblacion=10, generaciones=20, tasa_cruce=0.7, tasa_mutacion=0.3, sigma=0.5)
    imprimir_resultados(mejor_individuo, mejor_valor, historial)
