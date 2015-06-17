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
                if evento.key == K_ESCAPE:  # Sale del juego al presionar ESCAPE
                    terminar()
                return

def jugadorGolpeaVillano(rectanguloJugador, villanos):
    for v in villanos:
        if rectanguloJugador.colliderect(v['rect']):
            return True
    return False

def dibujarTexto(texto, fuente, superficie, x, y):
    objetotexto = fuente.render(texto, 1, COLORVENTANA)
    rectangulotexto = objetotexto.get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)

# establece un pygame, la ventana y el cursor del ratón
pygame.init()
relojPrincipal = pygame.time.Clock()
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA))
pygame.display.set_caption('Esquivador')
pygame.mouse.set_visible(False)

# establece las fuentes
fuente = pygame.font.SysFont(None, 48)

# establece los sonidos
sonidoJuegoTerminado = pygame.mixer.Sound('juegoterminado.wav')
pygame.mixer.music.load('musicaDeFondo.mid')

# establece las imagenes
imagenJugador = pygame.image.load('jugador.png')
rectanguloJugador = imagenJugador.get_rect()
imagenVillano = pygame.image.load('villano.png')

# Muestra la pantalla inicial
dibujarTexto('Evasor', fuente, superficieVentana, (ANCHOVENTANA / 3)+40, (ALTOVENTANA / 3))
dibujarTexto('Presione una tecla para comenzar.', fuente, superficieVentana, (ANCHOVENTANA / 3) - 180, (ALTOVENTANA / 3) + 50)
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
                # Si se mueve el ratón, este se mueve al lugar donde esté el cursor.
                rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento.pos[1] - rectanguloJugador.centery)

        # Añade villanos en la parte superior de la pantalla, de ser necesarios.
        if not trucoReversa and not trucoLento:
            contadorAgregarVillano += 1
        if contadorAgregarVillano == TASANUEVOVILLANO:
            contadorAgregarVillano = 0
            tamañoVillano = random.randint(TAMAÑOMINVILLANO, TAMAÑOMAXVILLANO)
            nuevoVillano = {'rect': pygame.Rect(random.randint(0, ANCHOVENTANA-tamañoVillano), 0 - tamañoVillano, tamañoVillano, tamañoVillano),
                        'velocidad': random.randint(VELOCIDADMINVILLANO, VELOCIDADMAXVILLANO),
                        'superficie':pygame.transform.scale(imagenVillano, (tamañoVillano, tamañoVillano)),
                        }

            villanos.append(nuevoVillano)

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
        for v in villanos:
            if not trucoReversa and not trucoLento:
                v['rect'].move_ip(0, v['velocidad'])
            elif trucoReversa:
                v['rect'].move_ip(0, -5)
            elif trucoLento:
                v['rect'].move_ip(0, 1)

        # Elimina los villanos que han caido por debajo.
        for v in villanos[:]:
            if v['rect'].top > ALTOVENTANA:
                villanos.remove(v)

        # Dibuja el mundo del juego en la ventana.
        superficieVentana.fill(COLORFONDO)

        # Dibuja el puntaje y el puntaje máximo
        dibujarTexto('Puntaje: %s' % (puntaje), fuente, superficieVentana, 10, 0)
        dibujarTexto('Puntaje Máximo: %s' % (puntajeMax), fuente, superficieVentana, 10, 40)

        # Dibuja el rectángulo del jugador
        superficieVentana.blit(imagenJugador, rectanguloJugador)

        # Dibuja cada villano
        for v in villanos:
            superficieVentana.blit(v['superficie'], v['rect'])

        pygame.display.update()

        # Verifica si algún villano impactó en el jugador.
        if jugadorGolpeaVillano(rectanguloJugador, villanos):
            if puntaje > puntajeMax:
                puntajeMax = puntaje # Establece nuevo puntaje máximo
            break

        relojPrincipal.tick(FPS)

    # Detiene el juego y muestra "Juego Terminado"
    pygame.mixer.music.stop()
    sonidoJuegoTerminado.play()

    dibujarTexto('Juego Terminado', fuente, superficieVentana, (ANCHOVENTANA / 3)-40, (ALTOVENTANA / 3))
    dibujarTexto('Presione una tecla jugar de nuevo.', fuente, superficieVentana, (ANCHOVENTANA / 3) - 150, (ALTOVENTANA / 3) + 50)
    pygame.display.update()
    esperarTeclaJugador()

    sonidoJuegoTerminado.stop()
