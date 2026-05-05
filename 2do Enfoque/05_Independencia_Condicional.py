# Independencia condicional
# Dos sensores son independientes si ya se conoce el estado real de la maquina.

p_estado = {"normal": 0.7, "falla": 0.3}
p_s1_alerta = {"normal": 0.10, "falla": 0.80}
p_s2_alerta = {"normal": 0.20, "falla": 0.70}

print("P(S1 alerta y S2 alerta | estado) usando independencia condicional:\n")

for estado in p_estado:
    conjunta = p_s1_alerta[estado] * p_s2_alerta[estado]
    print(f"Estado {estado}: {conjunta:.3f}")

print("\nLa multiplicacion se permite porque los sensores se tratan como independientes dado el estado.")
