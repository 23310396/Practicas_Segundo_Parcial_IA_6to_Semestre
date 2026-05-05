# Ejemplo sencillo de incertidumbre
# Un robot decide si salir o esperar, pero el clima no es seguro.

posibilidades = {
    "soleado": 0.55,
    "nublado": 0.30,
    "lluvia": 0.15
}

print("Probabilidades del clima:")
for clima, p in posibilidades.items():
    print(f"{clima}: {p:.2f}")

riesgo_lluvia = posibilidades["lluvia"]

if riesgo_lluvia < 0.25:
    decision = "salir"
else:
    decision = "esperar"

print("\nRiesgo de lluvia:", riesgo_lluvia)
print("Decision tomada:", decision)
