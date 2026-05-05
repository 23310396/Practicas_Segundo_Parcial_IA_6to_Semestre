# Distribucion de probabilidad
# Ejemplo: demanda diaria posible de un producto.

demanda = {
    0: 0.05,
    1: 0.15,
    2: 0.30,
    3: 0.35,
    4: 0.15
}

print("Distribucion de probabilidad de la demanda:")
for unidades, prob in demanda.items():
    print(f"P(demanda={unidades}) = {prob:.2f}")

esperanza = sum(unidades * prob for unidades, prob in demanda.items())
print(f"\nDemanda esperada = {esperanza:.2f} unidades")
print("Suma de probabilidades =", round(sum(demanda.values()), 2))
