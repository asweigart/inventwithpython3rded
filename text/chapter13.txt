Chapter 13 - Sonar Treasure Hunt

Topics Covered In This Chapter:

Data structures.
The remove() list method.
The isdigit() string method.
The sys.exit() function.
The game in this chapter only introduces a couple new helpful methods that come with Python, the remove() list method and the isdigit() string method. But this is the first program which will make use of Cartesian coordinates and the mathematical concepts we learned in chapter 11. This program will also use make use of data structures (which is really just a fancy way of saying variables that contain lists of lists.) As our games become more complicated, we will need to store our data in well-organized ways.

Sonar is a technology that ships use to locate objects under the sea. In this chapter's game, the player places sonar devices at various places in the ocean to locate sunken treasure chests. The sonar devices (in our game) can tell the player how far away a treasure chest is from the sonar device, but not in what direction. But by placing multiple sonar devices down, the player can figure out where exactly the treasure chest is.

There are three chests to collect, but the player has only sixteen sonar devices to use to find them. Imagine that we could not see the treasure chest in the following picture. Because each sonar device can only find the distance but not direction, the possible places the treasure could be is anywhere in a ring around the sonar device (see Figure 13-1).


Figure 13-1: The first sonar device shows a ring
of possible places the treasure could be located.


Figure 13-2: Combining the rings of all three sonar
devices shows only one possible place for the treasure.

But if we have multiple sonar devices working together, we can narrow it down to an exact place where all the rings intersect each other. (See Figure 13-2)

Sample Run

S O N A R !

Would you like to view the instructions? (yes/no)
no
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 `~~~`~~~`~`~~`~~~~~`~``~~~~`~`~~~`~``~``~~````~`~```~`~~~~`` 0
 1 ~`~~~```~~~~`~`~~`~``~`~~```~`~`~~`~`~~~~~~`~`````~`~~`~~~~` 1
 2 `~``~``~~~`~``~`~`~``~`````~~~~~~~~~`~`~~`~``~~~~~```~~`~``` 2
 3 ``~`~~``~`~``~`~`~`~~`~`~~`~`~``~~~`~``~````~``````~~~~``~`` 3
 4 ``~~`~~~``~``~~````~`~`~`~``~~~``~~```~`~~`~~`~`~`~~`~~~~``` 4
 5 ~~```~~~`~`~~``~`~``~```~`~~`~~~~~`~~``~`~`~~~`~~`~`~`~`~~~` 5
 6 ``~~`````~~~~`~`~~~```~~~~`~~`~~`~~```~~`~~~`~~~``~`~~~``~~~ 6
 7 `~`````````~```~``~``~~`~~~~`~~``~``~~~```~`~~`~``~``~~```~~ 7
 8 `~````~```~`~~`~~~`~~``~~~``~`~``~~~``~`~`````~`~~```~`~~~~` 8
 9 ~```~~`~`~``~``~~``~``~```~`~``~~~~`~`~`~~~`~`~`~`~~~``~~``` 9
10 ```~`~```~``~``~`~~`~``~````~``~~~`~~`~~``~~~~`~~~`~`~~````~ 10
11 ```~```~~~`~```~~`~~~`~`````~`~~`~`~~`~~`~`~~`~~~````~````~` 11
12 ~~~`~`~~~``~~~~~~`~~~``~`~`~~`~`~~`~```~~~```~~`~~`~``~``~`~ 12
13 `~~````~~``~```~~~`~```~`~~~~~~~~~`~~``~~~~~`````~`~`~``~~~~ 13
14 `~~`~`~````~```~`~`~```~~`~~~~`~```~``~``~``~~~````~~``````~ 14

   012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
You have 16 sonar devices left. 3 treasure chests remaining.
Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
10 10
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 `~~~`~~~`~`~~`~~~~~`~``~~~~`~`~~~`~``~``~~````~`~```~`~~~~`` 0
 1 ~`~~~```~~~~`~`~~`~``~`~~```~`~`~~`~`~~~~~~`~`````~`~~`~~~~` 1
 2 `~``~``~~~`~``~`~`~``~`````~~~~~~~~~`~`~~`~``~~~~~```~~`~``` 2
 3 ``~`~~``~`~``~`~`~`~~`~`~~`~`~``~~~`~``~````~``````~~~~``~`` 3
 4 ``~~`~~~``~``~~````~`~`~`~``~~~``~~```~`~~`~~`~`~`~~`~~~~``` 4
 5 ~~```~~~`~`~~``~`~``~```~`~~`~~~~~`~~``~`~`~~~`~~`~`~`~`~~~` 5
 6 ``~~`````~~~~`~`~~~```~~~~`~~`~~`~~```~~`~~~`~~~``~`~~~``~~~ 6
 7 `~`````````~```~``~``~~`~~~~`~~``~``~~~```~`~~`~``~``~~```~~ 7
 8 `~````~```~`~~`~~~`~~``~~~``~`~``~~~``~`~`````~`~~```~`~~~~` 8
 9 ~```~~`~`~``~``~~``~``~```~`~``~~~~`~`~`~~~`~`~`~`~~~``~~``` 9
10 ```~`~```~5`~``~`~~`~``~````~``~~~`~~`~~``~~~~`~~~`~`~~````~ 10
11 ```~```~~~`~```~~`~~~`~`````~`~~`~`~~`~~`~`~~`~~~````~````~` 11
12 ~~~`~`~~~``~~~~~~`~~~``~`~`~~`~`~~`~```~~~```~~`~~`~``~``~`~ 12
13 `~~````~~``~```~~~`~```~`~~~~~~~~~`~~``~~~~~`````~`~`~``~~~~ 13
14 `~~`~`~````~```~`~`~```~~`~~~~`~```~``~``~``~~~````~~``````~ 14

   012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
Treasure detected at a distance of 5 from the sonar device.
You have 15 sonar devices left. 3 treasure chests remaining.
Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
15 6
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 `~~~`~~~`~`~~`~~~~~`~``~~~~`~`~~~`~``~``~~````~`~```~`~~~~`` 0
 1 ~`~~~```~~~~`~`~~`~``~`~~```~`~`~~`~`~~~~~~`~`````~`~~`~~~~` 1
 2 `~``~``~~~`~``~`~`~``~`````~~~~~~~~~`~`~~`~``~~~~~```~~`~``` 2
 3 ``~`~~``~`~``~`~`~`~~`~`~~`~`~``~~~`~``~````~``````~~~~``~`` 3
 4 ``~~`~~~``~``~~````~`~`~`~``~~~``~~```~`~~`~~`~`~`~~`~~~~``` 4
 5 ~~```~~~`~`~~``~`~``~```~`~~`~~~~~`~~``~`~`~~~`~~`~`~`~`~~~` 5
 6 ``~~`````~~~~`~4~~~```~~~~`~~`~~`~~```~~`~~~`~~~``~`~~~``~~~ 6
 7 `~`````````~```~``~``~~`~~~~`~~``~``~~~```~`~~`~``~``~~```~~ 7
 8 `~````~```~`~~`~~~`~~``~~~``~`~``~~~``~`~`````~`~~```~`~~~~` 8
 9 ~```~~`~`~``~``~~``~``~```~`~``~~~~`~`~`~~~`~`~`~`~~~``~~``` 9
