import pygame, sys, random
from pygame.locals import *

# initiera pygame
pygame.init()
huvudKlocka = pygame.time.Clock()

# initiera fönstret
FÖNSTER_BREDD = 400
FÖNSTER_HÖJD = 400
fönsterYta = pygame.display.set_mode((FÖNSTER_BREDD, FÖNSTER_HÖJD), 0, 32)
pygame.display.set_caption('Inmatning')

# skapa färgkonstanter
SVART = (0, 0, 0)
GRÖN = (0, 255, 0)
VIT = (255, 255, 255)

# skapa spelaren och matbitarnas datastruktur
matbitsRäknare = 0
NY_MATBIT = 40
MATBIT_STORLEK = 20
spelare = pygame.Rect(300, 100, 50, 50)
matbitar = []
for i in range(20):
    matbitar.append(pygame.Rect(random.randint(0, FÖNSTER_BREDD - MATBIT_STORLEK), random.randint(0, FÖNSTER_HÖJD - MATBIT_STORLEK), MATBIT_STORLEK, MATBIT_STORLEK))

# skapa rörelsevariabler
flyttaVänster = False
flyttaHöger = False
flyttaUpp = False
flyttaNer = False

HASTIGHET = 6


# kör spelslingan
while True:
    # kontrollera händelser
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # uppdatera tangentbordsvariablerna
            if event.key == K_LEFT or event.key == ord('a'):
                flyttaHöger = False
                flyttaVänster = True
            if event.key == K_RIGHT or event.key == ord('d'):
                flyttaVänster = False
                flyttaHöger = True
            if event.key == K_UP or event.key == ord('w'):
                flyttaNer = False
                flyttaUpp = True
            if event.key == K_DOWN or event.key == ord('s'):
                flyttaUpp = False
                flyttaNer = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                flyttaVänster = False
            if event.key == K_RIGHT or event.key == ord('d'):
                flyttaHöger = False
            if event.key == K_UP or event.key == ord('w'):
                flyttaUpp = False
            if event.key == K_DOWN or event.key == ord('s'):
                flyttaNer = False
            if event.key == ord('x'):
                spelare.top = random.randint(0, FÖNSTER_HÖJD - spelare.height)
                spelare.left = random.randint(0, FÖNSTER_BREDD - spelare.width)

        if event.type == MOUSEBUTTONUP:
            matbitar.append(pygame.Rect(event.pos[0], event.pos[1], MATBIT_STORLEK, MATBIT_STORLEK))

    matbitsRäknare += 1
    if matbitsRäknare >= NY_MATBIT:
        # addera mera matbitar
        matbitsRäknare = 0
        matbitar.append(pygame.Rect(random.randint(0, FÖNSTER_BREDD - MATBIT_STORLEK), random.randint(0, FÖNSTER_HÖJD - MATBIT_STORLEK), MATBIT_STORLEK, MATBIT_STORLEK))

    # rita svart bakgrund på ytan
    fönsterYta.fill(SVART)

    # flytta spelaren
    if flyttaNer and spelare.bottom < FÖNSTER_HÖJD:
        spelare.top += HASTIGHET
    if flyttaUpp and spelare.top > 0:
        spelare.top -= HASTIGHET
    if flyttaVänster and spelare.left > 0:
        spelare.left -= HASTIGHET
    if flyttaHöger and spelare.right < FÖNSTER_BREDD:
        spelare.right += HASTIGHET

    # rita spelaren på ytan
    pygame.draw.rect(fönsterYta, VIT, spelare)

    # kontrollera om spelaren överlappar med någon matbit.
    for matbit in matbitar[:]:
        if spelare.colliderect(matbit):
            matbitar.remove(matbit)

    # rita matbitarna
    for i in range(len(matbitar)):
        pygame.draw.rect(fönsterYta, GRÖN, matbitar[i])

    # rita fönstret på skärmen
    pygame.display.update()
    huvudKlocka.tick(40)
