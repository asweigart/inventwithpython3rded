"""Hola, y bienvenido al código fuente de Gorilas.py. Este programa pretende estar muy bien documentado, de modo que sea
accesible a un programador novato. Este programa fue escrito por Al Sweigart, como acompañamiento a su libro gratuito
"Inventa Tus Propios Juegos de Computadora con Python", ofrecido bajo licencia Creative Commons cuyo texto completo está disponible en:

        http://inventwithpython.com

Siéntete libre de escribirle al autor con cualquier consulta sobre programación a al@inventwithpython.com

Este programa intenta replicar gorillas.bas, un programa de Qbasic que fue popular durante la década de 1990. Leyendo
los comentarios, puedes aprender cómo se arma un juego simple en Python con el motor de programación Pygame.

Los comentarios vendrán en general _después_ de las líneas de código que describen.

Si te gusta esto, dale un vistazo a inventwithpython.com para leer el libro (que contiene juegos similares) gratis!

La documentación de Pygame es bastante buena, y puedes encontrarla en: http://www.pygame.org/docs

Desafortunadamente este juego no tiene sonido.
"""

import pygame, sys, time, random, math
from pygame.locals import *
"""Importaremos unos cuantos módulos para este juego. "pygame" contiene todos los gráficos y funciones relacionadas con el juego
provistos por el motor Pygame. "sys" contiene la función exit(). "time" contiene la función sleep(). "random" contiene la 
función randint(), y "math" contiene la constante pi."""


"""Todas las variables a continuación en MAYÚSCULAS son constantes, es decir, sólo se supone que sean leídas y no
modificadas. (No hay nada que impida al programa modificarlas, es sólo una convención usada por los programadores).
Las constantes son un poco más descriptivas que simplemente usar los propios números. Y si alguna vez quieres cambiar
algún valor (como el tamaño de las explosiones o el color de los gorilas), sólo necesitas cambiarlo en un
lugar."""

ANCHO_PNT = 640
ALTURA_PNT = 350
FPS = 30
RELOJ_JUEGO = pygame.time.Clock()
"""Aquí hay varias constantes que usaremos en el juego. El juego original de Qbasic tenía un tamaño de pantalla de 640x350, de modo que
usaremos eso como nuestro tamaño de pantalla. Usaremos un solo objeto global Clock para manejar algunas cuestiones de sincronización en todas nuestras
funciones, y generalmente ajustaremos FPS a 30 (excepto cuando queramos ajustarlo a otro valor).

Las constantes son útiles porque puedes simplemente ajustar el valor en un lugar, y será usado en todo el programa.

Prueba experimentando con diferentes valores de estas constantes."""

COLORES_EDIFICIO = ((173, 170, 173), (0, 170, 173), (173, 0, 0))
VENTANA_CLARA = (255, 255, 82)
VENTANA_OSCURA = (82, 85, 82)
COLOR_CIELO = (0, 0, 173)
COLOR_GOR = (255, 170, 82)
COLOR_BAN = (255, 255, 82)
COLOR_EXPLOSIÓN = (255, 0, 0)
COLOR_SOL = (255, 255, 0)
COLOR_ROJO_OSCURO = (173, 0, 0)
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_GRIS = (173, 170, 173)
"""Aquí hay unos cuantos colores. Pygame usa una tupla de tres enteros para especificar un color. Los enteros son la
cantidad de Rojo, Azul, y Verde (en orden) en el color. Esto se conoce como un valor RGB.

COLORES_EDIFICIO contiene una tupla de estas tuplas RGB y representa los diferentes colores que los edificios pueden tomar."""

TAMAÑO_EXPLOSIÓN_EDIF = int(ALTURA_PNT / 50)
TAMAÑO_EXPLOSIÓN_GOR = 30
"""TAMAÑO_EXPLOSIÓN_EDIF contiene el tamaño de una explosión cuando una banana choca contra un edificio, y TAMAÑO_EXPLOSIÓN_GOR es el tamaño
cuando choca contra un gorila."""

SOL_X = 300
SOL_Y = 10
"""La posición del sol en el cielo."""

pygame.init()
FUENTE_JUEGO = pygame.font.SysFont(None, 20)
"""La función pygame.init() debe ser llamada antes de llamar a cualquiera de las funciones de Pygame.
Vamos a utilizar el tipo de letra predeterminado del sistema en un tamaño de 20 puntos."""

