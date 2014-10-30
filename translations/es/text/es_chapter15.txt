Chapter 15 - Reversi

Topics Covered In This Chapter:

The bool() Function
Evaluating Non-Boolean Values as Booleans
How to Play Reversi

In this chapter we will make a game called Reversi. Reversi (also called Othello) is a board game that is played on a grid (so we will use a Cartesian coordinate system with XY coordinates, like we did with Sonar.) It is a game played with two players. Our version of the game will have a computer AI that is more advanced than the AI we made for Tic Tac Toe. In fact, this AI is so good that it will probably beat you almost every time you play. (I know I lose whenever I play against it!)

If you would like to see a video of Reversi being played, there is a demonstration on this book's website. Go to the URL http://inventwithpython.com/videos and find the "Reversi Demo Video" video.

Reversi has an 8 x 8 board with tiles that are black on one side and white on the other (our game will use O's and X's though). The starting board looks like Figure 15-1. Each player takes turn placing down a new tile of their color. Any of the opponent's tiles that are between the new tile and the other tiles of that color is flipped. The goal of the game is to have as many of the tiles with your color as possible. For example, Figure 15-2 is what it looks like if the white player places a new white tile on space 5, 6.


Figure 15-1: The starting Reversi board
has two white tiles and two black tiles.    Figure 15-2: White places a new tile.
The black tile at 5, 5 is in between the new white tile and the existing white tile at 5, 4. That black tile is flipped over and becomes a new white tile, making the board look like Figure 15-3. Black makes a similar move next, placing a black tile on 4, 6 which flips the white tile at 4, 5. This results in a board that looks like Figure 15-4.


Figure 15-3: White's move will
flip over one of black's tiles. Figure 15-4: Black places a new tile,
which flips over one of white's tiles.
Tiles in all directions are flipped as long as they are in between the player's new tile and existing tile. In Figure 15-5, the white player places a tile at 3, 6 and flips black tiles in both directions (marked by the lines.) The result is in Figure 15-6.


Figure 15-5: White's second move
at 3, 6 will flip two of black's tiles. Figure 15-6: The board after white's second move.
As you can see, each player can quickly grab a majority of the tiles on the board in just one or two moves. Players must always make a move that captures at least one tile. The game ends when a player either cannot make a move, or the board is completely full. The player with the most tiles of their color wins.

The basic strategy of Reversi is to look at which move would turn over the most tiles. But you should also consider taking a move that will not let your opponent recapture many tiles after your move. Placing a tile on the sides or, even better, the corners is good because there is less chance that those tiles will end up between your opponent's tiles. The AI we make for this game will simply look for any corner moves they can take. If there are no corner moves available, then the computer will select the move that claims the most tiles.

You can learn more about Reversi from Wikipedia: http://en.wikipedia.org/wiki/Reversi



Sample Run

Notice that our version of Reversi doesn't use black and white tiles because the text that our program creates will always be the same color. Instead, we will use X's and O's to represent the human and computer players.

Welcome to Reversi!
Do you want to be X or O?
x
The player will go first.
    1   2   3   4   5   6   7   8
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
1 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
2 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
3 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
4 |   |   |   | X | O |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
5 |   |   |   | O | X |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
6 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
7 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
8 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
You have 2 points. The computer has 2 points.
Enter your move, or type quit to end the game, or hints to turn off/on hints.
53
    1   2   3   4   5   6   7   8
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
1 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
2 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
3 |   |   |   |   | X |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
4 |   |   |   | X | X |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
5 |   |   |   | O | X |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
6 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
7 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
8 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
You have 4 points. The computer has 1 points.
Press Enter to see the computer's move.


...skipped for brevity...


    1   2   3   4   5   6   7   8
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
1 | O | O | O | O | O | O | O | O |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
2 | O | O | O | O | O | O | O | O |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
3 | O | O | O | O | O | O | O | O |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
4 | O | O | X | O | O | O | O | O |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
5 | O | O | O | X | O | X | O | X |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
6 | O | X | O | X | X | O | O |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
7 | O | X | X | O | O | O | O | O |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
8 | O | X | X | O |   |   | X |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
You have 12 points. The computer has 48 points.
Enter your move, or type quit to end the game, or hints to turn off/on hints.
86
X scored 15 points. O scored 46 points.
You lost. The computer beat you by 31 points.
Do you want to play again? (yes or no)
no
As you can see, the AI was pretty good at beating me. To help the player out, we'll program our game to provide hints. If the player types 'hints' as their move, they can toggle the hints mode on and off. When hints mode is on, all the possible moves the player can make will show up on the board as '.' characters, like this:

    1   2   3   4   5   6   7   8
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
1 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
2 |   |   |   | . |   | . |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
3 |   |   |   | O | O | O |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
4 |   |   | . | O | O | X |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
5 |   |   | . | O | O | O | X |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
6 |   |   |   | . |   | . |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
7 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
  |   |   |   |   |   |   |   |   |
