import csv


def leer_csv():
    datos = {}
    with open("Paises.csv", newline="", encoding="latin-1") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            # convierto las columnas numéricas
            fila["Población"] = int(fila["Población"])  # población
            fila["Densidad"] = float(fila["Densidad"])  # Densidad
            fila["Superficie"] = int(fila["Superficie"])  # Superficie
            fila["PBI"] = int(fila["PBI"])  # PBI
            # guardo cada país usando su nombre como clave
            datos[fila["País"]] = fila
    return datos