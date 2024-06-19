#! python3
import random as rd
import pyinputplus as pyip
import copy

# Choose your players
while True:
    playerOne = pyip.inputMenu(["user", "random", "smartOne", "smartTwo"], prompt="Please select your first player\n")
    playerTwo = pyip.inputMenu(["user", "random", "smartOne", "smartTwo"], prompt="Please select your second player\n")
    if playerOne == playerTwo:
        print("Player One and Player Two need to be different players")
        continue
    else:
        break

# intial state of the board
# 1=empty, 2= playerOne red, 3 = playerOne blue, 4= playerTwo yellow and 5=playerTwo white
initialBoard = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1}


# intialize players


# place tile operation
def placeTile(board, cell, color):
    for k in board.keys():
        if k == cell:
            board[k] = color
            return board


# random flip operation
def randomFlipMove(board, color):
    randomMoveFrom = []
    randomMoveTo = []

    for k in board.keys():
        if board[k] == 4 and color == "redBlue" or board[k] == 5 and color == "redBlue":
            randomMoveFrom.append(k)
        elif board[k] == 2 and color == "yellowWhite" or board[k] == 3 and color == "yellowWhite":
            randomMoveFrom.append(k)
    randomCellFlipFrom = rd.choice(randomMoveFrom)
    for k in board.keys():
        if randomCellFlipFrom == k:
            if randomCellFlipFrom == 1:
                randomMoveTo.append(k + 1)
                randomMoveTo.append(k + 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo

            elif randomCellFlipFrom == 2 or randomCellFlipFrom == 3:
                randomMoveTo.append(k - 1)
                randomMoveTo.append(k + 1)
                randomMoveTo.append(k + 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo
            elif randomCellFlipFrom == 4:
                randomMoveTo.append(k - 1)
                randomMoveTo.append(k + 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo
            elif randomCellFlipFrom == 5 or randomCellFlipFrom == 9:
                randomMoveTo.append(k + 1)
                randomMoveTo.append(k - 4)
                randomMoveTo.append(k + 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo
            elif randomCellFlipFrom == 6 or randomCellFlipFrom == 7 or randomCellFlipFrom == 10 or randomCellFlipFrom == 11:
                randomMoveTo.append(k + 1)
                randomMoveTo.append(k - 1)
                randomMoveTo.append(k + 4)
                randomMoveTo.append(k - 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo
            elif randomCellFlipFrom == 8 or randomCellFlipFrom == 12:
                randomMoveTo.append(k - 1)
                randomMoveTo.append(k + 4)
                randomMoveTo.append(k - 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo
            elif randomCellFlipFrom == 13:
                randomMoveTo.append(k + 1)
                randomMoveTo.append(k - 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo
            elif randomCellFlipFrom == 14 or randomCellFlipFrom == 15:
                randomMoveTo.append(k + 1)
                randomMoveTo.append(k - 1)
                randomMoveTo.append(k - 4)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo
            elif randomCellFlipFrom == 16:
                randomMoveTo.append(k - 4)
                randomMoveTo.append(k - 1)
                randomCellFlipTo = rd.choice(randomMoveTo)
                return randomCellFlipFrom, randomCellFlipTo


# random place tile operation
def pickRandomCell(board):
    randomPlaceTile = []
    for k in board.keys():
        if board[k] == 1:
            randomPlaceTile.append(k)
    randomCell = rd.choice(randomPlaceTile)
    return randomCell


# flip tile operation
def flipTile(board, cellFlipFrom, cellFlipTo):
    for k in board:
        if cellFlipFrom == k:
            if board[k] == 2:
                board[cellFlipTo] = 3
                board[k] = 1
                return board
            elif board[k] == 3:
                board[cellFlipTo] = 2
                board[k] = 1
                return board

            elif board[k] == 4:
                board[cellFlipTo] = 5
                board[k] = 1
                return board
            elif board[k] == 5:
                board[cellFlipTo] = 4
                board[k] = 1
                return board


# validate tile flip
def isValidFlip(board, cellFlipFrom, cellFlipTo):
    for k in board.keys():
        if k == 1:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k + 1 or cellFlipTo == k + 4:
                    if board[cellFlipTo] == 1:
                        return 1
        elif k == 2 or k == 3:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k - 1 or cellFlipTo == k + 1 or cellFlipTo == k + 4:
                    if board[cellFlipTo] == 1:
                        return 1

        elif k == 4:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k - 1 or cellFlipTo == k + 4:
                    if board[cellFlipTo] == 1:
                        return 1

        elif k == 5 or k == 9:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k + 1 or cellFlipTo == k + 4 or cellFlipTo == k - 4:
                    if board[cellFlipTo] == 1:
                        return 1
        elif k == 6 or k == 7 or k == 10 or k == 11:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k + 1 or cellFlipTo == k - 1 or cellFlipTo == k + 4 or cellFlipTo == k - 4:
                    if board[cellFlipTo] == 1:
                        return 1

        elif k == 8 or k == 12:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k - 1 or cellFlipTo == k + 4 or cellFlipTo == k - 4:
                    if board[cellFlipTo] == 1:
                        return 1

        elif k == 13:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k + 1 or cellFlipTo == k - 4:
                    if board[cellFlipTo] == 1:
                        return 1

        elif k == 14 or k == 15:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k + 1 or cellFlipTo == k - 1 or cellFlipTo == k - 4:
                    if board[cellFlipTo] == 1:
                        return 1
        elif k == 16:
            if cellFlipFrom == k and board[k] != 1 and cellFlipFrom != cellFlipTo:
                if cellFlipTo == k - 4 or cellFlipTo == k - 1:
                    if board[cellFlipTo] == 1:
                        return 1


# check to see if no valid flip moves exist
def noValidFlip(board, color):
    for k in board.keys():
        if color == "redBlue":
            if board[k] == 4 or board[k] == 5:
                if (isValidFlip(board, k, k + 1) != 1 and isValidFlip(board, k, k - 1) != 1
                        and isValidFlip(board, k, k + 4) != 1 and isValidFlip(board, k, k - 4) != 1):
                    continue
                else:
                    return 0
        if color == "yellowWhite":
            if board[k] == 2 or board[k] == 3:
                if (isValidFlip(board, k, k + 1) != 1 and isValidFlip(board, k, k - 1) != 1
                        and isValidFlip(board, k, k + 4) != 1 and isValidFlip(board, k, k - 4) != 1):
                    continue
                else:
                    return 0
    return 1


# validate tile placement
def isValidCell(board, cell):
    for k in board.keys():
        if k == cell and board[k] == 1:
            return 1


# determine if board is in a terminal state
def isTerminal(board):
    for k in board.keys():
        if k == 1:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k + 3] != 1 and board[k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k + 1] != 1 and board[k + 5] != 1 and board[k + 9] != 1 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k + 1] != 1 and board[k + 4] != 1 and board[k + 6] != 1 and board[k + 9] != 1 and board[
                    k + 11] != 1 and board[k + 14] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1

        elif k == 2:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 5] != 1 and board[k + 6] != 1 and board[k + 4] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[k + 5] != 1 and board[
                    k + 7] != 1 and board[k + 9] != 9 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 4] != 1 and board[k + 6] != 1 and board[
                    k + 9] != 1 and board[k + 14] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 3:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[k + 5] != 1 and board[
                    k + 7] != 1 and board[k + 9] != 1 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 2] != 1 and board[k + 4] != 1 and board[
                    k + 7] != 1 and board[k + 10] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 4:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 3] != 1 and board[k + 7] != 1 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 2] != 1 and board[k + 4] != 1 and board[k + 5] != 1 and board[
                    k + 7] != 1 and board[k + 10] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 5:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k + 3] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k + 1] != 1 and board[k + 5] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k - 4] != 1 and board[k + 1] != 1 and board[k + 4] != 1 and board[k + 6] != 1 and board[
                    k + 9] != 1 and board[k + 11] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 6:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k - 1] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[
                    k + 5] != 1 and board[k + 7] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 4] != 1 and board[
                    k + 6] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 7:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[
                    k + 5] != 1 and board[k + 7] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 2] != 1 and board[
                    k + 4] != 1 and board[k + 7] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 8:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 3] != 1 and board[k + 7] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 2] != 1 and board[k + 4] != 1 and board[
                    k + 5] != 1 and board[k + 7] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 9:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k + 3] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 10:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k - 1] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 13:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k + 3] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
        elif k == 14:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k - 1] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 1
                    if board[k] == 4 or board[k] == 5:
                        return -1
    return 0