10 ```~`~```~5`~``~`~~`~``~````~``~~~`~~`~~``~~~~`~~~`~`~~````~ 10
11 ```~```~~~`~```~~`~~~`~`````~`~~`~`~~`~~`~`~~`~~~````~````~` 11
12 ~~~`~`~~~``~~~~~~`~~~``~`~`~~`~`~~`~```~~~```~~`~~`~``~``~`~ 12
13 `~~````~~``~```~~~`~```~`~~~~~~~~~`~~``~~~~~`````~`~`~``~~~~ 13
14 `~~`~`~````~```~`~`~```~~`~~~~`~```~``~``~``~~~````~~``````~ 14

   012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
Treasure detected at a distance of 4 from the sonar device.
You have 14 sonar devices left. 3 treasure chests remaining.
Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
15 10
             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 `~~~`~~~`~`~~`~~~~~`~``~~~~`~`~~~`~``~``~~````~`~```~`~~~~`` 0
 1 ~`~~~```~~~~`~`~~`~``~`~~```~`~`~~`~`~~~~~~`~`````~`~~`~~~~` 1
 2 `~``~``~~~`~``~`~`~``~`````~~~~~~~~~`~`~~`~``~~~~~```~~`~``` 2
 3 ``~`~~``~`~``~`~`~`~~`~`~~`~`~``~~~`~``~````~``````~~~~``~`` 3
 4 ``~~`~~~``~``~~````~`~`~`~``~~~``~~```~`~~`~~`~`~`~~`~~~~``` 4
 5 ~~```~~~`~`~~``~`~``~```~`~~`~~~~~`~~``~`~`~~~`~~`~`~`~`~~~` 5
 6 ``~~`````~~~~`~O~~~```~~~~`~~`~~`~~```~~`~~~`~~~``~`~~~``~~~ 6
 7 `~`````````~```~``~``~~`~~~~`~~``~``~~~```~`~~`~``~``~~```~~ 7
 8 `~````~```~`~~`~~~`~~``~~~``~`~``~~~``~`~`````~`~~```~`~~~~` 8
 9 ~```~~`~`~``~``~~``~``~```~`~``~~~~`~`~`~~~`~`~`~`~~~``~~``` 9
10 ```~`~```~O`~``O`~~`~``~````~``~~~`~~`~~``~~~~`~~~`~`~~````~ 10
11 ```~```~~~`~```~~`~~~`~`````~`~~`~`~~`~~`~`~~`~~~````~````~` 11
12 ~~~`~`~~~``~~~~~~`~~~``~`~`~~`~`~~`~```~~~```~~`~~`~``~``~`~ 12
13 `~~````~~``~```~~~`~```~`~~~~~~~~~`~~``~~~~~`````~`~`~``~~~~ 13
14 `~~`~`~````~```~`~`~```~~`~~~~`~```~``~``~``~~~````~~``````~ 14

   012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
You have found a sunken treasure chest!
You have 13 sonar devices left. 2 treasure chests remaining.
Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)


...skipped over for brevity....


             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 `~~~`~~~`~`~~`~~~~~`~``~~~~`~`~~~`~``~``~~````~`~```~`~~~~`` 0
 1 ~`~~~```~~~~`~`~~`~``~`~~```~O~`~~`~`~~~~~~`~`````~`~~`~~~~` 1
 2 `~``~``~~~`~``~`~`~``~`````~~O~~~O~~`~`~~`~``~~~~~```~~`~``` 2
 3 ``~3~~``8`~``~`~`~`~~`~`~~`~`~``~~~`~`O~````~``````~~~~``~`` 3
 4 ``~~`~~~``~``~~````~`~`~`~O`~~O``~~```~`~~`~~`~`~`~~`~~~~``` 4
 5 ~~```~~~`~`~~``~`~``~```~`~~`~~~~~`~~``~`~`~~~`~~`~`~`~`~~~` 5
 6 ``~~`````~~~~`~O~~~```~~~~`~~`~~`~~```~~`~~~`~~~``O`~~~``~~~ 6
 7 `~`````````~```~``~``~~`~~~~`~~``~``~~~```~`~~`~``~``~~```~~ 7
 8 `~````~```~`~~`~~~`~~``~~~``~`~``~~~``~`O```0`~`~~```~`~~~~` 8
 9 ~```~~`~`~``~``~~``~``~```~O~``~~~~`~`~`~~~`~`~`~`~~~``~~``` 9
