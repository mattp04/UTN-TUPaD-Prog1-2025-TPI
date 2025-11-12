import unicodedata

def quitar_tildes(texto):
    """
    Elimina las tildes y acentos de una cadena.
    Ejemplo: 'América' -> 'America'
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def filtrar_paises(diccionario, continente=None, min_poblacion=None, max_poblacion=None, min_superficie=None, max_superficie=None):
    resultado = []

    for nombre, datos in diccionario.items():
        continente_pais = datos["Continente"]

        # Coincidencia parcial e ignorando tildes
        if continente:
            if quitar_tildes(continente.lower()) not in quitar_tildes(continente_pais.lower()):
                continue

        # Rangos numéricos
        if min_poblacion is not None and datos["Población"] < min_poblacion:
            continue
        if max_poblacion is not None and datos["Población"] > max_poblacion:
            continue
        if min_superficie is not None and datos["Superficie"] < min_superficie:
            continue
        if max_superficie is not None and datos["Superficie"] > max_superficie:
            continue
        
        resultado.append((nombre, datos))

    return resultado