# show the board
def printBoard(board):
    for k in board.keys():
        board[k] = str(board[k])
    # file = open(fileName,"a")
    print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4])
    # print(board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4],file=file)
    print('- + - +')
    # print('- + - +',file = file)
    print(board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8])
    # print(board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8],file=file)
    print('- + - +')
    # print('- + - +',file=file)
    print(board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12])
    # print(board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12],file=file)
    print('- + - +')
    # print('- + - +',file=file)
    print(board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16])
    # print(board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16],file=file)
    # print("\n",file=file)
    # print("\n",file=file)


# evaluate functions
def firstEvaluation(board):
    tempBoard = []
    for k in board.keys():
        if k == 1:
            rowColumn = [[k, board[k]], [k + 1, board[k + 1]], [k + 2, board[k + 2]], [k + 3, board[k + 3]]]
            tempBoard.append(rowColumn)
        if k == 5:
            rowColumn = [[k, board[k]], [k + 1, board[k + 1]], [k + 2, board[k + 2]], [k + 3, board[k + 3]]]
            tempBoard.append(rowColumn)
        if k == 9:
            rowColumn = [[k, board[k]], [k + 1, board[k + 1]], [k + 2, board[k + 2]], [k + 3, board[k + 3]]]
            tempBoard.append(rowColumn)
        if k == 13:
            rowColumn = [[k, board[k]], [k + 1, board[k + 1]], [k + 2, board[k + 2]], [k + 3, board[k + 3]]]
            tempBoard.append(rowColumn)
    for k in board.keys():
        if k == 1:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k + 3] != 1 and board[k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k + 1] != 1 and board[k + 5] != 1 and board[k + 9] != 1 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k + 1] != 1 and board[k + 4] != 1 and board[k + 6] != 1 and board[k + 9] != 1 and board[
                    k + 11] != 1 and board[k + 14] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100

        elif k == 2:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 5] != 1 and board[k + 6] != 1 and board[k + 7] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[k + 5] != 1 and board[
                    k + 7] != 1 and board[k + 9] != 9 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 4] != 1 and board[k + 6] != 1 and board[
                    k + 9] != 1 and board[k + 14] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 3:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[k + 5] != 1 and board[
                    k + 7] != 1 and board[k + 9] != 1 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 1] != 1 and board[k + 2] != 1 and board[k + 4] != 1 and board[
                    k + 7] != 1 and board[k + 10] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 4:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 3] != 1 and board[k + 7] != 1 and board[k + 12] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 1] != 1 and board[k + 2] != 1 and board[k + 4] != 1 and board[k + 5] != 1 and board[
                    k + 7] != 1 and board[k + 10] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 5:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k + 3] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k + 1] != 1 and board[k + 5] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k - 4] != 1 and board[k + 1] != 1 and board[k + 4] != 1 and board[k + 6] != 1 and board[
                    k + 9] != 1 and board[k + 11] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 6:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k - 1] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[
                    k + 5] != 1 and board[k + 7] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 5] and board[k + 5] == board[k + 10] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 4] != 1 and board[
                    k + 6] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 7:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 3] != 1 and board[
                    k + 5] != 1 and board[k + 7] != 1 and board[k + 9] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 1] != 1 and board[k + 2] != 1 and board[
                    k + 4] != 1 and board[k + 7] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 8:
            if board[k] == board[k + 4] and board[k + 4] == board[k + 8] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 3] != 1 and board[k + 7] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
            elif board[k] == board[k + 3] and board[k + 3] == board[k + 6] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 1] != 1 and board[k + 2] != 1 and board[k + 4] != 1 and board[
                    k + 5] != 1 and board[k + 7] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 9:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k + 3] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 10:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k - 1] != 1 and board[
                    k + 4] != 1 and board[k + 5] != 1 and board[k + 6] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 13:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k + 3] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
        elif k == 14:
            if board[k] == board[k + 1] and board[k + 1] == board[k + 2] and board[k] != 1:
                if board[k - 4] != 1 and board[k - 3] != 1 and board[k - 2] != 1 and board[k - 1] != 1:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
    # Cell 1
    for i, j in enumerate(tempBoard):
        for m, _ in enumerate(j):
            if tempBoard[i][m][1] != 1:
                if i == 0 and m == 0:
                    if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] == tempBoard[i][m + 2][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 or
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 0):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # Cell 2
                if i == 0 and m == 1:
                    if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] == tempBoard[i][m + 2][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # cell 5 or cell 9
                if i == 1 and m == 0 or i == 2 and m == 0:
                    if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] == tempBoard[i][m + 2][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 or
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 75
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -75
                        if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # Cell 6 or Cell 10
                if i == 1 and m == 1 or i == 2 and m == 1:
                    if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] == tempBoard[i][m + 2][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 or
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 75
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -75
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # Cell 13
                if i == 3 and m == 0:
                    if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] == tempBoard[i][m + 2][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 or
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 0):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # cell 14
                if i == 0 and m == 1:
                    if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] == tempBoard[i][m + 2][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # check three in a column with the same value

                # cell 1
                if i == 0 and m == 0:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] == tempBoard[i + 2][m][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 0):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # cell 2 or Cell 3
                if i == 0 and m == 1 or i == 0 and m == 2:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] == tempBoard[i + 2][m][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 75
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -75
                        if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # cell 4
                if i == 0 and m == 3:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] == tempBoard[i + 2][m][
                        1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 0):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # cell 5
                if i == 1 and m == 0:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] == tempBoard[i + 2][m][
                        1]):
                        if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 0):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # cell 6 or cell 7
                if i == 1 and m == 1 or i == 1 and m == 2:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] == tempBoard[i + 2][m][
                        1]):
                        if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 75
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -75
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # Cell 8:
                if i == 1 and m == 3:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] == tempBoard[i + 2][m][
                        1]):
                        if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 or
                                isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 0):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # check the forward diagonals for any three that have the same value
                # Cell 1
                if i == 0 and m == 0:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m + 1][1] and tempBoard[i + 1][m + 1][1] ==
                            tempBoard[i + 2][m + 2]):
                        if (isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i + 2][m + 3][1] == 1 and tempBoard[i + 3][m + 2][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i + 2][m + 3][1] == 1 and tempBoard[i + 3][m + 2][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m][0]) != 1 and
                                tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                tempBoard[i + 2][m + 3][1] == 1 and tempBoard[i + 3][m + 2][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80
                        if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # Cell 2
                if i == 0 and m == 1:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m + 1][1] and tempBoard[i + 1][m + 1][1] ==
                            tempBoard[i + 2][m + 2]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i + 3][m + 2][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                tempBoard[i + 3][m + 2][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][
                                    1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i + 3][m + 2][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # Cell 5
                if i == 1 and m == 0:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m + 1][1] and tempBoard[i + 1][m + 1][1] ==
                            tempBoard[i + 2][m + 2]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i + 2][m + 3][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i - 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                tempBoard[i + 2][m + 3][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i - 1][m][1] == 1 and tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][
                                    1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i - 1][m][1] == 1 and tempBoard[i + 2][m + 3][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # Cell 6
                if i == 1 and m == 1:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m + 1][1] and tempBoard[i + 1][m + 1][1] ==
                            tempBoard[i + 2][m + 2]):
                        if (isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m][0]) != 1 and
                                tempBoard[i + 2][m + 1][1] == 1 and tempBoard[i + 1][m + 2][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                tempBoard[i + 1][m][1] == 1 and tempBoard[i][m + 1][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80
                        if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1 and
                                tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # check backward diagonals for any three that have the same value
                # cell 3
                if i == 0 and m == 2:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m - 1][1] and tempBoard[i + 1][m - 1][1] ==
                            tempBoard[i + 2][m - 2][1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i + 3][m - 2][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i][m + 1][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                tempBoard[i + 3][m - 2][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                tempBoard[i][m + 1][1] == 1 and tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][
                                    0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i][m + 1][1] == 1 and tempBoard[i + 3][m - 2][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90

                # cell 4
                if i == 0 and m == 3:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m - 1][1] and tempBoard[i + 1][m - 1][1] ==
                            tempBoard[i + 2][m - 2][1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i + 2][m - 3][1] == 1 and tempBoard[i + 3][m - 1][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                tempBoard[i + 2][m - 3][1] == 1 and tempBoard[i + 3][m - 1][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80
                        if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1 and
                                tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # Cell 7
                if i == 1 and m == 2:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m - 1][1] and tempBoard[i + 1][m - 1][1] ==
                            tempBoard[i + 2][m - 2][1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - +1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i - 1][m][0]) != 1 and
                                tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][1]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80
                        if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1 and
                                tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 80
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -80

                # cell 8
                if i == 1 and m == 3:
                    if (tempBoard[i][m][1] == tempBoard[i + 1][m - 1][1] and tempBoard[i + 1][m - 1][1] ==
                            tempBoard[i + 2][m - 2][1]):
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i + 2][m - 3][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i - 1][m][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 95
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -95
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                tempBoard[i + 2][m - 3][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                tempBoard[i - 1][m][1] == 1 and tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][
                                    0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 85
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -85
                        if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                tempBoard[i - 1][m][1] == 1 and tempBoard[i + 2][m - 3][0] == 1):
                            if tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3:
                                return 90
                            if tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5:
                                return -90
            if tempBoard[i][m][1] == 1:
                if (tempBoard[i][m][0] == 6 or tempBoard[i][m][0] == 7 or tempBoard[i][m][0] == 10 or tempBoard[i][m][
                    0] == 11):
                    return 50
                else:
                    return 25

    return 0


def secondEvaluation(board):
    for k in board.keys():
        if board[k] != 1:
            if k == 1:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 5] and board[k + 5] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                if board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                if board[k] == board[k + 5] and board[k + 5] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50

            elif k == 2:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 5] and board[k + 5] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                if board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                if board[k] == board[k + 5] or board[k + 5] == board[k + 10] or board[k] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
            elif k == 3:
                if board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 3] and board[k + 3] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 3] or board[k + 3] == board[k + 6] or board[k] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
            elif k == 4:
                if board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 3] and board[k + 3] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 3] or board[k + 3] == board[k + 6] or board[k] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
            elif k == 5:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 5] and board[k + 5] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 5] or board[k + 5] == board[k + 10] or board[k] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50

            elif k == 6:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 5] and board[k + 5] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 5] or board[k + 5] == board[k + 10] or board[k] == board[k + 10]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
            elif k == 7:
                if board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 3] and board[k + 3] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 3] or board[k + 3] == board[k + 6] or board[k] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
            elif k == 8:
                if board[k] == board[k + 4] and board[k + 4] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                elif board[k] == board[k + 3] and board[k + 3] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 4] or board[k + 4] == board[k + 8] or board[k] == board[k + 8]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
                elif board[k] == board[k + 3] or board[k + 3] == board[k + 6] or board[k] == board[k + 6]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
            elif k == 9:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
            elif k == 10:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50

            elif k == 13:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50

            elif k == 14:
                if board[k] == board[k + 1] and board[k + 1] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 100
                    if board[k] == 4 or board[k] == 5:
                        return -100
                if board[k] == board[k + 1] or board[k + 1] == board[k + 2] or board[k] == board[k + 2]:
                    if board[k] == 2 or board[k] == 3:
                        return 50
                    if board[k] == 4 or board[k] == 5:
                        return -50
    return 0


