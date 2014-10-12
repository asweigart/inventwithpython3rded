"""Hello, and welcome to the source code of Gorillas.py. This program is meant to be very well documented so that a
novice programmer can follow along. This program was written by Al Sweigart as a companion for his free, Creative
Commons-licensed book "Invent Your Own Computer Games with Python", which is available in full at:

        http://inventwithpython.com

Feel free to email the author with any programming questions at al@inventwithpython.com

This program seeks to replicate gorillas.bas, a Qbasic program that was popular in the 1990s. By reading
through the comments, you can learn how a simple Python game with the Pygame engine is put together.

The comments will generally come _after_ the lines of code they describe.

If you like this, then check out inventwithpython.com to read the book (which has similar game projects) for free!

The Pygame documentation is pretty good, and can be found at http://www.pygame.org/docs

Unfortunately there is no sound with this game.
"""

import pygame, sys, time, random, math
from pygame.locals import *
"""We'll import quite a few modules for this game. "pygame" has all the graphics & game-related functions that the
Pygame game engine provides. "sys" has the exit() function. "time" has the sleep() function. "random" has the randint()
function, and "math" contains the pi constant."""


"""All of the variables below in CAPS LETTERS are constants, that is, they are only supposed to be read and not
modified. (There's nothing to keep the program from modifying them, but it's just a convention programmers use.
The constants are a bit more descriptive than just using the numbers by themselves. And if you ever want to change
some value (such as the size of the explosions or the color of the gorillas), you only have to change it in one
place."""

SCR_WIDTH = 640
SCR_HEIGHT = 350
FPS = 30
GAME_CLOCK = pygame.time.Clock()
"""Here are several constants we will use in the game. The original Qbasic game had a screen size of 640x350, so we'll
use that as our screen size. We will use a single global Clock object to handle some of the timing stuff in all our
functions, and generally have FPS set to 30 (except when we want to set it to something else.

Constants are useful because you can just change the value in one place, and it will be used throughout the program.

Try experimenting with different values for these global constants."""

BUILDING_COLORS = ((173, 170, 173), (0, 170, 173), (173, 0, 0))
LIGHT_WINDOW = (255, 255, 82)
DARK_WINDOW = (82, 85, 82)
SKY_COLOR = (0, 0, 173)
GOR_COLOR = (255, 170, 82)
BAN_COLOR = (255, 255, 82)
EXPLOSION_COLOR = (255, 0, 0)
SUN_COLOR = (255, 255, 0)
DARK_RED_COLOR = (173, 0, 0)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GRAY_COLOR = (173, 170, 173)
"""Here are a bunch of colors. Pygame uses a tuple of three integers to specify a color. The integers are for the
amount of Red, Blue, and Green (in order) in the color. This is known as an RGB value.

BUILDING_COLORS will hold a tuple of these RGB tuples and represent the different colors the buildings can be."""

BUILD_EXPLOSION_SIZE = int(SCR_HEIGHT / 50)
GOR_EXPLOSION_SIZE = 30
"""BUILD_EXPLOSION_SIZE holds the size of an explosion when a banana hits a building, and GOR_EXPLOSION_SIZE is the size
when it hits a gorilla."""

SUN_X = 300
SUN_Y = 10
"""The position of the sun in the sky."""

pygame.init()
GAME_FONT = pygame.font.SysFont(None, 20)
"""The pygame.init() function needs to be called before calling any of the Pygame functions.
We will use the default system font at a size of 20 points."""

# orientation of the banana:
RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3
"""Some constants for the direction the banana (or anything else) faces."""

# gorilla arms drawing types
BOTH_ARMS_DOWN = 0
LEFT_ARM_UP = 1
RIGHT_ARM_UP = 2
"""Some constants for which of the three gorilla sprites to use: both arms down, left arm up, or right arm up."""


"""The following multiline strings are used with the makeSurfaceFromASCII() function. It's basically a way of
generating Surfaces other than using the drawing functions or including graphic files along with this .py file.

Try experimenting by changing the strings. The first and last line are ignored (so you don't have to deal with
indentation issues in the string)."""

STAR_ASCII = """


   XX  XX
    XXXX
  XXXXXXXX
    XXXX
   XX  XX
"""

GOR_DOWN_ASCII = """

          XXXXXXXX
          XXXXXXXX
         XX      XX
         XXXXXXXXXX
         XXX  X  XX
          XXXXXXXX
          XXXXXXXX
           XXXXXX
      XXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXX XXXXXXXXXXX
 XXXXXXXXXXXXX XXXXXXXXXXXX
 XXXXXXXXXXXX X XXXXXXXXXXX
XXXXX XXXXXX XXX XXXXX XXXXX
XXXXX XXX   XXXXX   XX XXXXX
XXXXX   XXXXXXXXXXXX   XXXXX
 XXXXX  XXXXXXXXXXXX  XXXXX
 XXXXX  XXXXXXXXXXXX  XXXXX
  XXXXX XXXXXXXXXXXX XXXXX
   XXXXXXXXXXXXXXXXXXXXXX
       XXXXXXXXXXXXX
     XXXXXX     XXXXXX
     XXXXX       XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
     XXXXX       XXXXX
"""

