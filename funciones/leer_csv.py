import csv


def leer_csv():
    datos = []
    with open("Paises.csv", newline="", encoding="latin-1") as f:
        reader = csv.reader(f)
        encabezados = next(reader) 
        datos.append(encabezados)
        for fila in reader:
            # convierto las columnas numéricas
            fila[1] = int(fila[1])  # población
            fila[2] = float(fila[2])  # Densidad
            fila[3] = int(fila[3])  # Superficie
            fila[4] = int(fila[4])  # PBI
            datos.append(fila)
    return datos