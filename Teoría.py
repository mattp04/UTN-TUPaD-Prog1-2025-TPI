# 1) Diseño (previo al código)
# • Explicar en un informe teórico los conceptos aplicados:
#     o Listas
#     o Diccionarios
#     o Funciones
#     o Condicionales
#     o Ordenamientos
#     o Estadísticas básicas
#     o Archivos CSV
# • Definir el flujo de operaciones principales en un diagrama o esquema.

# Listas
# Una lista es un conjunto ordenado de valores que se identifican por medio de un
# índice. Los valores que componen una lista se denominan elementos. Las listas son
# similares a las cadenas, que son conjuntos ordenados de caracteres, pero son mas
# generales, ya que pueden tener elementos de cualquier tipo de dato. Las listas se
# denominan secuencias.
# lista_ejemplo = ["hola", 2.0, 5, [10, 20]]

# Diccionarios
# Los tipos de dato compuestos como las cadenas o listas usan enteros como índices. Si
# intentáramos usar cualquier otro tipo de dato como índice provocaría un error.
# Los diccionarios son similares a otros tipos de dato compuestos, excepto en que pueden
# usar como índice cualquier tipo inmutable. A modo de ejemplo, crearemos un diccionario 
# que traduzca palabras inglesas al español. En este diccionario, los índices son strings.
# Una forma de crear un diccionario es empezar con el diccionario vacíıo y añadir
# elementos. El diccionario vacío se expresa como {}:

# >>> ing_a_esp = {}
# >>> ing_a_esp['one'] = 'uno'
# >>> ing_a_esp['two'] = 'dos'

# La primera asignación crea un diccionario llamado ing_a_esp; las otras asignaciones 
# añaden nuevos elementos al diccionario.

# Funciones
# ¿Qué es una función? Es un conjunto breve de instrucciones que
# permiten alcanzar fácilmente un pequeño objetivo. Las funciones son la
# base para resolver los tres grandes problemas de la programación: 
# a) la reutilización del código, 
# b) la simplificación del objetivo 
# c) la facilidad
# para realizar las pruebas en frío. Con las funciones se hace efectiva
# la estrategia "Divide y Vencerás" que es una manera de hacer que los
# programas, por complejos que parezcan, sean más fáciles de entender
# y, sobre todo, más fáciles de corregir.

# Definición y uso de funciones:
# Para Ejemplificar, empezaremos definiendo una función muy sencilla, 
# una que recibe un numero y devuelve el cuadrado de dicho numero. El nombre 
# que daremos a la función es "cuadrado".

# def cuadrado(x):
# return x ** 2

# Acabamos de definir la función cuadrado que se aplica sobre un valor al que
# llamamos x y devuelve un numero: el resultado de elevar x al cuadrado. 

# En el programa aparecen dos nuevas palabras reservadas: 
# def y return. La palabra def es abreviatura de ˂˂define˃˃ y 
# return significa ˂˂devuelve˃˃ en inglés. Podríamos leer el programa anterior
# como ˂˂define cuadrado de x como el valor que resulta de elevar x al cuadrado˃˃

# Condicionales
# Una sentencia condicional es un esquema de instrucciones que permite
# escoger uno de entre dos caminos lógicos o uno de entre varios caminos
# lógicos. Estas sentencias condicionales sirven para validar datos, es decir,
# para verificar que se cumplan determinadas condiciones que sean favorables a 
# los programas que construyamos. Vamos a comenzar con un ejemplo sencillo. 
# Supongamos que necesitamos leer un número (o sea que el usuario lo escriba) y 
# queremos determinar si el número leído es un 6. Un programa que resuelva este 
# enunciado podría ser el siguiente:

# # Se coloca un título
# print("PROGRAMA PARA VERIFICAR UN VALOR")

# # Se solicita y se lee un número entero
# num = int(input("\Escriba un número entero:"))

# # Se evalúa si es igual a 6 o no
# if num == 6:
#     print("El número recibido es un 6")
# else:
#     print("El número recibido NO es un 6")

# Ordenamientos
# Proceso de reorganizar los elementos de una colección (por ejemplo una lista) 
# según un criterio (orden ascendente, descendente).

# Algoritmos comunes:
#   • Burbuja (bubble sort)
#   • Selección (selection sort)
#   • Inserción (insertion sort)
#   • Merge Sort
#   • Quick Sort

# Implementación en Python (por ejemplo, un sort() nativo o un algoritmo escrito)

# Estadísticas básicas
# Media
# Suma de todos los valores dividida por el número de valores.
# Sinónimos:
# promedio

# Media ponderada
# Suma de todos los valores multiplicados por cada ponderación y dividida por la
# suma de las ponderaciones.
# Sinónimo
# promedio ponderado

# Mediana
# Valor tal que la mitad del número de datos se encuentra por encima y la otra mitad
# por debajo de dicho valor.
# Sinónimo
# Percentil 50

# Percentil
# Valor tal que el P por ciento de los datos se encuentra por debajo del mismo.
# Sinónimo
# cuantil

# Mediana ponderada
# Valor tal que la mitad de la suma de las ponderaciones se encuentra por encima y
# la otra mitad por debajo de los datos ordenados.

# Archivos CSV
# El tan llamado CSV (Valores Separados por Comas) es el formato más común de importación
#  y exportación de hojas de cálculo y bases de datos. El formato CSV se utilizó durante 
# muchos años antes de intentar describir el formato de manera estandarizada en RFC 4180. 
# La falta de un estándar bien definido significa que a veces existen pequeñas diferencias 
# en la información producida y consumida por diferentes aplicaciones. Estas diferencias pueden 
# ser molestas al momento de procesar archivos CSV desde múltiples fuentes. Aún así, aunque
#  los delimitadores y separadores varíen, el formato general es lo suficientemente similar 
# como para que sea posible un sólo módulo que puede manipular tal información eficientemente, 
# escondiendo los detalles de lectura y escritura de datos del programador.

# Bibliografía
# csv — CSV File Reading and Writing: https://docs.python.org/es/3.13/library/csv.html
# (Andrés Becerra Sandoval) Introducción a la programación con Python: https://ia802802.us.archive.org/34/items/IntroduccinALaProgramacinConPythonBecerra/Introducci%C3%B3n%20a%20la%20programaci%C3%B3n%20con%20Python%20-%20Becerra.pdf
# (Bruce-Gedeck) Estadística Práctica para Ciencia de Datos Con R y Python: https://es.scribd.com/document/660928067/Bruce-Gedeck-Estadistica-Practica-para-Ciencia-de-Datos-con-R-y-Python
# (Andrés Marzal, Isabel Gracia) Introducción a la programación con Python: https://aulavirtual.fio.unam.edu.ar/pluginfile.php/93521/mod_resource/content/1/Introducci%C3%B3n%20a%20la%20Programaci%C3%B3n%20con%20Python.pdf