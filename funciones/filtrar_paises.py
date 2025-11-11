def filtrar_paises(diccionario, continente=None, min_poblacion=None, max_poblacion=None, min_superficie=None, max_superficie=None):
    resultado = []

    for nombre, datos in diccionario.items():
        # Coincidencia parcial de continente
        if continente and continente.lower() not in datos["Continente"].lower():
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
        
        resultado.append(nombre)

    return resultado