# orientación de la banana:
DERECHA = 0
ARRIBA = 1
IZQUIERDA = 2
ABAJO = 3
"""Algunas constantes para la dirección en que se orienta la banana (o cualquier otra cosa)."""

# tipos de brazos del gorila
AMBOS_BRAZOS_ABAJO = 0
BRAZO_IZQUIERDO_ARRIBA = 1
BRAZO_DERECHO_ARRIBA = 2
"""Constantes para determinar cuál de los tres sprites del gorila usar: ambos brazos abajo, brazo izquierdo arriba, o brazo derecho arriba."""


"""Las siguientes cadenas multilínea son usadas con la función makeSurfaceFromASCII(). Es básicamente una forma de
generar superficies aparte de usar las funciones de dibujo o incluir archivos gráficos con este archivo .py.

Experimenta cambiando las cadenas. La primera y última línea son ignoradas (de modo que no tengas que lidiar con
cuestiones de indentación en la cadena)."""

ESTRELLA_ASCII = """


   XX  XX
    XXXX
  XXXXXXXX
    XXXX
   XX  XX
"""

GOR_ABAJO_ASCII = """

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

GOR_IZQUIERDA_ASCII = """
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

GOR_DERECHA_ASCII = """
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

BAN_DERECHA_ASCII = """
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

BAN_IZQUIERDA_ASCII = """
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

BAN_ARRIBA_ASCII = """
XX     XX
XXXXXXXXX
 XXXXXXX
  XXXXX
"""

BAN_ABAJO_ASCII = """
  XXXXX
 XXXXXXX
XXXXXXXXX
XX     XX
"""

SOL_NORMAL_ASCII = """
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

SOL_SORPRENDIDO_ASCII = """
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

GOR_DOWN_SURF    = makeSurfaceFromASCII(GOR_ABAJO_ASCII,    COLOR_GOR,      COLOR_CIELO)
GOR_LEFT_SURF    = makeSurfaceFromASCII(GOR_IZQUIERDA_ASCII,    COLOR_GOR,      COLOR_CIELO)
GOR_RIGHT_SURF   = makeSurfaceFromASCII(GOR_DERECHA_ASCII,   COLOR_GOR,      COLOR_CIELO)
BAN_RIGHT_SURF   = makeSurfaceFromASCII(BAN_DERECHA_ASCII,   COLOR_BAN,      COLOR_CIELO)
BAN_LEFT_SURF    = makeSurfaceFromASCII(BAN_IZQUIERDA_ASCII,    COLOR_BAN,      COLOR_CIELO)
BAN_UP_SURF      = makeSurfaceFromASCII(BAN_ARRIBA_ASCII,      COLOR_BAN,      COLOR_CIELO)
BAN_DOWN_SURF    = makeSurfaceFromASCII(BAN_ABAJO_ASCII,    COLOR_BAN,      COLOR_CIELO)
SUN_NORMAL_SURF  = makeSurfaceFromASCII(SOL_NORMAL_ASCII,  COLOR_SOL,      COLOR_CIELO)
SUN_SHOCKED_SURF = makeSurfaceFromASCII(SOL_SORPRENDIDO_ASCII, COLOR_SOL,      COLOR_CIELO)
STAR_SURF        = makeSurfaceFromASCII(ESTRELLA_ASCII,        COLOR_ROJO_OSCURO, COLOR_NEGRO)

assert GOR_DOWN_SURF.get_size() == GOR_LEFT_SURF.get_size() == GOR_RIGHT_SURF.get_size()
"""Create the pygame.Surface objects from the ASCII strings."""

sunRect = pygame.Rect(SOL_X, SOL_Y, SUN_NORMAL_SURF.get_width(), SUN_NORMAL_SURF.get_height())
"""sunRect will be a global value so we'll always know where the sun is."""

def drawText(text, surfObj, x, y, fgcol, bgcol, pos='left'):
    """A generic function to draw a string to a pygame.Surface object at a certain x,y location. This returns
    a pygame.Rect object which describes the area the string was drawn on.

    If the pos parameter is "left", then the x,y parameter specifies the top left corner of the text rectangle.
    If the pos parameter is "center", then the x,y parameter specifies the middle top point of the text rectangle."""

    textobj = FUENTE_JUEGO.render(text, 1, fgcol, bgcol) # creates the text in memory (it's not on a surface yet).
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
        RELOJ_JUEGO.tick(FPS)
    return inputText

