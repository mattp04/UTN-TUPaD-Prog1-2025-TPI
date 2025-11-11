def buscar_pais(diccionario, palabra):
    """
    Devuelve una lista de tuplas (pais, datos) cuyas claves coincidan parcialmente
    con 'palabra' (búsqueda case-insensitive).
    """
    if palabra is None:
        return []

    palabra = palabra.strip().lower()
    if palabra == "":
        return []

    coincidencias = []
    for pais, datos in diccionario.items():
        if palabra in pais.lower():
            # agrego la tupla (pais, datos)
            coincidencias.append((pais, datos))

    return coincidencias