8 |   |   |   |   |   |   |   |   |
  |   |   |   |   |   |   |   |   |
  +---+---+---+---+---+---+---+---+
Reversi's Source Code

Reversi is a mammoth program compared to our previous games. It comes in over 300 lines long! (But don't worry, many of these lines are just comments or blank lines to space out the code and make it more readable.) As always, you don't have to type in the program before reading this chapter. And you can also download the program by going to this book's website at the URL, http://inventwithpython.com/chapter15 and following the instructions online.

As with our other programs, we will first create several functions to carry out Reversi-related tasks that the main section of our program will call. Roughly the first 250 lines of code are for these helper functions, and the last 50 lines of code implement the Reversi game itself.

reversi.py
This code can be downloaded from http://inventwithpython.com/reversi.py
If you get errors after typing this code in, compare it to the book's code with the online diff tool at http://inventwithpython.com/diff or email the author at al@inventwithpython.com
# Reversi
import random
import sys
def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
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
    # Blanks out the board it is passed, except for the original starting position.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
    # Starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(8):
        board.append([' '] * 8)
    return board
def isValidMove(board, tile, xstart, ystart):
    # Returns False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    board[xstart][ystart] = tile # temporarily set the tile on the board.
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # There is a piece belonging to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    board[xstart][ystart] = ' ' # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip
def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7
def getBoardWithValidMoves(board, tile):
    # Returns a new board with . marking the valid moves the given player can make.
    dupeBoard = getBoardCopy(board)
    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard
def getValidMoves(board, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves
def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
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
    # Let's the player type which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()
    # the first element in the tuple is the player's tile, the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True
def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate.
    dupeBoard = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard
def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
def getPlayerMove(board, playerTile):
    # Let the player type in their move.
    # Returns the move as [x, y] (or returns the strings 'hints' or 'quit')
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
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
            print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
            print('For example, 81 will be the top-right corner.')
    return [x, y]
def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)
    # randomize the order of the possible moves
    random.shuffle(possibleMoves)
    # always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
    # Go through all the possible moves and remember the best scoring move
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
    # Prints out the current score.
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))
print('Welcome to Reversi!')
while True:
    # Reset the board and game.
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    while True:
        if turn == 'player':
            # Player's turn.
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            move = getPlayerMove(mainBoard, playerTile)
            if move == 'quit':
                print('Thanks for playing!')
                sys.exit() # terminate the program
            elif move == 'hints':
                showHints = not showHints
                continue
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])
            if getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'computer'
        else:
            # Computer's turn.
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            input('Press Enter to see the computer\'s move.')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)
            if getValidMoves(mainBoard, playerTile) == []:
                break
            else:
                turn = 'player'
    # Display the final score.
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie!')
    if not playAgain():
        break
How the Code Works

The Game Board Data Structure

Before we get into the code, we should talk about the board data structure. This data structure is a list of lists, just like the one in our previous Sonar game. The list is created so that board[x][y] will represent the character on space located at position x on the X-axis (going left/right) and position y on the Y-axis (going up/down). This character can either be a ' ' space character (to represent a blank space), a '.' period character (to represent a possible move in hint mode), or an 'X' or 'O' (to represent a player's tile). Whenever you see a parameter named board, that parameter variable is meant to be this list of lists board data structure.

Importing Other Modules

# Reversi
import random
import sys
We import the random module for its randint() and choice() functions and the sys module for its exit() function.

Drawing the Board Data Structure on the Screen

def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'
    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
The drawBoard() function will print out the current game board based on the data structure in board. Notice that each square of the board looks like this:

+---+
|   |
| X |
|   |
+---+
Since we are going to print the string with the horizontal line (and plus signs at the intersections) over and over again, we will store that in a constant variable named HLINE. There are also lines above and below the very center of X or O tile that are nothing but '|' characters (called "pipe" characters) with three spaces in between. We will store this string in a constant named VLINE.

Line 11 is the first print() function call executed, and it prints out the labels for the X-axis along the top of the board. Line 12 prints the top horizontal line of the board.

    for y in range(8):
        print(VLINE)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)
Printing each row of spaces on the board is fairly repetitive, so we can use a loop here. We will loop eight times, once for each row. Line 15 prints the label for the Y-axis on the left side of the board, and has an end=' ' keyword argument at the end of it to print a single space instead of a new line. This is so we can have another loop (which again loops eight times, once for each space) print out each space (along with the 'X', 'O', or ' ' character for that space depending on what is stored in board.)