# minimax
maxDepth = 2


def maxMove(board, depth, alpha, beta, player):
    move = [0, 0, 0, 0, 0]
    if depth == maxDepth or isTerminal(board) == 1 or isTerminal(board) == -1:
        if player == "smartOne":
            move[4] = firstEvaluation(board)
        if player == "smartTwo":
            move[4] = secondEvaluation(board)
        return move
    bestMove = [0, 0, 0, 0, alpha]
    colors = [2, 3]
    for k in board.keys():
        if board[k] == 4 or board[k] == 5:
            adjacentCells = [k + 1, k - 1, k + 4, k - 4]
            for i in adjacentCells:
                if isValidFlip(board, k, i) == 1:
                    flipTile(board, k, i)
                    for v in board.keys():
                        if board[v] == 1:
                            for j in colors:
                                if isValidCell(board, v) == 1:
                                    placeTile(board, v, j)
                                    move = minMove(board, depth + 1, bestMove[4], beta, player)
                                    board[v] = 1
                                    if move[4] > bestMove[4]:
                                        bestMove[4] = move[4]
                                        cellFrom = k
                                        cellTo = i
                                        cell = v
                                        color = j
                                        bestMove = [cellFrom, cellTo, cell, color, bestMove[4]]
                                        if move[4] > beta:
                                            bestMove[4] = beta
                                            break
                    if isValidFlip(board, i, k) == 1:
                        flipTile(board, i, k)

    return bestMove


