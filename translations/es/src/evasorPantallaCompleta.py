import pygame, random, sys
from pygame.locals import *

ANCHOVENTANA = 600
ALTOVENTANA = 600
COLORVENTANA = (255, 255, 255)
COLORFONDO = (0, 0, 0)
FPS = 40
TAMAÑOMINVILLANO = 10
TAMAÑOMAXVILLANO = 40
VELOCIDADMINVILLANO = 1
VELOCIDADMAXVILLANO = 8
TASANUEVOVILLANO = 6
TASAMOVIMIENTOJUGADOR = 5

def terminar():
    pygame.quit()
    sys.exit()

def esperarTeclaJugador():
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE: # Quita al presionar ESCAPE
                    terminar()
                return

def jugadorGolpeaVillano(rectanguloJugador, villanos):
    for v in villanos:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False

def dibujarTexto(texto, font, superficie, x, y):
    objetotexto = font.render(texto, 1, COLORVENTANA)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)

# establece un pygame, la ventana y el cursor del ratón
pygame.init()
relojPrincipal = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), pygame.FULLSCREEN)
pygame.display.set_caption('Esquivador')
pygame.mouse.set_visible(False)

# establece los fonts
font = pygame.font.SysFont(None, 48)

# establece los sonidos
gameOverSound = pygame.mixer.Sound('juegoterminado.wav')
pygame.mixer.music.load('musicaDeFondo.mid')

# establece las imagenes
playerImage = pygame.image.load('jugador.png')
rectanguloJugador = playerImage.get_rect()
baddieImage = pygame.image.load('villano.png')

# Muestra la pantalla inicial
dibujarTexto('Evasor', font, superficieVentana, (ANCHOVENTANA / 3)+40, (ALTOVENTANA / 3))
dibujarTexto('Presione una tecla para comenzar.', font, superficieVentana, (ANCHOVENTANA / 3) - 180, (ALTOVENTANA / 3) + 50)
pygame.display.update()
esperarTeclaJugador()


puntajeMax = 0
while True:
    # establece el comienzo del juego
    villanos = []
    puntaje = 0
    rectanguloJugador.topleft = (ANCHOVENTANA / 2, ALTOVENTANA - 50)
    moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
    trucoReversa = trucoLento = False
    contadorAgregarVillano = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # el ciclo del juego se mantiene mientras se este jugando
        puntaje += 1 # incrementa el puntaje

        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()

            if evento.type == KEYDOWN:
                if evento.key == ord('z'):
                    trucoReversa = True
                if evento.key == ord('x'):
                    trucoLento = True
                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverDerecha = False
                    moverIzquierda = True
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverIzquierda = False
                    moverDerecha = True
                if evento.key == K_UP or evento.key == ord('w'):
                    moverAbajo = False
                    moverArriba = True
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverArriba = False
                    moverAbajo = True

            if evento.type == KEYUP:
                if evento.key == ord('z'):
                    trucoReversa = False
                    puntaje = 0
                if evento.key == ord('x'):
                    trucoLento = False
                    puntaje = 0
                if evento.key == K_ESCAPE:
                        terminar()

                if evento.key == K_LEFT or evento.key == ord('a'):
                    moverIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord('d'):
                    moverDerecha = False
                if evento.key == K_UP or evento.key == ord('w'):
                    moverArriba = False
                if evento.key == K_DOWN or evento.key == ord('s'):
                    moverAbajo = False

            if evento.type == MOUSEMOTION:
                # Si se mueve el ratón, este se mueve adonde el cursor esté.
                rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)

        # Añade villanos en la parte superior de la pantalla, de ser necesarios.
        if not trucoReversa and not trucoLento:
            contadorAgregarVillano += 1
        if contadorAgregarVillano == TASANUEVOVILLANO:
            contadorAgregarVillano = 0
            baddieSize = random.randint(TAMAÑOMINVILLANO, TAMAÑOMAXVILLANO)
            newBaddie = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(VELOCIDADMINVILLANO, VELOCIDADMAXVILLANO),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                        }

            villanos.append(newBaddie)

        # Mueve el jugador.
        if moverIzquierda and rectanguloJugador.left > 0:
            rectanguloJugador.move_ip(-1 * TASAMOVIMIENTOJUGADOR, 0)
        if moverDerecha and rectanguloJugador.right < ANCHOVENTANA:
            rectanguloJugador.move_ip(TASAMOVIMIENTOJUGADOR, 0)
        if moverArriba and rectanguloJugador.top > 0:
            rectanguloJugador.move_ip(0, -1 * TASAMOVIMIENTOJUGADOR)
        if moverAbajo and rectanguloJugador.bottom < ALTOVENTANA:
            rectanguloJugador.move_ip(0, TASAMOVIMIENTOJUGADOR)

        # Mueve el cursor del ratón hacia el jugador.
        pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)

        # Mueve los villanos hacia abajo.
        for b in villanos:
            if not trucoReversa and not trucoLento:
                b['rect'].move_ip(0, b['speed'])
            elif trucoReversa:
                b['rect'].move_ip(0, -5)
            elif trucoLento:
                b['rect'].move_ip(0, 1)

        # Elimina los villanos que han caido por debajo.
        for b in villanos[:]:
            if b['rect'].top > ALTOVENTANA:
                villanos.remove(b)

        # Dibuja el mundo del juego en la ventana.
        superficieVentana.fill(COLORFONDO)

        # Dibuja el puntaje y el puntaje máximo
        dibujarTexto('Puntaje: %s' % (puntaje), font, superficieVentana, 10, 0)
        dibujarTexto('Puntaje Máximo: %s' % (puntajeMax), font, superficieVentana, 10, 40)

        # Dibuja el rectángulo del jugador
        superficieVentana.blit(playerImage, rectanguloJugador)

        # Dibuja cada villano
        for b in villanos:
            superficieVentana.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Verifica si algún villano impactó en el jugador.
        if jugadorGolpeaVillano(rectanguloJugador, villanos):
            if puntaje > puntajeMax:
                puntajeMax = puntaje # Establece nuevo puntaje máximo
            break

        relojPrincipal.tick(FPS)

    # Frena el juego y muestra "Juego Terminado"
    pygame.mixer.music.stop()
    gameOverSound.play()

    dibujarTexto('Juego Terminado', font, superficieVentana, (ANCHOVENTANA / 3)-40, (ALTOVENTANA / 3))
    dibujarTexto('Presione una tecla para repetir.', font, superficieVentana, (ANCHOVENTANA / 3) - 150, (ALTOVENTANA / 3) + 50)
    pygame.display.update()
    esperarTeclaJugador()

    gameOverSound.stop()
