import pygame, sys, random
from pygame.locals import *

# configurar pygame
pygame.init()
relojPrincipal = pygame.time.Clock()

# configurar la ventana
ANCHOVENTANA = 400
ALTURAVENTANA = 400
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTURAVENTANA), 0, 32)
pygame.display.set_caption('Entrada')

# configurar los colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

# configurar estructura de datos del jugador y la comida
contadorDeComida = 0
NUEVACOMIDA = 40
TAMAÑOCOMIDA = 20
jugador = pygame.Rect(300, 100, 50, 50)
comidas = []
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ALTURAVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

# configurar variables de movimiento
moverseIzquierda = False
moverseDerecha = False
moverseArriba = False
moverseAbajo = False

VELOCIDADMOVIMIENTO = 6


# ejecutar el bucle del juego
while True:
    # comprobar eventos
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
                jugador.top = random.randint(0, ALTURAVENTANA - jugador.height)
                jugador.left = random.randint(0, ANCHOVENTANA - jugador.width)

        if evento.type == MOUSEBUTTONUP:
            comidas.append(pygame.Rect(evento.pos[0], evento.pos[1], TAMAÑOCOMIDA, TAMAÑOCOMIDA))

    contadorDeComida += 1
    if contadorDeComida >= NUEVACOMIDA:
        # agregar nueva comida
        contadorDeComida = 0
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ALTURAVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

    # dibujar el fondo negro sobre la superficie
    superficieVentana.fill(NEGRO)

    # mover al jugador
    if moverseAbajo and jugador.bottom < ALTURAVENTANA:
        jugador.top += VELOCIDADMOVIMIENTO
    if moverseArriba and jugador.top > 0:
        jugador.top -= VELOCIDADMOVIMIENTO
    if moverseIzquierda and jugador.left > 0:
        jugador.left -= VELOCIDADMOVIMIENTO
    if moverseDerecha and jugador.right < ANCHOVENTANA:
        jugador.right += VELOCIDADMOVIMIENTO

    # dibujar al jugador sobre la superficie
    pygame.draw.rect(superficieVentana, BLANCO, jugador)

    # comprobar si el jugador ha intersectado alguno de los cuadrados de comida
    for comida in comidas[:]:
        if jugador.colliderect(comida):
            comidas.remove(comida)

    # dibujar la comida
    for i in range(len(comidas)):
        pygame.draw.rect(superficieVentana, VERDE, comidas[i])

    # dibujar la ventana sobre la pantalla
    pygame.display.update()
    relojPrincipal.tick(40)
