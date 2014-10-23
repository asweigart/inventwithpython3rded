import pygame, sys, time, random
from pygame.locals import *

# initiera pygame
pygame.init()
huvudKlocka = pygame.time.Clock()

# initiera fönstret
FÖNSTER_BREDD = 400
FÖNSTER_HÖJD = 400
fönsterYta = pygame.display.set_mode((FÖNSTER_BREDD, FÖNSTER_HÖJD), 0, 32)
pygame.display.set_caption('Sprajtar och Ljud')

# skapa färgkonstanter
SVART = (0, 0, 0)

# initiera blockets datastruktur
spelare = pygame.Rect(300, 100, 40, 40)
spelarBild = pygame.image.load('player.png')
skaladSpelarBild = pygame.transform.scale(spelarBild, (40, 40))
matBild = pygame.image.load('cherry.png')
matbitar = []
for i in range(20):
    matbitar.append(pygame.Rect(random.randint(0, FÖNSTER_BREDD - 20), random.randint(0, FÖNSTER_HÖJD - 20), 20, 20))

matbitsRäknare = 0
NY_MATBIT = 40

# skapa tangenbordsvariabler
flyttaVänster = False
flyttaHöger = False
flyttaUpp = False
flyttaNer = False

HASTIGHET = 6

# Skapa musik
plockaUppLjud = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
musikSpelas = True

# kör spelslingan
while True:
    # kontrollera om händelsen QUIT inträffat
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
            if event.key == ord('m'):
                if musikSpelas:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musikSpelas = not musikSpelas

        if event.type == MOUSEBUTTONUP:
            matbitar.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    matbitsRäknare += 1
    if matbitsRäknare >= NY_MATBIT:
        # addera mera matbitar
        matbitsRäknare = 0
        matbitar.append(pygame.Rect(random.randint(0, FÖNSTER_BREDD - 20), random.randint(0, FÖNSTER_HÖJD - 20), 20, 20))

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


    # rita blocket på ytan
    fönsterYta.blit(skaladSpelarBild, spelare)

    # kontrollera om blocket överlappar någon matbit.
    for matbit in matbitar[:]:
        if spelare.colliderect(matbit):
            matbitar.remove(matbit)
            spelare = pygame.Rect(spelare.left, spelare.top, spelare.width + 2, spelare.height + 2)
            skaladSpelarBild = pygame.transform.scale(spelarBild, (spelare.width, spelare.height))
            if musikSpelas:
                plockaUppLjud.play()

    # rita matbitarna
    for matbit in matbitar:
        fönsterYta.blit(matBild, matbit)

    # rita fönstret på skärmen
    pygame.display.update()
    huvudKlocka.tick(40)
