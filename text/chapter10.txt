Chapter 10 - Tic Tac Toe

Topics Covered In This Chapter:

Artificial Intelligence
List References
Short-Circuit Evaluation
The None Value
We will now create a Tic Tac Toe game where the player plays against a simple artificial intelligence. An artificial intelligence (or AI) is a computer program that can intelligently respond to the player's moves. This game doesn't introduce any complicated new concepts. We will see that the artificial intelligence that plays Tic Tac Toe is really just a few lines of code.

Tic Tac Toe is a simple game to play with a paper and pencil between two people. One player is X and the other player is O. On a simple nine square grid (which we call the board), the players take turns placing their X or O) on the board. If a player gets three of their marks on the board in a row, column or one of the two diagonals, they win.

Most games of Tic Tac Toe end in a draw, which happens when the board is filled up with neither player having three marks in a row. Instead of a second human player, our artificial intelligence will make moves against the user. You can learn more about Tic Tac Toe from Wikipedia: http://en.wikipedia.org/wiki/Tic-tac-toe

While this chapter may not introduce many new programming concepts, it does make use of our existing programming knowledge to make an intelligent Tic Tac Toe player. Let's get started by looking at a sample run of the program. The player makes their move by entering the number of the space they wish to go. These numbers are in the same places as the number keys on your keyboard's keypad (see Figure 10-2).

Sample Run of Tic Tac Toe

Welcome to Tic Tac Toe!
Do you want to be X or O?
X
The computer will go first.
   |   |
 O |   |
   |   |
-----------
   |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
What is your next move? (1-9)
3
   |   |
 O |   |
   |   |
-----------
   |   |
   |   |
   |   |
-----------
   |   |
 O |   | X
   |   |
What is your next move? (1-9)
4
   |   |
 O |   | O
   |   |
-----------
   |   |
 X |   |
   |   |
-----------
   |   |
 O |   | X
   |   |
What is your next move? (1-9)
5
   |   |
 O | O | O
   |   |
-----------
   |   |
 X | X |
   |   |
-----------
   |   |
 O |   | X
   |   |
The computer has beaten you! You lose.
Do you want to play again? (yes or no)
no
Source Code of Tic Tac Toe

In a new file editor window, type in this source code and save it as tictactoe.py. Then run the game by pressing F5. You do not need to type in this program before reading this chapter. You can also download the source code by visiting the website at the URL http://inventwithpython.com/chapter10 and following the instructions on the webpage.

tictactoe.py
This code can be downloaded from http://inventwithpython.com/tictactoe.py
If you get errors after typing this code in, compare it to the book's code with the online diff tool at http://inventwithpython.com/diff or email the author at al@inventwithpython.com
# Tic Tac Toe
import random
def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def inputPlayerLetter():
    # Let's the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X':
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
def makeMove(board, letter, move):
    board[move] = letter
def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '
def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
print('Welcome to Tic Tac Toe!')
while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
Designing the Program


Figure 10-1: Flow chart for Tic Tac Toe

Tic Tac Toe is a very easy and short game to play on paper. In our Tic Tac Toe computer game, we'll let the player choose if they want to be X or O, randomly choose who goes first, and then let the player and computer take turns making moves on the board. Figure 10-1 is what a flow chart of Tic Tac Toe could look like.

You can see a lot of the boxes on the left side of the chart are what happens during the player's turn. The right side of the chart shows what happens on the computer's turn. The player has an extra box for drawing the board because the computer doesn't need the board printed on the screen. After the player or computer makes a move, we check if they won or caused a tie, and then the game switches turns. After the game is over, we ask the player if they want to play again.

Representing the Board as Data

First, we need to figure out how we are going to represent the board as a variable. On paper, the Tic Tac Toe board is drawn as a pair of horizontal lines and a pair of vertical lines, with either an X, O, or empty space in each of the nine spaces.

In our program, we are going to represent the Tic Tac Toe board as a list of strings. Each string will represent one of the nine positions on the board. We will give a number to each of the spaces on the board. To make it easier to remember which index in the list is for which piece, we will mirror the numbers on the keypad of our keyboard. See Figure 10-2.


Figure 10-2: The board will be numbered like the keyboard's number pad.

The strings will either be 'X' for the X player, 'O' for the O player, or a space string ' ' to mark a spot on the board where no one has marked yet. The index of the string in the list will also be the number of the space on the board.

