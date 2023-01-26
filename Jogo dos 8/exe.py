import random
import copy
from queue import Queue, LifoQueue

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



# Movimentações
def movDown(originBoard, blank):
    if((blank[0]+1) < 3):
        board = copy.deepcopy(originBoard)
        aux = board[blank[0]+1][blank[1]]
        board[blank[0]+1][blank[1]] = board[blank[0]][blank[1]]
        board[blank[0]][blank[1]] = aux
        #ic(board)
        if board in knowStates:
            return False
        elif(board == estadoFinal):
            return True
        else:
            states.put(board)
            knowStates.append(board)
            return False

def movUp(originBoard, blank):
    if((blank[0]-1) > -1):
        board = copy.deepcopy(originBoard)
        aux = board[blank[0]-1][blank[1]]
        board[blank[0]-1][blank[1]] = board[blank[0]][blank[1]]
        board[blank[0]][blank[1]] = aux
        #ic(board)
        if board in knowStates:
            return False
        elif(board == estadoFinal):
            return True
        else:
            states.put(board)
            knowStates.append(board)
            return False

def movRight(originBoard, blank):
    if((blank[1]+1) < 3):
        board = copy.deepcopy(originBoard)
        aux = board[blank[0]][blank[1]+1]
        board[blank[0]][blank[1]+1] = board[blank[0]][blank[1]]
        board[blank[0]][blank[1]] = aux
        #ic(board)
        if board in knowStates:
            return False
        elif(board == estadoFinal):
            return True
        else:
            states.put(board)
            knowStates.append(board)
            return False

def movLeft(originBoard, blank):
    if((blank[1]-1) > -1):
        board = copy.deepcopy(originBoard)
        aux = board[blank[0]][blank[1]-1]
        board[blank[0]][blank[1]-1] = board[blank[0]][blank[1]]
        board[blank[0]][blank[1]] = aux
        #ic(board)
        if board in knowStates:
            return False
        elif(board == estadoFinal):
            return True
        else:
            states.put(board)
            knowStates.append(board)
            return False



# Verifica para qual direção o Blank pode ir e gera o estado
def statesGen(originBoard):
    blank = findBlank(originBoard)
    
    ic("new Gen", originBoard)
    ic(len(knowStates))

    b = movDown(originBoard, blank)
    a = movUp(originBoard, blank)
    c = movRight(originBoard, blank)
    d = movLeft(originBoard, blank)

    if(a or b or c or d):
        return True

    # Retorna falso após fazer os movimentos e não chegar ao estado final
    return False
        

# Solução por BFS
def solWidth():
    Initialboard = boardInit()
    states.put(Initialboard)
    knowStates.append(Initialboard)
    aux=0
    while(not(statesGen(states.get()))):
        aux+=1
        if(states.empty()):
            print("Não achou estado final")
            break
    print("Número iterações: ", aux)


# Solução por DFS
def solDepth():
    Initialboard = boardInit()
    states.put(Initialboard)
    knowStates.append(Initialboard)
    aux=0
    while(not(statesGen(states.get()))):
        aux+=1
        if(states.empty()):
            print("Não achou estado final")
            break
    print("Número iterações: ", aux)


def solAStar():
    ic("mango")


estadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
knowStates = []
#states = Queue()
#solWidth()
states = LifoQueue()
solDepth()