def minMove(board, depth, alpha, beta, player):
    move = [0, 0, 0, 0, 0]
    if depth == maxDepth or isTerminal(board) == 1 or isTerminal(board) == -1:
        if player == "smartOne":
            move[4] = firstEvaluation(board)
        if player == "smartTwo":
            move[4] = secondEvaluation(board)
        return move
    bestMove = [0, 0, 0, 0, beta]
    colors = [4, 5]
    for k in board.keys():
        if board[k] == 2 or board[k] == 3:
            adjacentCells = [k + 1, k - 1, k + 4, k - 4]
            for i in adjacentCells:
                if isValidFlip(board, k, i) == 1:
                    flipTile(board, k, i)
                    for v in board.keys():
                        if board[v] == 1:
                            for j in colors:
                                if isValidCell(board, v) == 1:
                                    placeTile(board, v, j)
                                    move = maxMove(board, depth + 1, alpha, bestMove[4], player)
                                    board[v] = 1
                                    if move[4] < bestMove[4]:
                                        bestMove[4] = move[4]
                                        cellFrom = k
                                        cellTo = i
                                        cell = v
                                        color = j
                                        bestMove = [cellFrom, cellTo, cell, color, bestMove[4]]
                                        if move[4] < alpha:
                                            bestMove[4] = alpha
                                            break
                    if isValidFlip(board, i, k) == 1:
                        flipTile(board, i, k)

    return bestMove


