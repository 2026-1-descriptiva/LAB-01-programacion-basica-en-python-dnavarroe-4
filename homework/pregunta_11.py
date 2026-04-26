"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split("\t")

            numero = int(partes[1])
            letras = partes[3].split(",")

            for letra in letras:
                if letra in suma:
                    suma[letra] += numero
                else:
                    suma[letra] = numero

    resultado = dict(sorted(suma.items()))
    return resultado
