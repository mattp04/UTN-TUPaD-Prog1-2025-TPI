from funciones.leer_csv import leer_csv
from funciones.menu import mostrar_menu


lista = leer_csv()

# Solo de Prueba
for fila in lista:
    print(fila, type(fila))

mostrar_menu()