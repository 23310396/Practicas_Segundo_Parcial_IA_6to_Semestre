# Probabilidad a priori
# Se calcula antes de observar evidencia nueva.

piezas = {
    "buenas": 92,
    "defectuosas": 8
}

total = sum(piezas.values())
prob_defectuosa = piezas["defectuosas"] / total
prob_buena = piezas["buenas"] / total

print("Total de piezas:", total)
print(f"P(buena) = {prob_buena:.3f}")
print(f"P(defectuosa) = {prob_defectuosa:.3f}")