10 ```~`~```~O`~``O`~~`~``~````~``~~~`~~`~~``~~~~`~~~`~`~~````~ 10
11 ```~```~~~`~```~~`~~~`~`````~`~~`~`~~`~~`~`~~`~~~````~````~` 11
12 ~~~`~`~~~``~~~~~~`~~~``~`~`~~`~`~~`~```~~~```~~`~~`~``~``~`~ 12
13 `~~````~~``~```~~~`~```~`~~~~~~~~~`~~``~~~~~`````~`~`~``~~~~ 13
14 `~~`~`~````~```~`~`~```~~`~~~~`~```~``~``~``~~~````~~``````~ 14

   012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
Treasure detected at a distance of 4 from the sonar device.
We've run out of sonar devices! Now we have to turn the ship around and head
for home with treasure chests still out there! Game over.
    The remaining chests were here:
    0, 4
Do you want to play again? (yes or no)
no
Sonar's Source Code

Knowing about Cartesian coordinates, number lines, negative numbers, and absolute values will help us out with our Sonar game. If you do not think you understand these concepts, go back to chapter 12. Below is the source code for the game. Type it into a new file, then save the file as sonar.py and run it by pressing the F5 key. You do not need to understand the code to type it in or play the game, the source code will be explained later.

Also, you can download the source code from the book's website at the URL http://inventwithpython.com/chapter13.

sonar.py
This code can be downloaded from http://inventwithpython.com/sonar.py
If you get errors after typing this code in, compare it to the book's code with the online diff tool at http://inventwithpython.com/diff or email the author at al@inventwithpython.com
# Sonar
import random
import sys
def drawBoard(board):
    # Draw the board data structure.
    hline = '    ' # initial space for the numbers down the left side of the board
    for i in range(1, 6):
        hline += (' ' * 9) + str(i)
    # print the numbers across the top
    print(hline)
    print('   ' + ('0123456789' * 6))
    print()
    # print each of the 15 rows
    for i in range(15):
        # single-digit numbers need to be padded with an extra space
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print('%s%s %s %s' % (extraSpace, i, getRow(board, i), i))
    # print the numbers across the bottom
    print()
    print('   ' + ('0123456789' * 6))
    print(hline)
def getRow(board, row):
    # Return a string from the board data structure at a certain row.
    boardRow = ''
    for i in range(60):
        boardRow += board[i][row]
    return boardRow
def getNewBoard():
    # Create a new 60x15 board data structure.
    board = []
    for x in range(60): # the main list is a list of 60 lists
        board.append([])
        for y in range(15): # each list in the main list has 15 single-character strings
            # use different characters for the ocean to make it more readable.
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board
def getRandomChests(numChests):
    # Create a list of chest data structures (two-item lists of x, y int coordinates)
    chests = []
    for i in range(numChests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])
    return chests
def isValidMove(x, y):
    # Return True if the coordinates are on the board, otherwise False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14
def makeMove(board, chests, x, y):
    # Change the board data structure with a sonar device character. Remove treasure chests
    # from the chests list as they are found. Return False if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    if not isValidMove(x, y):
        return False
    smallestDistance = 100 # any chest will be closer than 100.
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)
        if distance < smallestDistance: # we want the closest treasure chest.
            smallestDistance = distance
    if smallestDistance == 0:
        # xy is directly on a treasure chest!
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
        else:
            board[x][y] = 'O'
            return 'Sonar did not detect anything. All treasure chests out of range.'
def enterPlayerMove():
    # Let the player type in her move. Return a two-item list of int xy coordinates.
    print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]), int(move[1])):
            return [int(move[0]), int(move[1])]
        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
def showInstructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to find the three sunken treasure chests that are lurking in the part of the
ocean you are in and collect them.
To play, enter the coordinates of the point in the ocean you wish to drop a
sonar device. The sonar can find out how far away the closest chest is to it.
For example, the d below marks where the device was dropped, and the 2's
represent distances of 2 away from the device. The 4's represent
distances of 4 away from the device.
    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
Press enter to continue...''')
    input()
    print('''For example, here is a treasure chest (the c) located a distance of 2 away
from the sonar device (the d):
    22222
    c   2
    2 d 2
    2   2
    22222
