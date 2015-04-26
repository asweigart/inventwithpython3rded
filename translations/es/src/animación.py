import pygame, sys, time
from pygame.locals import *

# Establece pygame
pygame.init()

# Establece la ventana
ANCHOVENTANA = 400
ALTOVENTANA = 400
windowSurface = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.display.set_caption('Animación')

# Establece las variables de dirección
ABAJOIZQUIERDA = 1
ABAJODERECHA = 3
ARRIBAIZQUIERDA = 7
ARRIBADERECHA = 9

VELOCIDADMOVIMIENTO = 4

# Establece los colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Establece la estructura de datos de los bloques.
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':ROJO, 'dir':ARRIBADERECHA}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':VERDE, 'dir':ARRIBAIZQUIERDA}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':AZUL, 'dir':ABAJOIZQUIERDA}
bloques = [b1, b2, b3]

# Corre el ciclo de juego
while True:
    # Busca un evento QUIT.
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Dibuja el fondo negro sobre la superficie
    windowSurface.fill(NEGRO)

    for b in bloques:
        # mueve la estructura de datos de bloques
        if b['dir'] == ABAJOIZQUIERDA:
            b['rect'].left -= VELOCIDADMOVIMIENTO
            b['rect'].top += VELOCIDADMOVIMIENTO
        if b['dir'] == ABAJODERECHA:
            b['rect'].left += VELOCIDADMOVIMIENTO
            b['rect'].top += VELOCIDADMOVIMIENTO
        if b['dir'] == ARRIBAIZQUIERDA:
            b['rect'].left -= VELOCIDADMOVIMIENTO
            b['rect'].top -= VELOCIDADMOVIMIENTO
        if b['dir'] == ARRIBADERECHA:
            b['rect'].left += VELOCIDADMOVIMIENTO
            b['rect'].top -= VELOCIDADMOVIMIENTO

        # Verifica si el bloque se movió fuera de la ventana
        if b['rect'].top < 0:
            # el bloque se movió por arriba de la ventana
            if b['dir'] == ARRIBAIZQUIERDA:
                b['dir'] = ABAJOIZQUIERDA
            if b['dir'] == ARRIBADERECHA:
                b['dir'] = ABAJODERECHA
        if b['rect'].bottom > ALTOVENTANA:
            # el bloque se movió por debajo de la ventana
            if b['dir'] == ABAJOIZQUIERDA:
                b['dir'] = ARRIBAIZQUIERDA
            if b['dir'] == ABAJODERECHA:
                b['dir'] = ARRIBADERECHA
        if b['rect'].left < 0:
            # el bloque se movió por la izquierda de la ventana
            if b['dir'] == ABAJOIZQUIERDA:
                b['dir'] = ABAJODERECHA
            if b['dir'] == ARRIBAIZQUIERDA:
                b['dir'] = ARRIBADERECHA
        if b['rect'].right > ANCHOVENTANA:
            # el bloque se movió por la derecha de la ventana
            if b['dir'] == ABAJODERECHA:
                b['dir'] = ABAJOIZQUIERDA
            if b['dir'] == ARRIBADERECHA:
                b['dir'] = ARRIBAIZQUIERDA

        # Dibuja el bloque en la superficie
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    # Dibuja la ventana en la pantalla
    pygame.display.update()
    time.sleep(0.02)
