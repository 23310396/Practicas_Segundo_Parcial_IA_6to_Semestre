# Procesos estacionarios
# La distribucion se va estabilizando al aplicar muchas veces la misma matriz de transicion.

transicion = [
    [0.85, 0.15],
    [0.25, 0.75]
]

dist = [1.0, 0.0]  # inicia en estado Normal

for paso in range(1, 21):
    nueva = [0, 0]
    for actual in range(2):
        for sig in range(2):
            nueva[sig] += dist[actual] * transicion[actual][sig]
    dist = nueva

print("Distribucion despues de 20 pasos:")
print(f"Normal: {dist[0]:.3f}")
print(f"Falla: {dist[1]:.3f}")