The print() function call inside the inner loop also has an end=' ' keyword argument at the end of it, meaning a space character is printed instead of a newline character. This produces the second space in the pipe-space-tile-space string that we print out, over and over for eight times. That will produce a single line on the screen that looks like '| X | X | X | X | X | X | X | X ' (that is, if each of the board[x][y] values were 'X'). After the inner loop is done, the print() function call on line 18 prints out the final '|' character along with a newline (since it does not end with an end keyword argument).

(The print()call forces us to always print a newline character or a space at the end of everything we print. If we do not want this last character, then we can always use the sys.stdout.write() function, which has a single string parameter that it prints out. Be sure to import sys first before calling this function.)

The code inside the outer for loop from line 14 to line 20 prints out an entire row of the board like this:

|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
When the for loop on line 13 prints the row eight times, it forms the entire board (of course, some of the spaces on the board will have 'O' or ' ' instead of 'X'):

|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
| X | X | X | X | X | X | X | X |
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
Resetting the Game Board

An important thing to remember is that the coordinates that we print out to the player are from 1 to 8, but the indexes in the board data structure are from 0 to 7.

def resetBoard(board):
    # Blanks out the board it is passed, except for the original starting position.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
Here we use a loop inside a loop to set the board data structure to be all single-space strings to make a blank Reversi board. We will call the resetBoard() function whenever we start a new game and want to remove the tiles from a previous game.

Setting Up the Starting Pieces

    # Starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'
When we start a new game of Reversi, it isn't enough to have a completely blank board. At the very beginning, each player has two tiles already laid down in the very center, so we will also have to set those.

We do not have to return the board variable, because board is a reference to a list. Even when we make changes inside the local function's scope, these changes happen to the original list that was passed as an argument. (Remember, this is one way list variables are different from non-list variables.)

Creating a New Game Board Data Structure

def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(8):
        board.append([' '] * 8)
    return board
The getNewBoard() function creates a new board data structure and returns it. Line 38 creates the outer list and stores a reference to this list in board. Line 40 creates the inner lists using list replication. ([' '] * 8 evaluates to be the same as [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] but with less typing.) The for loop here runs line 40 eight times to create the eight inner lists. The spaces represent a completely empty game board.

What board ends up being is a list of eight lists, and each of those eight lists themselves has eight strings. The result is sixty four (8 x 8 = 64) strings. Each string is (right now) a single space character.

Checking if a Move is Valid

def isValidMove(board, tile, xstart, ystart):
    # Returns False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False
    board[xstart][ystart] = tile # temporarily set the tile on the board.
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    tilesToFlip = []
isValidMove() is one of the more complicated functions. Given a board data structure, the player's tile, and the XY coordinates for player's move, this function should return True if the Reversi game rules allow a move to those coordinates and False if they don't.

The easiest check we can do to disqualify a move is to see if the XY coordinates are on the game board or if the space at XY is not empty. This is what the if statement on line 48 checks for. isOnBoard() is a function we will write that makes sure both the X and Y coordinates are between 0 and 7. We do this on line 48 and 49.

For the purposes of this function, we will go ahead and copy the XY coordinate pointed to by xstart and ystart with the player's tile. We set this place on the board back to a space before we leave this function.

The player's tile (either the human player or the computer player) has been passed to us, but we will need to be able to identify the other player's tile. If the player's tile is 'X' then obviously the other player's tile is 'O', and vice versa.

Finally, if the given XY coordinate ends up as a valid position, we will return a list of all the opponent's tiles that would be flipped by this move.

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
The for loop iterates through a list of lists which represent directions you can move on the game board. The game board is a Cartesian coordinate system with an X and Y direction. There are eight directions you can move: up, down, left, right, and the four diagonal directions. Each of the eight 2-item lists in the list on line 59 represents one of these directions. We will move around the board in a direction by adding the first value in the two-item list to our X coordinate, and the second value to our Y coordinate.

Because the X coordinates increase as you go to the right, you can "move" to the right by adding 1 to the X coordinate. Moving to the left is the opposite: you would subtract 1 (or add -1) from the X coordinate. We can move up, down, left, and right by adding or subtracting to only one coordinate at a time. But to move diagonally, we need to add or subtract to both coordinates. For example, adding 1 to the X coordinate to move right and adding -1 to the Y coordinate to move up would result in moving to the up-right diagonal direction.

Checking Each of the Eight Directions

Here is a diagram to make it easier to remember which two-item list represents which direction:


