"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    file = "files/input/data.csv"

    with open(file, "r") as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.split('\t') for line in lines]
    lines = [line[2].split('-') for line in lines]

    month_count = {}
    for line in lines:
        month = line[1]
        if month in month_count:
            month_count[month] += 1
        else:
            month_count[month] = 1
    month_count = sorted(month_count.items())

    return month_count

if __name__ == '__main__':
    print(pregunta_04())
