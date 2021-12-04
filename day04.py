import sys

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

numbers = [int(i) for i in lines[0].split(',')]

boards = []
curr = []
for line in lines[2:]:
    if not line:
        boards.append(curr)
        curr = []
    else:
        row = [int(i) for i in line.split()]
        curr.append(row)
boards.append(curr)

def checkWin(board):
    for row in board:
        if all(elem in called for elem in row):
            return board
    for i in range(5):
        col = [board[0][i], board[1][i], board[2][i], board[3][i], board[4][i]]
        if all(elem in called for elem in col):
            return board
    diag1 = [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]]
    if all(elem in called for elem in diag1):
        return board
    diag2 = [board[0][4], board[1][3], board[2][2], board[3][1], board[4][0]]
    if all(elem in called for elem in diag1):
        return board


called = []
win = None
for n in numbers:
    called.append(n)
    for board in boards:
        win = checkWin(board)
        if win:
            break
    if win:
        break

total = 0
for row in win:
    for el in row:
        if el not in called:
            total += el

print(total * n)

called = []
final = None
for n in numbers:
    called.append(n)
    toRemove = []
    for board in boards:
        win = checkWin(board)
        if win and len(boards) == 1:
            final = win
            break
        if win:
            toRemove.append(board)
    if final:
        break
    for board in toRemove:
        boards.remove(board)

total = 0
for row in final:
    for el in row:
        if el not in called:
            total += el

print(total * n)
