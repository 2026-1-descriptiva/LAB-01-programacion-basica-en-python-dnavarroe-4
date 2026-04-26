"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    file = "files/input/data.csv"
    with open (file, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.split("\t") for line in lines]

    letter_count = {}

    for line in lines:
        letter = line[0]
        value = line[1]
        if letter in letter_count:
            letter_count[letter] += int(value)
        else:
            letter_count[letter] = int(value)

    letter_count = sorted(letter_count.items())

    return letter_count

if __name__ == "__main__":
    print(pregunta_03())
