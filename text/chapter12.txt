Chapter 12 - Cartesian Coordinates

Topics Covered In This Chapter:

Cartesian coordinate systems.
The X-axis and Y-axis.
The Commutative Property of Addition.
Absolute values and the abs() function.
This chapter does not introduce a new game, but instead goes over some simple mathematical concepts that we will use in the rest of the games in this book.

When you look at 2D games (such as Tetris or old Super Nintendo or Sega Genesis games) you can see that most of the graphics on the screen can move left or right (the first dimension) and up or down (the second dimension, hence 2D). In order for us to create games that have objects moving around two dimensions (such as the two dimensional computer screen), we need a system that can translate a place on the screen to integers that our program can deal with.

This is where Cartesian coordinate systems come in. The coordinates can point to a very specific point on the screen so that our program can keep track of different areas on the screen.

Negative numbers are often used with Cartesian coordinate systems as well. The second half of this chapter will explain how we can do math with negative numbers.

You may already know about Cartesian coordinate systems and negative numbers from math class. In that case, you can just give this chapter a quick read anyway to refresh yourself.

Grids and Cartesian Coordinates


Figure 12-1: A sample chessboard with a
black knight at a, 4 and a white knight at e, 6.
A problem in many games is how to talk about exact points on the board. A common way of solving this is by marking each individual row and column on a board with a letter and a number. Figure 12-1 is a chess board that has each row and each column marked.

In chess, the knight piece looks like a horse head. The white knight is located at the point e, 6 and the black knight is located at point a, 4. We can also see that every space on row 7 and every space in column c is empty.

A grid with labeled rows and columns like the chess board is a Cartesian coordinate system. By using a row label and column label, we can give a coordinate that is for one and only one space on the board. This can really help us describe to a computer the exact location we want. If you have learned about Cartesian coordinate systems in math class, you may know that usually we have numbers for both the rows and columns. This is handy, because otherwise after the 26th column we would run out of letters. That board would look like Figure 12-2.


Figure 12-2: The same chessboard but with
numeric coordinates for both rows and columns.
The numbers going left and right that describe the columns are part of the X-axis. The numbers going up and down that describe the rows are part of the Y-axis. When we describe coordinates, we always say the X-coordinate first, followed by the Y-coordinate. That means the white knight in the above picture is located at the coordinate 5, 6 (and not 6, 5). The black knight is located at the coordinate 1, 4 (not to be confused with 4, 1).

Notice that for the black knight to move to the white knight's position, the black knight must move up two spaces, and then to the right by four spaces. (Or move right four spaces and then move up two spaces.) But we don't need to look at the board to figure this out. If we know the white knight is located at 5, 6 and the black knight is located at 1, 4, then we can just use subtraction to figure out this information.

Subtract the black knight's X-coordinate and white knight's X-coordinate: 5 - 1 = 4. That means the black knight has to move along the X-axis by four spaces.

Subtract the black knight's Y-coordinate and white knight's Y-coordinate: 6 - 4 = 2. That means the black knight has to move along the Y-axis by two spaces.

Negative Numbers

Another concept that Cartesian coordinates use is negative numbers. Negative numbers are numbers that are smaller than zero. We put a minus sign in front of a number to show that it is a negative number. -1 is smaller than 0. And -2 is smaller than -1. And -3 is smaller than -2. If you think of regular numbers (called positive numbers) as starting from 1 and increasing, you can think of negative numbers as starting from -1 and decreasing. 0 itself is not positive or negative. In this picture, you can see the positive numbers increasing to the right and the negative numbers decreasing to the left:


Figure 12-3: A number line.

The number line is really useful for doing subtraction and addition with negative numbers. The expression 4 + 3 can be thought of as the white knight starting at position 4 and moving 3 spaces over to the right (addition means increasing, which is in the right direction).


Figure 12-4: Moving the white knight to the right adds to the coordinate.

As you can see, the white knight ends up at position 7. This makes sense, because 4 + 3 is 7.

Subtraction can be done by moving the white knight to the left. Subtraction means decreasing, which is in the left direction. 4 - 6 would be the white knight starting at position 4 and moving 6 spaces to the left, like in Figure 12-5:


Figure 12-5: Moving the white knight to the left subtracts from the coordinate.

The white knight ends up at position -2. That means 4 - 6 equals -2.

If we add or subtract a negative number, the white knight would move in the opposite direction. If you add a negative number, the knight moves to the left. If you subtract a negative number, the knight moves to the right. The expression -6 - -4 would be equal to -2. The knight starts at -6 and moves to the right by 4 spaces. Notice that -6 - -4 has the same answer as -6 + 4.


Figure 12-6: Even if the white knight starts at a negative coordinate, moving right still adds to the coordinate.


Figure 12-7: Putting two number lines together creates a Cartesian coordinate system.

The number line is the same as the X-axis. If we made the number line go up and down instead of left and right, it would model the Y-axis. Adding a positive number (or subtracting a negative number) would move the knight up the number line, and subtracting a positive number (or adding a negative number) would move the knight down. When we put these two number lines together, we have a Cartesian coordinate system like in Figure 12-7. The 0, 0 coordinate has a special name: the origin.