So if we had a list with ten strings named board, then board[7] would be the top-left square on the board (either an X, O, or blank space). board[5] would be the very center. When the player types in which place they want to move, they will type a number from 1 to 9. (Because there is no 0 on the keypad, we will just ignore the string at index 0 in our list.)

Game AI


Figure 10-3: Locations of the side, corner, and center places.
When we talk about how our AI behaves, we will be talking about which types of spaces on the board it will move on. Just to be clear, we will label three types of spaces on the Tic Tac Toe board: corners, sides, and the center. Figure 10-3 is a chart of what each space is:

The AI for this game will follow a simple algorithm. An algorithm is a series of instructions to compute something. This is a loose definition of algorithm. A single program can make use of several different algorithms. An algorithm, like a complete program, can be represented with a flow chart. In the case of our Tic Tac Toe AI's algorithm, the series of steps will determine which is the best place to move. (See Figure 10-4.) There is nothing in the code that says, "These lines are an algorithm." like there is with a function's def-block. We just consider the AI algorithm as all the code that is used in our program that determines the AI's next move.

Our algorithm will have the following steps:

First, see if there is a move the computer can make that will win the game. If there is, take that move. Otherwise, go to step 2.
See if there is a move the player can make that will cause the computer to lose the game. If there is, we should move there to block the player. Otherwise, go to step 3.
Check if any of the corner spaces (spaces 1, 3, 7, or 9) are free. (We always want to take a corner piece instead of the center or a side piece.) If no corner piece is free, then go to step 4.
Check if the center is free. If so, move there. If it isn't, then go to step 5.
Move on any of the side pieces (spaces 2, 4, 6, or 8). There are no more steps, because if we have reached step 5 the side spaces are the only spaces left.
This all takes place in the "Get computer's move." box on our flow chart. We could add this information to our flow chart like this:


Figure 10-4: The five steps of the "Get computer's move" algorithm.
The arrows leaving go to the "Check if computer won" box.

We will implement this algorithm as code in our getComputerMove() function, and the other functions that getComputerMove() calls.

How the Code Works: Lines 1 to 81

Now that we know about how we want the program to work, let's look at what each line does.

The Start of the Program

# Tic Tac Toe
import random
The first couple of lines are a comment and importing the random module so we can use the randint() function in our game.

Printing the Board on the Screen

def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
This function will print out the game board, marked as directed by the board parameter. Remember that our board is represented as a list of ten strings, where the string at index 1 is the mark on space 1 on the Tic Tac Toe board. (And remember that we ignore the string at index 0, because the spaces are labeled with numbers 1 to 9.) Many of our functions will work by passing the board as a list of ten strings to our functions. Be sure to get the spacing right in the strings, otherwise the board will look funny when it is printed on the screen.

Just as an example, here are some values that the board parameter could have (on the left side of the table) and what the drawBoard() function would print out (on the right):

Table 10-1: Examples of values of board and output from drawBoard(board) calls.
board value drawBoard(board) output
[' ', ' ', ' ', ' ', 'X',
 'O', ' ', 'X', ' ', 'O']      |   |
 X |   | O
   |   |
-----------
   |   |
 X | O |
   |   |
-----------
   |   |
   |   |
   |   |
[' ', 'O', 'O', ' ', ' ',
 'X', ' ', ' ', ' ', ' ']      |   |
   |   |
   |   |
-----------
   |   |
   | X |
   |   |
-----------
   |   |
 O | O |
   |   |
[' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ']      |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
[' ', 'X', 'X', 'X', 'X',
 'X', 'X', 'X', 'X', 'X']      |   |
 X | X | X
   |   |
-----------
   |   |
 X | X | X
   |   |
-----------
   |   |
 X | X | X
   |   |
['0', '1', '2', '3', '4',
'5', '6', '7', '8', '9']       |   |
 7 | 8 | 9
   |   |
-----------
   |   |
 4 | 5 | 6
   |   |
-----------
   |   |
 1 | 2 | 3
   |   |
The second to last board filled with X's could not possibly have happened (unless the X player skipped all of the O player's turns!) And the last board has strings of digits instead of X and O, which are invalid strings for the board. But the drawBoard() function doesn't care. It just prints the board parameter that it was passed. Computer programs only do exactly what you tell them, even if you tell them the wrong things to do. We will just make sure these invalid strings are not put into the passed list in the first place.

Letting the Player be X or O

def inputPlayerLetter():
    # Let's the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
The inputPlayerLetter() is a simple function. It asks if the player wants to be X or O, and will keep asking the player (with the while loop) until the player types in an X or O. Notice on line 26 that we automatically change the string returned by the call to input() to uppercase letters with the upper() string method.

