import pygame, sys, random
from pygame.locals import *

def verifSuperposiciónRects(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Verifica si las esquinas de a se encuentran dentro de b
        if ((puntoDentroDeRect(a.left, a.top, b)) or
            (puntoDentroDeRect(a.left, a.bottom, b)) or
            (puntoDentroDeRect(a.right, a.top, b)) or
            (puntoDentroDeRect(a.right, a.bottom, b))):
            return True

    return False

def puntoDentroDeRect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


# establece el juego
pygame.init()
relojPrincipal = pygame.time.Clock()

# establece la ventana
ANCHOVENTANA = 400
ALTOVENTANA = 400
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.display.set_caption('Deteccion de Colisiones')

# establece las variables de dirección
ABAJOIZQUIERDA = 1
ABAJODERECHA = 3
ARRIBAIZQUIERDA = 7
ARRIBADERECHA = 9

VELOCIDADMOVIMIENTO = 4

# establece los colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

# establece las estructuras de datos de comida y rebotín
contadorComida = 0
NUEVACOMIDA = 40
TAMAÑOCOMIDA = 20
rebotín = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':ARRIBAIZQUIERDA}
comidas = []
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ALTOVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

# corre el bucle de juego
while True:
    # busca un evento QUIT
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    contadorComida += 1
    if contadorComida >= NUEVACOMIDA:
        # añade nueva comida
        contadorComida = 0
        comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - TAMAÑOCOMIDA), random.randint(0, ALTOVENTANA - TAMAÑOCOMIDA), TAMAÑOCOMIDA, TAMAÑOCOMIDA))

    # Dibuja el fondo NEGRO sobre la superficie
    superficieVentana.fill(NEGRO)

    # Mueve la estructura de datos rebotín
    if rebotín['dir'] == ABAJOIZQUIERDA:
        rebotín['rect'].left -= VELOCIDADMOVIMIENTO
        rebotín['rect'].top += VELOCIDADMOVIMIENTO
    if rebotín['dir'] == ABAJODERECHA:
        rebotín['rect'].left += VELOCIDADMOVIMIENTO
        rebotín['rect'].top += VELOCIDADMOVIMIENTO
    if rebotín['dir'] == ARRIBAIZQUIERDA:
        rebotín['rect'].left -= VELOCIDADMOVIMIENTO
        rebotín['rect'].top -= VELOCIDADMOVIMIENTO
    if rebotín['dir'] == ARRIBADERECHA:
        rebotín['rect'].left += VELOCIDADMOVIMIENTO
        rebotín['rect'].top -= VELOCIDADMOVIMIENTO

    # Verifica si rebotín se movió fuera de la ventana
    if rebotín['rect'].top < 0:
        # rebotín se movió por arriba de la ventana
        if rebotín['dir'] == ARRIBAIZQUIERDA:
            rebotín['dir'] = ABAJOIZQUIERDA
        if rebotín['dir'] == ARRIBADERECHA:
            rebotín['dir'] = ABAJODERECHA
    if rebotín['rect'].bottom > ALTOVENTANA:
        # rebotín se movió por debajo de la ventana
        if rebotín['dir'] == ABAJOIZQUIERDA:
            rebotín['dir'] = ARRIBAIZQUIERDA
        if rebotín['dir'] == ABAJODERECHA:
            rebotín['dir'] = ARRIBADERECHA
    if rebotín['rect'].left < 0:
        # rebotín se movió por la izquierda de la ventana
        if rebotín['dir'] == ABAJOIZQUIERDA:
            rebotín['dir'] = ABAJODERECHA
        if rebotín['dir'] == ARRIBAIZQUIERDA:
            rebotín['dir'] = ARRIBADERECHA
    if rebotín['rect'].right > ANCHOVENTANA:
        # rebotín se movió por la derecha de la ventana
        if rebotín['dir'] == ABAJODERECHA:
            rebotín['dir'] = ABAJOIZQUIERDA
        if rebotín['dir'] == ARRIBADERECHA:
            rebotín['dir'] = ARRIBAIZQUIERDA

    # Dibuja a rebotín en la superficie
    pygame.draw.rect(superficieVentana, BLANCO, rebotín['rect'])

    # Verifica si rebotín intersectó algun cuadrado de comida
    for comida in comidas[:]:
        if verifSuperposiciónRects(rebotín['rect'], comida):
            comidas.remove(comida)

    # Dibuja la comida
    for i in range(len(comidas)):
        pygame.draw.rect(superficieVentana, VERDE, comidas[i])

    # Dibuja la ventana en la pantalla
    pygame.display.update()
    relojPrincipal.tick(40)
