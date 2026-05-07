# Red bayesiana sencilla
# Nube influye en lluvia, y lluvia influye en trafico.

p_nube = {True: 0.40, False: 0.60}
p_lluvia_dado_nube = {
    True: {True: 0.75, False: 0.25},
    False: {True: 0.20, False: 0.80}
}
p_trafico_dado_lluvia = {
    True: {True: 0.80, False: 0.20},
    False: {True: 0.30, False: 0.70}
}

p_trafico = 0
for nube in [True, False]:
    for lluvia in [True, False]:
        p = p_nube[nube]
        p *= p_lluvia_dado_nube[nube][lluvia]
        p *= p_trafico_dado_lluvia[lluvia][True]
        p_trafico += p

print(f"P(trafico=True) = {p_trafico:.3f}")
