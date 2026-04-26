"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    file = "files/input/data.csv"
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split('\t') for line in lines]
    count = {}

    for line in lines:
        key = line[0]
        pairs = line[4].split(',')
        split_pairs = [pair.split(':') for pair in pairs]
        value = sum(int(pair[1]) for pair in split_pairs)
        if key in count:
            count[key] += value
        else:
            count[key] = value
    
    count = dict(sorted(count.items()))

    return count
