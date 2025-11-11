from funciones.ordenar_lista import ordenar_lista

def ordenar_paises(diccionario, criterio="País", descendente=False):
    """
    Prepara los datos de países y llama a 'ordenar_lista' según el criterio elegido.
    Devuelve una lista de tuplas (nombre, datos).
    """
    lista = list(diccionario.items())

    # Convertir los datos a un formato comparable según el criterio
    if criterio == "País":
        lista_para_ordenar = [(nombre.lower(), nombre, datos) for nombre, datos in lista]
        lista_ordenada = ordenar_lista(lista_para_ordenar, indice=0, descendente=descendente)
        return [(nombre, datos) for _, nombre, datos in lista_ordenada]

    elif criterio in ["Población", "Superficie"]:
        lista_para_ordenar = [(datos[criterio], nombre, datos) for nombre, datos in lista]
        lista_ordenada = ordenar_lista(lista_para_ordenar, indice=0, descendente=descendente)
        return [(nombre, datos) for _, nombre, datos in lista_ordenada]