The while loop's condition contains parentheses, which means the expression inside the parentheses is evaluated first. If the letter variable was set to 'X', the expression would evaluate like this:

while not (letter == 'X' or letter == 'O'):
    A downward arrow
while not ('X' == 'X' or 'X' == 'O'):
    A downward arrow
while not (True or False):
    A downward arrow
while not (True):
    A downward arrow
while not True:
    A downward arrow
while False:
As you can see, if letter has the value 'X' or 'O', then the loop's condition will be False and lets the program execution continue.

    # the first element in the list is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
This function returns a list with two items. The first item (that is, the string at index 0) will be the player's letter, and the second item (that is, the string at index 1) will be the computer's letter. This if-else statement chooses the appropriate list to return.

Deciding Who Goes First

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
The whoGoesFirst() function does a virtual coin flip to determine who goes first, the computer or the player. Instead of flipping an actual coin, this code gets a random number of either 0 or 1 by calling the random.randint() function. If this function call returns a 0, the whoGoesFirst() function returns the string 'computer'. Otherwise, the function returns the string 'player'. The code that calls this function will use the return value to know who will make the first move of the game.

Asking the Player to Play Again

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
The playAgain() function asks the player if they want to play another game. The function returns True if the player types in 'yes' or 'YES' or 'y' or anything that begins with the letter Y. For any other response, the function returns False. The order of the method calls on line 45 is important. The return value from the call to the input() function is a string that has its lower() method called on it. The lower() method returns another string (the lowercase string) and that string has its startswith() method called on it, passing the argument 'y'.

There is no loop, because we assume that if the user entered anything besides a string that begins with 'y', they want to stop playing. So, we only ask the player once.

Placing a mark on the Board

def makeMove(board, letter, move):
    board[move] = letter
The makeMove() function is very simple and only one line. The parameters are a list with ten strings named board, one of the player's letters (either 'X' or 'O') named letter, and a place on the board where that player wants to go (which is an integer from 1 to 9) named move.

But wait a second. You might think that this function doesn't do much. It seems to change one of the items in the board list to the value in letter. But because this code is in a function, the board parameter will be forgotten when we exit this function and leave the function's scope.

Actually, this is not the case. This is because lists (and dictionaries) are special when you pass them as arguments to functions. This is because you pass a reference to the list (or dictionary) and not the list itself. Let's learn about the difference between lists and list references.

List References

Try entering the following into the shell:

>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42
This makes sense from what we know so far. We assign 42 to the spam variable, and then we copy the value in spam and assign it to the variable cheese. When we later change the value in spam to 100, this doesn't affect the value in cheese. This is because spam and cheese are different variables that store different values.

But lists don't work this way. When you assign a list to a variable with the = sign, you are actually assigning a list reference to the variable. A reference is a value that points to some bit of data, and a list reference is a value that points to a list. Here is some code that will make this easier to understand. Type this into the shell:

>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese[1] = 'Hello!'
>>> spam
[0, 'Hello!', 2, 3, 4, 5]
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
This looks odd. The code only changed the cheese list, but it seems that both the cheese and spam lists have changed.

Notice that the line cheese = spam copies the list reference in spam to cheese, instead of copying the list value itself. This is because the value stored in the spam variable is a list reference, and not the list value itself. This means that the values stored in both spam and cheese refer to the same list. There is only one list because the list was not copied, the reference to the list was copied. So when you modify cheese in the cheese[1] = 'Hello!' line, you are modifying the same list that spam refers to. This is why spam seems to have the same list value that cheese does.

Remember that variables are like boxes that contain values. List variables don't actually contain lists at all, they contain references to lists. Here are some pictures that explain what happens in the code you just typed in:


Figure 10-5: Variables do no store lists, but rather references to lists.

On the first line, the actual list is not contained in the spam variable but a reference to the list. The list itself is not stored in any variable.


Figure 10-6: Two variables store two references to the same list.

When you assign the reference in spam to cheese, the cheese variable contains a copy of the reference in spam. Now both cheese and spam refer to the same list.


Figure 10-7: Changing the list changes all variables with references to that list.

When you alter the list that cheese refers to, the list that spam refers to is also changed because they are the same list. If you want spam and cheese to store two different lists, you have to create two different lists instead of copying a reference:

>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = [0, 1, 2, 3, 4, 5]
In the above example, spam and cheese have two different lists stored in them (even though these lists are identical in content). Now if you modify one of the lists, it will not affect the other because spam and cheese have references to two different lists:

