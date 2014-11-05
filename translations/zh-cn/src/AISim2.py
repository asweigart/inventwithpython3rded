# 黑白棋

import random
import sys

def drawBoard(board):
    # 此函数输出传递进来的棋盘。无返回值。
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)


def resetBoard(board):
    # 清空棋盘，仅留下起始位置。
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    # 开局的棋子：
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def getNewBoard():
    # 生成一个全新的棋盘数据结构。
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board


def isValidMove(board, tile, xstart, ystart):
    # 如果玩家在xstart, ystart位置落子无效，返回False。
    # 如果落子有效，返回即将归属于玩家的一系列空间。
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = tile # 暂时落子。

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # 在横向上移动
        y += ydirection # 在纵向上移动
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # 在我们的棋子旁有一个其他玩家的棋子。
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # 跳出while循环，继续for循环
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # 找到需要翻转的棋子。沿相反反向遍历直到回到落子点，并且标记沿路的所有棋子。
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = ' ' # 还原落子点
    if len(tilesToFlip) == 0: # 如果没有翻转的棋子，该落子无效。
        return False
    return tilesToFlip


def isOnBoard(x, y):
    # 如果该坐标在棋盘上，返回True
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def getBoardWithValidMoves(board, tile):
    # 返回一个以“.”标记给定玩家所有可以落子的位置的棋盘。
    dupeBoard = getBoardCopy(board)

    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard


def getValidMoves(board, tile):
    # 返回一个给定玩家在该棋盘上所有可落子位置的[x,y]列表。
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    # 通过计数棋子来计算得分。返回一个以“X”和“O”为键名的词典。
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}


def enterPlayerTile():
    # 让玩家输入想使用哪种棋子。
    # 返回一个列表，其中第一个元素是玩家的棋子，第二个元素是电脑的棋子。
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    # 列表中的第一个元素是玩家的棋子，第二个是电脑的棋子。
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # 随机选择一个玩家先手。
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # 如果玩家想再玩一盘，返回True，否则返回False。
    print('是否再来一盘？（yes或no）')
    return input().lower().startswith('y')


def makeMove(board, tile, xstart, ystart):
    # 在棋盘上xstart, ystart位置落子，并翻转对手的棋子。
    # 如果该落子无效，返回False，有效则返回True。
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def getBoardCopy(board):
    # 生成并返回该棋盘的副本。
    dupeBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]

    return dupeBoard


def isOnCorner(x, y):
    # 如果该坐标位于棋盘的某一个角落中，返回True。
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def getPlayerMove(board, playerTile):
    # 让玩家输入落子操作。
    # 以[x, y]的格式返回操作（或者返回字符串“hints”或者“quit”）
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('输入落子位置，或者输入quit结束游戏，或者输入hints来打开/关闭提示。')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('落子无效。先输入横坐标x（1-8），再输入纵坐标y（1-8）。')
            print('例如，81代表棋盘的右上角。')

    return [x, y]


def getComputerMove(board, computerTile):
    # 给定棋盘和电脑的棋子，判断电脑落子
    # 的位置，并以[x, y]的格式返回落子。
    possibleMoves = getValidMoves(board, computerTile)

    # 将可行的落子操作随机排列
    random.shuffle(possibleMoves)

    # 优先在角落落子。
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # 遍历所有可行的落子操作，找出得分最高的落子方式
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def showPoints(playerTile, computerTile):
    # 显示现在的得分。
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))



print('欢迎来到黑白棋！')

xwins = 0
owins = 0
ties = 0
numGames = int(input('输入游戏的次数：'))

for game in range(numGames):
    print('第%s局：' % (game), end=' ')
    # 重置棋盘和游戏。
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    if whoGoesFirst() == 'player':
        turn = 'X'
    else:
        turn = 'O'

    while True:
        if turn == 'X':
            # 轮到X。
            otherTile = 'O'
            x, y = getComputerMove(mainBoard, 'X')
            makeMove(mainBoard, 'X', x, y)
        else:
            # 轮到O。
            otherTile = 'X'
            x, y = getComputerMove(mainBoard, 'O')
            makeMove(mainBoard, 'O', x, y)

        if getValidMoves(mainBoard, otherTile) == []:
            break
        else:
            turn = otherTile

    # 显示最后的得分。
    scores = getScoreOfBoard(mainBoard)
    print('X得到了%s分，O得到了%s分。' % (scores['X'], scores['O']))

    if scores['X'] > scores['O']:
        xwins += 1
    elif scores['X'] < scores['O']:
        owins += 1
    else:
        ties += 1

numGames = float(numGames)
xpercent = round(((xwins / numGames) * 100), 2)
opercent = round(((owins / numGames) * 100), 2)
tiepercent = round(((ties / numGames) * 100), 2)
print('X赢了%s局（%s%%），O赢了%s局（%s%%），平局%s局（%s%%），共%s局。' % (xwins, xpercent, owins, opercent, ties, tiepercent, numGames))