GOR_LEFT_ASCII = """
   XXXXX
  XXXXX   XXXXXXXX
 XXXXX    XXXXXXXX
 XXXXX   XX      XX
XXXXX    XXXXXXXXXX
XXXXX    XXX  X  XX
XXXXX     XXXXXXXX
 XXXXX    XXXXXXXX
 XXXXX     XXXXXX
  XXXXXXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXXXX
      XXXXXXXX XXXXXXXXXXX
      XXXXXXXX XXXXXXXXXXXX
      XXXXXXX X XXXXXXXXXXX
      XXXXXX XXX XXXXX XXXXX
      XXX   XXXXX   XX XXXXX
        XXXXXXXXXXXX   XXXXX
        XXXXXXXXXXXX  XXXXX
        XXXXXXXXXXXX  XXXXX
        XXXXXXXXXXXX XXXXX
       XXXXXXXXXXXXXXXXXX
       XXXXXXXXXXXXX
     XXXXXX     XXXXXX
     XXXXX       XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
     XXXXX       XXXXX
"""

GOR_RIGHT_ASCII = """
                    XXXXX
          XXXXXXXX   XXXXX
          XXXXXXXX    XXXXX
         XX      XX   XXXXX
         XXXXXXXXXX    XXXXX
         XXX  X  XX    XXXXX
          XXXXXXXX     XXXXX
          XXXXXXXX    XXXXX
           XXXXXX     XXXXX
      XXXXXXXXXXXXXXXXXXXX
   XXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXX XXXXXXX
 XXXXXXXXXXXXX XXXXXXX
 XXXXXXXXXXXX X XXXXXX
XXXXX XXXXXX XXX XXXXX
XXXXX XXX   XXXXX   XX
XXXXX   XXXXXXXXXXXX
 XXXXX  XXXXXXXXXXXX
 XXXXX  XXXXXXXXXXXX
  XXXXX XXXXXXXXXXXX
   XXXXXXXXXXXXXXXXX
       XXXXXXXXXXXXX
     XXXXXX     XXXXXX
     XXXXX       XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
    XXXXX         XXXXX
     XXXXX       XXXXX
"""

BAN_RIGHT_ASCII = """
     XX
    XXX
   XXX
   XXX
   XXX
   XXX
   XXX
    XXX
     XX
"""

BAN_LEFT_ASCII = """
XX
XXX
 XXX
 XXX
 XXX
 XXX
 XXX
XXX
XX
"""

BAN_UP_ASCII = """
XX     XX
XXXXXXXXX
 XXXXXXX
  XXXXX
"""

BAN_DOWN_ASCII = """
  XXXXX
 XXXXXXX
XXXXXXXXX
XX     XX
"""

SUN_NORMAL_ASCII = """
                    X
                    X
            X       X       X
             X      X      X
             X      X      X
     X        X     X     X        X
      X        X XXXXXXX X        X
       XX      XXXXXXXXXXX      XX
         X  XXXXXXXXXXXXXXXXX  X
          XXXXXXXXXXXXXXXXXXXXX
  X       XXXXXXXXXXXXXXXXXXXXX       X
   XXXX  XXXXXXXXXXXXXXXXXXXXXXX  XXXX
       XXXXXXXXXX XXXXX XXXXXXXXXX
        XXXXXXXX   XXX   XXXXXXXX
        XXXXXXXXX XXXXX XXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
       XXXXXX XXXXXXXXXXXXX XXXXXX
   XXXX  XXXXX  XXXXXXXXX  XXXXX  XXXX
  X       XXXXXX  XXXXX  XXXXXX       X
          XXXXXXXX     XXXXXXXX
         X  XXXXXXXXXXXXXXXXX  X
       XX      XXXXXXXXXXX      XX
      X        X XXXXXXX X        X
     X        X     X     X        X
             X      X      X
             X      X      X
            X       X       X
                    X
                    X
"""

SUN_SHOCKED_ASCII = """
                    X
                    X
            X       X       X
             X      X      X
             X      X      X
     X        X     X     X        X
      X        X XXXXXXX X        X
       XX      XXXXXXXXXXX      XX
         X  XXXXXXXXXXXXXXXXX  X
          XXXXXXXXXXXXXXXXXXXXX
  X       XXXXXXXXXXXXXXXXXXXXX       X
   XXXX  XXXXXXXXXXXXXXXXXXXXXXX  XXXX
       XXXXXXXXXX XXXXX XXXXXXXXXX
        XXXXXXXX   XXX   XXXXXXXX
        XXXXXXXXX XXXXX XXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
        XXXXXXXXXXXXXXXXXXXXXXXXX
       XXXXXXXXXXXXXXXXXXXXXXXXXXX
   XXXX  XXXXXXXXX     XXXXXXXXX  XXXX
  X       XXXXXXX       XXXXXXX       X
          XXXXXXX       XXXXXXX
         X  XXXXXX     XXXXXX  X
       XX      XXXXXXXXXXX      XX
      X        X XXXXXXX X        X
     X        X     X     X        X
             X      X      X
             X      X      X
            X       X       X
                    X
                    X
"""

def terminate():
    """Calls both the pygame.quit() and sys.exit() functions, to end the program. (I found that not calling
    pygame.quit() before sys.exit() can mess up IDLE sometimes."""
    pygame.quit()
    sys.exit()

def makeSurfaceFromASCII(ascii, fgColor=(255,255,255), bgColor=(0,0,0)):
    """Returns a new pygame.Surface object that has the image drawn on it as specified by the ascii parameter.
    The first and last line in ascii are ignored. Otherwise, any X in ascii marks a pixel with the foreground color
    and any other letter marks a pixel of the background color. The Surface object has a width of the widest line
    in the ascii string, and is always rectangular."""

    """Try experimenting with this function so that you can specify more than two colors. (Pass a dict of
    ascii letters and RGB tuples, say."""
    ascii = ascii.split('\n')[1:-1]
    width = max([len(x) for x in ascii])
    height = len(ascii)
    surf = pygame.Surface((width, height))
    surf.fill(bgColor)

    pArr = pygame.PixelArray(surf)
    for y in range(height):
        for x in range(len(ascii[y])):
            if ascii[y][x] == 'X':
                pArr[x][y] = fgColor
    return surf

