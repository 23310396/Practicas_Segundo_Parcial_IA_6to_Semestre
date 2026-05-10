# Gramatica probabilistica independiente del contexto
# Se calcula la probabilidad de una oracion generada por reglas.

reglas = {
    "O -> SN SV": 1.0,
    "SN -> el robot": 0.6,
    "SN -> la maquina": 0.4,
    "SV -> aprende": 0.7,
    "SV -> falla": 0.3
}

oracion = "el robot aprende"
prob = reglas["O -> SN SV"] * reglas["SN -> el robot"] * reglas["SV -> aprende"]

print("Oracion:", oracion)
print(f"Probabilidad segun la gramatica = {prob:.3f}")