Figure 15-7: Each two-item list represents one of the eight directions.

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
Line 60 sets an x and y variable to be the same value as xstart and ystart, respectively. We will change x and y to "move" in the direction that xdirection and ydirection dictate. xstart and ystart will stay the same so we can remember which space we originally intended to check. (Remember, we need to set this place back to a space character, so we shouldn't overwrite the values in them.)

We make the first step in the direction as the first part of our algorithm.

        if isOnBoard(x, y) and board[x][y] == otherTile:
            # There is a piece belonging to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
Remember, in order for this to be a valid move, the first step in this direction must be 1) on the board and 2) must be occupied by the other player's tile. Otherwise there is no chance to flip over any of the opponent's tiles. In that case, the if statement on line 63 is not True and execution goes back to the for statement for the next direction.

But if the first space does have the other player's tile, then we should keep proceeding in that direction until we reach on of our own tiles. If we move off of the board, then we should continue back to the for statement to try the next direction.

            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
The while loop on line 69 ensures that x and y keep going in the current direction as long as we keep seeing a trail of the other player's tiles. If x and y move off of the board, we break out of the for loop and the flow of execution moves to line 74. What we really want to do is break out of the while loop but continue in the for loop. But if we put a continue statement on line 73, that would only continue to the while loop on line 69.

Instead, we recheck not isOnBoard(x, y) on line 74 and then continue from there, which goes to the next direction in the for statement on line 59. It is important to know that break and continue will only break or continue in the loop they are called from, and not an outer loop that contain the loop they are called from.

Finding Out if There are Pieces to Flip Over

            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
If the while loop on line 69 stopped looping because the condition was False, then we have found a space on the board that holds our own tile or a blank space. Line 76 checks if this space on the board holds one of our tiles. If it does, then we have found a valid move. We will then start a new while loop, this time subtracting x and y to move in the opposite direction we were originally going. We note each space between our tiles on the board by appending the space to the tilesToFlip list.

We break out of the while loop once x and y have returned to the original position (which was still stored in xstart and ystart).

    board[xstart][ystart] = ' ' # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip
We perform this check in all eight directions, and afterwards the tilesToFlip list will contain the XY coordinates all of our opponent's tiles that would be flipped if the player moved on xstart, ystart. Remember, the isValidMove() function is only checking to see if the original move was valid, it does not actually change the data structure of the game board.

If none of the eight directions ended up flipping at least one of the opponent's tiles, then tilesToFlip would be an empty list and this move would not be valid. In that case, isValidMove() should return False. Otherwise, we should return tilesToFlip.

Checking for Valid Coordinates

def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7
isOnBoard() is a function called from isValidMove(), and is just shorthand for the rather complicated Boolean expression that returns True if both x and y are in between 0 and 7. This function lets us make sure that the coordinates are actually on the game board.

Getting a List with All Valid Moves

def getBoardWithValidMoves(board, tile):
    # Returns a new board with . marking the valid moves the given player can make.
    dupeBoard = getBoardCopy(board)
    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard
getBoardWithValidMoves() is used to return a game board data structure that has '.' characters for all valid moves on the board. This is used by the hints mode to display to the player a board with all possible moves marked on it.

Notice that this function creates a duplicate game board data structure instead of modifying the one passed to it in the board parameter. Line 100 calls getValidMoves(), which returns a list of XY coordinates with all the legal moves the player could make. The board copy is then marked with a period in those spaces. How getValidMoves() works is described next.

def getValidMoves(board, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves
The getValidMoves() function returns a list of two-item lists that hold the XY coordinates for all valid moves for tile's player, given a particular game board data structure in board.

This function uses two loops to check every single XY coordinate (all sixty four of them) by calling isValidMove() on that space and checking if it returns False or a list of possible moves (in which case it is a valid move). Each valid XY coordinate is appended to the list, validMoves.

The bool() Function

Remember how you could use the int() and str() functions to get the integer and string value of other data types? For example, str(42) would return the string '42', and int('100') would return the integer 100.

There is a similar function for the Boolean data type, bool(). Most other data types have one value that is considered the False value for that data type, and every other value is consider True. The integer 0, the floating point number 0.0, the empty string, the empty list, and the empty dictionary are all considered to be False when used as the condition for an if or loop statement. All other values are True. Try entering the following into the interactive shell:

>>> bool(0)
False
>>> bool(0.0)
False
>>> bool('')
False
>>> bool([])
False
>>> bool({})
False
>>> bool(1)
True
>>> bool('Hello')
True
>>> bool([1, 2, 3, 4, 5])
True
>>> bool({'spam':'cheese', 'fizz':'buzz'})
True
>>>
Whenever you have a condition, imagine that the entire condition is placed inside a call to bool() as the parameter. Conditions are automatically interpreted as Boolean values. This is similar to how print() can be passed non-string values and will automatically interpret them as strings when they print.

This is why the condition on line 111 works correctly. The call to the isValidMove() function either returns the Boolean value False or a non-empty list. If you imagine that the entire condition is placed inside a call to bool(), then the condition False becomes bool(False) (which, of course, evalutes to False). And a condition of a non-empty list placed as the parameter to bool() will return True. This is why the return value of isValidMove() can be used as a condition.

Getting the Score of the Game Board

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}
The getScoreOfBoard() function uses nested for loops to check all 64 spaces on the board (8 rows times 8 columns per row is 64 spaces) and see which tile (if any) is on them. For each 'X' tile, the code increments xscore. For each 'O' tile, the code increments oscore.

