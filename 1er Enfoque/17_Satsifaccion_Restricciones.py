def es_consistente(var, valor, asignacion, vecinos):
    """Comprueba si asignar valor a var no viola las restricciones con vecinos."""
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True


def seleccionar_variable(mrv_vars, dominios, asignacion):
    """Selecciona la siguiente variable usando MRV (mínimo dominio restante)."""
    no_asignadas = [v for v in mrv_vars if v not in asignacion]
    if not no_asignadas:
        return None
    return min(no_asignadas, key=lambda v: len(dominios[v]))


def ordenar_valores(var, dominios):
    """Ordena valores en el dominio de la variable. Aquí dejamos el orden natural."""
    return dominios[var]


def forward_checking(var, valor, dominios, vecinos, asignacion):
    """Elimina valores inconsistentes de los dominios de los vecinos no asignados."""
    dominios_nuevos = {v: list(dominios[v]) for v in dominios}
    for vecino in vecinos[var]:
        if vecino not in asignacion and valor in dominios_nuevos[vecino]:
            dominios_nuevos[vecino].remove(valor)
            if not dominios_nuevos[vecino]:
                return None
    return dominios_nuevos


def backtracking(asignacion, dominios, vecinos, mrv_vars):
    """Algoritmo de búsqueda por backtracking con MRV y forward checking."""
    if len(asignacion) == len(dominios):
        return asignacion

    var = seleccionar_variable(mrv_vars, dominios, asignacion)
    if var is None:
        return None

    for valor in ordenar_valores(var, dominios):
        if es_consistente(var, valor, asignacion, vecinos):
            nueva_asignacion = dict(asignacion)
            nueva_asignacion[var] = valor
            dominios_nuevos = forward_checking(var, valor, dominios, vecinos, nueva_asignacion)
            if dominios_nuevos is not None:
                resultado = backtracking(nueva_asignacion, dominios_nuevos, vecinos, mrv_vars)
                if resultado is not None:
                    return resultado
    return None


def resolver_csp(variables, dominios, vecinos):
    """Resuelve un CSP con variables, dominios y restricciones de diferencia entre vecinos."""
    asignacion_inicial = {}
    return backtracking(asignacion_inicial, dominios, vecinos, variables)


if __name__ == "__main__":
    print("=== SATISFACCIÓN DE RESTRICCIONES ===\n")
    print("Coloreo de mapa de Mexico")
    print("Variables: estados de Mexico")
    print("Dominio: colores ['Rojo', 'Verde', 'Azul']")
    print("Restricción: estados vecinos no pueden tener el mismo color.\n")

    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    dominios = {
        'WA': ['Rojo', 'Verde', 'Azul'],
        'NT': ['Rojo', 'Verde', 'Azul'],
        'SA': ['Rojo', 'Verde', 'Azul'],
        'Q': ['Rojo', 'Verde', 'Azul'],
        'NSW': ['Rojo', 'Verde', 'Azul'],
        'V': ['Rojo', 'Verde', 'Azul'],
        'T': ['Rojo', 'Verde', 'Azul']
    }
    vecinos = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    solucion = resolver_csp(variables, dominios, vecinos)
    if solucion:
        print("Solución encontrada:")
        for var in variables:
            print(f"  {var}: {solucion[var]}")
    else:
        print("No se encontró solución")
