import random

# Biblioteca para debug
from icecream import ic
ic.configureOutput(prefix='Debug| ')
#ic.disable()

# Inicializando o quadro
def boardInit():
    values = [1, 2, 3, 4, 5, 6, 7, 8, -1]
    random.shuffle(values)
    ic(values)
    quadro = []
    aux1 = 0
    for i in range(3):
        row = []
        for j in range(3):
            aux2 = values[aux1]
            row.append(aux2)
            aux1+=1
        quadro.append(row)
    ic(quadro)
    return quadro


quadro = boardInit()