GOR_DOWN_SURF    = makeSurfaceFromASCII(GOR_DOWN_ASCII,    GOR_COLOR,      SKY_COLOR)
GOR_LEFT_SURF    = makeSurfaceFromASCII(GOR_LEFT_ASCII,    GOR_COLOR,      SKY_COLOR)
GOR_RIGHT_SURF   = makeSurfaceFromASCII(GOR_RIGHT_ASCII,   GOR_COLOR,      SKY_COLOR)
BAN_RIGHT_SURF   = makeSurfaceFromASCII(BAN_RIGHT_ASCII,   BAN_COLOR,      SKY_COLOR)
BAN_LEFT_SURF    = makeSurfaceFromASCII(BAN_LEFT_ASCII,    BAN_COLOR,      SKY_COLOR)
BAN_UP_SURF      = makeSurfaceFromASCII(BAN_UP_ASCII,      BAN_COLOR,      SKY_COLOR)
BAN_DOWN_SURF    = makeSurfaceFromASCII(BAN_DOWN_ASCII,    BAN_COLOR,      SKY_COLOR)
SUN_NORMAL_SURF  = makeSurfaceFromASCII(SUN_NORMAL_ASCII,  SUN_COLOR,      SKY_COLOR)
SUN_SHOCKED_SURF = makeSurfaceFromASCII(SUN_SHOCKED_ASCII, SUN_COLOR,      SKY_COLOR)
STAR_SURF        = makeSurfaceFromASCII(STAR_ASCII,        DARK_RED_COLOR, BLACK_COLOR)

assert GOR_DOWN_SURF.get_size() == GOR_LEFT_SURF.get_size() == GOR_RIGHT_SURF.get_size()
"""Create the pygame.Surface objects from the ASCII strings."""

sunRect = pygame.Rect(SUN_X, SUN_Y, SUN_NORMAL_SURF.get_width(), SUN_NORMAL_SURF.get_height())
"""sunRect will be a global value so we'll always know where the sun is."""

def drawText(text, surfObj, x, y, fgcol, bgcol, pos='left'):
    """A generic function to draw a string to a pygame.Surface object at a certain x,y location. This returns
    a pygame.Rect object which describes the area the string was drawn on.

    If the pos parameter is "left", then the x,y parameter specifies the top left corner of the text rectangle.
    If the pos parameter is "center", then the x,y parameter specifies the middle top point of the text rectangle."""

    textobj = GAME_FONT.render(text, 1, fgcol, bgcol) # creates the text in memory (it's not on a surface yet).
    textrect = textobj.get_rect()

    if pos == 'left':
        textrect.topleft = (x, y)
    elif pos == 'center':
        textrect.midtop = (x, y)
    surfObj.blit(textobj, textrect) # draws the text onto the surface
    """Remember that the text will only appear on the screen if you pass the pygame.Surface object that was
    returned from the call to pygame.display.set_mode(), and only after pygame.display.update() is called."""
    return textrect

def getModCase(s, mod):
    """Checks the state of the shift and caps lock keys, and switches the case of the s string if needed."""
    if bool(mod & KMOD_RSHIFT or mod & KMOD_LSHIFT) ^ bool(mod & KMOD_CAPS):
        return s.swapcase()
    else:
        return s

def inputMode(prompt, screenSurf, x, y, fgcol, bgcol, maxlen=12, allowed=None, pos='left', cursor='_', cursorBlink=False):
    """Takes control of the program when called. This function displays a prompt on the screen (the "prompt" string)
    parameter) on the screenSurf surface at the x, y coordinates. The text is in the fgcol color with a bgcol color
    background. You can optionally specify maxlen for a maximum length of the user's response. "allowed" is a string
    of allowed characters (if the player can only type numbers, say) and ignores all other keystrokes. The "pos"
    parameter can either be the string "left" (where the x, y coordinates refer to the top left corner of the text
    box) or "center" (where the x, y coordinates refer to the top center of the text box).

    "cursor" is an optional character that is used for a cursor to show where the next letter will go. If "cursorBlink"
    is True, then this cursor character will blink on and off.

    The returned value is a string of what the player typed in, or None if the player pressed the Esc key.

    Note that the player can only press Backspace to delete characters, they cannot use the arrow keys to move the
    cursor."""
    inputText = ''
    """inputText will store the text of what the player has typed in so far."""
    done = False
    cursorTimestamp = time.time()
    cursorShow = cursor
    while not done:
        """We will keep looping until the player has pressed the Esc or Enter key."""

        if cursor and cursorBlink and time.time() - 1.0 > cursorTimestamp:
            if cursorShow == cursor:
                cursorShow = '   '
            else:
                cursorShow = cursor
            cursorTimestamp = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    return None
                elif event.key == K_RETURN:
                    done = True
                    if cursorShow:
                        cursorShow = '   '
                elif event.key == K_BACKSPACE:
                    if len(inputText):
                        drawText(prompt + inputText + cursorShow, screenSurf, textrect.left, textrect.top, bgcol, bgcol, 'left')
                        inputText = inputText[:-1]
                else:
                    if len(inputText) >= maxlen or (allowed is not None and chr(event.key) not in allowed):
                        continue
                    if event.key >= 32 and event.key < 128:
                        inputText += getModCase(chr(event.key), event.mod)

        textrect = drawText(prompt + cursorShow, screenSurf, x, y, fgcol, bgcol, pos)
        drawText(prompt + inputText + cursorShow, screenSurf, textrect.left, textrect.top, fgcol, bgcol, 'left')
        pygame.display.update()
        GAME_CLOCK.tick(FPS)
    return inputText

