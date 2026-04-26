"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    ruta = "files/input/data.csv"

    with open(ruta, "r") as f:
        lines = f.readlines()


    suma = 0
    for line in lines:
        line = line.strip()
        columns = line.split("\t")
        suma += int(columns[1])

    return suma

if __name__ == "__main__":
    print(pregunta_01())
