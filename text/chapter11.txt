Chapter 11 - Bagels

Topics Covered In This Chapter:

Hard-coding
Augmented Assignment Operators, +=, -=, *=, /=
The random.shuffle() Function
The sort() List Method
The join() List Method
String Interpolation (also called String Formatting)
Conversion Specifier %s
Nested Loops
In this chapter you will learn a few new methods and functions that come with Python. You will also learn about augmented assignment operators and string interpolation. These concepts don't let you do anything you couldn't do before, but they are nice shortcuts that make typing your code easier.

Bagels is a simple game you can play with a friend. Your friend thinks up a random 3-digit number with no repeating digits, and you try to guess what the number is. After each guess, your friend gives you clues on how close your guess was. If the friend tells you "bagels", that means that none of the three digits you guessed is in the secret number. If your friend tells you "pico", then one of the digits is in the secret number, but your guess has the digit in the wrong place. If your friend tells you "fermi", then your guess has a correct digit in the correct place. Of course, even if you get a pico or fermi clue, you still don't know which digit in your guess is the correct one.

You can also get multiple clues after each guess. Say the secret number is 456, and your guess is 546. The clue you get from your friend would be "fermi pico pico" because one digit is correct and in the correct place (the digit 6), and two digits are in the secret number but in the wrong place (the digits 4 and 5).

Sample Run

I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number. You have 10 guesses to get it.
Guess #1:
123
Fermi
Guess #2:
453
Pico
Guess #3:
425
Fermi
Guess #4:
326
Bagels
Guess #5:
489
Bagels
Guess #6:
075
Fermi Fermi
Guess #7:
015
Fermi Pico
Guess #8:
175
You got it!
Do you want to play again? (yes or no)
no
Bagel's Source Code

bagels.py
This code can be downloaded from http://inventwithpython.com/bagels.py
If you get errors after typing this code in, compare it to the book's code with the online diff tool at http://inventwithpython.com/diff or email the author at al@inventwithpython.com
import random
def getSecretNum(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum
def getClues(guess, secretNum):
    # Returns a string with the pico, fermi, bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'
    clue.sort()
    return ' '.join(clue)
def isOnlyDigits(num):
    # Returns True if num is a string made up only of digits. Otherwise returns False.
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
NUMDIGITS = 3
MAXGUESS = 10
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')
while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (numGuesses))
            guess = input()
        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1
        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))
    if not playAgain():
        break
Designing the Program

Here is a flow chart for this program. The flow chart in Figure 11-1 describes the basic events of what happens in this game, and in what order they can happen.


Figure 11-1: Flow chart for the Bagels game.

And here is the source code for our game. Start a new file and type the code in, and then save the file as bagels.py. We will design our game so that it is very easy to change the size of the secret number. It can be 3 digits or 5 digits or 30 digits. We will do this by using a constant variable named NUMDIGITS instead of hard-coding the integer 3 into our source code.

Hard-coding means writing a program in a way that it changing the behavior of the program requires changing a lot of the source code. For example, we could hard-code a name into a print() function call like: print('Hello, Albert'). Or we could use this line: print('Hello, ' + name) which would let us change the name that is printed by changing the name variable name the program is running.

How the Code Works: Lines 1 to 9

At the start of the program we import the random module and also create a function for generating a random secret number for the player to guess. The process of creating this number isn't hard, and also guarantees that it only has unique digits in it.

import random
This game imports the random module so we can use the module's random number functions.

Shuffling a Unique Set of Digits

