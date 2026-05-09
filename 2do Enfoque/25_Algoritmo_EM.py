# Algoritmo EM muy simple para dos monedas
# Se estiman las probabilidades de cara de dos monedas usando datos incompletos.

secuencias = ["CCCCC", "CCCCC", "CCCCC", "CCCCC", "CCCCC", "CCCXX", "XXCCC", "XXXXX", "XXXXX", "XXXXX"]
p_a = 0.6
p_b = 0.5
prior_a = 0.5

def verosimilitud(seq, p):
    caras = seq.count("C")
    cruces = seq.count("X")
    return (p ** caras) * ((1 - p) ** cruces)

for it in range(10):
    caras_a = cruces_a = caras_b = cruces_b = 0.0
    for seq in secuencias:
        la = prior_a * verosimilitud(seq, p_a)
        lb = (1 - prior_a) * verosimilitud(seq, p_b)
        peso_a = la / (la + lb)
        peso_b = 1 - peso_a
        caras_a += peso_a * seq.count("C")
        cruces_a += peso_a * seq.count("X")
        caras_b += peso_b * seq.count("C")
        cruces_b += peso_b * seq.count("X")
    p_a = caras_a / (caras_a + cruces_a)
    p_b = caras_b / (caras_b + cruces_b)

print(f"Probabilidad estimada moneda A: {p_a:.3f}")
print(f"Probabilidad estimada moneda B: {p_b:.3f}")
