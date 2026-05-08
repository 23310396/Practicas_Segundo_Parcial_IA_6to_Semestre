# Filtro de Kalman 1D
# Estima una posicion usando mediciones con ruido.

mediciones = [10.2, 10.7, 11.0, 11.4, 12.1]

estimacion = 10.0
incertidumbre = 1.0
ruido_proceso = 0.05
ruido_medicion = 0.25

print("Filtro de Kalman 1D:\n")
for z in mediciones:
    # prediccion
    incertidumbre += ruido_proceso

    # actualizacion
    k = incertidumbre / (incertidumbre + ruido_medicion)
    estimacion = estimacion + k * (z - estimacion)
    incertidumbre = (1 - k) * incertidumbre

    print(f"Medicion={z:.2f}, estimacion={estimacion:.3f}, K={k:.3f}")