def getSecretNum(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
Our first function is named getSecretNum(), which will generate the random secret number. Instead of having the code only produce 3-digit numbers, we use a parameter named numDigits to tell us how many digits the secret number should have. (This way, we can make the game produce secret numbers with four or six digits, for example, just by passing 4 or 6 as numDigits.)

You may have noticed that the return value of our call to range() was in turn passed to a function called list(). The list() function returns a list value of the value passed to it, much like the str() function returns a string form or the int() function returns an integer form. The reason we do this is because the range() function technically does not return a list but something called an iterator object. Iterators are a topic that you don't need to know at this point, so they aren't covered in this book.

Just about every time we use the range() function it is in a for loop. Iterators are fine to use in for loops (just like lists and strings are), but if we ever want to store a list of integers in a variable, be sure to convert the return value of range() to a list with the list() function first. (Just like we do on line 4.)

The random.shuffle() Function

First, we create a list of integers 0 to 9 by calling list(range(10)) and store a reference to this list in numbers. Then we call a function in the random module named shuffle(). The only parameter to random.shuffle() is a reference to a list. The shuffle() function will randomly change the order of all the items in the list.

Notice that random.shuffle() does not return a value. It changes the list you pass it "in place" (just like our makeMove() function in the Tic Tac Toe chapter modified the list it was passed in place, rather than return a new list with the change). It would actually be incorrect to write numbers = random.shuffle(numbers).

Try experimenting with the random.shuffle() function by entering the following code into the interactive shell:

>>> import random
>>> spam = list(range(10))
>>> print(spam)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> random.shuffle(spam)
>>> print(spam)
[3, 0, 5, 9, 6, 8, 2, 4, 1, 7]
>>> random.shuffle(spam)
>>> print(spam)
[1, 2, 5, 9, 4, 7, 0, 3, 6, 8]
>>> random.shuffle(spam)
>>> print(spam)
[9, 8, 3, 5, 4, 7, 1, 2, 0, 6]
>>>
Every time you pass a list reference to random.shuffle(), afterwards the list it references will have all the same items but in a different order. The reason we do this is because we want the secret number to have unique values. The Bagels game is much more fun if you don't have duplicate numbers in the secret number, such as '244' or '333'.

Getting the Secret Number from the Shuffled Digits

    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
   return secretNum
The secret number will be a string of the first three digits (because we'll pass 3 for the numDigits parameter) of the shuffled list of integers. For example, if the shuffled list is [9, 8, 3, 5, 4, 7, 1, 2, 0, 6] then we want the string returned by getSecretNum() to be '983'.

The secretNum variable starts out as a blank string. We then loop a number of times equal to the integer value in numDigits. On each iteration through the loop, a new integer is pulled from the shuffled list, converted to a string, and concatenated to the end of secretNum. So if numDigits is 3, the loop will iterate three times and three random digits will be concatenated as strings.

For example, if numbers refers to the list [9, 8, 3, 5, 4, 7, 1, 2, 0, 6], then on the first iteration, numbers[0] (that is, 9) will be passed to str(), which in turn returns '9' which is concatenated to the end of secretNum. On the second iteration, the same happens with numbers[1] (that is, 8) and on the third iteration the same happens with numbers[2] (that is, 3). The final value of secretNum that is returned is '983'.

You may notice that secretNum in this function is a string, not an integer. This may seem odd, but remember that our secret number could be something like '012'. If we stored this as an integer, it would be 12 (without the leading zero) which would make it harder to work with in our program.

Augmented Assignment Operators

The += operator on line 8 is new. This is one of the augmented assignment operators. Normally, if you wanted to add or concatenate a value to a variable, you would use code that looked like this:

spam = 42
spam = spam + 10
eggs = 'Hello '
eggs = eggs + 'world!'
After running the above code, spam would have the value 52 and eggs would have the value 'Hello world!'. The augmented assignment operators are a shortcut that frees you from retyping the variable name. The following code does the exact same thing as the above code:

spam = 42
spam += 10         # Like spam = spam + 10
eggs = 'Hello '
eggs += 'world!' # Like eggs = eggs + 'world!'
There are other augmented assignment operators. -= will subtract a value from an integer. *= will multiply the variable by a value. /= will divide a variable by a value. Notice that these augmented assignment operators do the same math operations as the -, *, and / operators. Augmented assignment operators are a neat shortcut.

How the Code Works: Lines 11 to 24

We also need a way of figuring out which clues to show to the player.

def getClues(guess, secretNum):
    # Returns a string with the pico, fermi, bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'
The getClues() function will return a string with the fermi, pico, and bagels clues, depending on what it is passed for the guess and secretNum parameters. The most obvious and easiest step is to check if the guess is the exact same as the secret number. In that case, we can just return 'You got it!'.

    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
If the guess is not the exact same as the secret number, we need to figure out what clues to give the player. First we'll set up a list named clue, which we will add the strings 'Fermi' and 'Pico' as needed. We will combine the strings in this list into a single string to return.

We do this by looping through each possible index in guess and secretNum (we make sure both strings are the same size before we call getClues()). We will assume that guess and secretNum are the same size. As the value of i changes from 0 to 1 to 2, and so on, the if statement checks if the first, second, third, etc. letter of guess is the same as the number in the same position in secretNum. If so, we will add a string 'Fermi' to clue.

If that condition is False we will check if the number at the ith position in guess exists anywhere in secretNum. If this condition is True we know that the number is somewhere in the secret number but not in the same position. This is why we add the 'Pico' to clue.

    if len(clue) == 0:
        return 'Bagels'
If we go through the entire for loop above and never add anything to the clue list, then we know that there are no correct digits at all in guess. In this case, we should just return the string 'Bagels' as our only clue.

The sort() List Method

    clue.sort()
Lists have a method named sort() that rearranges the items in the list to be in alphanumerical order (this means in alphabetical order, but numbers are also in order). Try entering the following into the interactive shell:

>>> spam = [5, 'bat', 3, 1, 4, 'cat', 2, 'ape']
>>> spam.sort()
>>> spam
[1, 2, 3, 4, 5, 'ape', 'bat', 'cat']
Notice that the sort() method does not return a sorted list, but rather just sorts the list it is called on "in place". This is much like how the reverse() method works. You would never want to use this line of code: return spam.sort() because that would return the value None (which is what sort() returns). Instead you would want a separate line spam.sort() and then the line return spam.

The reason we want to sort the clue list is because we might return extra clues that we did not intend based on the order of the clues. If clue referenced the list ['Pico', 'Fermi', 'Pico'], then that would tell us that the center digit of our guess is in the correct position. Since the other two clues are both Pico, then we know that all we have to do is swap the first and third digit and we have the secret number. But if the clues are always sorted in alphabetical order, the player can't be sure which number the Fermi clue refers to (which is what we want for this game).

The join() String Method

    return ' '.join(clue)
The join() string method returns a string of each item in the list argument joined together. The string that the method is called on (on line 27, this is a single space, ' ') appears in between each item in the list. So the string that is returned on line 27 is each string in clue combined together with a single space in between each string.

For an example, enter the following into the interactive shell:

>>> 'x'.join(['hello', 'world'])
'helloxworld'
>>> 'ABCDEF'.join(['x', 'y', 'z'])
'xABCDEFyABCDEFz'
>>> ' '.join(['My', 'name', 'is', 'Zophie'])
'My name is Zophie'
The join() string method is sort of like the opposite of the split() string method. While split() returns a list from a split up string, join() returns a string from a combined list.

How the Code Works: Lines 29 to 53

We need a couple more functions for our game to use. The first is a function that will tell us if the guess that the player entered is a valid integer. Remember that the input() function returns a string of whatever the player typed in. If the player enters in anything but numbers for their guess, we want to ask the player again for a proper guess.

The second function is something we've seen before in previous games. We want a function that will ask the player if they want to play the game again and from the player's response, figure out if it was a Yes or No answer.

Checking if a String Only has Numbers

def isOnlyDigits(num):
    # Returns True if num is a string made up only of digits. Otherwise returns False.
    if num == '':
        return False
The isOnlyDigits() is a small function that will help us determine if the player entered a guess that was only made up of numbers. To do this, we will check each individual letter in the string named num and make sure it is a number.

Line 31 does a quick check to see if we were sent the blank string, and if so, we return False.

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True
We use a for loop on the string num. The value of i will have a single character from the num string on each iteration. Inside the for-block, we check if i does not exist in the list returned by '0 1 2 3 4 5 6 7 8 9'.split(). If it doesn't, we know that there is a character in num that is something besides a number. In that case, we should return the value False.

If execution continues past the for loop, then we know that every character in num is a number because we did not return out of the function. In that case, we return the value True.

Finding out if the Player Wants to Play Again

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')
The playAgain() function is the same one we used in Hangman and Tic Tac Toe. The long expression on line 43 will evaluate to either True or False. The return value from the call to the input() function is a string that has its lower() method called on it. The lower() method returns another string (the lowercase string) and that string has its startswith() method called on it, passing the argument 'y'.

The Start of the Game

NUMDIGITS = 3
MAXGUESS = 10
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')
This is the actual start of the program. Instead of hard-coding three digits as the size of the secret number, we will use the constant variable NUMDIGITS. And instead of hard-coding a maximum of ten guesses that the player can make, we will use the constant variable MAXGUESS. (This is because if we increase the number of digits the secret number has, we also might want to give the player more guesses. We put the variable names in all capitals to show they are meant to be constant.)

The print() function calls will tell the player the rules of the game and what the Pico, Fermi, and Bagels clues mean. Line 48's print() call has % (NUMDIGITS) added to the end and %s inside the string. This is a technique know as string interpolation.



String Interpolation

String interpolation is another shortcut, like augmented assignment operators. Normally, if you want to use the string values inside variables in another string, you have to use the + concatenation operator:

>>> name = 'Alice'
>>> event = 'party'
>>> where = 'the pool'
>>> day = 'Saturday'
>>> time = '6:00pm'
>>> print('Hello, ' + name + '. Will you go to the ' + event + ' at ' + where + ' this ' + day + ' at ' + time + '?')
Hello, Alice. Will you go to the party at the pool this Saturday at 6:00pm?
>>>
As you can see, it can be very hard to type a line that concatenates several strings together. Instead, you can use string interpolation, which lets you put placeholders like %s (these placeholders are called conversion specifiers), and then put all the variable names at the end. Each %s is replaced with the value in the variable at the end of the line. For example, the following code does the same thing as the above code:

>>> name = 'Alice'
>>> event = 'party'
>>> where = 'the pool'
>>> day = 'Saturday'
>>> time = '6:00pm'
>>> print('Hello, %s. Will you go to the %s at %s this %s at %s?' % (name, event, where, day, time))
Hello, Alice. Will you go to the party at the pool this Saturday at 6:00pm?
>>>
String interpolation can make your code much easier to type and read, rather than using several + concatenation operators.

The final line has the print() call with a string with conversion specifiers, followed by the % sign, followed by a set of parentheses with the variables in them. The first variable name will be used for the first %s, the second variable with the second %s and so on. The Python interpreter will give you an error if you do not have the same number of %s conversion specifiers as you have variables.

Another benefit of using string interpolation instead of string concatenation is that interpolation works with any data type, not just strings. All values are automatically converted to the string data type. (This is what the s in %s stands for.) If you typed this code into the shell, you'd get an error:

>>> spam = 42
>>> print('Spam == ' + spam)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>>
You get this error because string concatenation can only combine two strings, and spam is an integer. You would have to remember to put str(spam) in there instead. But with string interpolation, you can have any data type. Try entering this into the shell:

>>> spam = 42
>>> print('Spam == %s' % (spam))
Spam == 42
>>>
As you can see, using string interpolation instead of string concatenation is much easier because you don't have to worry about the data type of the variable. Also, string interpolation can be done on any strings, not just strings used in print() function calls.

String interpolation is also known as string formatting.

How the Code Works: Lines 55 to 76

Now that the program has displayed the rules to Bagels to the player, the program will randomly create a secret number and then enter a loop where it repeatedly asks for the player's guesses until she has either correctly guessed the secret number, or has run out of guesses. After that, we will ask the player if she wants to play again.

Creating the Secret Number

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
    numGuesses = 1
    while numGuesses <= MAXGUESS:
We start with a while loop that has a condition of True, meaning it will loop forever until we execute a break statement. Inside the infinite loop, we get a secret number from our getSecretNum() function (passing it NUMDIGITS to tell how many digits we want the secret number to have) and assign it to secretNum. Remember that secretNum is a string, not an integer.

We tell the player how many digits is in our secret number by using string interpolation instead of string concatenation. We set a variable numGuesses to 1, to denote that this is the first guess. Then we enter a new while loop which will keep looping as long as numGuesses is less than or equal to MAXGUESS.

Getting the Player's Guess

Notice that this second while loop on line 60 is inside another while loop that started on line 55. Whenever we have these loops-inside-loops, we call them nested loops. You should know that any break or continue statements will only break or continue out of the innermost loop, and not any of the outer loops.

        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('Guess #%s: ' % (numGuesses))
            guess = input()
The guess variable will hold the player's guess. We will keep looping and asking the player for a guess until the player enters a guess that has the same number of digits as the secret number and is made up only of digits. This is what the while loop that starts on line 62 is for. We set guess as the blank string on line 61 so that the while loop's condition is False the first time, ensuring that we enter the loop at least once.

Getting the Clues for the Player's Guess

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1
After execution gets past the while loop on line 62, we know that guess contains a valid guess. We pass this and the secret number in secretNum to our getClues() function. It returns a string that contains our clues, which we will display to the player. We then increment numGuesses by 1 using the augmented assignment operator for addition.

Checking if the Player Won or Lost

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))
If guess is the same value as secretNum, then we know the player has correctly guessed the secret number and we can break out of this loop (the while loop that was started on line 60). If not, then execution continues to line 72, where we check to see if the player ran out of guesses. If so, then we tell the player that they have lost and what the secret number was. We know that the condition for the while loop on line 55 will be False, so there is no need for a break statement.