>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = [0, 1, 2, 3, 4, 5]
>>> cheese[1] = 'Hello!'
>>> spam
[0, 1, 2, 3, 4, 5]
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
Figure 10-8 shows how the two references point to two different lists:


Figure 10-8: Two variables each storing references to two different lists.

Dictionaries work in the same way. Dictionaries do not store values, they store references to values. These are called dictionary references (or you can call both dictionary references and list references by the plain name, "reference".)

Using List References in makeMove()

Let's go back to the makeMove() function:

def makeMove(board, letter, move):
    board[move] = letter
When we pass a list value as the argument for the board parameter, the function's local variable is a copy of the reference, not a copy of the list itself. The letter and move parameters are copies of the string and integer values that we pass. Since they are copies, if we modify letter or move in this function, the original variables we used when we called makeMove() would not be modified. Only the copies would be modified.

But a copy of the reference still refers to the same list that the original reference refers to. So if we make changes to board in this function, the original list is modified. When we exit the makeMove() function, the copy of the reference is forgotten along with the other parameters. But since we were actually changing the original list, those changes remain after we exit the function. This is how the makeMove() function modifies the list that a reference of is passed.

Checking if the Player Has Won

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
Lines 53 to 60 in the isWinner() function are actually one very long if statement. We use bo and le for the board and letter parameters so that we have less to type in this function. (This is a trick programmers sometimes use to reduce the amount they need to type. Be sure to add a comment that explains this though, otherwise you may forget what bo and le are supposed to mean.)

There are eight possible ways to win at Tic Tac Toe. You can have a line across the top, middle, and bottom. Or you can have a line down the left, middle, or right. And you can have either of the two diagonals. Note that each line of the condition checks if the three spaces are equal to the letter provided (combined with the and operator) and we use the or operator to combine the eight different ways to win. This means only one of the eight ways must be true in order for us to say that the player who owns letter in le is the winner.

Let's pretend that le is 'O', and the board looks like this:

   |   |
 X |   |
   |   |
-----------
   |   |
   | X |
   |   |
-----------
   |   |
 O | O | O
   |   |
If the board looks like that, then bo must be equal to [' ', 'O', 'O', 'O', ' ', 'X', ' ', 'X', ' ', ' ']. Here is how the expression after the return keyword on line 53 would evaluate:

Here is the expression as it is in the code:

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))
            A downward arrow
First Python will replace the variable bo with the value inside of it:

    return (('X' == 'O' and ' ' == 'O' and ' ' == 'O') or
    (' ' == 'O' and 'X' == 'O' and ' ' == 'O') or
    ('O' == 'O' and 'O' == 'O' and 'O' == 'O') or
    ('X' == 'O' and ' ' == 'O' and 'O' == 'O') or
    (' ' == 'O' and 'X' == 'O' and 'O' == 'O') or
    (' ' == 'O' and ' ' == 'O' and 'O' == 'O') or
    ('X' == 'O' and 'X' == 'O' and 'O' == 'O') or
    (' ' == 'O' and 'X' == 'O' and 'O' == 'O'))
            A downward arrow
Next, Python will evaluate all those == comparisons inside the parentheses to a Boolean value:

    return ((False and False and False) or
    (False and False and False) or
    (True and True and True) or
    (False and False and True) or
    (False and False and True) or
    (False and False and True) or
    (False and False and True) or
    (False and False and True))
            A downward arrow
Then the Python interpreter will evaluate all those expressions inside the parentheses:

    return ((False) or
    (False) or
    (True) or
    (False) or
    (False) or
    (False) or
    (False) or
    (False))
            A downward arrow
Since now there is only one value inside the parentheses, we can get rid of them:

    return (False or
    False or
    True or
    False or
    False or
    False or
    False or
    False)
            A downward arrow
Now we evaluate the expression that is connecter by all those or operators:

    return (True)
            A downward arrow
Once again, we get rid of the parentheses, and we are left with one value:

    return True
So given those values for bo and le, the expression would evaluate to True. Remember that the value of le matters. If le is 'O' and X has won the game, the isWinner() would return False.

Duplicating the Board Data

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
The getBoardCopy() function is here so that we can easily make a copy of a given 10-string list that represents a Tic Tac Toe board in our game. There are times that we will want our AI algorithm to make temporary modifications to a temporary copy of the board without changing the original board. In that case, we call this function to make a copy of the board's list. The actual new list is created on line 64, with the blank list brackets [].

