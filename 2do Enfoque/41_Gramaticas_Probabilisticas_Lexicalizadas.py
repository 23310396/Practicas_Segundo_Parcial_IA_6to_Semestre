# Gramatica probabilistica lexicalizada
# Se toma en cuenta una palabra principal o cabeza lexical.

reglas_lex = {
    ("robot", "aprende"): 0.72,
    ("robot", "falla"): 0.28,
    ("maquina", "aprende"): 0.40,
    ("maquina", "falla"): 0.60
}

sujeto = "robot"
verbo = "aprende"
prob = reglas_lex[(sujeto, verbo)]

print(f"Sujeto principal: {sujeto}")
print(f"Verbo: {verbo}")
print(f"Probabilidad lexicalizada = {prob:.2f}")
