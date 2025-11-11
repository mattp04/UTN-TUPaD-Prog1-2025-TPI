from funciones.leer_csv import leer_csv
from funciones.menu import mostrar_menu
from funciones.buscar_pais import buscar_pais
from funciones.filtrar_paises import filtrar_paises
from funciones.ordenar_paises import ordenar_paises
from funciones.mostrar_paises import mostrar_paises
from funciones.mostrar_estadisticas import mostrar_estadisticas
from funciones.utilidades import limpiar_consola, pausar_consola

limpiar_consola()
diccionario = leer_csv()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            limpiar_consola()
            dato = input("Ingrese país que desea buscar: ")
            lista = buscar_pais(diccionario, dato)
            mostrar_paises(lista, campos=["pais", "continente", "población", "superficie"])
            print("\n")
            pausar_consola()
            limpiar_consola()
        case "2":
            limpiar_consola()
            continente=None
            min_poblacion=None
            max_poblacion=None
            min_superficie=None
            max_superficie=None
            print("Desea filtrar paises por: ")
            print(" 1 - Continente")
            print(" 2 - Rango de población")
            print(" 3 - Rango de superficie\n")

            seleccion = input("Ingrese opción: ")
            if not seleccion.isdigit() or int(seleccion) not in [1, 2, 3]:
                print("Opción no válida. Intente nuevamente.")
                pausar_consola()
                limpiar_consola()
            else :
                seleccion = int(seleccion)
                if seleccion == 1:
                    continente = input("Ingrese continente a filtrar: ")
                elif seleccion == 2:
                    
                    min_poblacion = input("Ingrese min. población a filtrar: ")
                    max_poblacion = input("Ingrese max. población a filtrar: ")
                    # Validar que sean números
                    if not (min_poblacion.isdigit() and max_poblacion.isdigit()):
                        print("Ingrese solo números válidos para población.")
                        pausar_consola()
                        limpiar_consola()
                        continue
                    else:
                        min_poblacion = int(min_poblacion)
                        max_poblacion = int(max_poblacion)
                else:
                    min_superficie = input("Ingrese min. superficie a filtrar: ")
                    max_superficie = input("Ingrese max. superficie a filtrar: ")
                     # Validar que sean números
                    if not (min_superficie.isdigit() and max_superficie.isdigit()):
                        print("Ingrese solo números válidos para superficie.")
                        pausar_consola()
                        limpiar_consola()
                        continue
                    else:
                        min_superficie = int(min_superficie)
                        max_superficie = int(max_superficie)
                    
                lista = filtrar_paises(diccionario, continente, min_poblacion, max_poblacion, min_superficie, max_superficie)
                mostrar_paises(lista, campos=["pais", "continente", "población", "superficie"])
                print("\n")
                pausar_consola()
                limpiar_consola()
        case "3":
            
            limpiar_consola()
            criterio=None
            tipo_orden=False
            print("Desea ordenar paises por: ")
            print(" 1 - Nombre")
            print(" 2 - Población")
            print(" 3 - Superficie\n")
            seleccion = input("Ingrese opción: ")

            if not seleccion.isdigit() or int(seleccion) not in [1, 2, 3]:
                print("Opción no válida. Intente nuevamente.")
                pausar_consola()
                limpiar_consola()
            else :
                seleccion = int(seleccion)

                if seleccion == 1:
                    criterio = "País"
                elif seleccion == 2:
                    criterio = "Población"
                else:
                    criterio = "Superficie"

                print("Desea ordenar de manera: ")
                print(" 1 - Ascendente")
                print(" 2 - Descendente\n")
                seleccion_tipo = input("Ingrese opción: ")

                if not seleccion_tipo.isdigit() or int(seleccion_tipo) not in [1, 2]:
                    print("Opción no válida. Intente nuevamente.")
                    pausar_consola()
                    limpiar_consola()
                else :
                    seleccion_tipo = int(seleccion_tipo)
                    if seleccion_tipo == 2:
                        tipo_orden = True
                    lista = ordenar_paises(diccionario, criterio, tipo_orden)
                    mostrar_paises(lista, campos=["pais", "continente", "población", "superficie"])
                    print("\n")
                    pausar_consola()
                    limpiar_consola()

        case "4":
            limpiar_consola()
            mostrar_estadisticas(diccionario)
            pausar_consola()
            limpiar_consola()

        case "0":
            print("Fin del programa...")
            pausar_consola()
            limpiar_consola()
            break

        case _:
            print("Opción no válida. Intente nuevamente.")
            pausar_consola()
            limpiar_consola()