def maxFirstMove(board, depth, alpha, beta, player):
    move = [0, 0, 0]
    if depth == maxDepth or isTerminal(board) == 1 or isTerminal(board) == -1:
        if player == "smartOne":
            move[2] = firstEvaluation(board)
        if player == "smartTwo":
            move[2] = secondEvaluation(board)
        return move
    bestMove = [0, 0, alpha]
    colors = [2, 3]
    for v in board.keys():
        if board[v] == 1:
            for j in colors:
                if isValidCell(board, v) == 1:
                    placeTile(board, v, j)
                    move = minFirstMove(board, depth + 1, bestMove[2], beta, player)
                    board[v] = 1
                    if move[2] > bestMove[2]:
                        bestMove[2] = move[2]
                        cell = v
                        color = j
                        bestMove = [cell, color, bestMove[2]]
                        if move[2] > beta:
                            bestMove[2] = beta
                            return bestMove
    return bestMove


def minFirstMove(board, depth, alpha, beta, player):
    move = [0, 0, 0]
    if depth == maxDepth or isTerminal(board) == 1 or isTerminal(board) == -1:
        if player == "smartOne":
            move[2] = firstEvaluation(board)
        if player == "smartTwo":
            move[2] = secondEvaluation(board)
        return move
    bestMove = [0, 0, beta]
    colors = [4, 5]
    for v in board.keys():
        if board[v] == 1:
            for j in colors:
                if isValidCell(board, v) == 1:
                    placeTile(board, v, j)
                    move = maxFirstMove(board, depth + 1, alpha, bestMove[2], player)
                    board[v] = 1
                    if move[2] < bestMove[2]:
                        bestMove[2] = move[2]
                        cell = v
                        color = j
                        bestMove = [cell, color, bestMove[2]]
                        if move[2] < alpha:
                            bestMove[2] = alpha
                            return bestMove
    return bestMove