Line 64 actually creates a brand new list and stores a reference to it in dupeBoard. But the list stored in dupeBoard is just an empty list. The for loop will go through the board parameter, appending a copy of the string values in the original board to our duplicate board. Finally, after the loop, we will return the dupeBoard variable's reference to the duplicate board. So you can see how the getBoardCopy() function is building up a copy of the original board and returning a reference to this new board, and not the original one.

Checking if a Space on the Board is Free

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '
This is a simple function that, given a Tic Tac Toe board and a possible move, will return if that move is available or not. Remember that free spaces on our board lists are marked as a single space string.

Letting the Player Enter Their Move

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)
The getPlayerMove() function asks the player to enter the number for the space they wish to move. The function makes sure that they enter a space that is a valid space (an integer 1 through 9). It also checks that the space that is not already taken, given the Tic Tac Toe board passed to the function in the board parameter.

The two lines of code inside the while loop simply ask the player to enter a number from 1 to 9. The loop's condition will keep looping, that is, it will keep asking the player for a space, as long as the condition is True. The condition is True if either of the expressions on the left or right side of the or keyword is True.

The expression on the left side checks if the move that the player entered is equal to '1', '2', '3', and so on up to '9' by creating a list with these strings (with the split() method) and checking if move is in this list. '1 2 3 4 5 6 7 8 9'.split() evaluates to be the same as ['1', '2', '3', '4', '5', '6', '7', '8', '9'], but it easier to type.

The expression on the right side checks if the move that the player entered is a free space on the board. It checks this by calling the isSpaceFree() function we just wrote. Remember that isSpaceFree() will return True if the move we pass is available on the board. Note that isSpaceFree() expects an integer for move, so we use the int() function to evaluate an integer form of move.

We add the not operators to both sides so that the condition will be True when both of these requirements are unfulfilled. This will cause the loop to ask the player again and again until they enter a proper move.

Finally, on line 81, we will return the integer form of whatever move the player entered. Remember that input() returns a string, so we will want to use the int() function to evaluate the string as an integer.

Short-Circuit Evaluation

You may have noticed there is a possible problem in our getPlayerMove() function. What if the player typed in 'X' or some other non-integer string? The move not in '1 2 3 4 5 6 7 8 9'.split() expression on the left side of or would return False as expected, and then we would evaluate the expression on the right side of the or operator. But when we pass 'X' (which would be the value in move) to the int() function, int('X') would give us an error. It gives us this error because the int() function can only take strings of number characters, like '9' or '0', not strings like 'X'.

As an example of this kind of error, try entering this into the shell:

>>> int('42')
42
>>> int('X')

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int('X')
ValueError: invalid literal for int() with base 10: 'X'
But when you play our Tic Tac Toe game and try entering 'X' for your move, this error doesn't happen. The reason is because the while loop's condition is being short-circuited.

What short-circuiting means is that because the expression on the left side of the or keyword (move not in '1 2 3 4 5 6 7 8 9'.split()) evaluates to True, the Python interpreter knows that the entire expression will evaluate to True. It doesn't matter if the expression on the right side of the or keyword evaluates to True or False, because only one value on the side of the or operator needs to be True.

Think about it: The expression True or False evaluates to True and the expression True or True also evaluates to True. If the value on the left side is True, it doesn't matter what the value is on the right side. So Python stops checking the rest of the expression and doesn't even bother evaluating the not isSpaceFree(board, int(move)) part. This means the int() and the isSpaceFree() functions are never called as long as move not in '1 2 3 4 5 6 7 8 9'.split() is True.

This works out well for us, because if the expression on the right side is True then move is not a string in number form. That would cause int() to give us an error. The only times move not in '1 2 3 4 5 6 7 8 9'.split() evaluates to False are when move is a single-digit string. In that case, the call to int() would not give us an error.

An Example of Short-Circuit Evaluation

Here's a short program that gives a good example of short-circuiting. Open a new file in the IDLE editor and type in this program, save it as truefalsefizz.py, then press F5 to run it. Don't add the numbers down the left side of the program, those just appear in this book to make the program's explanation easier to understand. The function calls in bold are the function calls that are evaluated.

truefalsefizz.py
This code can be downloaded from http://inventwithpython.com/truefalsefizz.py
If you get errors after typing this code in, compare it to the book's code with the online diff tool at http://inventwithpython.com/diff or email the author at al@inventwithpython.com
def TrueFizz(message):
    print(message)
    return True
def FalseFizz(message):
    print(message)
    return False
if FalseFizz('Cats') or TrueFizz('Dogs'):
   print('Step 1')
