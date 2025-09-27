# 2) Funcionalidades mínimas del sistema
# El programa debe ofrecer un menú de opciones en consola que permita:
# • Buscar un país por nombre (coincidencia parcial o exacta).
# • Filtrar países por:
# o Continente
# o Rango de población
# o Rango de superficie
# • Ordenar países por:
# o Nombre
# o Población
# o Superficie (ascendente o descendente)
# • Mostrar estadísticas:
# o País con mayor y menor población
# o Promedio de población
# o Promedio de superficie
# o Cantidad de países por continente

def mostrar_menu () :
    print("------------------  Información Paises  ------------------")
    print("     Menú de opciones: ")
    print("     1 - Buscar un país por nombre")
    print("     2 - Filtrar países")
    print("     3 - Ordenar países")
    print("     4 - Mostrar estadísticas")
    print("     0 - Salir")
    print("----------------------------------------------------------")
    return