Math Tricks

Subtracting negative numbers or adding negative numbers seems easy when you have a number line in front of you, but it can be easy when you only have the numbers too. Here are three tricks you can do to make evaluating these expressions by yourself easier to do.

Trick 1: "A Minus Eats the Plus Sign on its Left"

The first is if you are adding a negative number, for example; 4 + -2. The first trick is "a minus eats the plus sign on its left". When you see a minus sign with a plus sign on the left, you can replace the plus sign with a minus sign. The answer is still the same, because adding a negative value is the same as subtracting a positive value. 4 + -2 and 4 - 2 both evaluate to 2.


Figure 12-8: Trick 1 - Adding a positive and negative number.

Trick 2: "Two Minuses Combine Into a Plus"

The second trick is if you are subtracting a negative number, for example, 4 - -2. The second trick is "two minuses combine into a plus". When you see the two minus signs next to each other without a number in between them, they can combine into a plus sign. The answer is still the same, because subtracting a negative value is the same as adding a positive value.


Figure 12-9: Trick 2 - Subtracting a positive and negative number.

Trick 3: The Commutative Property of Addition

A third trick is to remember that when you add two numbers like 6 and 4, it doesn't matter what order they are in. (This is called the commutative property of addition.) That means that 6 + 4 and 4 + 6 both equal the same value, 10. If you count the boxes in the figure below, you can see that it doesn't matter what order you have the numbers for addition.


Figure 12-10: Trick 3 - The commutative property of addition.

Say you are adding a negative number and a positive number, like -6 + 8. Because you are adding numbers, you can swap the order of the numbers without changing the answer. -6 + 8 is the same as 8 + -6. But when you look at 8 + -6, you see that the minus sign can eat the plus sign to its left, and the problem becomes 8 - 6 = 2. But this means that -6 + 8 is also 2! We've rearranged the problem to have the same answer, but made it easier for us to solve without using a calculator or the computer.


Figure 12-11: Using our math tricks together.

Of course, you can always use the interactive shell as a calculator to evaluate these expressions. It is still very useful to know the above three tricks when adding or subtracting negative numbers. After all, you won't always be in front of a computer with Python all the time!

>>> 4 + -2
2
>>> -4 + 2
-2
>>> -4 + -2
-6
>>> 4 - -2
6
>>> -4 - 2
-6
>>> -4 - -2
-2
>>>
Absolute Values and the abs() Function

The absolute value of a number is the number without the negative sign in front of it. This means that positive numbers do not change, but negative numbers become positive. For example, the absolute value of -4 is 4. The absolute value of -7 is 7. The absolute value of 5 (which is positive) is just 5.

We can find how far away two things on a number line are from each other by taking the absolute value of their difference. Imagine that the white knight is at position 4 and the black knight is at position -2. To find out the distance between them, you would find the difference by subtracting their positions and taking the absolute value of that number.

It works no matter what the order of the numbers is. -2 - 4 (that is, negative two minus four) is -6, and the absolute value of -6 is 6. However, 4 - -2 (that is, four minus negative two) is 6, and the absolute value of 6 is 6. Using the absolute value of the difference is a good way of finding the distance between two points on a number line (or axis).

The abs() function can be used to return the absolute value of an integer. The abs() function is a built-in function, so you do not need to import any modules to use it. Pass it an integer or float value and it will return the absolute value:

>>> abs(-5)
5
>>> abs(42)
42
>>> abs(-10.5)
10.5
Coordinate System of a Computer Monitor


Figure 12-12: The Cartesian coordinate system on a computer monitor.
It is common that computer monitors use a coordinate system that has the origin (0, 0) at the top left corner of the screen, which increases going down and to the right. There are no negative coordinates. This is because text is printed starting at the top left, and is printed going to the right and downwards. Most computer graphics use this coordinate system, and we will use it in our games. Also it is common to assume that monitors can display 80 text characters per row and 25 text characters per column (look at Figure 12-12). This used to be the maximum screen size that monitors could support. While today's monitors can usually display much more text, we will not assume that the user's screen is bigger than 80 by 25.

Summary: Using this Math in Games

This hasn't been too much math to learn for programming. In fact, most programming does not require understanding a lot of math. Up until this chapter, we have been getting by on simple addition and multiplication.

Cartesian coordinate systems are needed to describe exactly where in a two dimensional area a certain position is. Coordinates are made up of two numbers: the X-coordinate and the Y-coordinate. The X-axis runs left and right and the Y-axis runs up and down. On a computer screen (and in most computer programming), the X-axis starts at 0 at the left side and increases on the way to the right. The Y-axis starts at 0 on the top of the screen and increases on the way down.

The three tricks we learned in this chapter make it very easy to add positive and negative integers. The first trick is that a minus sign will eat the plus sign on its left. The second trick is that two minuses next to each other will combine into a plus sign. And the third trick is that you can swap the position of the numbers you are adding. This is called the commutative property of addition.

For the rest of the book, we will use the concepts we learned in this chapter in our games because they have two dimensional areas in them. All graphical games require understanding how Cartesian coordinates work.