if TrueFizz('Hello') or TrueFizz('Goodbye'):
    print('Step 2')
if TrueFizz('Spam') and TrueFizz('Cheese'):
    print('Step 3')
if FalseFizz('Red') and TrueFizz('Blue'):
    print('Step 4')
When you run this program, you can see the output (the letters on the left side have been added to make the output's explanation easier to understand):

Cats
Dogs
Step 1
Hello
Step 2
Spam
Cheese
Step 3
Red
This small program has two functions: TrueFizz() and FalseFizz(). TrueFizz() will display a message and return the value True, while FalseFizz() will display a message and return the value False. This lets us determine if these functions are being called, or if these functions are being skipped due to short-circuiting.

The First if Statement (Cats and Dogs)

The first if statement on line 9 in our small program will first evaluate TrueFizz(). We know this happens because Cats is printed to the screen (on line A in the output). The entire expression could still be True if the expression to the right of the or keyword is True. So the call TrueFizz('Dogs') on line 9 is evaluated, Dogs is printed to the screen (on line B in the output) and True is returned. On line 9, the if statement's condition evaluates to False or True, which in turn evaluates to True. 'Step 1' is then printed to the screen. No short-circuiting took place for this expression's evaluation.

The Second if Statement (Hello and Goodbye)

The second if statement on line 12 also has short-circuiting. This is because when we call TrueFizz('Hello') on line 12, it prints Hello (see line D in the output) and returns True. The Python interpreter doesn't call TrueFizz('Goodbye') because it doesn't matter what is on the right side of the or keyword. You can tell it is not called because Goodbye is not printed to the screen. The if statement's condition is True, so 'Step 2' is printed to the screen (see line E).

The Third if Statement (Spam and Cheese)

The third if statement on line 15 does not have short-circuiting. The call to TrueFizz('Spam') returns True, but we do not know if the entire condition is True or False because of the and operator. So Python will call TrueFizz('Cheese'), which prints Cheese and returns True. The if statement's condition is evaluated to True and True, which in turn evaluates to True. Because the condition is True, 'Step 3' is printed to the screen (see line H).

The Fourth if Statement (Red and Blue)

The fourth if statement on line 18 does have short-circuiting. The FalseFizz('Red') call prints Red (see line I in the output) and returns False. Because the left side of the and keyword is False, it does not matter if the right side is True or False, the condition will evaluate to False anyway. So TrueFizz('Blue') is not called and Blue does not appear on the screen. Because the if statement's condition evaluated to False, 'Step 4' is also not printed to the screen.

Short-circuiting can happen for any expression that includes the Boolean operators and and or. It is important to remember that this can happen; otherwise you may find that some function calls in the expression are never called and you will not understand why.

How the Code Works: Lines 83 to 94

Choosing a Move from a List of Moves

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
The chooseRandomMoveFromList() function will be of use to us when we are implementing the code for our AI. The first parameter board is the 10-string list that represents a Tic Tac Toe board. The second parameter movesList is a list of integers that represent possible moves. For example, if movesList is [1, 3, 7, 9], that means we should return the number for one of the corner spaces on the board.

The chooseRandomMoveFromList() function will then choose one of those moves from the possibleMoves list. It also makes sure that the move that it chooses is not already taken. To do this, we create a blank list and assign it to possibleMoves. The for loop will go through the list of moves passed to this function in movesList. If that move is available (which we figure out with a call to isSpaceFree()), then we add it to possibleMoves with the append() method.

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
At this point, the possibleMoves list has all of the moves that were in movesList that are also free spaces on the board represented by board. If the list is not empty, then there is at least one possible move that can be made on the board.

This list might be empty. For example, if movesList was [1, 3, 7, 9] but the board represented by the board parameter had all the corner spaces already taken, the possibleMoves list would have been empty.

If possibleMoves is empty, then len(possibleMoves) will evaluate to 0 and the code in the else-block will execute. Notice that it returns something called None.

The None Value

None is a special value that you can assign to a variable. The None value represents the lack of a value. None is the only value of the data type NoneType. (Just like the Boolean data type has only two values, the NoneType data type has only one value, None.) It can be very useful to use the None value when you need a value that means "does not exist". For example, say you had a variable named quizAnswer which holds the user's answer to some True-False pop quiz question. You could set quizAnswer to None if the user skipped the question and did not answer it. Using None would be better because if you set it to True or False before assigning the value of the user's answer, it may look like the user gave an answer the question even though they didn't.

Calls to functions that do not return anything (that is, they exit by reaching the end of the function and not from a return statement) will evaluate to None. The None value is written without quotes and with a capital "N" and lowercase "one".

How the Code Works: Lines 96 to 187

Creating the Computer's Artificial Intelligence

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
The getComputerMove() function is where our AI will be coded. The arguments are a Tic Tac Toe board (in the board parameter) and which letter the computer is (either 'X' or 'O' in the computerLetter parameter). The first few lines simply assign the other letter to a variable named playerLetter. This lets us use the same code, no matter who is X and who is O. This function will return the integer 1 to 9 that represents which space the computer will move.

Remember how our algorithm works: First, see if there is a move the computer can make that will win the game. If there is, take that move. Otherwise, go to the second step.

Second, see if there is a move the player can make that will cause the computer to lose the game. If there is, we should move there to block the player. Otherwise, go to the third step.

Third, check if any of the corner spaces (spaces 1, 3, 7, or 9) are free. (We always want to take a corner piece instead of the center or a side piece.) If no corner piece is free, then go to the fourth step.

Fourth, check if the center is free. If so, move there. If it isn't, then go to the fifth step.

Fifth, move on any of the side pieces (spaces 2, 4, 6, or 8). There are no more steps, because if we have reached this step then the side spaces are the only spaces left.

The Computer Checks if it Can Win in One Move

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
More than anything, if the computer can win in the next move, the computer should immediately make that winning move. We will do this by trying each of the nine spaces on the board with a for loop. The first line in the loop (line 106) makes a copy of the board list. We want to make a move on the copy of the board, and then see if that move results in the computer winning. We don't want to modify the original Tic Tac Toe board, which is why we make a call to getBoardCopy(). We check if the space we will move is free, and if so, we move on that space and see if this results in winning. If it does, we return that space's integer.

If moving on none of the spaces results in winning, then the loop will finally end and we move on to line 112.

The Computer Checks if the Player Can Win in One Move

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
At this point, we know we cannot win in one move. So we want to make sure the human player cannot win in one more move. The code is very similar, except on the copy of the board, we place the player's letter before calling the isWinner() function. If there is a position the player can move that will let them win, the computer should move there to block that move.

If the human player cannot win in one more move, the for loop will eventually stop and execution continues on to line 120.

Checking the Corner, Center, and Side Spaces (in that Order)

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
Our call to chooseRandomMoveFromList() with the list of [1, 3, 7, 9] will ensure that it returns the integer for one of the corner spaces. (Remember, the corner spaces are represented by the integers 1, 3, 7, and 9.) If all the corner spaces are taken, our chooseRandomMoveFromList() function will return the None value. In that case, we will move on to line 125.

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5
If none of the corners are available, we will try to move on the center space if it is free. If the center space is not free, the execution moves on to line 129.

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
This code also makes a call to chooseRandomMoveFromList(), except we pass it a list of the side spaces ([2, 4, 6, 8]). We know that this function will not return None, because the side spaces are the only spaces we have not yet checked. This is the end of the getComputerMove() function and our AI algorithm.

Checking if the Board is Full

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
The last function we will write is isBoardFull(), which returns True if the 10-string list board argument it was passed has an 'X' or 'O' in every index (except for index 0, which is just a placeholder that we ignore). If there is at least one space in board that is set to a single space ' ' then it will return False.

The for loop will let us check spaces 1 through 9 on the Tic Tac Toe board. (Remember that range(1, 10) will make the for loop iterate over the integers 1, 2, 3, 4, 5, 6, 7, 8, and 9.) As soon as it finds a free space in the board (that is, when isSpaceFree(board, i) returns True), the isBoardFull() function will return False.

If execution manages to go through every iteration of the loop, we will know that none of the spaces are free. So at that point (on line 137), we will execute return True.

The Start of the Game

print('Welcome to Tic Tac Toe!')
Line 140 is the first line that isn't inside of a function, so it is the first line of code that is executed when we run this program.

while True:
    # Reset the board
    theBoard = [' '] * 10
This while loop has True for the condition, so that means we will keep looping in this loop until we encounter a break statement. Line 144 sets up the main Tic Tac Toe board that we will use, named theBoard. It is a 10-string list, where each string is a single space ' '. Remember the little trick using the multiplication operator with a list to replicate it: [' '] * 10. That evaluates to [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], but is shorter for us to type [' '] * 10.

Deciding the Player's Mark and Who Goes First

    playerLetter, computerLetter = inputPlayerLetter()
The inputPlayerLetter() function lets the player type in whether they want to be X or O. The function returns a 2-string list, either ['X', 'O'] or ['O', 'X']. We use the multiple assignment trick here that we learned in the Hangman chapter. If inputPlayerLetter() returns ['X', 'O'], then playerLetter is set to 'X' and computerLetter is set to 'O'. If inputPlayerLetter() returns ['O', 'X'], then playerLetter is set to 'O' and computerLetter is set to 'X'.

    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
The whoGoesFirst() function randomly decides who goes first, and returns either the string 'player' or the string 'computer'. On line 147, we tell the player who will go first. The gameIsPlayer variable is what we will use to keep track of whether the game has been won, lost, tied or if it is the other player's turn.

Running the Player's Turn

    while gameIsPlaying:
This is a loop that will keep going back and forth between the player's turn and the computer's turn, as long as gameIsPlaying is set to True.

        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
The turn variable was originally set by the whoGoesFirst() call on line 146). It is either set to 'player' or 'computer'. If turn contains the string 'computer', then the condition is False and execution will jump down to line 169.