def nextBananaShape(orient):
    """Returns the next banana shape in the sequence of 0, 1, 2, 3, then 0 again. (These correspond to the DERECHA, ARRIBA,
    IZQUIERDA, and ABAJO variables."""
    if orient + 1 == 4:
        return 0
    else:
        return orient + 1

def drawBanana(screenSurf, orient, x, y):
    """Draws the banana shape to the screenSurf surface with its top left corner at the x y coordinate provided.
    "orient" is one of the DERECHA, ARRIBA, IZQUIERDA, or ABAJO values (which are the integers 0 to 3 respectively)"""
    if orient == ABAJO:
        screenSurf.blit(BAN_DOWN_SURF, (x, y))
    elif orient == ARRIBA:
        screenSurf.blit(BAN_UP_SURF, (x, y))
    elif orient == IZQUIERDA:
        screenSurf.blit(BAN_LEFT_SURF, (x, y))
    elif orient == DERECHA:
        screenSurf.blit(BAN_RIGHT_SURF, (x, y))


def drawSun(screenSurf, shocked=False):
    """Draws the sun sprite onto the screenSurf surface. If shocked is True, then use the shocked-looking face,
    otherwise use the normal smiley face. This function does not call python.display.update()"""
    if shocked:
        screenSurf.blit(SUN_SHOCKED_SURF, (SOL_X, SOL_Y))
    else:
        screenSurf.blit(SUN_NORMAL_SURF, (SOL_X, SOL_Y))


def drawGorilla(screenSurf, x, y, arms=AMBOS_BRAZOS_ABAJO):
    """Draws the gorilla sprite onto the screenSurf surface at a specific x, y coordinate. The x,y coordinate
    is for the top left corner of the gorilla sprite. Note that all three gorilla surfaces are the same size."""

    if arms == AMBOS_BRAZOS_ABAJO:
        gorSurf = GOR_DOWN_SURF
    elif arms == BRAZO_IZQUIERDO_ARRIBA:
        gorSurf = GOR_LEFT_SURF
    elif arms == BRAZO_DERECHO_ARRIBA:
        gorSurf = GOR_RIGHT_SURF
    """Above we choose which surface object we will use to draw the gorilla, depending on the "arms" parameter.
    The call to screenSurf.blit() will draw the surface onto the screen (but it won't show up on the screen until
    pygame.display.update() is called."""

    screenSurf.blit(gorSurf, (x, y))

