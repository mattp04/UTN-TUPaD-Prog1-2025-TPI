def mostrar_paises(lista, campos=None, ancho=40):
    """
    Muestra una lista de países formateada como tabla, con columnas de ancho fijo.

    Parámetros:
        lista: lista de tuplas (nombre, datos)
        campos: lista de campos a mostrar (por defecto solo 'nombre')
        ancho: ancho en caracteres de cada columna
    """

    if campos is None:
        campos = ["Pais"]

    # Encabezado
    encabezado = ""
    for campo in campos:
        encabezado += f"{campo.capitalize():<{ancho}}"
    
    print("-" * len(encabezado))
    print(encabezado)
    print("-" * len(encabezado))

    # Filas
    for elemento in lista:
        # Puede venir como (nombre, datos) o solo nombre
        if isinstance(elemento, tuple):
            nombre, datos = elemento
        else:
            nombre = elemento
            datos = {}

        fila = ""
        for campo in campos:
            campo_lower = campo.lower()
            valor = ""

            if campo_lower == "pais":
                valor = nombre
            elif campo_lower == "población" and "Población" in datos:
                valor = f"{datos['Población']:,}"
            elif campo_lower == "superficie" and "Superficie" in datos:
                valor = f"{datos['Superficie']:,} km²"
            elif campo_lower == "continente" and "Continente" in datos:
                valor = datos["Continente"]
            else:
                valor = "-"

            # Ajuste de ancho fijo
            fila += f"{valor:<{ancho}}"

        print(fila)