At this point, execution jumps back to the while loop on line 60 where we let the player have another guess. If the player ran out of guesses (or we broke out of the loop with the break statement on line 71), then execution would proceed past the loop and to line 75.

Asking the Player to Play Again

    if not playAgain():
        break
After leaving the while loop that starts on line 60, we ask the player if want to play again by calling our playAgain() function. If playAgain() returns False, then we should break out of the while loop that was started on line 55. Since there is no more code after this loop, the program terminates.

If playAgain() returned True, then we would not execute the break statement and execution would jump back to line 55. A new secret number would be generated so that the player can play a new game.

Summary: Getting Good at Bagels

Bagels is a fairly simple game to program but can be difficult to win at. But if you keep playing, you will eventually discover better ways to guess and make use of the clues the game gives you.

This chapter introduced a few new functions and methods (random.shuffle(), sort(), and join()), along with a couple handy shortcuts. Using the augmented assignment operators involve less typing when you want to change a variable's relative value (such as in spam = spam + 1, which can be shortend to spam += 1). String interpolation can make your code much more readable by placing %s (called a conversion specifier) inside the string instead of using many string concatenation operations.

The join() string method is passed a list of strings that will be concatenated together, with the original associated string in between them. For example, 'X'.join( ['hello', 'world', 'yay'] ) will evaluate to the string, 'helloXworldXyay'.

The sort() list method will rearrange the items in the list to be in alphabetical order.

The append() list method will add a value to the end of the associated list. If spam contains the list ['a', 'b', 'c'], then calling spam.append('d') will change the list in spam to be ['a', 'b', 'c', 'd'].

The next chapter is not about programming directly, but will be necessary for the games we want to create in the later chapters of this book. We will learn about the math concepts of Cartesian coordinates and negative numbers. These will be used in the Sonar, Reversi, and Dodger games, but Cartesian coordinates and negative numbers are used in almost all games (especially graphical games). If you already know about these concepts, give the next chapter a brief read anyway just to freshen up. Let's dive in!