def makeCityScape():
    """This function creates and returns a new cityscape of various buildings on a pygame.Surface object and returns
    this surface object."""

    screenSurf = pygame.Surface((ANCHO_PNT, ALTURA_PNT)) # first make the new surface the same size of the screen.
    screenSurf.fill(COLOR_CIELO) # fill in the surface with the background sky color

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

    while x < ANCHO_PNT - heightInc:
        # In this loop we keep drawing new buildings until we run out of space on the screen.

        # First the slope type determines if the building should grow or shrink.
        if slope == 'upward':
            newHeight += heightInc
        elif slope == 'downward':
            newHeight -= heightInc
        elif slope == 'v':
            if x > ANCHO_PNT / 2:
                newHeight -= (2 * heightInc)
                # For valley slopes, buildings shrink on the left half of the screen...
            else:
                newHeight += (2 * heightInc)
                # ...and grow on the right half.
        else:
            if x > ANCHO_PNT / 2:
                newHeight += (2 * heightInc)
                # For hilley slopes, buildings grow on the left half of the screen...
            else:
                newHeight -= (2 * heightInc)
                # ...and shrink on the right half.

        # Get the new building's width.
        buildWidth = defBuildWidth + random.randint(0, defBuildWidth)
        if buildWidth + x > ANCHO_PNT:
            buildWidth = ANCHO_PNT - x -2

        # Get the new building's height
        buildHeight = random.randint(heightInc, randomHeightDiff) + newHeight

        # Check if the height is too high.
        if bottomLine - buildHeight <= gHeight:
            buildHeight = gHeight

        # Randomly select one of the building colors.
        buildingColor = COLORES_EDIFICIO[random.randint(0, len(COLORES_EDIFICIO)-1)]

        # Draw the building
        pygame.draw.rect(screenSurf, buildingColor, (x+1, bottomLine - (buildHeight+1), buildWidth-1, buildHeight-1))

        buildingCoords.append( (x, bottomLine - buildHeight) )

        # Draw the windows
        for winx in range(3, buildWidth - windowSpacingX + windowWidth, windowSpacingX):
            for winy in range(3, buildHeight - windowSpacingY, windowSpacingY):
                if random.randint(1, 4) == 1:
                    winColor = VENTANA_OSCURA
                else:
                    winColor = VENTANA_CLARA
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
        screenSurf.fill(COLOR_NEGRO)

        drawStars(screenSurf, vertAdj, horAdj)
        vertAdj += 1
        if vertAdj == 4: vertAdj = 0
        horAdj += 12
        if horAdj == 84: horAdj = 0
        """The stars on the sides of the screen move 1 pixel each iteration through this loop and reset every 4
        pixels. The stars on the top and bottom of the screen move 12 pixels each iteration and reset every 84 pixels."""

        drawText('P  y  t  h  o  n     G  O  R  I  L  L  A  S', screenSurf, ANCHO_PNT / 2, 50, COLOR_BLANCO, COLOR_NEGRO, pos='center')
        drawText('Your mission is to hit your opponent with the exploding', screenSurf, ANCHO_PNT / 2, 110, COLOR_GRIS, COLOR_NEGRO, pos='center')
        drawText('banana by varying the angle and power of your throw, taking', screenSurf, ANCHO_PNT / 2, 130, COLOR_GRIS, COLOR_NEGRO, pos='center')
        drawText('into account wind speed, gravity, and the city skyline.', screenSurf, ANCHO_PNT / 2, 150, COLOR_GRIS, COLOR_NEGRO, pos='center')
        drawText('The wind speed is shown by a directional arrow at the bottom', screenSurf, ANCHO_PNT / 2, 170, COLOR_GRIS, COLOR_NEGRO, pos='center')
        drawText('of the playing field, its length relative to its strength.', screenSurf, ANCHO_PNT / 2, 190, COLOR_GRIS, COLOR_NEGRO, pos='center')
        drawText('Press any key to continue', screenSurf, ANCHO_PNT / 2, 300, COLOR_GRIS, COLOR_NEGRO, pos='center')

        pygame.display.update()
        RELOJ_JUEGO.tick(FPS)

def showGameOverScreen(screenSurf, p1name, p1score, p2name, p2score):
    """Draws the game over screen to screenSurf, showing the players' names and scores. This screen has rotating
    red stars too, and hangs around until the user presses a key."""
    p1score = str(p1score)
    p2score = str(p2score)
    vertAdj = 0
    horAdj = 0
    while not checkForKeyPress():
        screenSurf.fill(COLOR_NEGRO)

        drawStars(screenSurf, vertAdj, horAdj)
        vertAdj += 1
        if vertAdj == 4: vertAdj = 0
        horAdj += 12
        if horAdj == 84: horAdj = 0
        """The stars on the sides of the screen move 1 pixel each iteration through this loop and reset every 4
        pixels. The stars on the top and bottom of the screen move 12 pixels each iteration and reset every 84 pixels."""

        drawText('GAME OVER!', screenSurf, ANCHO_PNT / 2, 120, COLOR_GRIS, COLOR_NEGRO, pos='center')
        drawText('Score:', screenSurf, ANCHO_PNT / 2, 155, COLOR_GRIS, COLOR_NEGRO, pos='center')
        drawText(p1name, screenSurf, 225, 170, COLOR_GRIS, COLOR_NEGRO)
        drawText(p1score, screenSurf, 395, 170, COLOR_GRIS, COLOR_NEGRO)
        drawText(p2name, screenSurf, 225, 185, COLOR_GRIS, COLOR_NEGRO)
        drawText(p2score, screenSurf, 395, 185, COLOR_GRIS, COLOR_NEGRO)
        drawText('Press any key to continue', screenSurf, ANCHO_PNT / 2, 298, COLOR_GRIS, COLOR_NEGRO, pos='center')

        pygame.display.update()
        RELOJ_JUEGO.tick(FPS)