def nextBananaShape(orient):
    """Returns the next banana shape in the sequence of 0, 1, 2, 3, then 0 again. (These correspond to the RIGHT, UP,
    LEFT, and DOWN variables."""
    if orient + 1 == 4:
        return 0
    else:
        return orient + 1

def drawBanana(screenSurf, orient, x, y):
    """Draws the banana shape to the screenSurf surface with its top left corner at the x y coordinate provided.
    "orient" is one of the RIGHT, UP, LEFT, or DOWN values (which are the integers 0 to 3 respectively)"""
    if orient == DOWN:
        screenSurf.blit(BAN_DOWN_SURF, (x, y))
    elif orient == UP:
        screenSurf.blit(BAN_UP_SURF, (x, y))
    elif orient == LEFT:
        screenSurf.blit(BAN_LEFT_SURF, (x, y))
    elif orient == RIGHT:
        screenSurf.blit(BAN_RIGHT_SURF, (x, y))


def drawSun(screenSurf, shocked=False):
    """Draws the sun sprite onto the screenSurf surface. If shocked is True, then use the shocked-looking face,
    otherwise use the normal smiley face. This function does not call python.display.update()"""
    if shocked:
        screenSurf.blit(SUN_SHOCKED_SURF, (SUN_X, SUN_Y))
    else:
        screenSurf.blit(SUN_NORMAL_SURF, (SUN_X, SUN_Y))


def drawGorilla(screenSurf, x, y, arms=BOTH_ARMS_DOWN):
    """Draws the gorilla sprite onto the screenSurf surface at a specific x, y coordinate. The x,y coordinate
    is for the top left corner of the gorilla sprite. Note that all three gorilla surfaces are the same size."""

    if arms == BOTH_ARMS_DOWN:
        gorSurf = GOR_DOWN_SURF
    elif arms == LEFT_ARM_UP:
        gorSurf = GOR_LEFT_SURF
    elif arms == RIGHT_ARM_UP:
        gorSurf = GOR_RIGHT_SURF
    """Above we choose which surface object we will use to draw the gorilla, depending on the "arms" parameter.
    The call to screenSurf.blit() will draw the surface onto the screen (but it won't show up on the screen until
    pygame.display.update() is called."""

    screenSurf.blit(gorSurf, (x, y))

def makeCityScape():
    """This function creates and returns a new cityscape of various buildings on a pygame.Surface object and returns
    this surface object."""

    screenSurf = pygame.Surface((SCR_WIDTH, SCR_HEIGHT)) # first make the new surface the same size of the screen.
    screenSurf.fill(SKY_COLOR) # fill in the surface with the background sky color

    """We will choose an upward, downward, valley "v" curve, or hilly "^" curve for the slope of the buildings.
    Half of the time we will choose the valley slope shape, while the remaining three each have a 1/6 chance of
    being choosen. The slope also determines the height of the first building, which is stored in newHeight."""
    slope = random.randint(1, 6)
    if slope == 1:
        slope = 'upward'
        newHeight = 15
    elif slope == 2:
        slope = 'downward'
        newHeight = 130
    elif slope >= 3 and slope <= 5:
        slope = 'v'
        newHeight = 15
    else:
        slope = '^'
        newHeight = 130

    bottomLine = 335 # the bottom line of the buildings. We want some space for the wind arrow to go
    heightInc = 10 # a baseline for how much buildings grow or shrink compared to the last building
    defBuildWidth = 37 # default building width, also judges how wide buildings can be
    randomHeightDiff = 120 # about how much buildings grow or shrink
    windowWidth = 4 # the width of each window in pixels
    windowHeight = 7 # the height of each window in pixels
    windowSpacingX = 10 # how many pixels apart each window's left edge is
    windowSpacingY = 15 # how many pixels apart each window's top edge is
    gHeight = 25 # (I'm not sure what this suppoes to be in the original Qbasic code, but I copied it anyway)
    # (There also was a maxHeight variable in the original Qbasic, but I don't think it did anything so I left it out.)

    buildingCoords = [] # a list of (left, top) coords of each building, left to right

    x = 2 # x refers to the top left corner of the current building being drawn

    while x < SCR_WIDTH - heightInc:
        # In this loop we keep drawing new buildings until we run out of space on the screen.

        # First the slope type determines if the building should grow or shrink.
        if slope == 'upward':
            newHeight += heightInc
        elif slope == 'downward':
            newHeight -= heightInc
        elif slope == 'v':
            if x > SCR_WIDTH / 2:
                newHeight -= (2 * heightInc)
                # For valley slopes, buildings shrink on the left half of the screen...
            else:
                newHeight += (2 * heightInc)
                # ...and grow on the right half.
        else:
            if x > SCR_WIDTH / 2:
                newHeight += (2 * heightInc)
                # For hilley slopes, buildings grow on the left half of the screen...
            else:
                newHeight -= (2 * heightInc)
                # ...and shrink on the right half.

        # Get the new building's width.
        buildWidth = defBuildWidth + random.randint(0, defBuildWidth)
        if buildWidth + x > SCR_WIDTH:
            buildWidth = SCR_WIDTH - x -2

        # Get the new building's height
        buildHeight = random.randint(heightInc, randomHeightDiff) + newHeight

        # Check if the height is too high.
        if bottomLine - buildHeight <= gHeight:
            buildHeight = gHeight

        # Randomly select one of the building colors.
        buildingColor = BUILDING_COLORS[random.randint(0, len(BUILDING_COLORS)-1)]

        # Draw the building
        pygame.draw.rect(screenSurf, buildingColor, (x+1, bottomLine - (buildHeight+1), buildWidth-1, buildHeight-1))

        buildingCoords.append( (x, bottomLine - buildHeight) )

        # Draw the windows
        for winx in range(3, buildWidth - windowSpacingX + windowWidth, windowSpacingX):
            for winy in range(3, buildHeight - windowSpacingY, windowSpacingY):
                if random.randint(1, 4) == 1:
                    winColor = DARK_WINDOW
                else:
                    winColor = LIGHT_WINDOW
                pygame.draw.rect(screenSurf, winColor, (x + 1 + winx, (bottomLine - buildHeight) + 1 + winy, windowWidth, windowHeight))

        x += buildWidth

    # We want to return both the surface object we've drawn the buildings on, and the coordinates of each building.
    return screenSurf, buildingCoords

