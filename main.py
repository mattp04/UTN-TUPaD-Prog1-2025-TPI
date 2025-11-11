from funciones.leer_csv import leer_csv
from funciones.menu import mostrar_menu
from funciones.buscar_pais import buscar_pais
from funciones.obtener_dato import obtener_dato

diccionario = leer_csv()

# paises = list(diccionario.keys())
# print(paises)  # ['Argentina', 'Brasil']

# mostrar_menu()

# lista = buscar_pais(diccionario, 'republi')
# print(lista)

# for item in lista :
#     print(diccionario[item])

lista= obtener_dato(diccionario, "Argentina", "Población")
print(lista)