def drawStars(screenSurf, vertAdj, horAdj):
    """This function draws the red stars on the border of screenSurf."""
    for i in range(16):
        # draw top row of stars
        screenSurf.blit(STAR_SURF, (2 + (((3 - vertAdj) + i * 4) * STAR_SURF.get_width()), 3))
        # draw bottom row of stars
        screenSurf.blit(STAR_SURF, (2 + ((vertAdj + i * 4) * STAR_SURF.get_width()), ALTURA_PNT - 7 - STAR_SURF.get_height()))

    for i in range(4):
        # draw left column of stars going down
        screenSurf.blit(STAR_SURF, (5, 6 + STAR_SURF.get_height() + (horAdj + i * 84)))
        # draw right column of stars going up
        screenSurf.blit(STAR_SURF, (ANCHO_PNT - 5 - STAR_SURF.get_width(), (ALTURA_PNT - (6 + STAR_SURF.get_height() + (horAdj + i * 84)))))



def showSettingsScreen(screenSurf):
    """This is the screen that lets the user type in their name and settings for the game."""
    p1name = None
    p2name = None
    points = None
    gravity = None

    screenSurf.fill(COLOR_NEGRO)

    while p1name is None:
        p1name = inputMode("Name of Player 1 (Default = 'Player 1'):  ", screenSurf, ANCHO_PNT / 2 - 146, 50, COLOR_GRIS, COLOR_NEGRO, maxlen=10, pos='left', cursorBlink=True)
    if p1name == '':
        p1name = 'Player 1'

    while p2name is None:
        p2name = inputMode("Name of Player 2 (Default = 'Player 2'):  ", screenSurf, ANCHO_PNT / 2 - 146, 80, COLOR_GRIS, COLOR_NEGRO, maxlen=10, pos='left', cursorBlink=True)
    if p2name == '':
        p2name = 'Player 2'

    while points is None:
        points = inputMode("Play to how many total points (Default = 3)?  ", screenSurf, ANCHO_PNT / 2 - 155, 110, COLOR_GRIS, COLOR_NEGRO, maxlen=6, allowed='0123456789', pos='left', cursorBlink=True)
    if points == '':
        points = 3
    else:
        points = int(points)

    while gravity is None:
        gravity = inputMode("Gravity in Meters/Sec (Earth = 9.8)?  ", screenSurf, ANCHO_PNT / 2 - 150, 140, COLOR_GRIS, COLOR_NEGRO, maxlen=6, allowed='0123456789.', pos='left', cursorBlink=True)
    if gravity == '':
        gravity = 9.8
    else:
        gravity = float(gravity)

    drawText('--------------', screenSurf, ANCHO_PNT / 2 -10, 170, COLOR_GRIS, COLOR_NEGRO, pos='center')
    drawText('V = View Intro', screenSurf, ANCHO_PNT / 2 -10, 200, COLOR_GRIS, COLOR_NEGRO, pos='center')
    drawText('P = Play Game', screenSurf, ANCHO_PNT / 2 -10, 230, COLOR_GRIS, COLOR_NEGRO, pos='center')
    drawText('Your Choice?', screenSurf, ANCHO_PNT / 2 -10, 260, COLOR_GRIS, COLOR_NEGRO, pos='center')
    pygame.display.update()

    key = waitForPlayerToPressKey()
    while chr(key) != 'v' and chr(key) != 'p':
        key = waitForPlayerToPressKey()

    return p1name, p2name, points, gravity, chr(key) # returns 'v' or 'p'

