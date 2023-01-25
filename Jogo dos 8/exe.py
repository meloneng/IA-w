import random
from queue import Queue

# Biblioteca para debug
from icecream import ic
ic.configureOutput(prefix='Debug| ')
#ic.disable()

# Inicializando o board
def boardInit():
    values = [1, 2, 3, 4, 5, 6, 7, 8, -1]
    random.shuffle(values)
    ic(values)
    board = []
    aux1 = 0
    for i in range(3):
        row = []
        for j in range(3):
            aux2 = values[aux1]
            row.append(aux2)
            aux1+=1
        board.append(row)
    ic(board)
    return board


def findBlank(board):
    for i_idx, i in enumerate(board):
        for j_idx, j in enumerate(i):
            if(j == -1):
                return (i_idx,j_idx)



def statesGen(board):
    blank = findBlank(board)
    if(blank[0] == 0):
        if(blank[1] == 0):
        if(blank[1] == 2)
    if(blank[0] == 2):
        if(blank[1] == 0)
        if(blank[1] == 2)
    



estadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
board = boardInit()
states = Queue()

