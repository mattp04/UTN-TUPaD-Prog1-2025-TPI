def ordenar_lista(lista, indice=0, descendente=False):
    """
    Ordena una lista de tuplas según la posición 'indice' usando bubble sort.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            val1 = lista[j][indice]
            val2 = lista[j + 1][indice]

            if (not descendente and val1 > val2) or (descendente and val1 < val2):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista
