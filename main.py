from funciones.leer_csv import leer_csv
from funciones.menu import mostrar_menu
from funciones.buscar_pais import buscar_pais
from funciones.filtrar_paises import filtrar_paises
from funciones.ordenar_paises import ordenar_paises
from funciones.mostrar_paises import mostrar_paises
from funciones.mostrar_estadisticas import mostrar_estadisticas

diccionario = leer_csv()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            dato = input("Ingrese país que desea buscar: ")
            lista = buscar_pais(diccionario, dato)
            mostrar_paises(lista, campos=["pais", "continente", "población", "superficie"])
            print("\n")
        case "2":
            continente=None
            min_poblacion=None
            max_poblacion=None
            min_superficie=None
            max_superficie=None
            print("Desea filtrar paises por: ")
            print(" 1 - Continente")
            print(" 2 - Rango de población")
            print(" 3 - Rango de superficie")
            seleccion = int(input("Ingrese opción: "))

            if seleccion == 1 or seleccion == 2 or seleccion == 3 :
                if seleccion == 1:
                    continente = input("Ingrese continente a filtrar: ")
                elif seleccion == 2:
                    min_poblacion = int(input("Ingrese min. población a filtrar: "))
                    max_poblacion = int(input("Ingrese max. población a filtrar: "))
                else:
                    min_superficie = int(input("Ingrese min. superficie a filtrar: "))
                    max_superficie = int(input("Ingrese max. superficie a filtrar: "))
                    
                lista = filtrar_paises(diccionario, continente, min_poblacion, max_poblacion, min_superficie, max_superficie)
                mostrar_paises(lista, campos=["pais", "continente", "población", "superficie"])
                print("\n")
            else : 
                print("Opción no válida. Intente nuevamente.")

        case "3":
            criterio=None
            tipo_orden=False
            print("Desea ordenar paises por: ")
            print(" 1 - Nombre")
            print(" 2 - Población")
            print(" 3 - Superficie")
            seleccion = int(input("Ingrese opción: "))

            if seleccion == 1 or seleccion == 2 or seleccion == 3 :
                if seleccion == 1:
                    criterio = "País"
                elif seleccion == 2:
                    criterio = "Población"
                else:
                    criterio = "Superficie"
                print("Desea ordenar de manera: ")
                print(" 1 - Ascendente")
                print(" 2 - Descendente")
                seleccion_tipo = int(input("Ingrese opción: "))
                if seleccion_tipo == 1 or seleccion_tipo == 2:
                    if seleccion_tipo == 2:
                        tipo_orden = True
                    lista = ordenar_paises(diccionario, criterio, tipo_orden)
                    mostrar_paises(lista, campos=["pais", "continente", "población", "superficie"])
                    print("\n")
                else : 
                    print("Opción no válida. Intente nuevamente.")
            else : 
                print("Opción no válida. Intente nuevamente.")
        case "4":
            mostrar_estadisticas(diccionario)
        case "0":
            print("Fin del programa...")
            break

        case _:
            print("Opción no válida. Intente nuevamente.")
