"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta = os.path.join(base_dir, "files", "input", "data.csv")
    with open(ruta, "r") as f:
        lines = f.readlines()   

    lines = [line.strip() for line in lines]
    letter_count = {}
    for line in lines:
        letter = line[0]
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    sorted_letter_count = sorted(letter_count.items())
    return sorted_letter_count

if __name__ == "__main__":
    print(pregunta_02())
