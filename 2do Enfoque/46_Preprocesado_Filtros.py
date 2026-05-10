# Preprocesado: filtro promedio en una senal.

senal = [10, 12, 50, 13, 12, 11, 55, 12]

filtrada = []
for i in range(len(senal)):
    vecinos = senal[max(0, i-1):min(len(senal), i+2)]
    filtrada.append(sum(vecinos) / len(vecinos))

print("Senal original:", senal)
print("Senal filtrada:", [round(x, 2) for x in filtrada])