The point where the device was dropped will be marked with a d.
The treasure chests don't move around. Sonar devices can detect treasure
chests up to a distance of 9. If all chests are out of range, the point
will be marked with O
If a device is directly dropped on a treasure chest, you have discovered
the location of the chest, and it will be collected. The sonar device will
remain there.
When you collect a chest, all sonar devices will update to locate the next
closest sunken treasure chest.
Press enter to continue...''')
    input()
    print()
print('S O N A R !')
print()
print('Would you like to view the instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()
while True:
    # game setup
    sonarDevices = 16
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []
    while sonarDevices > 0:
        # Start of a turn:
        # show sonar device/chest status
        if sonarDevices > 1: extraSsonar = 's'
        else: extraSsonar = ''
        if len(theChests) > 1: extraSchest = 's'
        else: extraSchest = ''
        print('You have %s sonar device%s left. %s treasure chest%s remaining.' % (sonarDevices, extraSsonar, len(theChests), extraSchest))
        x, y = enterPlayerMove()
        previousMoves.append([x, y]) # we must track all moves so that sonar devices can be updated.
        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'You have found a sunken treasure chest!':
                # update all the sonar devices currently on the map.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)
        if len(theChests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game!')
            break
        sonarDevices -= 1
    if sonarDevices == 0:
        print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print('for home with treasure chests still out there! Game over.')
        print('    The remaining chests were here:')
        for x, y in theChests:
            print('    %s, %s' % (x, y))
    if not playAgain():
        sys.exit()
Designing the Program

Sonar is kind of complicated, so it might be better to type in the game's code and play it a few times first to understand what is going on. After you've played the game a few times, you can kind of get an idea of the sequence of events in this game.

The Sonar game uses lists of lists and other complicated variables. These complicated variables are known as data structures. Data structures will let us store arrangements of values in a single variable to represent something (such as the locations of the treasure chests in Sonar). We will use data structures for the locations of the treasure chests and dropped sonar devices. One example of a data structure was the board variable in the Tic Tac Toe chapter.

It is also helpful to write out the things we need our program to do, and come up with some function names that will handle these actions. Remember to name functions after what they specifically do. Otherwise we might end up forgetting a function, or typing in two different functions that do the same thing.

Table 13-1: A list of each function the Sonar game needs.
What the code should do.    The function that will do it.
Prints the game board on the screen based on the board data structure it is passed, including the coordinates along the top, bottom, and left and right sides.  drawBoard()
Create a fresh board data structure.    getNewBoard()
Create a fresh chests data structure that has a number of chests randomly scattered across the game board.  getRandomChests()
Check that the XY coordinates that are passed to this function are located on the game board or not.    isValidMove()
Let the player type in the XY coordinates of his next move, and keep asking until they type in the coordinates correctly.   enterPlayerMove()
Place a sonar device on the game board, and update the board data structure then return a string that describes what happened.  makeMove()
Ask the player if they want to play another game of Sonar.  playAgain()
Print out instructions for the game.    showInstructions()
These might not be all of the functions we need, but a list like this is a good idea to help you get started with programming your own games. For example, when designing the drawBoard() function in the Sonar game, we find out we also need a function that does what getRow() does. Writing out a function once and then calling it twice is preferable to writing out the code twice. The whole point of functions is to reduce duplicate code down to one place, so if we ever need to make changes to that code we only need to change one place in our program.

How the Code Works: Lines 1 to 38

# Sonar
import random
import sys
Here we import two modules, random and sys. The sys module contains the exit() function, which causes the program to immediately terminate. We will call this function later in our program.

Drawing the Game Board

def drawBoard(board):
The back tick (`) and tilde (~) characters are located next to the 1 key on your keyboard. They resemble the waves of the ocean. Somewhere in this ocean are three treasure chests, but you don't know where. You can figure it out by planting sonar devices, and tell the game program where by typing in the X and Y coordinates (which are printed on the four sides of the screen.)

The drawBoard() function is the first function we will define for our program. The sonar game's board is an ASCII-art ocean with coordinates going along the X- and Y-axis, and looks like this:

             1         2         3         4         5
   012345678901234567890123456789012345678901234567890123456789

 0 ~~~`~``~~~``~~~~``~`~`~`~`~~`~~~`~~`~``````~~`~``~`~~```~`~` 0
 1 `~`~````~~``~`~```~```~```~`~~~``~~`~~~``````~`~``~~``~~`~~` 1
 2 ```~~~~`~`~~```~~~``~````~~`~`~~`~`~`~```~~`~``~~`~`~~~~~~`~ 2
 3 ~~~~`~~~``~```~``~~`~`~~`~`~~``~````~`~````~```~`~`~`~`````~ 3
 4 ~```~~~~~`~~````~~~~```~~~`~`~`~````~`~~`~`~~``~~`~``~`~``~~ 4
 5 `~```~`~`~~`~~~```~~``~``````~~``~`~`~~~~`~~``~~~~~~`~```~~` 5
 6 ``~~`~~`~``~`````~````~~``~`~~~~`~~```~~~``~`~`~~``~~~```~~~ 6
 7 ``~``~~~~~~```~`~```~~~``~`~``~`~~~~~~```````~~~`~~`~~`~~`~~ 7
 8 ~~`~`~~```~``~~``~~~``~~`~`~~`~`~```~```~~~```~~~~~~`~`~~~~` 8
 9 ```~``~`~~~`~~```~``~``~~~```~````~```~`~~`~~~~~`~``~~~~~``` 9
10 `~~~~```~`~````~`~`~~``~`~~~~`~``~``~```~~```````~`~``~````` 10
11 ~~`~`~~`~``~`~~~````````````````~~`````~`~~``~`~~~~`~~~`~~`~ 11
12 ~~`~~~~```~~~`````~~``~`~`~~``````~`~~``~```````~~``~~~`~~`~ 12
13 `~``````~~``~`~~~```~~~~```~~`~`~~~`~```````~~`~```~``~`~~~~ 13
14 ~~~``~```~`````~~`~`~``~~`~``~`~~`~`~``~`~``~~``~`~``~```~~~ 14

   012345678901234567890123456789012345678901234567890123456789
             1         2         3         4         5
We will split up the drawing in the drawBoard() function into four steps. First, we create a string variable of the line with 1, 2, 3, 4, and 5 spaced out with wide gaps (to mark the coordinates for 10, 20, 30, 40, and 50). Second, we use that string to display the X-axis coordinates along the top of the screen. Third, we print each row of the ocean along with the Y-axis coordinates on both sides of the screen. And fourth, we print out the X-axis again at the bottom. Having the coordinates on all sides makes it easier for the player to move their finger along the spaces to see where exactly they want to plan a sonar device.

Drawing the X-coordinates Along the Top

    # Draw the board data structure.
    hline = '    ' # initial space for the numbers down the left side of the board
    for i in range(1, 6):
        hline += (' ' * 9) + str(i)
Let's look again at the top part of the board, this time with plus signs instead of blank spaces so we can count the spaces easier:


Figure 13-3: The spacing we use for printing the top of the game board.

The numbers on the first line which mark the tens position all have nine spaces in between them, and there are thirteen spaces in front of the 1. We are going to create a string with this line and store it in a variable named hline.

    # print the numbers across the top
    print(hline)
    print('   ' + ('0123456789' * 6))
    print()
To print the numbers across the top of the sonar board, we first print the contents of the hline variable. Then on the next line, we print three spaces (so that this row lines up correctly), and then print the string '012345678901234567890123456789012345678901234567890123456789'. But this is tedious to type into the source, so instead we type ('0123456789' * 6) which evaluates to the same string.

Drawing the Rows of the Ocean

    # print each of the 15 rows
    for i in range(15):
        # single-digit numbers need to be padded with an extra space
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print('%s%s %s %s' % (extraSpace, i, getRow(board, i), i))
Now we print the each row of the board, including the numbers down the side to label the Y-axis. We use the for loop to print rows 0 through 14 on the board, along with the row numbers on either side of the board.

We have a small problem. Numbers with only one digit (like 0, 1, 2, and so on) only take up one space when we print them out, but numbers with two digits (like 10, 11, and 12) take up two spaces. This means the rows might not line up and would look like this:

8 ~~`~`~~```~``~~``~~~``~~`~`~~`~`~```~```~~~```~~~~~~`~`~~~~` 8
9 ```~``~`~~~`~~```~``~``~~~```~````~```~`~~`~~~~~`~``~~~~~``` 9
10 `~~~~```~`~````~`~`~~``~`~~~~`~``~``~```~~```````~`~``~````` 10
11 ~~`~`~~`~``~`~~~````````````````~~`````~`~~``~`~~~~`~~~`~~`~ 11
The solution is easy. We just add a space in front of all the single-digit numbers. The if-else statement that starts on line 21 does this. We will print the variable extraSpace when we print the row, and if i is less than 10 (which means it will have only one digit), we assign a single space string to extraSpace. Otherwise, we set extraSpace to be a blank string. This way, all of our rows will line up when we print them.

The getRow() function will return a string representing the row number we pass it. Its two parameters are the board data structure stored in the board variable and a row number. We will look at this function next.

Drawing the X-coordinates Along the Bottom

    # print the numbers across the bottom
    print()
    print('   ' + ('0123456789' * 6))
    print(hline)
This code is similar to lines 13 to 16. This will print the X-axis coordinates along the bottom of the screen.

Getting the State of a Row in the Ocean

def getRow(board, row):
    # Return a string from the board data structure at a certain row.
    boardRow = ''
    for i in range(60):
        boardRow += board[i][row]
    return boardRow
This function constructs a string called boardRow from the characters stored in board. First we set boardRow to the blank string. The row number (which is the Y coordinate) is passed as a parameter. The string we want is made by concatenating board[0][row], board[1][row], board[2][row], and so on up to board[59][row]. (This is because the row is made up of 60 characters, from index 0 to index 59.)

The for loop iterates from integers 0 to 59. On each iteration the next character in the board data structure is copied on to the end of boardRow. By the time the loop is done, boardRow is fully formed, so we return it.

How the Code Works: Lines 40 to 62

Now that we have a function to print a given board data structure to the string, let's turn to the other functions that we will need. At the start of the game, we will need to create a new game board data structure (kind of like a blank Tic Tac Toe board) and also place treasure chests randomly around the board. We should also create a function that can tell if the coordinates entered by the player are a valid move or not.

Creating a New Game Board

def getNewBoard():
    # Create a new 60x15 board data structure.
    board = []
    for x in range(60): # the main list is a list of 60 lists
        board.append([])
At the start of each new game, we will need a fresh board data structure. The board data structure is a list of lists of strings. The first list represents the X coordinate. Since our game's board is 60 characters across, this first list needs to contain 60 lists. So we create a for loop that will append 60 blank lists to it.

        for y in range(15): # each list in the main list has 15 single-character strings
            # use different characters for the ocean to make it more readable.
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
But board is more than just a list of 60 blank lists. Each of the 60 lists represents the Y coordinate of our game board. There are 15 rows in the board, so each of these 60 lists must have 15 characters in them. We have another for loop to add 15 single-character strings that represent the ocean. The "ocean" will just be a bunch of '~' and '`' strings, so we will randomly choose between those two. We can do this by generating a random number between 0 and 1 with a call to random.randint(). If the return value of random.randint() is 0, we add the '~' string. Otherwise we will add the '`' string.

This is like deciding which character to use by tossing a coin. And since the return value from random.randint() will be 0 about half the time, half of the ocean characters will be '~' and the other half will be '`'. This will give our ocean a random, choppy look to it.

Remember that the board variable is a list of 60 lists that have 15 strings. That means to get the string at coordinate 26, 12, we would access board[26][12], and not board[12][26]. The X coordinate is first, then the Y coordinate.

Figure 13-4 is the picture to demonstrate the indexes of a list of lists named x. The red arrows point to indexes of the inner lists themselves. The image is also flipped on its side to make it easier to read:


Figure 13-4: The indexes of a list of lists.

    return board
Finally, we return the board variable. Remember that in this case, we are returning a reference to the list that we made. Any changes we made to the list (or the lists inside the list) in our function will still be there outside of the function.

Creating the Random Treasure Chests

def getRandomChests(numChests):
    # Create a list of chest data structures (two-item lists of x, y int coordinates)
    chests = []
    for i in range(numChests):
        chests.append([random.randint(0, 59), random.randint(0, 14)])
    return chests
Another task we need to do at the start of the game is decide where the hidden treasure chests are. We will represent the treasure chests in our game as a list of lists of two integers. These two integers will be the X and Y coordinates. For example, if the chest data structure was [[2, 2], [2, 4], [10, 0]], then this would mean there are three treasure chests, one at 2, 2, another at 2, 4, and a third one at 10, 0.

We will pass the numChests parameter to tell the function how many treasure chests we want it to generate. We set up a for loop to iterate this number of times, and on each iteration we append a list of two random integers. The X coordinate can be anywhere from 0 to 59, and the Y coordinate can be from anywhere between 0 and 14. The expression [random.randint(0, 59), random.randint(0, 14)] that is passed to the append method will evaluate to something like [2, 2] or [2, 4] or [10, 0]. This data structure is then returned.

Determining if a Move is Valid

def isValidMove(x, y):
    # Return True if the coordinates are on the board, otherwise False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14
The player will type in X and Y coordinates of where they want to drop a sonar device. But they may not type in coordinates that do not exist on the game board. The X coordinates must be between 0 and 59, and the Y coordinate must be between 0 and 14. This function uses a simple expression that uses and operators to ensure that each part of the condition is True. If just one is False, then the entire expression evaluates to False. This Boolean value is returned by the function.

How the Code Works: Lines 64 to 91

Placing a Move on the Board

def makeMove(board, chests, x, y):
    # Change the board data structure with a sonar device character. Remove treasure chests
    # from the chests list as they are found. Return False if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    if not isValidMove(x, y):
        return False
In our Sonar game, the game board is updated to display a number for each sonar device dropped. The number shows how far away the closest treasure chest is. So when the player makes a move by giving the program an X and Y coordinate, we will change the board based on the positions of the treasure chests. This is why our makeMove() function takes four parameters: the game board data structure, the treasure chests data structures, and the X and Y coordinates.

This function will return the False Boolean value if the X and Y coordinates if was passed do not exist on the game board. If isValidMove() returns False, then makeMove() will return False.

If the coordinates land directly on the treasure, makeMove() will return the string 'You have found a sunken treasure chest!'. If the XY coordinates are within a distance of 9 or less of a treasure chest, we return the string 'Treasure detected at a distance of %s from the sonar device.' (where %s is the distance). Otherwise, makeMove() will return the string 'Sonar did not detect anything. All treasure chests out of range.'.

    smallestDistance = 100 # any chest will be closer than 100.
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)
        if distance < smallestDistance: # we want the closest treasure chest.
            smallestDistance = distance
Given the XY coordinates of where the player wants to drop the sonar device, and a list of XY coordinates for the treasure chests (in the chests list of lists), we will need an algorithm to find out which treasure chest is closest.

An Algorithm for Finding the Closest Treasure Chest

While the x and y variables are just integers (say, 5 and 0), together they represent the location on the game board (which is a Cartesian coordinate system) where the player guessed. The chests variable may have a value such as [[5, 0], [0, 2], [4, 2]], that value represents the locations of three treasure chests. Even though these variables are a bunch of numbers, we can visualize it like this:


Figure 13-5: The places on the board that [[5, 0], [0, 2], [4, 2]] represents.

We figure out the distance from the sonar device located at 0, 2 with "rings" and the distances around it:


Figure 13-6: The board marked with distances from the 0, 2 position.

But how do we translate this into code for our game? We need a way to represent distance as an expression. Notice that the distance from an XY coordinate is always the larger of two values: the absolute value of the difference of the two X coordinates and the absolute value of the difference of the two Y coordinates.

That means we should subtract the sonar device's X coordinate and a treasure chest's X coordinate, and then take the absolute value of this number. We do the same for the sonar device's Y coordinate and a treasure chest's Y coordinate. The larger of these two values is the distance. Let's look at our example board with rings above to see if this algorithm is correct.

The sonar's X and Y coordinates are 3 and 2. The first treasure chest's X and Y coordinates (first in the list [[5, 0], [0, 2], [4, 2]] that is) are 5 and 0.

For the X coordinates, 3 - 5 evaluates to -2, and the absolute value of -2 is 2.

For the Y coordinates, 2 - 1 evaluates to 1, and the absolute value of 1 is 1.

Comparing the two absolute values 2 and 1, the larger value is 2 so that should be the distance between the sonar device and the treasure chest at coordinates 5, 1. We can look at the board and see that this algorithm works, because the treasure chest at 5,1 is in the sonar device's 2nd ring. Let's quickly compare the other two chests to see if his distances work out correctly also.

The abs() function returns the absolute value of the number we pass to it. Let's find the distance from the sonar device at 3,2 and the treasure chest at 0,2: abs(3 - 0) evaluates to 3. abs(2 - 2) evaluates to 0. 3 is larger than 0, so the distance from the sonar device at 3,2 and the treasure chest at 0,2 is 3. We can look at the board and see this is true.

Let's find the distance from the sonar device at 3,2 and the last treasure chest at 4,2. abs(3 - 4) evaluates to 1. abs(2 - 2) evaluates to 0. 1 is larger than 0, so the distance from the sonar device at 3,2 and the treasure chest at 4,2 is 1. We look at the board and see this is true also.

All three distances worked out correctly, so it seems our algorithm works. The distances from the sonar device to the three sunken treasure chests are 2, 3, and 1. On each guess, we want to know the distance from the sonar device to the closest of the three treasure chest distances. To do this we use a variable called smallestDistance. Let's look at the code again:

    smallestDistance = 100 # any chest will be closer than 100.
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)
        if distance < smallestDistance: # we want the closest treasure chest.
            smallestDistance = distance
You can also use multiple assignment in for loops. Remember, the assignment statement a, b = [5, 10] will assign 5 to a and 10 to b. Also, the for loop for i in [0, 1, 2, 3, 4] will assign the i variable the values 0 and 1 and so on for each iteration.

for cx, cy in chests: combines both of these principles. Because chests is a list where each item in the list is itself a list of two integers, the first of these integers is assigned to cx and the second integer is assigned to cy. So if chests has the value [[5, 0], [0, 2], [4, 2]], cx will have the value 5 and cy will have the value 0 on the first iteration through the loop.

Line 73 determines which is larger: the absolute value of the difference of the X coordinates, or the absolute value of the difference of the Y coordinates. (abs(cx - x) < abs(cy - y) seems like much easier way to say that, doesn't it?). The if-else statement assigns the larger of the values to the distance variable.

So on each iteration of the for loop, the distance variable holds the distance of a treasure chest's distance from the sonar device. But we want the shortest (that is, smallest) distance of all the treasure chests. This is where the smallestDistance variable comes in. Whenever the distance variable is smaller than smallestDistance, then the value in distance becomes the new value of smallestDistance.

We give smallestDistance the impossibly high value of 100 at the beginning of the loop so that at least one of the treasure chests we find will be put into smallestDistance. By the time the for loop has finished, we know that smallestDistance holds the shortest distance between the sonar device and all of the treasure chests in the game.

    if smallestDistance == 0:
        # xy is directly on a treasure chest!
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'
The only time that smallestDistance is equal to 0 is when the sonar device's XY coordinates are the same as a treasure chest's XY coordinates. This means the player has correctly guessed the location of a treasure chest. We should remove this chest's two-integer list from the chests data structure with the remove() list method.

The remove() List Method

The remove() list method will remove the first occurrence of the value passed as a parameter from the list. For example, try typing the following into the interactive shell:

>>> x = [42, 5, 10, 42, 15, 42]
>>> x.remove(10)
>>> x
[42, 5, 42, 15, 42]
You can see that the 10 value has been removed from the x list. The remove() method removes the first occurrence of the value you pass it, and only the first. For example, type the following into the shell:

>>> x = [42, 5, 10, 42, 15, 42]
>>> x.remove(42)
>>> x
[5, 10, 42, 15, 42]
Notice that only the first 42 value was removed, but the second and third ones are still there. The remove() method will cause an error if you try to remove a value that is not in the list:

>>> x = [5, 42]
>>> x.remove(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>>
After removing the found treasure chest from the chests list, we return the string 'You have found a sunken treasure chest!' to tell the caller that the guess was correct. Remember that any changes made to the list in a function will exist outside the function as well.

    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
        else:
            board[x][y] = 'O'
            return 'Sonar did not detect anything. All treasure chests out of range.'
The else block executes if smallestDistance was not 0, which means the player did not guess an exact location of a treasure chest. We return two different strings, depending on if the sonar device was placed within range of any of the treasure chests. If it was, we mark the board with the string version of smallestDistance. If not, we mark the board with a '0'.

How the Code Works: Lines 94 to 162

The last few functions we need are to let the player enter their move on the game board, ask the player if he wants to play again (this will be called at the end of the game), and print the instructions for the game on the screen (this will be called at the beginning of the game).

Getting the Player's Move

def enterPlayerMove():
    # Let the player type in her move. Return a two-item list of int xy coordinates.
    print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()
This function collects the XY coordinates of the player's next move. It has a while loop so that it will keep asking the player for her next move. The player can also type in quit in order to quit the game. In that case, we call the sys.exit() function which immediately terminates the program.

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]), int(move[1])):
            return [int(move[0]), int(move[1])]
        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')
Assuming the player has not typed in 'quit', we call the split() method on move and set the list it returns as the new value of move. What we expect move to be is a list of two numbers. These numbers will be strings, because the split() method returns a list of strings. But we can convert these to integers with the int() function.

If the player typed in something like '1 2 3', then the list returned by split() would be ['1', '2', '3']. In that case, the expression len(move) == 2 would be False and the entire expression immediately evaluates to False (because of short-circuiting as described in chapter 10.)

If the list returned by split() does have a length of 2, then it will have a move[0] and move[1]. We call the string method isdigit() on those strings. isdigit() will return True if the string consists solely of numbers. Otherwise it returns False. Try typing the following into the interactive shell:

>>> '42'.isdigit()
True
>>> 'forty'.isdigit()
False
>>> ''.isdigit()
False
>>> 'hello'.isdigit()
False
>>> x = '10'
>>> x.isdigit()
True
>>>
As you can see, both move[0].isdigit() and move[1].isdigit() must be True for the whole condition to be True. The final part of this expression calls our move[1] function to check if the XY coordinates exist on the board. If all these expressions are True, then this function returns a two-integer list of the XY coordinates. Otherwise, the player will be asked to enter coordinates again.

Asking the Player to Play Again

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
The playAgain() function will ask the player if they want to play again, and will keep asking until the player types in a string that begins with 'y'.

Printing the Game Instructions for the Player

def showInstructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to find the three sunken treasure chests that are lurking in the part of the
ocean you are in and collect them.
To play, enter the coordinates of the point in the ocean you wish to drop a
sonar device. The sonar can find out how far away the closest chest is to it.
For example, the d below marks where the device was dropped, and the 2's
represent distances of 2 away from the device. The 4's represent
distances of 4 away from the device.
    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
Press enter to continue...''')
    input()