Notice that this function does not return a two-item list of the scores. A two-item list might be a bit confusing, because you may forget which item is for X and which item is for O. Instead the function returns a dictionary with keys 'X' and 'O' whose values are the scores.

Getting the Player's Tile Choice

def enterPlayerTile():
    # Let's the player type which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()
This function asks the player which tile they want to be, either 'X' or 'O'. The for loop will keep looping until the player types in 'X' or 'O'.

    # the first element in the tuple is the player's tile, the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
The enterPlayerTile() function then returns a two-item list, where the player's tile choice is the first item and the computer's tile is the second. We use a list here instead of a dictionary so that the assignment statement calling this function can use the multiple assignment trick. (See line 252.)

Determining Who Goes First

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
The whoGoesFirst() function randomly selects who goes first, and returns either the string 'computer' or the string 'player'.

Asking the Player to Play Again

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
We have used the playAgain() in our previous games. If the player types in something that begins with 'y', then the function returns True. Otherwise the function returns False.

Placing Down a Tile on the Game Board

def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
makeMove() is the function we call when we want to place a tile on the board and flip the other tiles according to the rules of Reversi. This function modifies the board data structure that is passed as a parameter directly. Changes made to the board variable (because it is a list) will be made to the global scope as well. Most of the work is done by isValidMove(), which returns a list of XY coordinates (in a two-item list) of tiles that need to be flipped. (Remember, if the the xstart and ystart arguments point to an invalid move, then isValidMove() will return the Boolean value False.)

    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True
On lines 163 and 164, if the return value of isValidMove() was False, then makeMove() will also return False.

Otherwise, isValidMove() would have returned a list of spaces on the board to put down our tiles (the 'X' or 'O' string in tile). Line 166 sets the space that the player has moved on, and the for loop after that sets all the tiles that are in tilesToFlip.

Copying the Board Data Structure

def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate.
    dupeBoard = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard
getBoardCopy() is different from getNewBoard(). getNewBoad() will create a new game board data structure which has only empty spaces and the four starting tiles. getBoardCopy() will create a new game board data structure, but then copy all of the pieces in the board parameter. This function is used by our AI to have a game board that it can change around so that it doesn't have to change the real game board. This is like how you may imagine making moves on a copy of the board in your mind, but not actually put pieces down on the real board.

A call to getNewBoard() handles getting a fresh game board data structure. Then the two for loops copy each of the 64 tiles from board to our duplicate board data structure named dupeBoard.

Determining if a Space is on a Corner

def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
This function is much like isOnBoard(). Because all Reversi boards are 8 x 8 in size, we only need the XY coordinates to be passed to this function, not a game board data structure itself. This function returns True if the coordinates are on either (0,0), (7,0), (0,7) or (7,7). Otherwise isOnCorner() returns False.

Getting the Player's Move

def getPlayerMove(board, playerTile):
    # Let the player type in their move.
    # Returns the move as [x, y] (or returns the strings 'hints' or 'quit')
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
The getPlayerMove() function is called to let the player type in the coordinates of their next move (and check if the move is valid). The player can also type in 'hints' to turn hints mode on (if it is off) or off (if it is on). The player can also type in 'quit' to quit the game.