def placeGorillas(buildCoords):
    """Using the buildingCoords value returned from makeCityScape(), we want to place the gorillas on the left and right
    side of the screen on the second or third building from the edge."""

    gorPos = [] # item 0 is for (left, top) of player one, item 1 is for player two.
    xAdj = int(GOR_DOWN_SURF.get_rect().width / 2)
    yAdj = GOR_DOWN_SURF.get_rect().height

    for i in range(0,2): # place first and then second player

        # place gorillas on second or third building from the edge.
        if i == 0:
            buildNum = random.randint(1,2)
        else:
            buildNum = random.randint(len(buildCoords)-3, len(buildCoords)-2)

        buildWidth = buildCoords[buildNum + 1][0] - buildCoords[buildNum][0]
        gorPos.append( (buildCoords[buildNum][0] + int(buildWidth / 2) - xAdj, buildCoords[buildNum][1] - yAdj - 1) )

    # The format of the gorPos list is [(p1 x, p1 y), (p2 x, p2 y)]
    return gorPos

def waitForPlayerToPressKey():
    """Calling this function will pause the program until the user presses a key. The key is returned."""
    while True:
        key = checkForKeyPress()
        if key:
            return key

def checkForKeyPress():
    """Calling this function will check if a key has recently been pressed. If so, the key is returned.
    If not, then False is returned. If the Esc key was pressed, then the program terminates."""
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE: # pressing escape quits
                terminate()
            return event.key
    return False

