def buscar_pais (diccionario, palabara):
    # Listo todos los paises del diccionario
    paises = list(diccionario.keys())
    coincidencias = []
    for pais in paises:
        # Solo minusculas para que busque coincidencias inclucio a mitad de palabra
        if palabara.lower() in pais.lower():
            coincidencias.append(pais)
    # Retorno lista con paises que coinciden con la busqueda
    return coincidencias