# game loop
def gamePlay(initialBoard, playerOne, playerTwo):
    board = copy.deepcopy(initialBoard)
    turn = playerOne
    for i in range(16):
        if i == 0:
            if turn == "user":
                print(
                    "Player One, your tiles are red and blue(2 for red and 3 for blue)\nPlayer One you get to go first\n")
                cell = pyip.inputInt(
                    "Player One, please enter the cell where you would like to place your first tile\n", min=1, max=16)
                color = pyip.inputInt("Player one, please enter the color you want facing up for your first tile\n",
                                      min=2, max=3)
                if isValidCell(board, cell) == 1:
                    placeTile(board, cell, color)
                    turn = playerTwo
                    continue

            if turn == "random":
                print("Player One gets to go first, random's tiles are red and blue\n")
                cell = pickRandomCell(board)
                color = rd.randint(2, 3)
                if isValidCell(board, cell) == 1:
                    placeTile(board, cell, color)
                    turn = playerTwo
                    continue

            if turn == "smartOne":
                print("Player One gets to go first, smartOne's tiles are red and blue\n")
                cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartOne")
                if isValidCell(board, cell) == 1:
                    placeTile(board, cell, color)
                    turn = playerTwo
                    continue

            if turn == "smartTwo":
                print("Player One gets to go first, smartTwo's tiles are red and blue\n")
                cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartTwo")
                if isValidCell(board, cell) == 1:
                    placeTile(board, cell, color)
                    turn = playerTwo
                    continue

        elif i == 15:
            if turn == playerTwo:
                if playerTwo == "user":
                    if noValidFlip(board, "yellowWhite") == 1:
                        print("There are no valid flip moves\n")
                        cell = pyip.inputInt(
                            "Player Two, please enter the cell where you would like to place your last tile\n1-16\n",
                            min=1, max=16)
                        color = pyip.inputInt(
                            "Player Two, please enter the color you want facing up for your last tile\n4 for yellow and 5 for white\n",
                            min=4, max=5)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("the game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            elif isTerminal(board) == 0:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                    else:
                        cellFrom = pyip.inputInt(
                            "Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",
                            min=1, max=16)
                        cellTo = pyip.inputInt(
                            "Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",
                            min=1, max=16)
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            boardCopy = copy.deepcopy(board)
                            printBoard(boardCopy)
                            print("\n")
                            cell = pyip.inputInt(
                                "Player Two, please enter where you would like to place your last tile(1-16)\n", min=1,
                                max=16)
                            color = pyip.inputInt(
                                "Player Two please enter the color you want facing up for your last tile(4 for yellow, 5 for white)\n",
                                min=4, max=5)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("the game is a draw with two winning lines")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                elif isTerminal(board) == 0:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                            else:
                                print("You can't place a tile in this cell\n try again\n")
                                cell = pyip.inputInt(
                                    "Player Two, please enter where you would like to place your last tile(1-16)\n",
                                    min=1, max=16)
                                color = pyip.inputInt(
                                    "Player Two please enter the color you want facing up for your last tile(4 for yellow, 5 for white)\n",
                                    min=4, max=5)
                        else:
                            print("That's not a valid flip move\nplease try again\n")
                            cellFrom = pyip.inputInt(
                                "Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",
                                min=1, max=16)
                            cellTo = pyip.inputInt(
                                "Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",
                                min=1, max=16)

                if playerTwo == "random":
                    if noValidFlip(board, "yellowWhite") == 1:
                        print("There are no valid flip moves")
                        cell = pickRandomCell(board)
                        color = rd.randint(4, 5)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("the game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            elif isTerminal(board) == 0:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            turn = playerOne
                    else:
                        cellFrom, cellTo = randomFlipMove(board, "yellowWhite")
                        while isValidFlip(board, cellFrom, cellTo) != 1:
                            cellFrom, cellTo = randomFlipMove(board, "yellowWhite")
                        flipTile(board, cellFrom, cellTo)
                        cell = pickRandomCell(board)
                        color = rd.randint(4, 5)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            elif isTerminal(board) == 0:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            turn = playerOne
                            continue

                if playerTwo == "smartOne":
                    if noValidFlip(board, "yellowWhite") == 1:
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartOne")
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            elif isTerminal(board) == 0:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            turn = playerOne
                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartOne")
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                elif isTerminal(board) == 0:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                                turn = playerOne
                if playerTwo == "smartTwo":
                    if noValidFlip(board, "yellowWhite") == 1:
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartTwo")
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            elif isTerminal(board) == 0:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            turn = playerOne
                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartTwo")
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                elif isTerminal(board) == 0:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                                turn = playerOne


        else:
            if turn == playerOne:
                if playerOne == "user":
                    if noValidFlip(board, "redBlue") == 1:
                        print("There are no valid flip moves\n")
                        cell = pyip.inputInt(
                            "Player One, please enter the cell where you would like to place your tile\n1-16", min=1,
                            max=16)
                        color = pyip.inputInt(
                            "Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",
                            min=2, max=3)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerTwo
                            continue

                        else:
                            print("That's not a valid cell, try again\n")
                            cell = pyip.inputInt(
                                "Player One, please enter the cell where you would like to place your tile\n1-16\n",
                                min=1, max=16)
                            color = pyip.inputInt(
                                "Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",
                                min=2, max=3)
                    else:
                        cellFrom = pyip.inputInt(
                            "Player One, please enter the cell you would like to flip your opponent's tile from\n1-16\n",
                            min=1, max=16)
                        cellTo = pyip.inputInt(
                            "Player One,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",
                            min=1, max=16)
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            boardCopy = copy.deepcopy(board)
                            printBoard(boardCopy)
                            print("\n")
                            cell = pyip.inputInt(
                                "Player One, please enter where you would like to place your tile\n1-16\n", min=1,
                                max=16)
                            color = pyip.inputInt(
                                "Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",
                                min=2, max=3)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw with two winning lines")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                turn = playerTwo
                                continue

                            else:
                                print("You can't place a tile in this cell,try again\n")
                                cell = pyip.inputInt(
                                    "Player One, please enter where you would like to place your tile\n1-16\n", min=1,
                                    max=16)
                                color = pyip.inputInt(
                                    "Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",
                                    min=2, max=3)
                        else:
                            print("That's not a valid flip move\nplease try again\n")
                            cellFrom = pyip.inputInt(
                                "Player One, please enter the cell you would like to flip your opponent's tile from\n1-16\n",
                                min=1, max=16)
                            cellTo = pyip.inputInt(
                                "Player One,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",
                                min=1, max=16)

                if playerOne == "random":
                    if noValidFlip(board, "redBlue") == 1:
                        # print("There are no valid flip moves")
                        cell = pickRandomCell(board)
                        color = rd.randint(2, 3)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerTwo
                            continue

                    else:
                        cellFrom, cellTo = randomFlipMove(board, "redBlue")
                        while isValidFlip(board, cellFrom, cellTo) != 1:
                            cellFrom, cellTo = randomFlipMove(board, "redBlue")
                        flipTile(board, cellFrom, cellTo)
                        cell = pickRandomCell(board)
                        color = rd.randint(2, 3)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw with two winiing lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerTwo
                            continue
                if playerOne == "smartOne":
                    if noValidFlip(board, "redBlue") == 1:
                        # print("There are no valid flip moves\n")
                        cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartOne")
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerTwo
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = maxMove(board, 0, -1000, 1000, "smartOne")
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                turn = playerTwo
                if playerOne == "smartTwo":
                    if noValidFlip(board, "redBlue") == 1:
                        # print("There are no valid flips")
                        cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartTwo")
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            elif isTerminal(board) == 1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player One has won the game", file = fileName )
                                return playerOne
                            elif isTerminal(board) == -1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player Two has won the game",file=fileName)
                                return playerTwo
                            turn = playerTwo
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = maxMove(board, 0, -1000, 1000, "smartTwo")
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("The game is a draw",file=fileName)
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player One has won the game", file = fileName)
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player Two has won the game",file=fileName)
                                    return playerTwo
                                turn = playerTwo
                                continue

            if turn == playerTwo:

                if playerTwo == "user":
                    if noValidFlip(board, "yellowWhite") == 1:
                        print("There are no valid flip moves\n")
                        cell = pyip.inputInt(
                            "Player Two, please enter the cell where you would like to place your tile\n1-16\n", min=1,
                            max=16)
                        color = pyip.inputInt(
                            "Player Two, please enter the color you want facing up for your tile\n4 for yellow and 5 for white\n",
                            min=4, max=5)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerOne
                            continue

                        else:
                            print("That's not a valid cell, try again\n")
                            cell = pyip.inputInt(
                                "Player Two, please enter the cell where you would like to place your tile\n1-16\n",
                                min=1, max=16)
                            color = pyip.inputInt(
                                "Player Two, please enter the color you want facing up for your tile\n4 for yellow and 5 for white\n",
                                min=4, max=5)
                    else:
                        cellFrom = pyip.inputInt(
                            "Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",
                            min=1, max=16)
                        cellTo = pyip.inputInt(
                            "Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",
                            min=1, max=16)
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            boardCopy = copy.deepcopy(board)
                            printBoard(boardCopy)
                            print("\n")
                            cell = pyip.inputInt(
                                "Player Two, please enter where you would like to place your tile\n(1-16)\n", min=1,
                                max=16)
                            color = pyip.inputInt(
                                "Player Two please enter the color you want facing up for your tile\n4 for yellow, 5 for white\n",
                                min=4, max=5)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw with two winning lines")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                turn = playerOne
                                continue

                            else:
                                print("You can't place a tile in this cell\n try again\n")
                                cell = pyip.inputInt(
                                    "Player Two, please enter where you would like to place your tile\n1-16\n", min=1,
                                    max=16)
                                color = pyip.inputInt(
                                    "Player Two please enter the color you want facing up for your tile\n4 for yellow, 5 for white\n",
                                    min=4, max=5)
                        else:
                            print("That's not a valid flip move\nplease try again\n")
                            cellFrom = pyip.inputInt(
                                "Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",
                                min=1, max=16)
                            cellTo = pyip.inputInt(
                                "Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",
                                min=1, max=16)

                if playerTwo == "random":
                    if noValidFlip(board, "yellowWhite") == 1:
                        # print("There are no valid flip moves\n")
                        cell = pickRandomCell(board)
                        color = rd.randint(4, 5)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                print("the game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerOne
                            continue


                    else:
                        cellFrom, cellTo = randomFlipMove(board, "yellowWhite")
                        while isValidFlip(board, cellFrom, cellTo) != 1:
                            cellFrom, cellTo = randomFlipMove(board, "yellowWhite")
                        flipTile(board, cellFrom, cellTo)
                        cell = pickRandomCell(board)
                        color = rd.randint(4, 5)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerOne
                            continue
                if playerTwo == "smartOne":
                    if noValidFlip(board, "yellowWhite") == 1:
                        # print("There are no valid flip moves\n")
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartOne")
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")

                              return playerOne
                            elif (isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerOne
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartOne")
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                turn = playerOne
                                continue

                if playerTwo == "smartTwo":
                    if noValidFlip(board, "yellowWhite") == 1:
                        # print("There are no valid flip moves\n")
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartTwo")
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif isTerminal(board) == 1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerOne
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartTwo")
                        if isValidFlip(board, cellFrom, cellTo) == 1:
                            flipTile(board, cellFrom, cellTo)
                            if isValidCell(board, cell) == 1:
                                placeTile(board, cell, color)
                                if isTerminal(board) == 1 and isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw")
                                    return "draw"
                                elif isTerminal(board) == 1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                turn = playerOne
                                continue


# to run user inputted players
gamePlay(initialBoard, playerOne, playerTwo)

# Four games where I played each of the AI's
# gamePlay(board,"user","smartOne","gameOne.txt")
# gamePlay(board,"smartOne","user","gameTwo.txt")
# gamePlay(board,"user","smartTwo","gameThree.txt")
# gamePlay(board,"smartTwo","user","gameFour.txt")


'''

#run 100 games between random and smartOne, smarttwo and random, and smartOne and SmartTwo


#smartOne vs random
winningListOne = []
for i in range(100):
    if(i < 50):
        temp = gamePlay(initialBoard,"random","smartOne")
        winningListOne.append(temp)
    else:
        temp = gamePlay(initialBoard,"smartOne","random")
        winningListOne.append(temp)



#smartTwo vs random
winningListTwo = []
for i in range(100):
    if(i<50):
        temp = gamePlay(initialBoard,"smartTwo","random")
        winningListTwo.append(temp)
    else:
        temp = gamePlay(initialBoard,"random","smartTwo")
        winningListTwo.append(temp)



#smartOne versus smartTwo
winningListThree = []
for i in range(100):
    if(i<50):
        temp = gamePlay(initialBoard,"smartTwo","smartOne")
        winningListThree.append(temp)
    else:
        temp = gamePlay(initialBoard,"smartOne","smartTwo")
        winningListThree.append(temp)


smartOneWins = 0
draw = 0
randomWins = 0
for i in winningListOne:
    if i == "smartOne":
        smartOneWins += 1
    if i == "draw":
        draw += 1
    if i == "random":
        randomWins += 1

with open('games.txt', 'a') as f:
    print('Over 100 games, Smart One won %d times, random won %d times, and there were %d draws\n'%(smartOneWins,randomWins,draw), file=f)

smartTwoWins = 0
draw = 0
randomWins = 0
for i in winningListTwo:
    if i == "smartTwo":
        smartTwoWins += 1
    if i == "draw":
        draw += 1
    if i == "random":
        randomWins += 1
with open('games.txt', 'a') as f:
    print('Over 100 games, Smart Two won %d times, random won %d times, and there were %d draws\n'%(smartTwoWins,randomWins,draw), file=f)

smartTwoWins = 0
draw = 0
smartOneWins = 0
for i in winningListThree:
    if i == "smartTwo":
        smartTwoWins += 1
    if i == "draw":
        draw += 1
    if i == "smartOne":
        smartOneWins += 1
with open('games.txt', 'a') as f:
    print('Over 100 games, Smart Two won %d times, Smart One won %d times, and there were %d draws\n'%(smartTwoWins,smartOneWins,draw), file=f)

f.close()
'''