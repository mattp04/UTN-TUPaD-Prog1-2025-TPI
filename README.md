# UTN-TUPaD-Prog1-2025-TPI

-----------------------------------------------------------------------------------------------------------------------------
                                         Proyecto: Gestión de Datos de Países en Python
-----------------------------------------------------------------------------------------------------------------------------

                                ------------------  Descripción del programa:   ------------------

Este programa permite gestionar y analizar información sobre distintos países.
Los datos incluyen nombre, continente, población y superficie. A través de un menú interactivo
en consola, el usuario puede:

1-   Buscar países por nombre (admite coincidencias parciales e ignora tildes).
2-   Filtrar países por continente, rango de población o superficie.
4-   ordenar y listar países por continente, población o superficie de maere ascendente y descendente.
4-   Mostrar estadísticas generales (mayor/menor población, promedios y cantidad por continente).
5-   Visualizar los resultados en una tabla formateada.

El programa está desarrollado en Python 3 y utiliza estructuras de datos tipo diccionario para el manejo de la información.

                                --------------------  Instrucciones de uso:   --------------------

Ejecutar el programa principal en la consola:
-   python main.py

El menú principal mostrará distintas opciones:

1 - Buscar un país por nombre
2 - Filtrar países
3 - Ordenar países
4 - Mostrar estadísticas
5 - Salir

Según la opción elegida:

1 - Buscar país: permite escribir parte del nombre (ej: “arg” → Argentina).

2 - Filtrar países: ofrece tres criterios:
    a - Por continente (ej: América, Europa).
    b - Por rango de población (mínima y máxima).
    c - Por rango de superficie (mínima y máxima).

3 - Ordenar países: brinda las siguientes opciones 
    a - Ordenar por nombre.
    b - Ordenar por población.
    c - Ordenar por superficie.
para cualquierea de ellas se puede elegir criterio aqscendente o descendente.

4 - Mostrar estadísticas: muestra resultados agregados:
    País con mayor y menor población.
    Promedio de población y superficie.
    Cantidad de países por continente.


Los resultados se muestran en una tabla con columnas alineadas:
---------------------------------------------------------------------
País                | Continente      | Población      | Superficie
---------------------------------------------------------------------
Argentina           | América del Sur | 45,808,747     | 2,780,400
Brasil              | América del Sur | 212,559,417    | 8,515,767
---------------------------------------------------------------------

                            ------------------ Ejemplos de entradas y salidas ------------------
Ejemplo 1: Búsqueda
Entrada:
Ingrese nombre o parte del país a buscar: arge

Salida:

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Pais                                    Continente                              Población                               Superficie
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Argentina                               América del Sur                         46,621,847                              2,780,400 km²

**********************************************************************************

Ejemplo 2: Filtro por continente
Entrada:
Ingrese continente a filtrar: america

Salida:

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Pais                                    Continente                              Población                               Superficie
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Estados Unidos                          América del Norte                       339,665,118                             9,833,517 km²
Brasil                                  América del Sur                         218,689,757                             8,515,770 km²
México                                  América del Norte                       129,875,529                             1,964,375 km²
Colombia                                América del Sur                         49,336,454                              1,138,910 km²
Argentina                               América del Sur                         46,621,847                              2,780,400 km²
Canadá                                  América del Norte                       38,516,736                              9,984,670 km²
...

(Nótese que se ignoraron las tildes al buscar “america” en lugar de “américa”)

**********************************************************************************

Ejemplo 3: Ordenamiento

Ordenar paises por: 1 - Nombre
criterio: 1 - ascendente

Salida:

----------------------------------------------------------------------------------------------------------------------------------------------------------------
Pais                                    Continente                              Población                               Superficie
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Afghanistan                             Asia                                    39,232,003                              652,230 km²
Albania                                 Europa                                  3,101,621                               28,748 km²
Alemania                                Europa                                  84,220,184                              357,022 km²
Algeria                                 África                                  44,758,398                              2,381,740 km²
American Samoa                          Oceanía                                 44,620                                  224 km²
Andorra                                 Europa                                  85,468                                  468 km²
Angola                                  África                                  35,981,281                              1,246,700 km²
Antigua y Barbuda                       América del Norte                       101,489                                 443 km²
Arabia Saudita                          Asia                                    35,939,806                              2,149,690 km²
Argentina                               América del Sur                         46,621,847                              2,780,400 km²
...

***********************************************************************************

Ejemplo 3: Estadísticas

Salida:

------------------------------------------------------------
    Estadísticas Generales
------------------------------------------------------------
País con mayor población: China (1,413,142,846 hab.)
País con menor población: Nauru (9,852 hab.)
Promedio de población: 40,482,278 hab.
Promedio de superficie: 685,351 km²

Cantidad de países por continente:
  - Asia: 48
  - América del Norte: 27
  - África: 48
  - América del Sur: 12
  - Europa: 42
  - Oceanía: 16
  - Seven seas (open ocean): 3
------------------------------------------------------------

                            ------------------ Participación de los integrantes: ------------------

Integrante:
Lucas Daniel Perez.

Tareas realizadas:
- Desarrollo de las funciones (buscar_pais, mostrar_paises, ordenar_lista, ordenar_paises,mostrar_paises, menu, leer_csv). 
- Manejo de entrada y salida de datos en consola.
- Adaptación del dataset

Integrante:
Matías Pavón.	

Tareas realizadas:
- Desarrollo de las funciones (mostrar_estadísticas, filtrar_paises, utilidades) 
- Estructura del main. 
- Validaciones de entrada. 
- Documentación y creación del archivo README.md.