def showIntroScreen(screenSurf, p1name, p2name):
    """This is the screen that plays if the user selected "view intro" from the starting screen."""
    screenSurf.fill(COLOR_CIELO)
    drawText('P  y  t  h  o  n     G  O  R  I  L  L  A  S', screenSurf, ANCHO_PNT / 2, 15, COLOR_BLANCO, COLOR_CIELO, pos='center')
    drawText('STARRING:', screenSurf, ANCHO_PNT / 2, 55, COLOR_BLANCO, COLOR_CIELO, pos='center')
    drawText('%s AND %s' % (p1name, p2name), screenSurf, ANCHO_PNT / 2, 115, COLOR_BLANCO, COLOR_CIELO, pos='center')

    x = 278
    y = 175

    for i in range(2):
        drawGorilla(screenSurf, x-13, y, BRAZO_DERECHO_ARRIBA)
        drawGorilla(screenSurf, x+47, y, BRAZO_IZQUIERDO_ARRIBA)
        pygame.display.update()

        time.sleep(2)

        drawGorilla(screenSurf, x-13, y, BRAZO_IZQUIERDO_ARRIBA)
        drawGorilla(screenSurf, x+47, y, BRAZO_DERECHO_ARRIBA)
        pygame.display.update()

        time.sleep(2)

    for i in range(4):
        drawGorilla(screenSurf, x-13, y, BRAZO_IZQUIERDO_ARRIBA)
        drawGorilla(screenSurf, x+47, y, BRAZO_DERECHO_ARRIBA)
        pygame.display.update()

        time.sleep(0.3)

        drawGorilla(screenSurf, x-13, y, BRAZO_DERECHO_ARRIBA)
        drawGorilla(screenSurf, x+47, y, BRAZO_IZQUIERDO_ARRIBA)
        pygame.display.update()

        time.sleep(0.3)


def getShot(screenSurf, p1name, p2name, playerNum):
    """getShot() is called when we want to get the angle and velocity from the player."""
    pygame.draw.rect(screenSurf, COLOR_CIELO, (0, 0, 200, 50))
    pygame.draw.rect(screenSurf, COLOR_CIELO, (550, 0, 00, 50))

    drawText(p1name, screenSurf, 2, 2, COLOR_BLANCO, COLOR_CIELO)
    drawText(p2name, screenSurf, 538, 2, COLOR_BLANCO, COLOR_CIELO)

    if playerNum == 1:
        x = 2
    else:
        x = 538

    angle = ''
    while angle == '':
        angle = inputMode('Angle:  ', screenSurf, x, 18, COLOR_BLANCO, COLOR_CIELO, maxlen=3, allowed='0123456789')
    if angle is None: terminate()
    angle = int(angle)

    velocity = ''
    while velocity == '':
        velocity = inputMode('Velocity:  ', screenSurf, x, 34, COLOR_BLANCO, COLOR_CIELO, maxlen=3, allowed='0123456789')
    if velocity is None: terminate()
    velocity = int(velocity)

    # Erase the user's input
    drawText('Angle:   ' + str(angle), screenSurf, x, 2, COLOR_CIELO, COLOR_CIELO)
    drawText('Velocity:   ' + str(angle), screenSurf, x, 2, COLOR_CIELO, COLOR_CIELO)
    pygame.display.update()

    if playerNum == 2:
        angle = 180 - angle

    return (angle, velocity)

def displayScore(screenSurf, oneScore, twoScore):
    """Draws the score on the screenSurf surface."""
    drawText(str(oneScore) + '>Score<' + str(twoScore), screenSurf, 270, 310, COLOR_BLANCO, COLOR_CIELO, pos='left')

