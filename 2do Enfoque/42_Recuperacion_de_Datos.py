# Recuperacion de datos
# Busqueda simple por coincidencia de palabras.

documentos = {
    1: "probabilidad bayesiana y sensores",
    2: "redes neuronales y aprendizaje profundo",
    3: "sensores robotica probabilidad",
    4: "vision por computador y filtros"
}

consulta = "probabilidad sensores"
terminos = consulta.split()

puntajes = {}
for doc_id, texto in documentos.items():
    palabras = texto.split()
    puntajes[doc_id] = sum(1 for t in terminos if t in palabras)

ordenados = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
print("Consulta:", consulta)
print("Resultados ordenados:")
for doc_id, score in ordenados:
    print(doc_id, "score=", score, "->", documentos[doc_id])
