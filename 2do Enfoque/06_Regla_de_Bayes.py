# Regla de Bayes
# Calcular P(falla | sensor_alerta)

p_falla = 0.02
p_no_falla = 1 - p_falla

p_alerta_dado_falla = 0.90
p_alerta_dado_no_falla = 0.05

p_alerta = (p_alerta_dado_falla * p_falla) + (p_alerta_dado_no_falla * p_no_falla)
p_falla_dado_alerta = (p_alerta_dado_falla * p_falla) / p_alerta

print(f"P(alerta) = {p_alerta:.4f}")
print(f"P(falla | alerta) = {p_falla_dado_alerta:.4f}")
