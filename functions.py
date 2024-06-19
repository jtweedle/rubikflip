import copy


def gamePlay(initialBoard, playerOne, playerTwo):
    board = copy.deepcopy(initialBoard)
    turn = playerOne
    for i in range(16):
        boardCopy = copy.deepcopy(board)
        printBoard(boardCopy)
        print()
        print(i)
        print(turn)
        print()
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
                # print("Player One gets to go first, random's tiles are red and blue\n")
                cell = pickRandomCell(board)
                color = rd.randint(2, 3)
                if isValidCell(board, cell) == 1:
                    placeTile(board, cell, color)
                    turn = playerTwo
                    continue

            if turn == "smartOne":
                # print("Player One gets to go first, smartOne's tiles are red and blue\n")
                cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartOne")
                if isValidCell(board, cell) == 1:
                    placeTile(board, cell, color)
                    turn = playerTwo
                    continue

            if turn == "smartTwo":
                # print("Player One gets to go first, smartTwo's tiles are red and blue\n")
                cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartTwo")
                if isValidCell(board, cell) == 1:
                    placeTile(board, cell, color)
                    turn = playerTwo
                    continue

        elif i == 15:
            if turn == playerTwo:
                '''if(playerTwo == "user"):
                    if(noValidFlip(board,"yellowWhite") == 1):
                        print("There are no valid flip moves\n")
                        cell = pyip.inputInt("Player Two, please enter the cell where you would like to place your last tile\n1-16\n",min = 1, max = 16)
                        color = pyip.inputInt("Player Two, please enter the color you want facing up for your last tile\n4 for yellow and 5 for white\n",min = 4, max= 5)
                        if(isValidCell(board,cell) == 1):
                            placeTile(board,cell,color)
                            if(isTerminal(board) == 1 and isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("the game is a draw with two winning lines")
                                return "draw"
                            elif(isTerminal(board) == 1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif(isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            elif(isTerminal(board) == 0):
                                #boardCopy = copy.deepcopy(board)
                                #printBoard(boardCopy,fileName)
                                #print("The game is a draw",file=fileName)
                                return "draw"
                    else:
                        cellFrom = pyip.inputInt("Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",min=1,max=16)
                        cellTo = pyip.inputInt("Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",min=1,max=16)
                        if(isValidFlip(board,cellFrom,cellTo) == 1):
                            flipTile(board,cellFrom,cellTo)
                            boardCopy = copy.deepcopy(board)
                            printBoard(boardCopy)
                            print("\n")
                            cell = pyip.inputInt("Player Two, please enter where you would like to place your last tile(1-16)\n",min=1,max=16)
                            color = pyip.inputInt("Player Two please enter the color you want facing up for your last tile(4 for yellow, 5 for white)\n",min=4,max=5)
                            if(isValidCell(board,cell) == 1):
                                placeTile(board,cell,color)
                                if(isTerminal(board) == 1 and isTerminal(board) == -1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("the game is a draw with two winning lines")
                                    return "draw"
                                elif(isTerminal(board) == 1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif(isTerminal(board) == -1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                elif(isTerminal(board) == 0):
                                    #boardCopy = copy.deepcopy(board)
                                    #printBoard(boardCopy,fileName)
                                    #print("The game is a draw",file=fileName)
                                    return "draw"
                            else:
                                print("You can't place a tile in this cell\n try again\n")
                                cell = pyip.inputInt("Player Two, please enter where you would like to place your last tile(1-16)\n",min=1,max=16)
                                color = pyip.inputInt("Player Two please enter the color you want facing up for your last tile(4 for yellow, 5 for white)\n",min=4,max=5)
                        else:
                            print("That's not a valid flip move\nplease try again\n")
                            cellFrom = pyip.inputInt("Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",min=1,max=16)
                            cellTo = pyip.inputInt("Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",min=1,max=16)'''

                if playerTwo == "random":
                    if noValidFlip(board, "yellowWhite") == 1:
                        # print("There are no valid flip moves")
                        cell = pickRandomCell(board)
                        color = rd.randint(4, 5)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy)
                                # print("the game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy)
                                # print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy)
                                # print("Player Two has won the game")
                                return playerTwo
                            elif isTerminal(board) == 0:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            turn = playerOne
                    else:
                        while True:
                            cellFrom, cellTo = randomFlipMove(board, "yellowWhite")
                            if isValidFlip(board, cellFrom, cellTo) == 1:
                                flipTile(board, cellFrom, cellTo)
                                cell = pickRandomCell(board)
                                color = rd.randint(4, 5)
                                if isValidCell(board, cell) == 1:
                                    placeTile(board, cell, color)
                                    if isTerminal(board) == 1 and isTerminal(board) == -1:
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("The game is a draw with two winning lines")
                                        return "draw"
                                    elif isTerminal(board) == 1:
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("Player One has won the game")
                                        return playerOne
                                    elif isTerminal(board) == -1:
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("Player Two has won the game")
                                        return playerTwo
                                    elif isTerminal(board) == 0:
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy,fileName)
                                        # print("The game is a draw",file=fileName)
                                        return "draw"
                                    turn = playerOne
                                    break

                if playerTwo == "smartOne":
                    if noValidFlip(board, "yellowWhite") == 1:
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartOne")
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            elif (isTerminal(board) == 1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player One has won the game",file=fileName)
                                return playerOne
                            elif (isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player Two has won the game",file=fileName)
                                return playerTwo
                            elif (isTerminal(board) == 0):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            turn = playerOne
                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartOne")
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
                                    # print("Player One has won the game",file=fileName)
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player Two has won the game",file=fileName)
                                    return playerTwo
                                elif isTerminal(board) == 0:
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("The game is a draw",file=fileName)
                                    return "draw"
                                turn = playerOne
                if playerTwo == "smartTwo":
                    if noValidFlip(board, "yellowWhite") == 1:
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartTwo")
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
                                # print("Player One has won the game",file=fileName)
                                return playerOne
                            elif isTerminal(board) == -1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player Two has won the game",file=fileName)
                                return playerTwo
                            elif isTerminal(board) == 0:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            turn = playerOne
                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartTwo")
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
                                    # print("Player One has won the game",file=fileName)
                                    return playerOne
                                elif isTerminal(board) == -1:
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player Two has won the game",file=fileName)
                                    return playerTwo
                                elif isTerminal(board) == 0:
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("The game is a draw",file=fileName)
                                    return "draw"
                                turn = playerOne


        else:
            if turn == playerOne:
                '''if(playerOne == "user"):
                    if(noValidFlip(board,"redBlue") == 1):
                        print("There are no valid flip moves\n")
                        cell = pyip.inputInt("Player One, please enter the cell where you would like to place your tile\n1-16",min = 1, max = 16)
                        color = pyip.inputInt("Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",min = 2, max= 3)
                        if(isValidCell(board,cell) == 1):
                            placeTile(board,cell,color)
                            if(isTerminal(board) == 1 and isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif(isTerminal(board) == 1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif(isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerTwo
                            continue
                            
                        else:
                            print("That's not a valid cell, try again\n")
                            cell = pyip.inputInt("Player One, please enter the cell where you would like to place your tile\n1-16\n",min = 1, max = 16)
                            color = pyip.inputInt("Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",min = 2, max= 3)
                    else:
                        cellFrom = pyip.inputInt("Player One, please enter the cell you would like to flip your opponent's tile from\n1-16\n",min=1,max=16)
                        cellTo = pyip.inputInt("Player One,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",min=1,max=16)
                        if(isValidFlip(board,cellFrom,cellTo) == 1):
                            flipTile(board,cellFrom,cellTo)
                            boardCopy = copy.deepcopy(board)
                            printBoard(boardCopy)
                            print("\n")
                            cell = pyip.inputInt("Player One, please enter where you would like to place your tile\n1-16\n",min=1,max=16)
                            color = pyip.inputInt("Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",min=2,max=3)
                            if(isValidCell(board,cell) == 1):
                                placeTile(board,cell,color)
                                if(isTerminal(board) == 1 and isTerminal(board) == -1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw with two winning lines")
                                    return "draw"
                                elif(isTerminal(board) == 1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif(isTerminal(board) == -1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                turn = playerTwo
                                continue
                                
                            else:
                                print("You can't place a tile in this cell,try again\n")
                                cell = pyip.inputInt("Player One, please enter where you would like to place your tile\n1-16\n",min=1,max=16)
                                color = pyip.inputInt("Player One, please enter the color you want facing up for your tile\n2 for red and 3 for blue\n",min=2,max=3)
                        else:
                            print("That's not a valid flip move\nplease try again\n")
                            cellFrom = pyip.inputInt("Player One, please enter the cell you would like to flip your opponent's tile from\n1-16\n",min=1,max=16)
                            cellTo = pyip.inputInt("Player One,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",min=1,max=16)'''

                if playerOne == "random":
                    if noValidFlip(board, "redBlue") == 1:
                        print("There are no valid flip moves")
                        cell = pickRandomCell(board)
                        color = rd.randint(2, 3)
                        if isValidCell(board, cell) == 1:
                            placeTile(board, cell, color)
                            if isTerminal(board) == 1 and isTerminal(board) == -1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy)
                                # print("The game is a draw with two winning lines")
                                return "draw"
                            elif isTerminal(board) == 1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy)
                                # print("Player One has won the game")
                                return playerOne
                            elif isTerminal(board) == -1:
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy)
                                # print("Player Two has won the game")
                                return playerTwo
                            turn = playerTwo
                            continue

                    else:
                        while True:
                            cellFrom, cellTo = randomFlipMove(board, "redBlue")
                            print(cellFrom, cellTo)
                            print()
                            if (isValidFlip(board, cellFrom, cellTo) == 1):
                                flipTile(board, cellFrom, cellTo)
                                cell = pickRandomCell(board)
                                color = rd.randint(2, 3)
                                if (isValidCell(board, cell) == 1):
                                    placeTile(board, cell, color)
                                    if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("The game is a draw with two winiing lines")
                                        return "draw"
                                    elif (isTerminal(board) == 1):
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("Player One has won the game")
                                        return playerOne
                                    elif (isTerminal(board) == -1):
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("Player Two has won the game")
                                        return playerTwo
                                    turn = playerTwo
                                    break
                                continue
                if (playerOne == "smartOne"):
                    if (noValidFlip(board, "redBlue") == 1):
                        # print("There are no valid flip moves\n")
                        cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartOne")
                        if (isValidCell(board, cell) == 1):
                            placeTile(board, cell, color)
                            if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            elif (isTerminal(board) == 1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player One has won the game", file = fileName)
                                return playerOne
                            elif (isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player Two has won the game",file=fileName)
                                return playerTwo
                            turn = playerTwo
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = maxMove(board, 0, -1000, 1000, "smartOne")
                        if (isValidFlip(board, cellFrom, cellTo) == 1):
                            flipTile(board, cellFrom, cellTo)
                            if (isValidCell(board, cell) == 1):
                                placeTile(board, cell, color)
                                if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("The game is a draw",file=fileName)
                                    return "draw"
                                elif (isTerminal(board) == 1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player One has won the game", file = fileName)
                                    return playerOne
                                elif (isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player Two has won the game",file=fileName)
                                    return playerTwo
                                turn = playerTwo
                if (playerOne == "smartTwo"):
                    if (noValidFlip(board, "redBlue") == 1):
                        # print("There are no valid flips")
                        cell, color, _ = maxFirstMove(board, 0, -1000, 1000, "smartTwo")
                        if (isValidCell(board, cell) == 1):
                            placeTile(board, cell, color)
                            if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            elif (isTerminal(board) == 1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player One has won the game", file = fileName )
                                return playerOne
                            elif (isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player Two has won the game",file=fileName)
                                return playerTwo
                            turn = playerTwo
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = maxMove(board, 0, -1000, 1000, "smartTwo")
                        if (isValidFlip(board, cellFrom, cellTo) == 1):
                            flipTile(board, cellFrom, cellTo)
                            if (isValidCell(board, cell) == 1):
                                placeTile(board, cell, color)
                                if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("The game is a draw",file=fileName)
                                    return "draw"
                                elif (isTerminal(board) == 1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player One has won the game", file = fileName)
                                    return playerOne
                                elif (isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player Two has won the game",file=fileName)
                                    return playerTwo
                                turn = playerTwo
                                continue

            if turn == playerTwo:

                '''if(playerTwo == "user"):
                    if(noValidFlip(board,"yellowWhite") == 1):
                        print("There are no valid flip moves\n")
                        cell = pyip.inputInt("Player Two, please enter the cell where you would like to place your tile\n1-16\n",min = 1, max = 16)
                        color = pyip.inputInt("Player Two, please enter the color you want facing up for your tile\n4 for yellow and 5 for white\n",min = 4, max= 5)
                        if(isValidCell(board,cell) == 1):
                            placeTile(board,cell,color)
                            if(isTerminal(board) == 1 and isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("The game is a draw")
                                return "draw"
                            elif(isTerminal(board) == 1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player One has won the game")
                                return playerOne
                            elif(isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Player Two has won the game")
                                return playerTwo
                            turn = playerOne
                            continue
                            
                        else:
                            print("That's not a valid cell, try again\n")
                            cell = pyip.inputInt("Player Two, please enter the cell where you would like to place your tile\n1-16\n",min = 1, max = 16)
                            color = pyip.inputInt("Player Two, please enter the color you want facing up for your tile\n4 for yellow and 5 for white\n",min = 4, max= 5)
                    else:
                        cellFrom = pyip.inputInt("Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",min=1,max=16)
                        cellTo = pyip.inputInt("Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",min=1,max=16)
                        if(isValidFlip(board,cellFrom,cellTo) == 1):
                            flipTile(board,cellFrom,cellTo)
                            boardCopy = copy.deepcopy(board)
                            printBoard(boardCopy)
                            print("\n")
                            cell = pyip.inputInt("Player Two, please enter where you would like to place your tile\n(1-16)\n",min=1,max=16)
                            color = pyip.inputInt("Player Two please enter the color you want facing up for your tile\n4 for yellow, 5 for white\n",min=4,max=5)
                            if(isValidCell(board,cell) == 1):
                                placeTile(board,cell,color)
                                if(isTerminal(board) == 1 and isTerminal(board) == -1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("The game is a draw with two winning lines")
                                    return "draw"
                                elif(isTerminal(board) == 1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player One has won the game")
                                    return playerOne
                                elif(isTerminal(board) == -1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Player Two has won the game")
                                    return playerTwo
                                turn = playerOne
                                continue
                                
                            else:
                                print("You can't place a tile in this cell\n try again\n")
                                cell = pyip.inputInt("Player Two, please enter where you would like to place your tile\n1-16\n",min=1,max=16)
                                color = pyip.inputInt("Player Two please enter the color you want facing up for your tile\n4 for yellow, 5 for white\n",min=4,max=5)
                        else:
                            print("That's not a valid flip move\nplease try again\n")
                            cellFrom = pyip.inputInt("Player Two, please enter the cell you would like to flip your opponent's tile from\n1-16\n",min=1,max=16)
                            cellTo = pyip.inputInt("Player Two,please enter the cell where you would like to flip your opponent's piece to\n1-16\n",min=1,max=16)'''

                if (playerTwo == "random"):
                    if (noValidFlip(board, "yellowWhite") == 1):
                        # print("There are no valid flip moves\n")
                        cell = pickRandomCell(board)
                        color = rd.randint(4, 5)
                        if (isValidCell(board, cell) == 1):
                            placeTile(board, cell, color)
                            if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                # print("the game is a draw with two winning lines")
                                return "draw"
                            elif (isTerminal(board) == 1):
                                # print("Player One has won the game")
                                return playerOne
                            elif (isTerminal(board) == -1):
                                # print("Player Two has won the game")
                                return playerTwo
                            turn = playerOne
                            continue


                    else:
                        while True:
                            cellFrom, cellTo = randomFlipMove(board, "yellowWhite")
                            if (isValidFlip(board, cellFrom, cellTo) == 1):
                                flipTile(board, cellFrom, cellTo)
                                cell = pickRandomCell(board)
                                color = rd.randint(4, 5)
                                if (isValidCell(board, cell) == 1):
                                    placeTile(board, cell, color)
                                    if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("The game is a draw with two winning lines")
                                        return "draw"
                                    elif (isTerminal(board) == 1):
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("Player One has won the game")
                                        return playerOne
                                    elif (isTerminal(board) == -1):
                                        # boardCopy = copy.deepcopy(board)
                                        # printBoard(boardCopy)
                                        # print("Player Two has won the game")
                                        return playerTwo
                                    turn = playerOne
                                    break
                if (playerTwo == "smartOne"):
                    if (noValidFlip(board, "yellowWhite") == 1):
                        # print("There are no valid flip moves\n")
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartOne")
                        if (isValidCell(board, cell) == 1):
                            placeTile(board, cell, color)
                            if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            elif (isTerminal(board) == 1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player One has won the game", file = fileName)
                                return playerOne
                            elif (isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player Two has won the game",file=fileName)
                                return playerTwo
                            turn = playerOne
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartOne")
                        if (isValidFlip(board, cellFrom, cellTo) == 1):
                            flipTile(board, cellFrom, cellTo)
                            if (isValidCell(board, cell) == 1):
                                placeTile(board, cell, color)
                                if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("The game is a draw",file=fileName)
                                    return "draw"
                                elif (isTerminal(board) == 1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player One has won the game", file = fileName)
                                    return playerOne
                                elif (isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player Two has won the game",file=fileName)
                                    return playerTwo
                                turn = playerOne
                                continue

                if (playerTwo == "smartTwo"):
                    if (noValidFlip(board, "yellowWhite") == 1):
                        # print("There are no valid flip moves\n")
                        cell, color, _ = minFirstMove(board, 0, -1000, 1000, "smartTwo")
                        if (isValidCell(board, cell) == 1):
                            placeTile(board, cell, color)
                            if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("The game is a draw",file=fileName)
                                return "draw"
                            elif (isTerminal(board) == 1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player One has won the game", file = fileName)
                                return playerOne
                            elif (isTerminal(board) == -1):
                                # boardCopy = copy.deepcopy(board)
                                # printBoard(boardCopy,fileName)
                                # print("Player Two has won the game",file=fileName)
                                return playerTwo
                            turn = playerOne
                            continue

                    else:
                        cellFrom, cellTo, cell, color, _ = minMove(board, 0, -1000, 1000, "smartTwo")
                        if (isValidFlip(board, cellFrom, cellTo) == 1):
                            flipTile(board, cellFrom, cellTo)
                            if (isValidCell(board, cell) == 1):
                                placeTile(board, cell, color)
                                if (isTerminal(board) == 1 and isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("The game is a draw",file=fileName)
                                    return "draw"
                                elif (isTerminal(board) == 1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player One has won the game", file = fileName)
                                    return playerOne
                                elif (isTerminal(board) == -1):
                                    # boardCopy = copy.deepcopy(board)
                                    # printBoard(boardCopy,fileName)
                                    # print("Player Two has won the game",file=fileName)
                                    return playerTwo
                                turn = playerOne
                                continue
                                '''
                                









































#gamePlay
turn = 1
color = rd.choice(tiles)
playerOneColor = "yellowWhite"
if playerOneColor == "redBlue":
    playerTwoColor = "yellowWhite"
else:
    playerTwoColor = "redBlue"


f = open("gameOne.txt","w")
for i in range(16):
    boardCopy = copy.deepcopy(board)
    printBoard(boardCopy)
    print("\n")
    if i == 0:
        if turn == 1:
            if playerOneColor == "redBlue":
                print("Player One, your tiles are red and blue(2 for red and 3 for blue)\n")
                cell = pyip.inputInt("Player One, you get to go first.\nPlease enter the cell where you like to place your first tile\n",min=1,max=16)
                color = pyip.inputInt("Player one, please choose the color you want facing up(2 for red, 3 for blue)\n",min=2,max=3)
                placeTile(board,cell,color)
                turn = 2      
            else:
                print("Player one, your tiles are yellow and white(4 for yellow and 5 for white)\n ")
                cell = pyip.inputInt("Player One, you get to go first.\nPlease enter the cell where you like to place your first tile\n",min=1,max=16)
                color = pyip.inputInt("Player one, please choose the color you want facing up(4 for yellow, 5 for white)\n",min=4,max=5)
                placeTile(board,cell,color)
                turn = 2
        else:
            if playerTwoColor == "redBlue":
                cell,color,_ = maxFirstMove(board,0,-1000,1000)
                if(isValidCell(board,cell) == 1):
                    placeTile(board,cell,color)
                    turn = 1 
            else:
                cell = pickRandomCell(board)
                color = rd.randint(4,5)
                placeTile(board,cell,color)
                turn = 1 
    else:
        if turn == 1:
            if playerOneColor == "redBlue":
                while True:
                    print("Player one, your tiles are red and blue(2 for red and 3 for blue)")
                    print("\n")
                    flipFromCell = pyip.inputInt("Player One, pick the cell where you would like to flip from\n",min=1,max=16)
                    flipToCell = pyip.inputInt("Player One, pick the cell where you like to flip to\n",min=1,max=16)
                    if(isValidFlip(board,flipFromCell,flipToCell) == 1):
                        flipTile(board,flipFromCell,flipToCell)
                        boardCopy = copy.deepcopy(board)
                        printBoard(boardCopy)
                        print("\n")
                        cell = pyip.inputInt("Player One, please enter the cell where you like to place your tile\n",min=1,max=16)
                        color = pyip.inputInt("Player one, please choose the color you want facing up(2 for red, 3 for blue)\n",min=2,max=3)
                        if(isValidCell(board,cell) == 1):
                            placeTile(board,cell,color)
                            turn = 2
                            if(isTerminal(board) == 1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Congratulations,Player one has won the game")
                                exit()
                            else:
                                break
                    elif(noValidFlip(board))
            else:
                while True:
                    print("Player one your tiles are yellow and white(4 for yellow and 5 for white)")
                    print("\n")
                    flipFromCell = pyip.inputInt("Player One, pick the cell where you would like to flip from\n",min=1,max=16)
                    flipToCell = pyip.inputInt("Player One, pick the cell where you like to flip to\n",min=1,max=16)
                    if(isValidFlip(board,flipFromCell,flipToCell) == 1):
                        flipTile(board,flipFromCell,flipToCell)
                        boardCopy = copy.deepcopy(board)
                        printBoard(boardCopy)
                        print("\n")
                        cell = pyip.inputInt("Player One, please enter the cell where you like to place your tile\n",min=1,max=16)
                        color = pyip.inputInt("Player one, please choose the color you want facing up(4 for yellow, 5 for white)\n",min=4,max=5)
                        if(isValidCell(board,cell) == 1):
                            placeTile(board,cell,color)
                            turn = 2
                            if(isTerminal(board) == -1):
                                boardCopy = copy.deepcopy(board)
                                printBoard(boardCopy)
                                print("Congratulations,Player one has won the game")
                                exit()
                            break
                        
        else:
            if playerTwoColor == "redBlue":
                while True:
                    if(noValidFlip(board,"redBlue") == 1):
                        print("There are no valid flips")
                        cell,color,_ = maxFirstMove(board,0,-1000,1000)
                        if(isValidCell(board,cell) == 1):
                            placeTile(board,cell,color)
                            turn = 1 
                    else:
                        fromCell,toCell,cell,color,_= maxMove(board,0,-1000,1000)
                        if(isValidFlip(board,fromCell,toCell) == 1):
                            flipTile(board,fromCell,toCell) 
                            if(isValidCell(board,cell) == 1):
                                placeTile(board,cell,color)
                                turn = 1
                                if(isTerminal(board) == 1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy,file = f)
                                    print("Congratulations,Player Two has won the game")
                                    exit()
                                break
            else:
                while True:
                    if(noValidFlip(board,"yellowWhite") == 1):
                        print("There are no valid flips")
                        cell,color,_ = minFirstMove(board,0,-1000,1000)
                        if(isValidCell(board,cell) == 1):
                            placeTile(board,cell,color)
                            turn = 1 
                    
                    else:
                        flipFromCell, flipToCell = randomFlipMove(board,playerTwoColor)
                        if(isValidFlip(board,flipFromCell,flipToCell) == 1):
                            flipTile(board,flipFromCell,flipToCell)
                            cell = pickRandomCell(board)
                            color = rd.randint(4,5)
                            if(isValidCell(board,cell) == 1):
                                placeTile(board,cell,color)
                                turn = 1
                                if(isTerminal(board) == -1):
                                    boardCopy = copy.deepcopy(board)
                                    printBoard(boardCopy)
                                    print("Congratulations,Player two has won the game")
                                    exit()
                                break
    if(i == 16 and isTerminal(board) == 0):
        print("The game is a tie")


 

stdoutOrigin=sys.stdout 
sys.stdout = open("gameOne.txt", "w")
sys.stdout.close()
sys.stdout=stdoutOrigin
































'''  # Cell 1
                    if i == 0 and m == 0:
                        if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] ==
                                tempBoard[i][m + 2][1]):
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 or
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 0):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    # Cell 2
                    if i == 0 and m == 1:
                        if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] ==
                                tempBoard[i][m + 2][1]):
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    # cell 5 or cell 9
                    if i == 1 and m == 0 or i == 2 and m == 0:
                        if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] ==
                                tempBoard[i][m + 2][1]):
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 or
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 75
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -75
                            if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80

                    # Cell 6 or Cell 10
                    if i == 1 and m == 1 or i == 2 and m == 1:
                        if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] ==
                                tempBoard[i][m + 2][1]):
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 or
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i + 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 75
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -75
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80

                    # Cell 13
                    if i == 3 and m == 0:
                        if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] ==
                                tempBoard[i][m + 2][1]):
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 or
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 0):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i][m + 3][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    # cell 14
                    if i == 0 and m == 1:
                        if (tempBoard[i][m][1] == tempBoard[i][m + 1][1] and tempBoard[i][m + 1][1] ==
                                tempBoard[i][m + 2][1]):
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m + 1][0], tempBoard[i - 1][m + 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i][m + 2][0], tempBoard[i - 1][m + 2][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    # check three in a column with the same value

                    # cell 1
                    if i == 0 and m == 0:
                        if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] ==
                                tempBoard[i + 2][m][1]):
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 0):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    # cell 2 or Cell 3
                    if i == 0 and m == 1 or i == 0 and m == 2:
                        if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] ==
                                tempBoard[i + 2][m][1]):
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 75
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -75
                            if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80

                    # cell 4
                    if i == 0 and m == 3:
                        if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] ==
                                tempBoard[i + 2][m][1]):
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 0):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 3][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    # cell 5
                    if i == 1 and m == 0:
                        if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] ==
                                tempBoard[i + 2][m][1]):
                            if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 0):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    # cell 6 or cell 7
                    if i == 1 and m == 1 or i == 1 and m == 2:
                        if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] ==
                                tempBoard[i + 2][m][1]):
                            if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 75
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -75
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80

                    # Cell 8:
                    if i == 1 and m == 3:
                        if (tempBoard[i][m][1] == tempBoard[i + 1][m][1] and tempBoard[i + 1][m][1] ==
                                tempBoard[i + 2][m][1]):
                            if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 2][m][0], tempBoard[i + 2][m - 1][0]) != 1 or
                                    isValidFlip(board, tempBoard[i + 1][m][0], tempBoard[i + 1][m - 1][0]) != 0):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i + 2][m + 3][1] == 1 and tempBoard[i + 3][m + 2][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m][0]) != 1 and
                                    tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                    tempBoard[i + 2][m + 3][1] == 1 and tempBoard[i + 3][m + 2][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80
                            if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                    tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                    tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                    tempBoard[i + 3][m + 2][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 3][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][
                                        1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i + 3][m + 2][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i - 1][m][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                    tempBoard[i + 2][m + 3][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 3][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i - 1][m][1] == 1 and tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][
                                        1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i - 1][m][1] == 1 and tempBoard[i + 2][m + 3][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m + 1][0], tempBoard[i + 1][m][0]) != 1 and
                                    tempBoard[i + 2][m + 1][1] == 1 and tempBoard[i + 1][m + 2][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    tempBoard[i + 1][m + 2][1] == 1 and tempBoard[i + 2][m + 1][1] == 1 and
                                    tempBoard[i + 1][m][1] == 1 and tempBoard[i][m + 1][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80
                            if (isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 1][m + 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m + 2][0], tempBoard[i + 2][m + 1][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1 and
                                    tempBoard[i][m + 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    tempBoard[i][m + 1][0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                    tempBoard[i + 3][m - 2][0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                    tempBoard[i][m + 1][1] == 1 and tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][
                                        0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    tempBoard[i][m + 1][1] == 1 and tempBoard[i + 3][m - 2][0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                    tempBoard[i + 2][m - 3][1] == 1 and tempBoard[i + 3][m - 1][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80
                            if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 3][m - 2][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1 and
                                    tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][1]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m + 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -80
                            if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i - 1][m][1] == 1 and
                                    tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][1] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 80
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
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
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    tempBoard[i - 1][m][0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 95
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -95
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i - 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    tempBoard[i + 1][m - 2][1] == 1 and tempBoard[i + 2][m - 1][1] == 1 and
                                    tempBoard[i + 2][m - 3][0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 2][m - 2][0], tempBoard[i + 2][m - 3][0]) != 1 and
                                    tempBoard[i - 1][m][1] == 1 and tempBoard[i][m - 1][1] == 1 and tempBoard[i + 1][m][
                                        0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 85
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -85
                            if (isValidFlip(board, tempBoard[i][m][0], tempBoard[i][m - 1][0]) != 1 and
                                    isValidFlip(board, tempBoard[i][m][0], tempBoard[i + 1][m][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 1][m - 2][0]) != 1 and
                                    isValidFlip(board, tempBoard[i + 1][m - 1][0], tempBoard[i + 2][m - 1][0]) != 1 and
                                    tempBoard[i - 1][m][1] == 1 and tempBoard[i + 2][m - 3][0] == 1):
                                if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                                    return 90
                                if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                                    return -90

                    if (tempBoard[i][m][1] == 2 and tempBoard[i][m][0] == 6 or
                            tempBoard[i][m][1] == 2 and tempBoard[i][m][0] == 7 or
                            tempBoard[i][m][1] == 2 and tempBoard[i][m][0] == 10 or
                            tempBoard[i][m][1] == 2 and tempBoard[i][m][0] == 11 or
                            tempBoard[i][m][1] == 3 and tempBoard[i][m][0] == 6 or
                            tempBoard[i][m][1] == 3 and tempBoard[i][m][0] == 7 or
                            tempBoard[i][m][1] == 3 and tempBoard[i][m][0] == 10 or
                            tempBoard[i][m][1] == 3 and tempBoard[i][m][0] == 11):
                        return 50
                    if (tempBoard[i][m][1] == 4 and tempBoard[i][m][0] == 6 or
                            tempBoard[i][m][1] == 4 and tempBoard[i][m][0] == 7 or
                            tempBoard[i][m][1] == 4 and tempBoard[i][m][0] == 10 or
                            tempBoard[i][m][1] == 4 and tempBoard[i][m][0] == 11 or
                            tempBoard[i][m][1] == 5 and tempBoard[i][m][0] == 6 or
                            tempBoard[i][m][1] == 5 and tempBoard[i][m][0] == 7 or
                            tempBoard[i][m][1] == 5 and tempBoard[i][m][0] == 10 or
                            tempBoard[i][m][1] == 5 and tempBoard[i][m][0] == 11):
                        return -50

                    if (tempBoard[i][m][1] == 2 or tempBoard[i][m][1] == 3):
                        return 25
                    if (tempBoard[i][m][1] == 4 or tempBoard[i][m][1] == 5):
                        return -25
                if tempBoard[i][m][1] == 1:

                    # cell 1
                    if (i == 0 and m == 0):
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m + 1][1] == 2 or tempBoard[i + 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m + 1][1] == 4 or tempBoard[i + 1][m + 1][1] == 5):
                            return -30

                    # cell 2
                    if (i == 0 and m == 1):
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m + 1][1] == 2 or tempBoard[i + 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m + 1][1] == 4 or tempBoard[i + 1][m + 1][1] == 5):
                            return -30

                    # cell 3
                    if (i == 0 and m == 2):
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m - 1][1] == 2 or tempBoard[i + 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m - 1][1] == 4 or tempBoard[i + 1][m - 1][1] == 5):
                            return 30
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i + 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i + 1][m - 1][1] == 5):
                            return -30

                    # cell 4
                    if (i == 0 and m == 3):
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i][m - 1][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m - 1][1] == 2 or tempBoard[i + 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m - 1][1] == 4 or tempBoard[i + 1][m - 1][1] == 5):
                            return -30

                    # cells 5
                    if (i == 1 and m == 0):
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m + 1][1] == 2 or tempBoard[i + 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m + 1][1] == 4 or tempBoard[i + 1][m + 1][1] == 5):
                            return -30

                    # Cells 6
                    if (i == 1 and m == 1):
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m + 1][1] == 2 or tempBoard[i + 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m + 1][1] == 4 or tempBoard[i + 1][m + 1][1] == 5):
                            return -30

                    # cell 7
                    if (i == 1 and m == 2):
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m - 1][1] == 2 or tempBoard[i + 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m - 1][1] == 4 or tempBoard[i + 1][m - 1][1] == 5):
                            return -30
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i][m - 1][1] == 5):
                            return -30

                    # Cell 8
                    if (i == 1 and m == 3):
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i][m - 1][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m][1] == 2 or tempBoard[i + 1][m][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m][1] == 4 or tempBoard[i + 1][m][1] == 5):
                            return -30
                        if (tempBoard[i + 1][m - 1][1] == 2 or tempBoard[i + 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i + 1][m - 1][1] == 2 or tempBoard[i + 1][m - 1][1] == 3):
                            return -30

                    # Cell 9
                    if (i == 2 and m == 0):
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m][1] == 2 or tempBoard[i - 1][m][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m][1] == 4 or tempBoard[i - 1][m][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m + 1][1] == 2 or tempBoard[i - 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m + 1][1] == 4 or tempBoard[i - 1][m + 1][1] == 5):
                            return -30

                    # Cell 10
                    if (i == 2 and m == 1):
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m][1] == 2 or tempBoard[i - 1][m][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m][1] == 4 or tempBoard[i - 1][m][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m + 1][1] == 2 or tempBoard[i - 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m + 1][1] == 4 or tempBoard[i - 1][m + 1][1] == 5):
                            return -30
                    # cell 11
                    if (i == 2 and m == 2):
                        if (tempBoard[i - 1][m][1] == 2 or tempBoard[i - 1][m][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m][1] == 4 or tempBoard[i - 1][m][1] == 5):
                            return -30
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i][m - 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m - 1][1] == 2 or tempBoard[i - 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m - 1][1] == 4 or tempBoard[i - 1][m - 1][1] == 5):
                            return -30

                    # cell 12
                    if (i == 2 and m == 3):
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i][m - 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m - 1][1] == 2 or tempBoard[i - 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m - 1][1] == 4 or tempBoard[i - 1][m - 1][1] == 5):
                            return -30

                    # cell 13
                    if (i == 2 and m == 0):
                        if (tempBoard[i - 1][m][1] == 2 or tempBoard[i - 1][m][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m][1] == 4 or tempBoard[i - 1][m][1] == 5):
                            return -30
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m + 1][1] == 2 or tempBoard[i - 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m + 1][1] == 4 or tempBoard[i - 1][m + 1][1] == 5):
                            return -30

                    # cell 14
                    if (i == 2 and m == 1):
                        if (tempBoard[i - 1][m][1] == 2 or tempBoard[i - 1][m][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m][1] == 4 or tempBoard[i - 1][m][1] == 5):
                            return -30
                        if (tempBoard[i][m + 1][1] == 2 or tempBoard[i][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i][m + 1][1] == 4 or tempBoard[i][m + 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m + 1][1] == 2 or tempBoard[i - 1][m + 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m + 1][1] == 4 or tempBoard[i - 1][m + 1][1] == 5):
                            return -30

                    # cell 15
                    if (i == 2 and m == 2):
                        if (tempBoard[i - 1][m][1] == 2 or tempBoard[i - 1][m][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m][1] == 4 or tempBoard[i - 1][m][1] == 5):
                            return -30
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i][m - 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m - 1][1] == 2 or tempBoard[i - 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m - 1][1] == 4 or tempBoard[i - 1][m - 1][1] == 5):
                            return -30

                    # cell 16
                    if (i == 0 and m == 3):
                        if (tempBoard[i - 1][m][1] == 2 or tempBoard[i - 1][m][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m][1] == 4 or tempBoard[i - 1][m][1] == 5):
                            return -30
                        if (tempBoard[i][m - 1][1] == 2 or tempBoard[i][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i][m - 1][1] == 4 or tempBoard[i][m - 1][1] == 5):
                            return -30
                        if (tempBoard[i - 1][m - 1][1] == 2 or tempBoard[i - 1][m - 1][1] == 3):
                            return 30
                        if (tempBoard[i - 1][m - 1][1] == 4 or tempBoard[i - 1][m - 1][1] == 5):
                            return -30
                            '''
