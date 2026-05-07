# Regla de la cadena
# P(A, B, C) = P(A) * P(B|A) * P(C|A,B)

p_a = 0.60
p_b_dado_a = 0.70
p_c_dado_a_b = 0.80

p_conjunta = p_a * p_b_dado_a * p_c_dado_a_b

print("P(A) =", p_a)
print("P(B|A) =", p_b_dado_a)
print("P(C|A,B) =", p_c_dado_a_b)
print(f"P(A,B,C) = {p_conjunta:.3f}")
