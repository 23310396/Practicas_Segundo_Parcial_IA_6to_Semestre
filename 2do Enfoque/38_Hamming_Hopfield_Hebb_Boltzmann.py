# Red de Hopfield con aprendizaje de Hebb
# Recupera un patron binario con valores -1 y 1.

patron = [1, -1, 1, -1]
n = len(patron)

# pesos Hebbianos
pesos = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            pesos[i][j] = patron[i] * patron[j]

estado = [1, -1, -1, -1]  # patron con ruido

for _ in range(5):
    for i in range(n):
        suma = sum(pesos[i][j] * estado[j] for j in range(n))
        estado[i] = 1 if suma >= 0 else -1

print("Patron original:", patron)
print("Patron recuperado:", estado)
