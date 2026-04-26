"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(path,'files','input','data.csv')
    with open(file, "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split('\t') for line in lines]
    lines = [line[4].split(',') for line in lines]
    lines = [element.split(':') for sub in lines for element in sub]
    lines = [element[0] for element in lines]
    chain_count = {}

    for element in lines:
        if element in chain_count:
            chain_count[element] += 1
        else:
            chain_count[element] = 1
    
    chain_count = dict(sorted(chain_count.items()))

    return chain_count

if __name__ == '__main__':
    print(pregunta_09())