def plotShot(screenSurf, skylineSurf, angle, velocity, playerNum, wind, gravity, gor1, gor2):
    # startx and starty is the upper left corner of the gorilla.
    angle = angle / 180.0 * math.pi
    initXVel = math.cos(angle) * velocity
    initYVel = math.sin(angle) * velocity
    gorWidth, gorHeight = GOR_DOWN_SURF.get_size()
    gor1rect = pygame.Rect(gor1[0], gor1[1], gorWidth, gorHeight)
    gor2rect = pygame.Rect(gor2[0], gor2[1], gorWidth, gorHeight)


    if playerNum == 1:
        gorImg = BRAZO_IZQUIERDO_ARRIBA
    else:
        gorImg = BRAZO_DERECHO_ARRIBA
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
    drawGorilla(screenSurf, startx, starty, AMBOS_BRAZOS_ABAJO)
    pygame.display.update()
    """Draw the gorilla throwing the banana."""

    bananaShape = ARRIBA

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

        if x >= ANCHO_PNT - 10 or x <= 3 or y >= ALTURA_PNT:
            bananaInPlay = False

        bananaRect = getBananaRect(x, y, bananaShape)
        if bananaShape == ARRIBA:
            bananaSurf = BAN_UP_SURF
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == ABAJO:
            bananaSurf = BAN_DOWN_SURF
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == IZQUIERDA:
            bananaSurf = BAN_LEFT_SURF
        elif bananaShape == DERECHA:
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
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(TAMAÑO_EXPLOSIÓN_GOR*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=TAMAÑO_EXPLOSIÓN_GOR, speed=0.005)
                drawSun(screenSurf)
                return 'gorilla1'
            elif bananaRect.colliderect(gor2rect):
                # banana has hit player 2
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(TAMAÑO_EXPLOSIÓN_GOR*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=TAMAÑO_EXPLOSIÓN_GOR, speed=0.005)
                screenSurf.fill(COLOR_CIELO, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'gorilla2'
            elif collideWithNonColor(srcPixArray, screenSurf, bananaRect, COLOR_CIELO):
                # banana has hit a building
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery)
                screenSurf.fill(COLOR_CIELO, bananaRect) # erase banana
                drawSun(screenSurf)
                return 'building'

        del srcPixArray
        """Pygame doesn't let us blit a surface while there is a pixel array of it existing, so we delete it."""

        screenSurf.blit(bananaSurf, (bananaRect.topleft))
        pygame.display.update()
        time.sleep(0.02)

        screenSurf.fill(COLOR_CIELO, bananaRect) # erase banana

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
    rightSide = min(rect.right, ANCHO_PNT)
    bottomSide = min(rect.bottom, ALTURA_PNT)

    for x in range(rect.left, rightSide):
        for y in range(rect.top, bottomSide):
            if surfObj.unmap_rgb(pixArr[x][y]) != color:
                return True
    return False


def getBananaRect(x, y, shape):
    if shape == ARRIBA:
        return pygame.Rect((x, y), BAN_UP_SURF.get_size())
    if shape == ABAJO:
        return pygame.Rect((x, y), BAN_DOWN_SURF.get_size())
    if shape == IZQUIERDA:
        return pygame.Rect((x, y), BAN_LEFT_SURF.get_size())
    if shape == DERECHA:
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
        pygame.draw.line(screenSurf, COLOR_EXPLOSIÓN, (int(ANCHO_PNT / 2), ALTURA_PNT - 5), (int(ANCHO_PNT / 2) + wind, ALTURA_PNT - 5))
        # draw the arrow end
        if wind > 0: arrowDir = -2
        else:        arrowDir = 2
        pygame.draw.line(screenSurf, COLOR_EXPLOSIÓN, (int(ANCHO_PNT / 2) + wind, ALTURA_PNT - 5), (int(ANCHO_PNT / 2) + wind + arrowDir, ALTURA_PNT - 5 - 2))
        pygame.draw.line(screenSurf, COLOR_EXPLOSIÓN, (int(ANCHO_PNT / 2) + wind, ALTURA_PNT - 5), (int(ANCHO_PNT / 2) + wind + arrowDir, ALTURA_PNT - 5 + 2))

def doExplosion(screenSurf, skylineSurf, x, y, explosionSize=TAMAÑO_EXPLOSIÓN_EDIF, speed=0.05):
    for r in range(1, explosionSize):
        pygame.draw.circle(screenSurf, COLOR_EXPLOSIÓN, (x, y), r)
        pygame.draw.circle(skylineSurf, COLOR_EXPLOSIÓN, (x, y), r)
        pygame.display.update()
        time.sleep(speed)
    for r in range(explosionSize, 1, -1):
        pygame.draw.circle(screenSurf, COLOR_CIELO, (x, y), explosionSize)
        pygame.draw.circle(skylineSurf, COLOR_CIELO, (x, y), explosionSize)
        pygame.draw.circle(screenSurf, COLOR_EXPLOSIÓN, (x, y), r)
        pygame.draw.circle(skylineSurf, COLOR_EXPLOSIÓN, (x, y), r)
        pygame.display.update()
        time.sleep(speed)
    pygame.draw.circle(screenSurf, COLOR_CIELO, (x, y), 2)
    pygame.draw.circle(skylineSurf, COLOR_CIELO, (x, y), 2)
    pygame.display.update()


def main():
    winSurface = pygame.display.set_mode((ANCHO_PNT, ALTURA_PNT), 0, 32)
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