The first thing we do when it is the player's turn (according to the flow chart we drew at the beginning of this chapter) is show the board to the player. Calling the drawBoard() and passing the theBoard variable will print the board on the screen. We then let the player type in his move by calling our getPlayerMove() function, and set the move on the board by calling our makeMove() function.

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
Now that the player has made his move, our program should check if they have won the game with this move. If the isWinner() function returns True, we should show them the winning board (the previous call to drawBoard() shows the board before they made the winning move) and print a message telling them they have won.

Then we set gameIsPlaying to False so that execution does not continue on to the computer's turn.

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
If the player did not win with his last move, then maybe his last move filled up the entire board and we now have a tie. In this else-block, we check if the board is full with a call to the isBoardFull() function. If it returns True, then we should draw the board by calling drawBoard() and tell the player a tie has occurred. The break statement will break us out of the while loop we are in and jump down to line 186.

Running the Computer's Turn

                else:
                    turn = 'computer'
If the player has not won or tied the game, then we should just set the turn variable to 'computer' so that when this while loop loops back to the start it will execute the code for the computer's turn.

        else:
If the turn variable was not set to 'player' for the condition on line 151, then we know it is the computer's turn and the code in this else-block will execute. This code is very similar to the code for the player's turn, except the computer does not need the board printed on the screen so we skip calling the drawBoard() function.

            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