The DIGITS1TO8 constant variable is the list ['1', '2', '3', '4', '5', '6', '7', '8']. We create this constant because it is easier type DIGITS1TO8 than the entire list. (We can't use the isdigit() method because that would allow 0 and 9 to be entered, which are not valid coordinates on our 8x8 board.)

    while True:
        print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'
The while loop will keep looping until the player has typed in a valid move. First we check if the player wants to quit or toggle hints mode, and return the string 'quit' or 'hints'. We use the lower() method on the string returned by input() so the player can type 'HINTS' or 'Quit' but still have the command understood by our game.

The code that calls getPlayerMove() will handle what to do if the player wants to quit or toggle hints mode.

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
Our game is expecting that the player would have typed in the XY coordinates of their move as two numbers without anything in between them. The if statement first checks that the size of the string the player typed in is 2. After that, the if statement also checks that both move[0] (the first character in the string) and move[1] (the second character in the string) are strings that exist in DIGITS1TO8, which we defined at the beginning of the function.

Remember that our game board data structures have indexes from 0 to 7, not 1 to 8. We show 1 to 8 when we print the board using drawBoard() because people are used to numbers beginning at 1 instead of 0. So when we convert the strings in move[0] and move[1] to integers, we also subtract 1.

Even if the player typed in a correct move, we still need to check that the move is allowed by the rules of Reversi. We do this by calling isValidMove(), passing the game board data structure, the player's tile, and the XY coordinates of the move. If isValidMove() returns False, then we execute the continue statement so that the flow of execution goes back to the beginning of the while loop and asks the player for the move again.

If isValidMove() does not return False, then we know the player typed in a valid move and we should break out of the while loop.

        else:
            print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
            print('For example, 81 will be the top-right corner.')
If the if statement's condition on line 200 was False, then the player did not type in a valid move. We should display a message instructing them how to type in moves that our Reversi program can understand. Afterwards, the execution moves back to the while statement on line 192 because line 209 is not only the last line in the else-block, but also the last line in the while-block.

    return [x, y]
Finally, getPlayerMove() returns a two-item list with the XY coordinates of the player's valid move.

Getting the Computer's Move

def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)
getComputerMove() and is where our AI algorithm is implemented. The getValidMoves() function is very helpful for our AI. Normally we use the results from getValidMoves() for hints mode. Hints mode will print '.' period characters on the board to show the player all the potential moves they can make. But if we call getValidMoves() with the computer AI's tile (in computerTile), we can get all the possible moves that the computer can make. We will select the best move from this list.

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)
First, we are going to use the random.shuffle() function to randomize the order of moves in the possibleMoves list. Remember that the random.shuffle() function will reorder the items in the list that you pass to it. The function also modifies the list directly, much like our resetBoard() function does with the game board data structure.

We will explain why we want to shuffle the possibleMoves list, but first let's look at our algorithm.

Corner Moves are the Best Moves

    # always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
First, we loop through every move in possibleMoves and if any of them are on the corner, we return that as our move. Corner moves are a good idea because once a tile has been placed on the corner, it can never be flipped over. Since possibleMoves is a list of two-item lists, we use the multiple assignment trick in our for loop to set x and y.

Because we immediately return on finding the first corner move in possibleMoves, if possibleMoves contains multiple corner moves we always go with the first one. But since possibleMoves was shuffled on line 220, it is completely random which corner move is first in the list.

Get a List of the Best Scoring Moves

    # Go through all the possible moves and remember the best scoring move
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove
If there are no corner moves, we will go through the entire list and find out which move gives us the highest score. The for loop will set x and y to every move in possibleMoves. bestMove will be set to the highest scoring move we've found so far, and bestScore will be set to the best move's score. When the code in the loop finds a move that scores higher than bestScore, we will store that move and score as the new values of bestMove and bestScore (see lines 233, 234, and 235).

Simulate All Possible Moves on Duplicate Board Data Structures

In order to figure out the score of the possible move we are currently iterating on, we first make a duplicate game board data structure by calling getBoardCopy() on line 230. We want a copy so we can modify without changing the real game board data structure stored in the board variable.

Then we call makeMove() on line 231, passing the duplicate board (stored in dupeBoard) instead of the real board. makeMove() will handle placing the computer's tile and the flipping the player's tiles on the duplicate board.

We call getScoreOfBoard() on line 232 with the duplicate board, which returns a dictionary where the keys are 'X' and 'O', and the values are the scores. getScoreOfBoard() does not know if the computer is 'X' or 'O', which is why it returns a dictionary with both scores.

By making a duplicate board, we can simulate a future move and test the results of that move without changing the actual game board data structure. This is very helpful in deciding which move is the best possible move to make.

Pretend that getScoreOfBoard() returns the dictionary {'X':22, 'O':8} and computerTile is 'X'. Then getScoreOfBoard(dupeBoard)[computerTile] would evaluate to {'X':22, 'O':8}['X'], which would then evaluate to 22. If 22 is larger than bestScore, bestScore is set to 22 and bestMove is set to the current x and y values we are looking at. By the time this for loop is finished, we can be sure that bestScore is the highest possible score a move can make, and that move is stored in bestMove.

You may have noticed that on line 228 we first set bestScore to -1. This is so that the first move we look at in our for loop over possibleMoves will be set to the first bestMove. This will guarantee that bestMove is set to one of the moves when we return it.

