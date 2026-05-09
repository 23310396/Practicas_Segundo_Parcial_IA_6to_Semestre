# Aprendizaje bayesiano
# Actualiza la probabilidad de que una moneda este cargada.

hipotesis = {
    "justa": {"prior": 0.70, "p_cara": 0.50},
    "cargada": {"prior": 0.30, "p_cara": 0.80}
}

observaciones = ["cara", "cara", "cruz", "cara"]

posterior = {h: datos["prior"] for h, datos in hipotesis.items()}

for obs in observaciones:
    for h, datos in hipotesis.items():
        p_obs = datos["p_cara"] if obs == "cara" else 1 - datos["p_cara"]
        posterior[h] *= p_obs
    total = sum(posterior.values())
    posterior = {h: p / total for h, p in posterior.items()}

print("Posterior despues de observar lanzamientos:")
for h, p in posterior.items():
    print(f"{h}: {p:.3f}")
