from funciones.leer_csv import leer_csv
from funciones.menu import mostrar_menu
from funciones.buscar_pais import buscar_pais
from funciones.obtener_dato import obtener_dato
from funciones.filtrar_paises import filtrar_paises
from funciones.ordenar_paises import ordenar_paises
from funciones.mostrar_paises import mostrar_paises

diccionario = leer_csv()

# paises = list(diccionario.keys())
# print(paises)  # ['Argentina', 'Brasil']

# mostrar_menu()

# lista = buscar_pais(diccionario, 'republi')
# print(lista)

# for item in lista :
#     print(diccionario[item])

# lista= obtener_dato(diccionario, "América del Sur", diccionario.keys())
# print(lista)

lista= ordenar_paises(diccionario)
# mostrar_paises(lista)
mostrar_paises(lista, campos=["pais", "continente", "superficie"])