The showInstructions() is just a couple of print() calls that print multi-line strings. The input() function just gives the player a chance to press Enter before printing the next string. This is because the screen can only show 25 lines of text at a time.

    print('''For example, here is a treasure chest (the c) located a distance of 2 away
from the sonar device (the d):
    22222
    c   2
    2 d 2
    2   2
    22222
The point where the device was dropped will be marked with a d.
The treasure chests don't move around. Sonar devices can detect treasure
chests up to a distance of 9. If all chests are out of range, the point
will be marked with O
If a device is directly dropped on a treasure chest, you have discovered
the location of the chest, and it will be collected. The sonar device will
remain there.
When you collect a chest, all sonar devices will update to locate the next
closest sunken treasure chest.
Press enter to continue...''')
    input()
    print()
This is the rest of the instructions in one multi-line string. After the player presses Enter, the function returns. These are all of the functions we will define for our game. The rest of the program is the main part of our game.

How the Code Works: Lines 165 to 217

Now that we are done writing all of the functions our game will need, let's start the main part of the program.

The Start of the Game

print('S O N A R !')
print()
print('Would you like to view the instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()
The expression input().lower().startswith('y') asks the player if they want to see the instructions, and evaluates to True if the player typed in a string that began with 'y' or 'Y'. If so, showInstructions() is called.

while True:
    # game setup
    sonarDevices = 16
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []
This while loop is the main loop for this game. Here are what the variables are for:

Table 13-2: Variables used in the main game loop.
Variable    Description
sonarDevices    The number of sonar devices (and turns) the player has left.
theBoard    The board data structure we will use for this game.
theChests   The list of chest data structures. getRandomChests() will return a list of three treasure chests at random places on the board.
previousMoves   A list of all the XY moves that the player has made in the game.
Displaying the Game Status for the Player

    while sonarDevices > 0:
        # Start of a turn:
        # show sonar device/chest status
        if sonarDevices > 1: extraSsonar = 's'
        else: extraSsonar = ''
        if len(theChests) > 1: extraSchest = 's'
        else: extraSchest = ''
        print('You have %s sonar device%s left. %s treasure chest%s remaining.' % (sonarDevices, extraSsonar, len(theChests), extraSchest))
This while loop executes as long as the player has sonar devices remaining. We want to print a message telling the user how many sonar devices and treasure chests are left. But there is a problem. If there are two or more sonar devices left, we want to print '2 sonar devices'. But if there is only one sonar device left, we want to print '1 sonar device' left. We only want the plural form of "devices" if there are multiple sonar devices. The same goes for '2 treasure chests' and '1 treasure chest'.

Notice on lines 183 through 186 that we have code after the if and else statements' colon. This is perfectly valid Python. Instead of having a block of code after the statement, instead you can just use the rest of the same line to make your code more concise. (Of course, this means you can only have one line of code.) This applies to any statement that uses colons, including while and for loops.

So we have two string variables named extraSsonar and extraSchest, which are set to ' ' (space) if there are multiple sonar devices or treasures chests. Otherwise, they are blank. We use them in the while statement on line 187.

Getting the Player's Move

        x, y = enterPlayerMove()
        previousMoves.append([x, y]) # we must track all moves so that sonar devices can be updated.
        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
Line 189 uses the multiple assignment trick. enterPlayerMove() returns a two-item list. The first item will be stored in the x variable and the second will be stored in the y variable. We then put these two variables into another two-item list, which we store in the previousMoves list with the append() method. This means previousMoves is a list of XY coordinates of each move the player makes in this game.

The x and y variables, along with theBoard and theChests (which represent the current state of the game board) are all sent to the makeMove() function. As we have already seen, this function will make the necessary modifications to the game board. If makeMove() returns the value False, then there was a problem with the x and y values we passed it. The continue statement will send the execution back to the start of the while loop that began on line 179 to ask the player for XY coordinates again.

Finding a Sunken Treasure Chest

        else:
            if moveResult == 'You have found a sunken treasure chest!':
                # update all the sonar devices currently on the map.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)
If makeMove() did not return the value False, it would have returned a string that tells us what were the results of that move. If this string was 'You have found a sunken treasure chest!', then that means we should update all the sonar devices on the board so they detect the next closest treasure chest on the board. We have the XY coordinates of all the sonar devices currently on the board stored in previousMoves. So we can just pass all of these XY coordinates to the makeMove() function again to have it redraw the values on the board.

We don't have to worry about this call to makeMove() having errors, because we already know all the XY coordinates in previousMoves are valid. We also know that this call to makeMove() won't find any new treasure chests, because they would have already been removed from the board when that move was first made.

The for loop on line 198 also uses the same multiple assignment trick for x and y because the items in previousMoves list are themselves two-item lists. Because we don't print anything here, the player doesn't realize we are redoing all of the previous moves. It just appears that the board has been entirely updated.

Checking if the Player has Won

        if len(theChests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game!')
            break
Remember that the makeMove() function modifies the theChests list we send it. Because theChests is a list, any changes made to it inside the function will persist after execution returns from the function. makeMove() removes items from theChests when treasure chests are found, so eventually (if the player guesses correctly) all of the treasure chests will have been removed. (Remember, by "treasure chest" we mean the two-item lists of the XY coordinates inside the theChests list.)

When all the treasure chests have been found on the board and removed from theChests, the theChests list will have a length of 0. When that happens, we display a congratulations to the player, and then execute a break statement to break out of this while loop. Execution will then move down to line 209 (the first line after the while-block.)

Checking if the Player has Lost

        sonarDevices -= 1
This is the last line of the while loop that started on line 179. We decrement the sonarDevices variable because the player has used one. If the player keeps missing the treasure chests, eventually sonarDevices will be reduced to 0. After this line, execution jumps back up to line 179 so we can re-evaluate the while statement's condition (which is sonarDevices > 0). If sonarDevices is 0, then the condition will be False and execution will continue outside the while-block on line 209.

But until then, the condition will remain True and the player can keep making guesses.

    if sonarDevices == 0:
        print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print('for home with treasure chests still out there! Game over.')
        print('    The remaining chests were here:')
        for x, y in theChests:
            print('    %s, %s' % (x, y))
Line 209 is the first line outside the while loop. By this point the game is over. But how do we tell if the player won or not? The only two places where the program execution would have left the while loop is on line 179 if the condition failed. In that case, sonarDevices would be 0 and the player would have lost.

The second place is the break statement on line 205. That statement is executed if the player has found all the treasure chests before running out of sonar devices. In that case, sonarDevices would be some value greater than 0.

Lines 210 to 212 will tell the player they've lost. The for loop on line 213 will go through the treasure chests remaining in theChests and show their location to the player so that they can know where the treasure chests had been lurking.

Asking the Player to Play Again, and the sys.exit() Function

    if not playAgain():
        sys.exit()
Win or lose, we call the playAgain() function to let the player type in whether they want to keep playing or not. If not, then playAgain() returns False. The not operator changes this to True, making the if statement's condition True and the sys.exit() function is executed. This will cause the program to terminate.

Otherwise, execution jumps back to the beginning of the while loop on line 171.

Summary: Review of our Sonar Game

Remember how our Tic Tac Toe game numbered the spaces on the Tic Tac Toe board 1 through 9? This sort of coordinate system might have been okay for a board with less than ten spaces. But the Sonar board has nine hundred spaces! The Cartesian coordinate system we learned in the last chapter really makes all these spaces manageable, especially when our game needs to find the distance between two points on the board.

Locations in games that use a Cartesian coordinate system are often stored in a list of lists so that the first index is the x-coordinate and the second index is the y-coordinate. This make accessing a coordinates look like board[x][y].

These data structures (such as the ones used for the ocean and locations of the treasure chests) make it possible to have complicated concepts represented as data in our program, and our game programs become mostly about modifying these data structures.

In the next chapter, we will be representing letters as numbers using their ASCII numbers. (This is the same ASCII term we used in "ASCII art" previously.) By representing text as numbers, we can perform mathematically operations on them which will encrypt or decrypt secret messages.