Say that the highest scoring move in possibleMoves would give the computer a score of 42. What if there was more than one move in possibleMoves that would give this score? The for loop we use would always go with the first move that scored 42 points, because bestMove and bestScore only change if the move is greater than the highest score. A tie will not change bestMove and bestScore.

We do not always want to go with the first move in the possibleMoves list if it had not been shuffled on line 220, because that would make our AI predictable by the player. Even though our code always chooses the first of these tied moves, is random which of the moves will be first in the list because the order is random. This ensures that the AI will not be predictable when there is more than one best move.

Printing the Scores to the Screen

def showPoints(playerTile, computerTile):
    # Prints out the current score.
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))
showPoints() simply calls the getScoreOfBoard() function and then prints out the player's score and the computer's score. Remember that getScoreOfBoard() returns a dictionary with the keys 'X' and 'O' and values of the scores for the X and O players.

That's all the functions we define for our Reversi game. The code starting on line 246 will implement the actual game and make calls to these functions when they are needed.

The Start of the Game

print('Welcome to Reversi!')
while True:
    # Reset the board and game.
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
The while loop on line 248 is the main game loop. The program will loop back to line 248 each time we want to start a new game. First we get a new game board data structure by calling getNewBoard() and set the starting tiles by calling resetBoard(). mainBoard is the main game board data structure we will use for this program. The call to enterPlayerTile() will let the player type in whether they want to be 'X' or 'O', which is then stored in playerTile and computerTile.

showHints is a Boolean value that determines if hints mode is on or off. We originally set it to off by setting showHints to False.

The turn variable is a string will either have the string value 'player' or 'computer', and will keep track of whose turn it is. We set turn to the return value of whoGoesFirst(), which randomly chooses who will go first. We then print out who goes first to the player on line 255.

Running the Player's Turn

    while True:
        if turn == 'player':
            # Player's turn.
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
The while loop that starts on line 257 will keep looping each time the player or computer takes a turn. We will break out of this loop when the current game is over.

Line 258 has an if statement whose body has the code that runs if it is the player's turn. (The else-block that starts on line 282 has the code for the computer's turn.) The first thing we want to do is display the board to the player. If hints mode is on (which it is if showHints is True), then we want to get a board data structure that has '.' period characters on every space the player could go.

Our getBoardWithValidMoves() function does that, all we have to do is pass the game board data structure and it will return a copy that also contains '.' period characters. We then pass this board to the drawBoard() function on line 262.

If hints mode is off, then we just pass mainBoard to drawBoard() on line 264.

After printing out the game board to the player, we also want to print out the current score by calling showPoints() on line 265.

            move = getPlayerMove(mainBoard, playerTile)
Next we let the player type in their move. getPlayerMove() handles this, and its return value is a two-item list of the XY coordinate of the player's move. getPlayerMove() makes sure that the move the player typed in is a valid move, so we don't have to worry about it here.

Handling the Quit or Hints Commands

            if move == 'quit':
                print('Thanks for playing!')
                sys.exit() # terminate the program
            elif move == 'hints':
                showHints = not showHints
                continue
            else:
                makeMove(mainBoard, playerTile, move[0], move[1])
If the player typed in the string 'quit' for their move, then getPlayerMove() would have returned the string 'quit'. In that case, we should call the sys.exit() to terminate the program.

If the player typed in the string 'hints' for their move, then getPlayerMove() would have returned the string 'hints'. In that case, we want to turn hints mode on (if it was off) or off (if it was on). The showHints = not showHints assignment statement handles both of these cases, because not False evaluates to True and not True evaluates to False. Then we run the continue statement to loop back (turn has not changed, so it will still be the player's turn when we continue).

Make the Player's Move

Otherwise, if the player did not quit or toggle hints mode, then we will call makeMove() to make the player's move on the board.

            if getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'computer'
After making the player's move, we call False to see if the computer could possibly make any moves. If False returns a blank list, then there are no more moves left that the computer could make (most likely because the board is full). In that case, we break out of the while loop and end the current game.

Otherwise, we set turn to 'computer'. The flow of execution skips the else-block and reaches the end of the while-block, so execution jumps back to the while statement on line 257. This time, however, it will be the computer's turn.

Running the Computer's Turn

        else:
            # Computer's turn.
            drawBoard(mainBoard)
            showPoints(playerTile, computerTile)
            input('Press Enter to see the computer\'s move.')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)
The first thing we do when it is the computer's turn is call drawBoard() to print out the board to the player. Why do we do this now? Because either the computer was selected to make the first move of the game, in which case we should display the original starting picture of the board to the player before the computer makes its move. Or the player has gone first, and we want to show what the board looks like after the player has moved but before the computer has gone.