def showStartScreen(screenSurf):
    """Draws the starting introductory screen to screenSurf, with red stars rotating around the border. This screen
    remains until the user presses a key."""
    vertAdj = 0
    horAdj = 0
    while not checkForKeyPress():
        screenSurf.fill(BLACK_COLOR)

        drawStars(screenSurf, vertAdj, horAdj)
        vertAdj += 1
        if vertAdj == 4: vertAdj = 0
        horAdj += 12
        if horAdj == 84: horAdj = 0
        """The stars on the sides of the screen move 1 pixel each iteration through this loop and reset every 4
        pixels. The stars on the top and bottom of the screen move 12 pixels each iteration and reset every 84 pixels."""

        drawText('P  y  t  h  o  n     G  O  R  I  L  L  A  S', screenSurf, SCR_WIDTH / 2, 50, WHITE_COLOR, BLACK_COLOR, pos='center')
        drawText('Your mission is to hit your opponent with the exploding', screenSurf, SCR_WIDTH / 2, 110, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('banana by varying the angle and power of your throw, taking', screenSurf, SCR_WIDTH / 2, 130, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('into account wind speed, gravity, and the city skyline.', screenSurf, SCR_WIDTH / 2, 150, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('The wind speed is shown by a directional arrow at the bottom', screenSurf, SCR_WIDTH / 2, 170, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('of the playing field, its length relative to its strength.', screenSurf, SCR_WIDTH / 2, 190, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('Press any key to continue', screenSurf, SCR_WIDTH / 2, 300, GRAY_COLOR, BLACK_COLOR, pos='center')

        pygame.display.update()
        GAME_CLOCK.tick(FPS)

def showGameOverScreen(screenSurf, p1name, p1score, p2name, p2score):
    """Draws the game over screen to screenSurf, showing the players' names and scores. This screen has rotating
    red stars too, and hangs around until the user presses a key."""
    p1score = str(p1score)
    p2score = str(p2score)
    vertAdj = 0
    horAdj = 0
    while not checkForKeyPress():
        screenSurf.fill(BLACK_COLOR)

        drawStars(screenSurf, vertAdj, horAdj)
        vertAdj += 1
        if vertAdj == 4: vertAdj = 0
        horAdj += 12
        if horAdj == 84: horAdj = 0
        """The stars on the sides of the screen move 1 pixel each iteration through this loop and reset every 4
        pixels. The stars on the top and bottom of the screen move 12 pixels each iteration and reset every 84 pixels."""

        drawText('GAME OVER!', screenSurf, SCR_WIDTH / 2, 120, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText('Score:', screenSurf, SCR_WIDTH / 2, 155, GRAY_COLOR, BLACK_COLOR, pos='center')
        drawText(p1name, screenSurf, 225, 170, GRAY_COLOR, BLACK_COLOR)
        drawText(p1score, screenSurf, 395, 170, GRAY_COLOR, BLACK_COLOR)
        drawText(p2name, screenSurf, 225, 185, GRAY_COLOR, BLACK_COLOR)
        drawText(p2score, screenSurf, 395, 185, GRAY_COLOR, BLACK_COLOR)
        drawText('Press any key to continue', screenSurf, SCR_WIDTH / 2, 298, GRAY_COLOR, BLACK_COLOR, pos='center')

        pygame.display.update()
        GAME_CLOCK.tick(FPS)

def drawStars(screenSurf, vertAdj, horAdj):
    """This function draws the red stars on the border of screenSurf."""
    for i in range(16):
        # draw top row of stars
        screenSurf.blit(STAR_SURF, (2 + (((3 - vertAdj) + i * 4) * STAR_SURF.get_width()), 3))
        # draw bottom row of stars
        screenSurf.blit(STAR_SURF, (2 + ((vertAdj + i * 4) * STAR_SURF.get_width()), SCR_HEIGHT - 7 - STAR_SURF.get_height()))

    for i in range(4):
        # draw left column of stars going down
        screenSurf.blit(STAR_SURF, (5, 6 + STAR_SURF.get_height() + (horAdj + i * 84)))
        # draw right column of stars going up
        screenSurf.blit(STAR_SURF, (SCR_WIDTH - 5 - STAR_SURF.get_width(), (SCR_HEIGHT - (6 + STAR_SURF.get_height() + (horAdj + i * 84)))))



def showSettingsScreen(screenSurf):
    """This is the screen that lets the user type in their name and settings for the game."""
    p1name = None
    p2name = None
    points = None
    gravity = None

    screenSurf.fill(BLACK_COLOR)

    while p1name is None:
        p1name = inputMode("Name of Player 1 (Default = 'Player 1'):  ", screenSurf, SCR_WIDTH / 2 - 146, 50, GRAY_COLOR, BLACK_COLOR, maxlen=10, pos='left', cursorBlink=True)
    if p1name == '':
        p1name = 'Player 1'

    while p2name is None:
        p2name = inputMode("Name of Player 2 (Default = 'Player 2'):  ", screenSurf, SCR_WIDTH / 2 - 146, 80, GRAY_COLOR, BLACK_COLOR, maxlen=10, pos='left', cursorBlink=True)
    if p2name == '':
        p2name = 'Player 2'

    while points is None:
        points = inputMode("Play to how many total points (Default = 3)?  ", screenSurf, SCR_WIDTH / 2 - 155, 110, GRAY_COLOR, BLACK_COLOR, maxlen=6, allowed='0123456789', pos='left', cursorBlink=True)
    if points == '':
        points = 3
    else:
        points = int(points)

    while gravity is None:
        gravity = inputMode("Gravity in Meters/Sec (Earth = 9.8)?  ", screenSurf, SCR_WIDTH / 2 - 150, 140, GRAY_COLOR, BLACK_COLOR, maxlen=6, allowed='0123456789.', pos='left', cursorBlink=True)
    if gravity == '':
        gravity = 9.8
    else:
        gravity = float(gravity)

    drawText('--------------', screenSurf, SCR_WIDTH / 2 -10, 170, GRAY_COLOR, BLACK_COLOR, pos='center')
    drawText('V = View Intro', screenSurf, SCR_WIDTH / 2 -10, 200, GRAY_COLOR, BLACK_COLOR, pos='center')
    drawText('P = Play Game', screenSurf, SCR_WIDTH / 2 -10, 230, GRAY_COLOR, BLACK_COLOR, pos='center')
    drawText('Your Choice?', screenSurf, SCR_WIDTH / 2 -10, 260, GRAY_COLOR, BLACK_COLOR, pos='center')
    pygame.display.update()

    key = waitForPlayerToPressKey()
    while chr(key) != 'v' and chr(key) != 'p':
        key = waitForPlayerToPressKey()

    return p1name, p2name, points, gravity, chr(key) # returns 'v' or 'p'

def showIntroScreen(screenSurf, p1name, p2name):
    """This is the screen that plays if the user selected "view intro" from the starting screen."""
    screenSurf.fill(SKY_COLOR)
    drawText('P  y  t  h  o  n     G  O  R  I  L  L  A  S', screenSurf, SCR_WIDTH / 2, 15, WHITE_COLOR, SKY_COLOR, pos='center')
    drawText('STARRING:', screenSurf, SCR_WIDTH / 2, 55, WHITE_COLOR, SKY_COLOR, pos='center')
    drawText('%s AND %s' % (p1name, p2name), screenSurf, SCR_WIDTH / 2, 115, WHITE_COLOR, SKY_COLOR, pos='center')

    x = 278
    y = 175

    for i in range(2):
        drawGorilla(screenSurf, x-13, y, RIGHT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, LEFT_ARM_UP)
        pygame.display.update()

        time.sleep(2)

        drawGorilla(screenSurf, x-13, y, LEFT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, RIGHT_ARM_UP)
        pygame.display.update()

        time.sleep(2)

    for i in range(4):
        drawGorilla(screenSurf, x-13, y, LEFT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, RIGHT_ARM_UP)
        pygame.display.update()

        time.sleep(0.3)

        drawGorilla(screenSurf, x-13, y, RIGHT_ARM_UP)
        drawGorilla(screenSurf, x+47, y, LEFT_ARM_UP)
        pygame.display.update()

        time.sleep(0.3)


def getShot(screenSurf, p1name, p2name, playerNum):
    """getShot() is called when we want to get the angle and velocity from the player."""
    pygame.draw.rect(screenSurf, SKY_COLOR, (0, 0, 200, 50))
    pygame.draw.rect(screenSurf, SKY_COLOR, (550, 0, 00, 50))

    drawText(p1name, screenSurf, 2, 2, WHITE_COLOR, SKY_COLOR)
    drawText(p2name, screenSurf, 538, 2, WHITE_COLOR, SKY_COLOR)

    if playerNum == 1:
        x = 2
    else:
        x = 538

    angle = ''
    while angle == '':
        angle = inputMode('Angle:  ', screenSurf, x, 18, WHITE_COLOR, SKY_COLOR, maxlen=3, allowed='0123456789')
    if angle is None: terminate()
    angle = int(angle)

    velocity = ''
    while velocity == '':
        velocity = inputMode('Velocity:  ', screenSurf, x, 34, WHITE_COLOR, SKY_COLOR, maxlen=3, allowed='0123456789')
    if velocity is None: terminate()
    velocity = int(velocity)

    # Erase the user's input
    drawText('Angle:   ' + str(angle), screenSurf, x, 2, SKY_COLOR, SKY_COLOR)
    drawText('Velocity:   ' + str(angle), screenSurf, x, 2, SKY_COLOR, SKY_COLOR)
    pygame.display.update()

    if playerNum == 2:
        angle = 180 - angle

    return (angle, velocity)

def displayScore(screenSurf, oneScore, twoScore):
    """Draws the score on the screenSurf surface."""
    drawText(str(oneScore) + '>Score<' + str(twoScore), screenSurf, 270, 310, WHITE_COLOR, SKY_COLOR, pos='left')

def plotShot(screenSurf, skylineSurf, angle, velocity, playerNum, wind, gravity, gor1, gor2):
    # startx and starty is the upper left corner of the gorilla.
    angle = angle / 180.0 * math.pi
    initXVel = math.cos(angle) * velocity
    initYVel = math.sin(angle) * velocity
    gorWidth, gorHeight = GOR_DOWN_SURF.get_size()
    gor1rect = pygame.Rect(gor1[0], gor1[1], gorWidth, gorHeight)
    gor2rect = pygame.Rect(gor2[0], gor2[1], gorWidth, gorHeight)


    if playerNum == 1:
        gorImg = LEFT_ARM_UP
    else:
        gorImg = RIGHT_ARM_UP
    """The player 1 gorilla on the left uses his left arm to throw, the player 2 gorilla on the right uses his
    right arm to throw."""

    if playerNum == 1:
        startx = gor1[0]
        starty = gor1[1]
    elif playerNum == 2:
        startx = gor2[0]
        starty = gor2[1]

    drawGorilla(screenSurf, startx, starty, gorImg)
    pygame.display.update()
    time.sleep(0.3)
    drawGorilla(screenSurf, startx, starty, BOTH_ARMS_DOWN)
    pygame.display.update()
    """Draw the gorilla throwing the banana."""

    bananaShape = UP

    if playerNum == 2:
        startx += GOR_DOWN_SURF.get_size()[0]

    starty -= getBananaRect(0, 0, bananaShape).height + BAN_UP_SURF.get_size()[1]

    impact = False
    bananaInPlay = True

    t = 1.0
    sunHit = False

    while not impact and bananaInPlay:
        x = startx + (initXVel * t) + (0.5 * (wind / 5) * t**2)
        y = starty + ((-1 * (initYVel * t)) + (0.5 * gravity * t**2))
        """This is basically the equation that describes the banana's arc."""

        if x >= SCR_WIDTH - 10 or x <= 3 or y >= SCR_HEIGHT:
            bananaInPlay = False

        bananaRect = getBananaRect(x, y, bananaShape)
        if bananaShape == UP:
            bananaSurf = BAN_UP_SURF
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == DOWN:
            bananaSurf = BAN_DOWN_SURF
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == LEFT:
            bananaSurf = BAN_LEFT_SURF
        elif bananaShape == RIGHT:
            bananaSurf = BAN_RIGHT_SURF

        bananaShape = nextBananaShape(bananaShape)

        srcPixArray = pygame.PixelArray(skylineSurf)
        if bananaInPlay and y > 0:

            if sunRect.collidepoint(x, y):
                # banana has hit the sun, so draw the "shocked" face.
                sunHit = True

            # draw the appropriate sun face
            drawSun(screenSurf, shocked=sunHit)

            if bananaRect.colliderect(gor1rect):
                # banana has hit player 1

                """Note that we draw the explosion on the screen (on screenSurf) and on the separate skyline surface (on skylineSurf).
                This is done so that bananas won't hit the sun or any text and accidentally think they've hit something. We also want
                the skylineSurf surface object to keep track of what chunks of the buildings are left."""
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(GOR_EXPLOSION_SIZE*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=GOR_EXPLOSION_SIZE, speed=0.005)
                drawSun(screenSurf)
                return 'gorilla1'
            elif bananaRect.colliderect(gor2rect):
                # banana has hit player 2
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(GOR_EXPLOSION_SIZE*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=GOR_EXPLOSION_SIZE, speed=0.005)
                screenSurf.fill(SKY_COLOR, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'gorilla2'
            elif collideWithNonColor(srcPixArray, screenSurf, bananaRect, SKY_COLOR):
                # banana has hit a building
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery)
                screenSurf.fill(SKY_COLOR, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'building'

        del srcPixArray
        """Pygame doesn't let us blit a surface while there is a pixel array of it existing, so we delete it."""

        screenSurf.blit(bananaSurf, (bananaRect.topleft))
        pygame.display.update()
        time.sleep(0.02)

        screenSurf.fill(SKY_COLOR, bananaRect) # erase banana

        t += 0.1 # go forward in the plot.
    drawSun(screenSurf)
    return 'miss'

def victoryDance(screenSurf, x, y):
    """Given the x,y coordinates of the topleft corner of the gorilla sprite, this goes through
    the victory dance routine of the gorilla where they start waving their arms in the air."""
    for i in range(4):
        screenSurf.blit(GOR_LEFT_SURF, (x, y))
        pygame.display.update()
        time.sleep(0.3)
        screenSurf.blit(GOR_RIGHT_SURF, (x, y))
        pygame.display.update()
        time.sleep(0.3)


def collideWithNonColor(pixArr, surfObj, rect, color):
    """This checks the area (described by "rect") on pixArr (a pixel array derived from the surfObj surface object)
    if it has any pixels that are not the color specified by the "color" parameter. This function is used to detect
    if the banana has hit any non-sky colored parts (which means a gorilla or a building)."""
    rightSide = min(rect.right, SCR_WIDTH)
    bottomSide = min(rect.bottom, SCR_HEIGHT)

    for x in range(rect.left, rightSide):
        for y in range(rect.top, bottomSide):
            if surfObj.unmap_rgb(pixArr[x][y]) != color:
                return True
    return False


def getBananaRect(x, y, shape):
    if shape == UP:
        return pygame.Rect((x, y), BAN_UP_SURF.get_size())
    if shape == DOWN:
        return pygame.Rect((x, y), BAN_DOWN_SURF.get_size())
    if shape == LEFT:
        return pygame.Rect((x, y), BAN_LEFT_SURF.get_size())
    if shape == RIGHT:
        return pygame.Rect((x, y), BAN_RIGHT_SURF.get_size())

def getWind():
    """Randomly determine what the wind speed and direction should be for this game."""
    wind = random.randint(5, 15)
    if random.randint(0, 1):
        wind *= -1
    return wind

def drawWind(screenSurf, wind):
    """Draws the wind arrow on the screenSurf object at the bottom of the screen. The "wind" parameter comes from
    a call to getWind()."""
    if wind != 0:
        wind *= 3
        pygame.draw.line(screenSurf, EXPLOSION_COLOR, (int(SCR_WIDTH / 2), SCR_HEIGHT - 5), (int(SCR_WIDTH / 2) + wind, SCR_HEIGHT - 5))
        # draw the arrow end
        if wind > 0: arrowDir = -2
        else:        arrowDir = 2
        pygame.draw.line(screenSurf, EXPLOSION_COLOR, (int(SCR_WIDTH / 2) + wind, SCR_HEIGHT - 5), (int(SCR_WIDTH / 2) + wind + arrowDir, SCR_HEIGHT - 5 - 2))
        pygame.draw.line(screenSurf, EXPLOSION_COLOR, (int(SCR_WIDTH / 2) + wind, SCR_HEIGHT - 5), (int(SCR_WIDTH / 2) + wind + arrowDir, SCR_HEIGHT - 5 + 2))

def doExplosion(screenSurf, skylineSurf, x, y, explosionSize=BUILD_EXPLOSION_SIZE, speed=0.05):
    for r in range(1, explosionSize):
        pygame.draw.circle(screenSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.draw.circle(skylineSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.display.update()
        time.sleep(speed)
    for r in range(explosionSize, 1, -1):
        pygame.draw.circle(screenSurf, SKY_COLOR, (x, y), explosionSize)
        pygame.draw.circle(skylineSurf, SKY_COLOR, (x, y), explosionSize)
        pygame.draw.circle(screenSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.draw.circle(skylineSurf, EXPLOSION_COLOR, (x, y), r)
        pygame.display.update()
        time.sleep(speed)
    pygame.draw.circle(screenSurf, SKY_COLOR, (x, y), 2)
    pygame.draw.circle(skylineSurf, SKY_COLOR, (x, y), 2)
    pygame.display.update()


def main():
    winSurface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), 0, 32)
    """winSurface, being the surface object returned by pygame.display.set_mode(), will be drawn to the screen
    every time pygame.display.update() is called."""

    # Uncomment either of the following lines to put the game into full screen mode.
    ##winSurface = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), pygame.FULLSCREEN, 32)
    ##pygame.display.toggle_fullscreen()
    pygame.display.set_caption('Gorillas.py')

    showStartScreen(winSurface)

    while True:
        # start a new game
        p1name, p2name, winPoints, gravity, nextScreen = showSettingsScreen(winSurface)
        if nextScreen == 'v':
            showIntroScreen(winSurface, p1name, p2name)

        # Reset the score and make it the first player's turn.
        p1score = 0
        p2score = 0
        turn = 1

        newRound = True
        while p1score < winPoints and p2score < winPoints:
            if newRound:
                # At the start of a new round, make a new city scape, place the gorillas, and get the wind speed.
                skylineSurf, buildCoords = makeCityScape() # Note that the city skyline goes on skylineSurf, not winSurface.
                gorPos = placeGorillas(buildCoords)
                wind = getWind()
                newRound = False

            # Do all the drawing.
            winSurface.blit(skylineSurf, (0,0))
            drawGorilla(winSurface, gorPos[0][0], gorPos[0][1], 0)
            drawGorilla(winSurface, gorPos[1][0], gorPos[1][1], 0)
            drawWind(winSurface, wind)
            drawSun(winSurface)
            displayScore(winSurface, p1score, p2score)

            pygame.display.update()

            angle, velocity = getShot(winSurface, p1name, p2name, turn)
            if turn == 1:
                gorx, gory = gorPos[0][0], gorPos[0][1]
            elif turn == 2:
                gorx, gory = gorPos[1][0], gorPos[1][1]
            result = plotShot(winSurface, skylineSurf, angle, velocity, turn, wind, 9.8, gorPos[0], gorPos[1])

            if result == 'gorilla1':
                victoryDance(winSurface, gorPos[1][0], gorPos[1][1])
                p2score += 1
                newRound = True
            elif result == 'gorilla2':
                victoryDance(winSurface, gorPos[0][0], gorPos[0][1])
                p1score += 1
                newRound = True

            if turn == 1:
                turn = 2
            else:
                turn = 1

        showGameOverScreen(winSurface, p1name, p1score, p2name, p2score)

if __name__ == '__main__':
    main()

