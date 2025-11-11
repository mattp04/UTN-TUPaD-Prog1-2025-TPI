def mostrar_estadisticas(diccionario):
    """
    Muestra estadísticas generales del conjunto de países:
      - País con mayor y menor población
      - Promedio de población
      - Promedio de superficie
      - Cantidad de países por continente
    """

    if not diccionario:
        print("No hay datos disponibles.")
        return

    # Variables iniciales
    total_poblacion = 0
    total_superficie = 0
    cantidad_paises = len(diccionario)
    poblacion_max = ("", 0)
    poblacion_min = ("", float("inf"))
    continentes = {}

    for pais, datos in diccionario.items():
        poblacion = datos.get("Población", 0)
        superficie = datos.get("Superficie", 0)
        continente = datos.get("Continente", "Desconocido")

        # Acumular totales
        total_poblacion += poblacion
        total_superficie += superficie

        # Máximo y mínimo
        if poblacion > poblacion_max[1]:
            poblacion_max = (pais, poblacion)
        if poblacion < poblacion_min[1]:
            poblacion_min = (pais, poblacion)

        # Contar países por continente
        continentes[continente] = continentes.get(continente, 0) + 1

    # Cálculos de promedios
    promedio_poblacion = total_poblacion / cantidad_paises
    promedio_superficie = total_superficie / cantidad_paises

    # Mostrar resultados
    print("\n" + "-" * 60)
    print("Estadísticas Generales")
    print("-" * 60)
    print(f"País con mayor población: {poblacion_max[0]} ({poblacion_max[1]:,} hab.)")
    print(f"País con menor población: {poblacion_min[0]} ({poblacion_min[1]:,} hab.)")
    print(f"Promedio de población: {promedio_poblacion:,.0f} hab.")
    print(f"Promedio de superficie: {promedio_superficie:,.0f} km²")
    print("\nCantidad de países por continente:")
    for cont, cantidad in continentes.items():
        print(f"  - {cont}: {cantidad}")
    print("-" * 60)