After printing out the board with drawBoard(), we also want to print out the current score with a call to showPoints() on line 284.

Next we have a call to input() on line 285 to pause the script while the player can look at the board. This is much like how we use input() to pause the program in our Jokes chapter. Instead of using a print() call to print a string before a call to input(), you can pass the string as a parameter to input(). input() has an optional string parameter. The string we pass in this call is 'Press Enter to see the computer\'s move.'.

After the player has looked at the board and pressed Enter (any text the player typed is ignored since we do not assign the return value of input() to anything), we call getComputerMove() to get the XY coordinates of the computer's next move. We store these coordinates in variables x and y, respectively.

Finally, we pass x and y, along with the game board data structure and the computer's tile to the makeMove() function to change the game board to reflect the computer's move. Our call to getComputerMove() on line 286 got the computer's move (and stored it in variables x and y), and the call to makeMove() on line 287 makes the move on the board.

            if getValidMoves(mainBoard, playerTile) == []:
                break
            else:
                turn = 'player'
Lines 289 to 292 are very similar to lines 276 to 279. After the computer has made its move, we check if there exist any possible moves the human player can make. If getValidMoves() returns an empty list, then there are no possible moves. That means the game is over, and we should break out of the while loop that we are in.

Otherwise, there is at least one possible move the player should make, so we should set turn to 'player'. There is no more code in the while-block after line 292, so execution loops back to the while statement on line 257.

Drawing Everything on the Screen

    # Display the final score.
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie!')
Line 294 is the first line beyond the while-block that started on line 257. This code is executed when we have broken out of that while loop, either on line 290 or 277. (The while statement's condition on line 257 is simply the value True, so we can only exit the loop through break statements.)

At this point, the game is over. We should print out the board and scores, and determine who won the game. getScoreOfBoard() will return a dictionary with keys 'X' and 'O' and values of both players' scores. By checking if the player's score is greater than, less than, or equal to the computer's score, we can know if the player won, if the player lost, or if the player and computer tied.

Subtracting one score from the other is an easy way to see by how much one player won over the other. Our print() calls on lines 299 and 301 use string interpolation to put the integer result of this subtraction into the string that is printed.

Ask the Player to Play Again

    if not playAgain():
        break
The game is now over and the winner has been declared. We should call our playAgain() function, which returns True if the player typed in that they want to play another game. If playAgain() returns False (which makes the if statement's condition True), we break out of the while loop (the one that started on line 248), and since there are no more lines of code after this while-block, the program terminates.

Otherwise, playAgain() has returned True (which makes the if statement's condition False), and so execution loops back to the while statement on line 248 and a new game board is created.

Changing The drawBoard() Function

The board we draw for our Reversi game is fairly large. But we could change the drawBoard() function's code to draw out a much smaller board, while keeping the rest of the game code the same. The new, smaller board would look something like this:

  12345678
 +--------+
1|    O   |
2|   XOX  |
3|    O   |
4| XXXXX  |
5|  .OX   |
6|  OOO   |
7| ..O..  |
8|   O    |
 +--------+
You have 8 points. The computer has 9 points.
Enter your move, or type quit to end the game, or hints to turn off/on hints.
Here is the code for this new drawBoard() function, starting at line 6. You can also download this code from http://inventwithpython.com/reversi_mini.py

def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = ' +--------+'
    print(' 12345678')
    print(HLINE)
    for y in range(8):
        print('%s|' % (y+1), end='')
        for x in range(8):
            print(board[x][y], end='')
        print('|')
    print(HLINE)
Summary: Reviewing the Reversi Game

The AI may seem almost unbeatable, but this isn't because the computer is very smart. The strategy it follows is very simple: move on the corner if you can, otherwise make the move that will flip over the most tiles. We could do that, but it would take us a long time to figure out how many tiles would be flipped for every possible valid move we could make. But calculating this for the computer is very simple. The computer isn't smarter than us, it's just much faster!

This game is very similar to Sonar because it makes use of a grid for a board. It is also like the Tic Tac Toe game because there is an AI that plans out the best move for it to take. This chapter only introduced one new concept: using the bool() function and the fact that empty lists, blank strings, and the integer 0 all evaluate to False in the context of a condition.

Other than that, this game used programming concepts that you already knew! You don't have to know very much about programming in order to create interesting games. However, this game is stretching how far you can get with ASCII art. The board took up almost the entire screen to draw, and the game didn't have any color.

Later in this book, we will learn how to create games with graphics and animation, not just text. We will do this using a module called Pygame, which adds new functions and features to Python so that we can break away from using just text and keyboard input.

