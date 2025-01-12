"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re
    # Leer archivos, se agrega encoding para poder que se lean los diferetes caracteres. 
    filename = "files/input/clusters_report.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Aqui se excluyen la sprimeras cuatro lineas dado que separar las columnas  no dadba ni con saltos de lineas, ni con espacios. Lo mejor era eliminar y crearlas al final. 
    data_lines = lines[4:]

    # aqui se prepara la lista para almacenar los datos por cada linea y eliminar cada blanco y dividir las wqpalabras 
    processed_data = []
    temp_row = []  # Para almacenar datos temporalmente
    is_first_line = True  # Identificar si es la primera línea de un registro

    for line in data_lines:
        line = line.strip()  # Eliminar espacios en blanco al inicio y fin
        words = line.split()  # Dividir la línea en palabras

        # Aqui se recorre cada linea  para organizar y limpiar los datos que son numericos y los uq eletras

        if words and is_first_line:  # Si es la primera línea de un registro
            temp_row = [
                int(words[0]),  # Número de cluster
                int(words[1]),  # Cantidad de palabras clave
                float(words[2].replace(',', '.')),  # Porcentaje de palabras clave
                " ".join(words[4:]),  # Fragmento inicial de palabras clave
            ]

          #En esta parte se organiza todo lo que se necesita para que se unan los parrafos donde se pone el punto, dado que anteriormente solo esta por linea y separado por las comas. 
            is_first_line = False
        elif words:  # Si no es la primera línea pero hay contenido
            temp_row[-1] += " " + " ".join(words)  # Concatenar palabras clave
        else:  # Línea vacía indica el final de un registro
            # Finalizar procesamiento de palabras clave
            temp_row[-1] = temp_row[-1].replace('.', '')
            processed_data.append(temp_row)  # Agregar registro completo
            temp_row = []  # Reiniciar registro temporal
            is_first_line = True

    # Crear DataFrame a partir de los datos procesados
    columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    return pd.DataFrame(processed_data, columns=columns)

print(pregunta_01())