The code above is almost identical to the code for the player's turn on lines 154 and 155.

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
We want to check if the computer won with its last move. The reason we call drawBoard() here is because the player will want to see what move the computer made to win the game. We then set gameIsPlaying to False so that the game does not continue. Notice that lines 174 to 177 are almost identical to lines 157 to 160.

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
The lines of code above are identical to the code on lines 162 to 165. The only difference is this is a check for a tied game after the computer has moved, instead of the player.

                else:
                    turn = 'player'
If the game is neither won nor tied, it then becomes the player's turn. There are no more lines of code inside the while loop, so execution would jump back to the while statement on line 150.

    if not playAgain():
        break
These lines of code are located immediately after the while-block started by the while statement on line 150. Remember, we would only exit out of that while loop if it's condition (the gameIsPlaying variable) was False. gameIsPlaying is set to False when the game has ended, so at this point we are going to ask the player if they want to play again.

Remember, when we evaluate the condition in this if statement, we call the playAgain() function which will let the user type in if they want to play or not. playAgain() will return True if the player typed something that began with a 'y' like 'yes' or 'y'. Otherwise playAgain() will return False.

If playAgain() returns False, then the if statement's condition is True (because of the not operator that reverses the Boolean value) and we execute the break statement. That breaks us out of the while loop that was started on line 142. But there are no more lines of code after that while-block, so the program terminates.

Summary: Creating Game-Playing Artificial Intelligences

Creating a program that can play a game comes down to carefully considering all the possible situations the AI can be in and how it should respond in each of those situations. Our Tic Tac Toe AI is fairly simple because there are not many possible moves in Tic Tac Toe compared to a game like chess or checkers.

Our AI simply blocks the players move if the player is about to win. If the player is not about to win, it checks if any possible move can allow itself to win. Then the AI simply chooses any available corner space, then the center space, then the side spaces. This is a simple algorithm for the computer to follow.

The key to implementing our AI is by making copies of the board data and simulating moves on the copy. That way, the AI code can see if a move will result in a win or loss. Then the AI can make that move on the real board. This type of simulation is very effective at predicting what is a good move or not.
