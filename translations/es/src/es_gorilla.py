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
DER = 0
ARRIBA = 1
IZQ = 2
ABAJO = 3
"""Algunas constantes para la dirección en que se orienta la banana (o cualquier otra cosa)."""

# tipos de brazos del gorila
AMBOS_BRAZOS_ABAJO = 0
BRAZO_IZQ_ARRIBA = 1
BRAZO_DER_ARRIBA = 2
"""Constantes para determinar cuál de los tres sprites del gorila usar: ambos brazos abajo, brazo izquierdo arriba, o brazo derecho arriba."""


"""Las siguientes cadenas multilínea son usadas con la función crearSuperficieDesdeASCII(). Es básicamente una forma de
generar superficies aparte de usar las funciones de dibujo o incluir archivos gráficos con este archivo .py.

Intenta experimentar cambiando las cadenas. La primera y última línea son ignoradas (de modo que no tengas que lidiar con
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

GOR_IZQ_ASCII = """
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

GOR_DER_ASCII = """
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

BAN_DER_ASCII = """
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

BAN_IZQ_ASCII = """
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

def terminar():
    """Llama a las funciones pygame.quit() y sys.exit(), para terminar el programa. (He descubierto que no llamar a
    pygame.quit() antes de sys.exit() ocasiona problemas con IDLE algunas veces."""
    pygame.quit()
    sys.exit()

def crearSuperficieDesdeASCII(ascii, colFig=(255,255,255), colFon=(0,0,0)):
    """Devuelve un nuevo objeto pygame.Surface que tiene la imágen especificada por el parámetro ascii dibujada sobre él.
    La primera y última líneas ascii son ignoradas. por lo demás, cualquier X en ascii indica un píxel con el color de primer plano
    y cualquier otra letra indica un píxel del color del fondo. El objeto Surface tiene el ancho de la línea más larga
    en la cadena ascii, y es siempre rectangular."""

    """Intenta experimentar con esta función para poder especificar más que dos colores. (Pasa un dict de
    letras ascii y tuplas RGB, por ejemplo."""
    ascii = ascii.split('\n')[1:-1]
    ancho = max([len(x) for x in ascii])
    altura = len(ascii)
    sup = pygame.Surface((ancho, altura))
    sup.fill(colFon)

    pArr = pygame.PixelArray(sup)
    for y in range(altura):
        for x in range(len(ascii[y])):
            if ascii[y][x] == 'X':
                pArr[x][y] = colFig
    return sup

GOR_ABAJO_SUP       = crearSuperficieDesdeASCII(GOR_ABAJO_ASCII,       COLOR_GOR,         COLOR_CIELO)
GOR_IZQ_SUP         = crearSuperficieDesdeASCII(GOR_IZQ_ASCII,         COLOR_GOR,         COLOR_CIELO)
GOR_DER_SUP         = crearSuperficieDesdeASCII(GOR_DER_ASCII,         COLOR_GOR,         COLOR_CIELO)
BAN_DER_SUP         = crearSuperficieDesdeASCII(BAN_DER_ASCII,         COLOR_BAN,         COLOR_CIELO)
BAN_IZQ_SUP         = crearSuperficieDesdeASCII(BAN_IZQ_ASCII,         COLOR_BAN,         COLOR_CIELO)
BAN_ARRIBA_SUP      = crearSuperficieDesdeASCII(BAN_ARRIBA_ASCII,      COLOR_BAN,         COLOR_CIELO)
BAN_ABAJO_SUP       = crearSuperficieDesdeASCII(BAN_ABAJO_ASCII,       COLOR_BAN,         COLOR_CIELO)
SOL_NORMAL_SUP      = crearSuperficieDesdeASCII(SOL_NORMAL_ASCII,      COLOR_SOL,         COLOR_CIELO)
SOL_SORPRENDIDO_SUP = crearSuperficieDesdeASCII(SOL_SORPRENDIDO_ASCII, COLOR_SOL,         COLOR_CIELO)
ESTRELLA_SUP        = crearSuperficieDesdeASCII(ESTRELLA_ASCII,        COLOR_ROJO_OSCURO, COLOR_NEGRO)

assert GOR_ABAJO_SUP.get_size() == GOR_IZQ_SUP.get_size() == GOR_DER_SUP.get_size()
"""Crea los objetos pygame.Surface de las cadenas ASCII."""

solRect = pygame.Rect(SOL_X, SOL_Y, SOL_NORMAL_SUP.get_width(), SOL_NORMAL_SUP.get_height())
"""solRect será un valor global de modo que siempre sabremos dónde está el sol."""

def dibujarTexto(texto, supObj, x, y, coltex, colfon, pos='izq'):
    """Una función genérica para dibujar una cadena sobre un objeto pygame.Surface en una cierta ubicación x,y. Esto devuelve
    un objeto pygame.Rect que describe el área sobre la cual se dibujó la cadena.

    Si el parámetro pos es "izq", el parámetro x,y especifica la esquina superior izquierda del rectángulo de texto.
    Si el parámetro pos es "centro", el parámetro x,y especifica el punto medio superior del rectángulo de texto."""

    texobj = FUENTE_JUEGO.render(texto, 1, coltex, colfon) # crea el texto en memoria (todavía no está sobre una superficie).
    texrect = texobj.get_rect()

    if pos == 'izq':
        texrect.topleft = (x, y)
    elif pos == 'centro':
        texrect.midtop = (x, y)
    supObj.blit(texobj, texrect) # dibuja el texto sobre la superficie
    """Recuerda que el texto sólo aparecerá en la pantalla si pasas el objeto pygame.Surface que fue
    devuelto de la llamada a pygame.display.set_mode(), y sólo después de haber llamado a pygame.display.update()."""
    return texrect

def obtenerCapitalizaciónMod(s, mod):
    """Comprueba el estado de las teclas Shift y Bloq Mayús, y si es necesario cambia la capitalización de la cadena s."""
    if bool(mod & KMOD_RSHIFT or mod & KMOD_LSHIFT) ^ bool(mod & KMOD_CAPS):
        return s.swapcase()
    else:
        return s

def modoEntrada(prompt, supPant, x, y, coltex, colfon, longmax=12, permitidos=None, pos='izq', cursor='_', destelloCursor=False):
    """Toma control del programa cuando es llamada. Esta función muestra una línea de comandos (el parámetro "prompt") en la pantalla
    sobre la superficie supPant en las coordenadas x, y. El texto se muestra en color coltex con un fondo de color colfon.
    Opcionalmente puedes especificar longmax para la máxima longitud en la respuesta del usuario. "permitidos" es una cadena
    de caracteres permitidos (por ejemplo si el jugador sólo puede ingresar números) y se ignoran todas las otras teclas. El parámetro "pos"
    puede ser la cadena "izq" (donde las coordenadas x, y refieren a la esquina superior izquierda del cuadro de texto)
    o "centro" (donde las coordenadas x, y refiere al punto medio superior del cuadro de texto).

    "cursor" es un caracter opcional que se usa para mostrar un cursor donde la próxima letra aparecerá. Si "destelloCursor"
    es True, este caracter se mostrará y ocultará en forma intermitente.

    El valor devuelto es una cadena con lo que el jugador ha tipeado, o None si el jugador presionó la tecla Esc.

    El jugador sólo puede presionar Retroceso para borrar caracteres, no pueden usarse las flechas del teclado para mover el
    cursor."""
    textoIngresado = ''
    """textoIngresado almacena el texto que el jugador ha entrado hasta el momento."""
    hecho = False
    tiempoCursor = time.time()
    mostrarCursor = cursor
    while not hecho:
        """Se seguirá iterando hasta que el jugador haya presionado las teclas Esc o Intro."""

        if cursor and destelloCursor and time.time() - 1.0 > tiempoCursor:
            if mostrarCursor == cursor:
                mostrarCursor = '   '
            else:
                mostrarCursor = cursor
            tiempoCursor = time.time()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()
            elif evento.type == KEYUP:
                if evento.key == K_ESCAPE:
                    return None
                elif evento.key == K_RETURN:
                    hecho = True
                    if mostrarCursor:
                        mostrarCursor = '   '
                elif evento.key == K_BACKSPACE:
                    if len(textoIngresado):
                        dibujarTexto(prompt + textoIngresado + mostrarCursor, supPant, texrect.left, texrect.top, colfon, colfon, 'izq')
                        textoIngresado = textoIngresado[:-1]
                else:
                    if len(textoIngresado) >= longmax or (permitidos is not None and chr(evento.key) not in permitidos):
                        continue
                    if evento.key >= 32 and evento.key < 128:
                        textoIngresado += obtenerCapitalizaciónMod(chr(evento.key), evento.mod)

        texrect = dibujarTexto(prompt + mostrarCursor, supPant, x, y, coltex, colfon, pos)
        dibujarTexto(prompt + textoIngresado + mostrarCursor, supPant, texrect.left, texrect.top, coltex, colfon, 'izq')
        pygame.display.update()
        RELOJ_JUEGO.tick(FPS)
    return textoIngresado

def siguienteFormaBanana(orient):
    """Devuelve la próxima forma de banana en la secuencia 0, 1, 2, 3, y 0 de nuevo. (Estas corresponden a las variables
    DER, ARRIBA, IZQ, y ABAJO."""
    if orient + 1 == 4:
        return 0
    else:
        return orient + 1

def dibujarBanana(supPant, orient, x, y):
    """Dibuja la forma de banana sobre la superficie supPant con su esquina superior izquierda en la coordenada x y proporcionada.
    "orient" toma como valor alguno de los siguientes: DER, ARRIBA, IZQ, or ABAJO (que son los enteros de 0 a 3 respectivamente)"""
    if orient == ABAJO:
        supPant.blit(BAN_ABAJO_SUP, (x, y))
    elif orient == ARRIBA:
        supPant.blit(BAN_ARRIBA_SUP, (x, y))
    elif orient == IZQ:
        supPant.blit(BAN_IZQ_SUP, (x, y))
    elif orient == DER:
        supPant.blit(BAN_DER_SUP, (x, y))


def dibujarSol(supPant, sorprendido=False):
    """Dibuja el sprite sol sobre la superficie supPant. Si sorprendido es True, usa la versión sorprendida del sol,
    de lo contrario usa la versión normal.Esta función no llama a python.display.update()"""
    if sorprendido:
        supPant.blit(SOL_SORPRENDIDO_SUP, (SOL_X, SOL_Y))
    else:
        supPant.blit(SOL_NORMAL_SUP, (SOL_X, SOL_Y))


def drawGorilla(supPant, x, y, brazos=AMBOS_BRAZOS_ABAJO):
    """Dibuja el sprite gorila sobre la superficie supPant en una coordenada específica x, y. La coordenada x,y
    es para la esquina superior izquierda del sprite gorila. Notar que las tres superficies gorila son del mismo tamaño."""

    if brazos == AMBOS_BRAZOS_ABAJO:
        gorSurf = GOR_ABAJO_SUP
    elif brazos == BRAZO_IZQ_ARRIBA:
        gorSurf = GOR_IZQ_SUP
    elif brazos == BRAZO_DER_ARRIBA:
        gorSurf = GOR_DER_SUP
    """Arriba elegimos qué objeto superficie usaremos para dibujar al gorila, dependiendo del parámetro "brazos".
    La llamada a supPant.blit() dibujará la superficie sobre la pantalla (pero no se mostrará en pantalla hasta que
    pygame.display.update() sea llamada."""

    supPant.blit(gorSurf, (x, y))

def crearPaisajeUrbano():
    """Esta función crea y devuelve un nuevo paisaje urbano con varios edificios sobre un objeto pygame.Surface y devuelve
    este objeto superficie."""

    supPant = pygame.Surface((ANCHO_PNT, ALTURA_PNT)) # primero crea la nueva superficie del mismo tamaño que la pantalla.
    supPant.fill(COLOR_CIELO) # rellena la superficie con el color de fondo del cielo

    """Elegiremos una curva ascendente, descendente, en forma de "v", o montañosa "^" para la inclinación de los edificios.
    La mitad del tiempo elegiremos la curva en forma de "v", mientras que las 3 formas restantes tendrán cada una probabilidad 1/6
    de ser elegidas. La inclinación también determina la altura del primer edificio, que es almacenada en nuevaAltura."""
    inclinación = random.randint(1, 6)
    if inclinación == 1:
        inclinación = 'ascendente'
        nuevaAltura = 15
    elif inclinación == 2:
        inclinación = 'descendente'
        nuevaAltura = 130
    elif inclinación >= 3 and inclinación <= 5:
        inclinación = 'v'
        nuevaAltura = 15
    else:
        inclinación = '^'
        nuevaAltura = 130

    líneaInferior = 335 # la línea inferior de los edificios. Queremos un poco de espacio para ubicar la flecha de viento
    incAltura = 10 # una referencia de cuánto crecen o se reducen los edificios en comparación con el último
    anchoEdifDef = 37 # anchura de los edificios por defecto, tambien juzga qué tan anchos pueden ser los edificios
    difAlturaAleat = 120 # aproximadamente cuánto pueden crecer o reducirse los edificios
    anchoVentana = 4 # el ancho de cada ventana en píxeles
    alturaVentana = 7 # la altura de cada ventana en píxeles
    separaciónVentanaX = 10 # a qué distancia en píxeles se encuentra el borde izquierdo de cada ventana
    separaciónVentanaY = 15 # a qué distancia en píxeles se encuentra el borde superior de cada ventana
    gAltura = 25 # (No estoy seguro de qué se supone que es esto en el código original Qbasic, pero igual lo he copiado)
    # (También había una variable alturaMax en el Qbasic original, pero no creo que hiciera nada, así que la he omitido)

    coordsEdificio = [] # una lista de las coordenadas (arriba, izquierda) de cada edificio, de izquierda a derecha

    x = 2 # x referencia la esquina superior izquierda del edificio que está siendo dibujado

    while x < ANCHO_PNT - incAltura:
        # En este bucle continuamos dibujando nuevos edificios hasta que se acaba el espacio en la pantalla.

        # Primero el tipo de inclinación determina si el edificio debería crecer o encogerse.
        if inclinación == 'ascendente':
            nuevaAltura += incAltura
        elif inclinación == 'descendente':
            nuevaAltura -= incAltura
        elif inclinación == 'v':
            if x > ANCHO_PNT / 2:
                nuevaAltura -= (2 * incAltura)
                # Para curvas en forma de "v", los edificios se encogen en la mitad izquierda de la pantalla...
            else:
                nuevaAltura += (2 * incAltura)
                # ...y crecen en la mitad derecha.
        else:
            if x > ANCHO_PNT / 2:
                nuevaAltura += (2 * incAltura)
                # Para curvas "montañosas", los edificios crecen en la mitad izquierda de la pantalla...
            else:
                nuevaAltura -= (2 * incAltura)
                # ...y se encogen en la mitad derecha.

        # Obtener el ancho del nuevo edificio.
        anchoEdif = anchoEdifDef + random.randint(0, anchoEdifDef)
        if anchoEdif + x > ANCHO_PNT:
            anchoEdif = ANCHO_PNT - x -2

        # Obtener la altura del nuevo edificio
        alturaEdif = random.randint(incAltura, difAlturaAleat) + nuevaAltura

        # Comprobar si la altura es excesiva.
        if líneaInferior - alturaEdif <= gAltura:
            alturaEdif = gAltura

        # Seleccionar en forma aleatoria uno de los colores de la lista para el edificio.
        colorEdificio = COLORES_EDIFICIO[random.randint(0, len(COLORES_EDIFICIO)-1)]

        # Dibujar el edificio
        pygame.draw.rect(supPant, colorEdificio, (x+1, líneaInferior - (alturaEdif+1), anchoEdif-1, alturaEdif-1))

        coordsEdificio.append( (x, líneaInferior - alturaEdif) )

        # Dibujar las ventanas
        for venx in range(3, anchoEdif - separaciónVentanaX + anchoVentana, separaciónVentanaX):
            for veny in range(3, alturaEdif - separaciónVentanaY, separaciónVentanaY):
                if random.randint(1, 4) == 1:
                    colorVen = VENTANA_OSCURA
                else:
                    colorVen = VENTANA_CLARA
                pygame.draw.rect(supPant, colorVen, (x + 1 + venx, (líneaInferior - alturaEdif) + 1 + veny, anchoVentana, alturaVentana))

        x += anchoEdif

    # Queremos devolver el objeto surface sobre el que hemos dibujado los edificios, y también las coordenadas de cada edificio.
    return supPant, coordsEdificio

def ubicarGorilas(coordsEdif):
    """Usando el valor de coordsEdif devuelto por crearPaisajeUrbano(), queremos ubicar los gorilas a los lados
    izquierdo y derecho de la pantalla sobre el segundo y el tercer edificio desde el borde."""

    posGor = [] # el ítem 0 es para (izq, arriba) del jugador uno, el ítem 1 es para el jugador dos.
    xAj = int(GOR_ABAJO_SUP.get_rect().width / 2)
    yAj = GOR_ABAJO_SUP.get_rect().height

    for i in range(0,2): # ubicar al primer jugador y luego al segundo

        # ubicar a los gorilas en el segundo y tercer edificio desde el borde.
        if i == 0:
            númEdif = random.randint(1,2)
        else:
            númEdif = random.randint(len(coordsEdif)-3, len(coordsEdif)-2)

        anchoEdif = coordsEdif[númEdif + 1][0] - coordsEdif[númEdif][0]
        posGor.append( (coordsEdif[númEdif][0] + int(anchoEdif / 2) - xAj, coordsEdif[númEdif][1] - yAj - 1) )

    # El formato de la lista posGor es [(j1 x, j1 y), (j2 x, j2 y)]
    return posGor

def esperarEntradaDelTeclado():
    """Llamar a esta función pondrá el programa en pausa hasta que el usuario presione una tecla. Se devuelve la tecla."""
    while True:
        tecla = comprobarTeclaPulsada()
        if tecla:
            return tecla

def comprobarTeclaPulsada():
    """Llamar a esta función comprobará si se ha pulsado una tecla recientemente. Si es así, se devuelve esa tecla.
    Si no, se devuelve False. Si la tecla Esc fue presionada, el programa termina."""
    for evento in pygame.event.get():
        if evento.type == QUIT:
            terminar()
        if evento.type == KEYUP:
            if evento.key == K_ESCAPE: # presionando Esc se sale del programa
                terminar()
            return evento.key
    return False

def mostrarPantallaInicio(supPant):
    """Dibuja la pantalla inicial introductoria sobre supPant, con estrellas rojas rotando alrededor del borde. Esta pantalla
    permanece hasta que el usuario presione una tecla."""
    ajVert = 0
    ajHor = 0
    while not comprobarTeclaPulsada():
        supPant.fill(COLOR_NEGRO)

        dibujarEstrellas(supPant, ajVert, ajHor)
        ajVert += 1
        if ajVert == 4: ajVert = 0
        ajHor += 12
        if ajHor == 84: ajHor = 0
        """Las estrellas a los lados de la pantalla se mueven 1 píxel por cada iteración de este bucle y se reinician cada 4
        píxeles. Las estrellas en los bordes superior e inferior se mueven 12 píxels cada iteración y se reinician cada 84 píxeles."""

        dibujarTexto('P  y  t  h  o  n     G  O  R  I  L  A  S', supPant, ANCHO_PNT / 2, 50, COLOR_BLANCO, COLOR_NEGRO, pos='centro')
        dibujarTexto('Tu misión es golpear a tu oponente con la banana explosiva', supPant, ANCHO_PNT / 2, 110, COLOR_GRIS, COLOR_NEGRO, pos='centro')
        dibujarTexto('variando el ángulo y la potencia de tu tiro, tomando en', supPant, ANCHO_PNT / 2, 130, COLOR_GRIS, COLOR_NEGRO, pos='centro')
        dibujarTexto('cuenta la velocidad del viento, gravedad, y el perfil urbano.', supPant, ANCHO_PNT / 2, 150, COLOR_GRIS, COLOR_NEGRO, pos='centro')
        dibujarTexto('La velocidad del viento se indica por la flecha debajo', supPant, ANCHO_PNT / 2, 170, COLOR_GRIS, COLOR_NEGRO, pos='centro')
        dibujarTexto('del campo de juego, siendo su longitud proporcional a su fuerza.', supPant, ANCHO_PNT / 2, 190, COLOR_GRIS, COLOR_NEGRO, pos='centro')
        dibujarTexto('Pulsa cualquier tecla para continuar', supPant, ANCHO_PNT / 2, 300, COLOR_GRIS, COLOR_NEGRO, pos='centro')

        pygame.display.update()
        RELOJ_JUEGO.tick(FPS)

def mostrarPantallaJuegoTerminado(supPant, j1nombre, j1puntaje, j2nombre, j2puntaje):
    """Dibuja la pantalla de juego terminado sobre supPant, mostrando los nombres y puntajes de los jugadores. Esta pantalla también
    tiene estrellas rojas rotantes, y permanece hasta que el usuario pulse una tecla."""
    j1puntaje = str(j1puntaje)
    j2puntaje = str(j2puntaje)
    ajVert = 0
    ajHor = 0
    while not comprobarTeclaPulsada():
        supPant.fill(COLOR_NEGRO)

        dibujarEstrellas(supPant, ajVert, ajHor)
        ajVert += 1
        if ajVert == 4: ajVert = 0
        ajHor += 12
        if ajHor == 84: ajHor = 0
        """Las estrellas a los lados de la pantalla se mueven 1 píxel por cada iteración de este bucle y se reinician cada 4
        píxeles. Las estrellas en los bordes superior e inferior se mueven 12 píxels cada iteración y se reinician cada 84 píxeles."""

        dibujarTexto('¡JUEGO TERMINADO!', supPant, ANCHO_PNT / 2, 120, COLOR_GRIS, COLOR_NEGRO, pos='centro')
        dibujarTexto('Puntaje:', supPant, ANCHO_PNT / 2, 155, COLOR_GRIS, COLOR_NEGRO, pos='centro')
        dibujarTexto(j1nombre, supPant, 225, 170, COLOR_GRIS, COLOR_NEGRO)
        dibujarTexto(j1puntaje, supPant, 395, 170, COLOR_GRIS, COLOR_NEGRO)
        dibujarTexto(j2nombre, supPant, 225, 185, COLOR_GRIS, COLOR_NEGRO)
        dibujarTexto(j2puntaje, supPant, 395, 185, COLOR_GRIS, COLOR_NEGRO)
        dibujarTexto('Pulsa cualquier tecla para continuar', supPant, ANCHO_PNT / 2, 298, COLOR_GRIS, COLOR_NEGRO, pos='centro')

        pygame.display.update()
        RELOJ_JUEGO.tick(FPS)

def dibujarEstrellas(supPant, ajVert, ajHor):
    """Esta función dibuja las estrellas rojas sobre el borde de supPant."""
    for i in range(16):
        # dibujar fila superior de estrellas
        supPant.blit(ESTRELLA_SUP, (2 + (((3 - ajVert) + i * 4) * ESTRELLA_SUP.get_width()), 3))
        # dibujar fila inferior de estrellas
        supPant.blit(ESTRELLA_SUP, (2 + ((ajVert + i * 4) * ESTRELLA_SUP.get_width()), ALTURA_PNT - 7 - ESTRELLA_SUP.get_height()))

    for i in range(4):
        # dibuja la columna izquierda de estrellas moviéndose hacia abajo
        supPant.blit(ESTRELLA_SUP, (5, 6 + ESTRELLA_SUP.get_height() + (ajHor + i * 84)))
        # dibuja la columna derecha de estrellas moviéndose hacia arriba
        supPant.blit(ESTRELLA_SUP, (ANCHO_PNT - 5 - ESTRELLA_SUP.get_width(), (ALTURA_PNT - (6 + ESTRELLA_SUP.get_height() + (ajHor + i * 84)))))



def mostrarPantallaConfiguración(supPant):
    """Esta es la pantalla que permite al jugador ingresar su nombre y ajustes para el juego."""
    j1nombre = None
    j2nombre = None
    puntos = None
    gravedad = None

    supPant.fill(COLOR_NEGRO)

    while j1nombre is None:
        j1nombre = modoEntrada("Nombre del Jugador 1 (Defecto = 'Jugador 1'):  ", supPant, ANCHO_PNT / 2 - 146, 50, COLOR_GRIS, COLOR_NEGRO, longmax=10, pos='izq', destelloCursor=True)
    if j1nombre == '':
        j1nombre = 'Jugador 1'

    while j2nombre is None:
        j2nombre = modoEntrada("Nombre del Jugador 2 (Defecto = 'Jugador 2'):  ", supPant, ANCHO_PNT / 2 - 146, 80, COLOR_GRIS, COLOR_NEGRO, longmax=10, pos='izq', destelloCursor=True)
    if j2nombre == '':
        j2nombre = 'Jugador 2'

    while puntos is None:
        puntos = modoEntrada("¿Jugar a cuántos puntos en total (Defecto = 3)?  ", supPant, ANCHO_PNT / 2 - 155, 110, COLOR_GRIS, COLOR_NEGRO, longmax=6, permitidos='0123456789', pos='izq', destelloCursor=True)
    if puntos == '':
        puntos = 3
    else:
        puntos = int(puntos)

    while gravedad is None:
        gravedad = modoEntrada("¿Gravedad en Metros/Seg (Tierra = 9.8)?  ", supPant, ANCHO_PNT / 2 - 150, 140, COLOR_GRIS, COLOR_NEGRO, longmax=6, permitidos='0123456789.', pos='izq', destelloCursor=True)
    if gravedad == '':
        gravedad = 9.8
    else:
        gravedad = float(gravedad)

    dibujarTexto('--------------------', supPant, ANCHO_PNT / 2 -10, 170, COLOR_GRIS, COLOR_NEGRO, pos='centro')
    dibujarTexto('V = Ver Introducción', supPant, ANCHO_PNT / 2 -10, 200, COLOR_GRIS, COLOR_NEGRO, pos='centro')
    dibujarTexto('J = Jugar', supPant, ANCHO_PNT / 2 -10, 230, COLOR_GRIS, COLOR_NEGRO, pos='centro')
    dibujarTexto('¿Tu Elección?', supPant, ANCHO_PNT / 2 -10, 260, COLOR_GRIS, COLOR_NEGRO, pos='centro')
    pygame.display.update()

    key = esperarEntradaDelTeclado()
    while chr(key) != 'v' and chr(key) != 'j':
        key = esperarEntradaDelTeclado()

    return j1nombre, j2nombre, puntos, gravedad, chr(key) # devuelve 'v' o 'j'

def mostrarPantallaIntro(supPant, j1nombre, j2nombre):
    """Esta es la pantalla que se reproduce si el jugador eligió "ver introducción" de la pantalla de inicio."""
    supPant.fill(COLOR_CIELO)
    dibujarTexto('P  y  t  h  o  n     G  O  R  I  L  L  A  S', supPant, ANCHO_PNT / 2, 15, COLOR_BLANCO, COLOR_CIELO, pos='centro')
    dibujarTexto('STARRING:', supPant, ANCHO_PNT / 2, 55, COLOR_BLANCO, COLOR_CIELO, pos='centro')
    dibujarTexto('%s AND %s' % (j1nombre, j2nombre), supPant, ANCHO_PNT / 2, 115, COLOR_BLANCO, COLOR_CIELO, pos='centro')

    x = 278
    y = 175

    for i in range(2):
        drawGorilla(supPant, x-13, y, BRAZO_DER_ARRIBA)
        drawGorilla(supPant, x+47, y, BRAZO_IZQ_ARRIBA)
        pygame.display.update()

        time.sleep(2)

        drawGorilla(supPant, x-13, y, BRAZO_IZQ_ARRIBA)
        drawGorilla(supPant, x+47, y, BRAZO_DER_ARRIBA)
        pygame.display.update()

        time.sleep(2)

    for i in range(4):
        drawGorilla(supPant, x-13, y, BRAZO_IZQ_ARRIBA)
        drawGorilla(supPant, x+47, y, BRAZO_DER_ARRIBA)
        pygame.display.update()

        time.sleep(0.3)

        drawGorilla(supPant, x-13, y, BRAZO_DER_ARRIBA)
        drawGorilla(supPant, x+47, y, BRAZO_IZQ_ARRIBA)
        pygame.display.update()

        time.sleep(0.3)


def getShot(screenSurf, p1name, p2name, playerNum):
    """getShot() is called when we want to get the angle and velocity from the player."""
    pygame.draw.rect(screenSurf, COLOR_CIELO, (0, 0, 200, 50))
    pygame.draw.rect(screenSurf, COLOR_CIELO, (550, 0, 00, 50))

    dibujarTexto(p1name, screenSurf, 2, 2, COLOR_BLANCO, COLOR_CIELO)
    dibujarTexto(p2name, screenSurf, 538, 2, COLOR_BLANCO, COLOR_CIELO)

    if playerNum == 1:
        x = 2
    else:
        x = 538

    angle = ''
    while angle == '':
        angle = modoEntrada('Angle:  ', screenSurf, x, 18, COLOR_BLANCO, COLOR_CIELO, longmax=3, permitidos='0123456789')
    if angle is None: terminar()
    angle = int(angle)

    velocity = ''
    while velocity == '':
        velocity = modoEntrada('Velocity:  ', screenSurf, x, 34, COLOR_BLANCO, COLOR_CIELO, longmax=3, permitidos='0123456789')
    if velocity is None: terminar()
    velocity = int(velocity)

    # Erase the user's input
    dibujarTexto('Angle:   ' + str(angle), screenSurf, x, 2, COLOR_CIELO, COLOR_CIELO)
    dibujarTexto('Velocity:   ' + str(angle), screenSurf, x, 2, COLOR_CIELO, COLOR_CIELO)
    pygame.display.update()

    if playerNum == 2:
        angle = 180 - angle

    return (angle, velocity)

def displayScore(screenSurf, oneScore, twoScore):
    """Draws the score on the screenSurf surface."""
    dibujarTexto(str(oneScore) + '>Score<' + str(twoScore), screenSurf, 270, 310, COLOR_BLANCO, COLOR_CIELO, pos='izq')

def plotShot(screenSurf, skylineSurf, angle, velocity, playerNum, wind, gravity, gor1, gor2):
    # startx and starty is the upper left corner of the gorilla.
    angle = angle / 180.0 * math.pi
    initXVel = math.cos(angle) * velocity
    initYVel = math.sin(angle) * velocity
    gorWidth, gorHeight = GOR_ABAJO_SUP.get_size()
    gor1rect = pygame.Rect(gor1[0], gor1[1], gorWidth, gorHeight)
    gor2rect = pygame.Rect(gor2[0], gor2[1], gorWidth, gorHeight)


    if playerNum == 1:
        gorImg = BRAZO_IZQ_ARRIBA
    else:
        gorImg = BRAZO_DER_ARRIBA
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
        startx += GOR_ABAJO_SUP.get_size()[0]

    starty -= getBananaRect(0, 0, bananaShape).height + BAN_ARRIBA_SUP.get_size()[1]

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
            bananaSurf = BAN_ARRIBA_SUP
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == ABAJO:
            bananaSurf = BAN_ABAJO_SUP
            bananaRect.left -= 2
            bananaRect.top += 2
        elif bananaShape == IZQ:
            bananaSurf = BAN_IZQ_SUP
        elif bananaShape == DER:
            bananaSurf = BAN_DER_SUP

        bananaShape = siguienteFormaBanana(bananaShape)

        srcPixArray = pygame.PixelArray(skylineSurf)
        if bananaInPlay and y > 0:

            if solRect.collidepoint(x, y):
                # banana has hit the sun, so draw the "shocked" face.
                sunHit = True

            # draw the appropriate sun face
            dibujarSol(screenSurf, sorprendido=sunHit)

            if bananaRect.colliderect(gor1rect):
                # banana has hit player 1

                """Note that we draw the explosion on the screen (on screenSurf) and on the separate skyline surface (on skylineSurf).
                This is done so that bananas won't hit the sun or any text and accidentally think they've hit something. We also want
                the skylineSurf surface object to keep track of what chunks of the buildings are left."""
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(TAMAÑO_EXPLOSIÓN_GOR*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=TAMAÑO_EXPLOSIÓN_GOR, speed=0.005)
                dibujarSol(screenSurf)
                return 'gorilla1'
            elif bananaRect.colliderect(gor2rect):
                # banana has hit player 2
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=int(TAMAÑO_EXPLOSIÓN_GOR*2/3), speed=0.005)
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery, explosionSize=TAMAÑO_EXPLOSIÓN_GOR, speed=0.005)
                screenSurf.fill(COLOR_CIELO, bananaRect) # erase banana
                dibujarSol(screenSurf)
                return 'gorilla2'
            elif collideWithNonColor(srcPixArray, screenSurf, bananaRect, COLOR_CIELO):
                # banana has hit a building
                doExplosion(screenSurf, skylineSurf, bananaRect.centerx, bananaRect.centery)
                screenSurf.fill(COLOR_CIELO, bananaRect) # erase banana
                dibujarSol(screenSurf)
                return 'building'

        del srcPixArray
        """Pygame doesn't let us blit a surface while there is a pixel array of it existing, so we delete it."""

        screenSurf.blit(bananaSurf, (bananaRect.topleft))
        pygame.display.update()
        time.sleep(0.02)

        screenSurf.fill(COLOR_CIELO, bananaRect) # erase banana

        t += 0.1 # go forward in the plot.
    dibujarSol(screenSurf)
    return 'miss'

def victoryDance(screenSurf, x, y):
    """Given the x,y coordinates of the topleft corner of the gorilla sprite, this goes through
    the victory dance routine of the gorilla where they start waving their arms in the air."""
    for i in range(4):
        screenSurf.blit(GOR_IZQ_SUP, (x, y))
        pygame.display.update()
        time.sleep(0.3)
        screenSurf.blit(GOR_DER_SUP, (x, y))
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
        return pygame.Rect((x, y), BAN_ARRIBA_SUP.get_size())
    if shape == ABAJO:
        return pygame.Rect((x, y), BAN_ABAJO_SUP.get_size())
    if shape == IZQ:
        return pygame.Rect((x, y), BAN_IZQ_SUP.get_size())
    if shape == DER:
        return pygame.Rect((x, y), BAN_DER_SUP.get_size())

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

    mostrarPantallaInicio(winSurface)

    while True:
        # start a new game
        p1name, p2name, winPoints, gravity, nextScreen = mostrarPantallaConfiguración(winSurface)
        if nextScreen == 'v':
            mostrarPantallaIntro(winSurface, p1name, p2name)

        # Reset the score and make it the first player's turn.
        p1score = 0
        p2score = 0
        turn = 1

        newRound = True
        while p1score < winPoints and p2score < winPoints:
            if newRound:
                # At the start of a new round, make a new city scape, place the gorillas, and get the wind speed.
                skylineSurf, buildCoords = crearPaisajeUrbano() # Note that the city skyline goes on skylineSurf, not winSurface.
                gorPos = ubicarGorilas(buildCoords)
                wind = getWind()
                newRound = False

            # Do all the drawing.
            winSurface.blit(skylineSurf, (0,0))
            drawGorilla(winSurface, gorPos[0][0], gorPos[0][1], 0)
            drawGorilla(winSurface, gorPos[1][0], gorPos[1][1], 0)
            drawWind(winSurface, wind)
            dibujarSol(winSurface)
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

        mostrarPantallaJuegoTerminado(winSurface, p1name, p1score, p2name, p2score)

if __name__ == '__main__':
    main()

