import pygame, sys, time, random
from pygame.locals import *

# configurar pygame
pygame.init()
relojPrincipal = pygame.time.Clock()

# configurar la ventana
ANCHOVENTANA = 400
ALTOVENTANA = 400
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.display.set_caption('Sprites y Sonido')

# configurar los colores
NEGRO = (0, 0, 0)

# configurar la estructura de bloque de datos
jugador = pygame.Rect(300, 100, 40, 40)
imagenJugador = pygame.image.load('jugador.png')
imagenEstiradaJugador = pygame.transform.scale(imagenJugador, (40, 40))
imagenComida = pygame.image.load('cereza.png')
comidas = []
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20))

contadorComida = 0
NUEVACOMIDA = 40

# configurar variables del teclado
moverseIzquierda = False
moverseDerecha = False
moverseArriba = False
moverseAbajo = False

VELOCIDADMOVIMIENTO = 6

# configurar música
sonidoRecolección = pygame.mixer.Sound('recolección.wav')
pygame.mixer.music.load('músicaDeFondo.mid')
pygame.mixer.music.play(-1, 0.0)
músicaSonando = True

# ejecutar el bucle del juego
while True:
    # comprobar si se ha disparado el evento QUIT (salir)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN:
            # cambiar las variables del teclado
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseDerecha = False
                moverseIzquierda = True
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseIzquierda = False
                moverseDerecha = True
            if evento.key == K_UP or evento.key == ord('w'):
                moverseAbajo = False
                moverseArriba = True
            if evento.key == K_DOWN or evento.key == ord('s'):
                moverseArriba = False
                moverseAbajo = True
        if evento.type == KEYUP:
            if evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if evento.key == K_LEFT or evento.key == ord('a'):
                moverseIzquierda = False
            if evento.key == K_RIGHT or evento.key == ord('d'):
                moverseDerecha = False
            if evento.key == K_UP or evento.key == ord('w'):
                moverseArriba = False
            if evento.key == K_DOWN or evento.key == ord('s'):
                moverseAbajo = False
            if evento.key == ord('x'):
                jugador.top = random.randint(0, ALTOVENTANA - jugador.height)
                jugador.left = random.randint(0, ANCHOVENTANA - jugador.width)
            if evento.key == ord('m'):
                if músicaSonando:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                músicaSonando = not músicaSonando

        if evento.type == MOUSEBUTTONUP:
            comidas.append(pygame.Rect(evento.pos[0] - 10, evento.pos[1] - 10, 20, 20))

    contadorComida += 1
    if contadorComida >= NUEVACOMIDA:
        # agregar nueva comida
        contadorComida = 0
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20))

    # pintar el fondo negro sobre la superficie
    superficieVentana.fill(NEGRO)

    # mover el jugador
    if moverseAbajo and jugador.bottom < ALTOVENTANA:
        jugador.top += VELOCIDADMOVIMIENTO
    if moverseArriba and jugador.top > 0:
        jugador.top -= VELOCIDADMOVIMIENTO
    if moverseIzquierda and jugador.left > 0:
        jugador.left -= VELOCIDADMOVIMIENTO
    if moverseDerecha and jugador.right < ANCHOVENTANA:
        jugador.right += VELOCIDADMOVIMIENTO


    # dibujar el bloque sobre la superficie
    superficieVentana.blit(imagenEstiradaJugador, jugador)

    # comprobar si el jugador ha intersectado alguno de los cuadrados de comida
    for comida in comidas[:]:
        if jugador.colliderect(comida):
            comidas.remove(comida)
            jugador = pygame.Rect(jugador.left, jugador.top, jugador.width + 2, jugador.height + 2)
            imagenEstiradaJugador = pygame.transform.scale(imagenJugador, (jugador.width, jugador.height))
            if músicaSonando:
                sonidoRecolección.play()

    # dibujar la comida
    for comida in comidas:
        superficieVentana.blit(imagenComida, comida)

    # dibujar la ventana sobre la pantalla
    pygame.display.update()
    relojPrincipal.tick(40)
