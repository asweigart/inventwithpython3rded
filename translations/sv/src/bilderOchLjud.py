import pygame, sys, time, random
from pygame.locals import *

# initiera pygame
pygame.init()
huvudklocka = pygame.time.Clock()

# initiera fönstret
FÖNSTERBREDD = 400
FÖNSTERHÖJD = 400
fönsteryta = pygame.display.set_mode((FÖNSTERBREDD, FÖNSTERHÖJD), 0, 32)
pygame.display.set_caption('Bilder och ljud')

# skapa färgkonstanter
SVART = (0, 0, 0)

# initiera blockets datastruktur
spelare = pygame.Rect(300, 100, 40, 40)
spelarbild = pygame.image.load('player.png')
skaladSpelarbild = pygame.transform.scale(spelarbild, (40, 40))
matbild = pygame.image.load('cherry.png')
matbitar = []
for i in range(20):
    matbitar.append(pygame.Rect(random.randint(0, FÖNSTERBREDD - 20), random.randint(0, FÖNSTERHÖJD - 20), 20, 20))

matbitsräknare = 0
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
                spelare.top = random.randint(0, FÖNSTERHÖJD - spelare.height)
                spelare.left = random.randint(0, FÖNSTERBREDD - spelare.width)
            if event.key == ord('m'):
                if musikSpelas:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musikSpelas = not musikSpelas

        if event.type == MOUSEBUTTONUP:
            matbitar.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    matbitsräknare += 1
    if matbitsräknare >= NY_MATBIT:
        # addera mera matbitar
        matbitsräknare = 0
        matbitar.append(pygame.Rect(random.randint(0, FÖNSTERBREDD - 20), random.randint(0, FÖNSTERHÖJD - 20), 20, 20))

    # rita svart bakgrund på ytan
    fönsteryta.fill(SVART)

    # flytta spelaren
    if flyttaNer and spelare.bottom < FÖNSTERHÖJD:
        spelare.top += HASTIGHET
    if flyttaUpp and spelare.top > 0:
        spelare.top -= HASTIGHET
    if flyttaVänster and spelare.left > 0:
        spelare.left -= HASTIGHET
    if flyttaHöger and spelare.right < FÖNSTERBREDD:
        spelare.right += HASTIGHET


    # rita blocket på ytan
    fönsteryta.blit(skaladSpelarbild, spelare)

    # kontrollera om blocket överlappar någon matbit.
    for matbit in matbitar[:]:
        if spelare.colliderect(matbit):
            matbitar.remove(matbit)
            spelare = pygame.Rect(spelare.left, spelare.top, spelare.width + 2, spelare.height + 2)
            skaladSpelarbild = pygame.transform.scale(spelarbild, (spelare.width, spelare.height))
            if musikSpelas:
                plockaUppLjud.play()

    # rita matbitarna
    for matbit in matbitar:
        fönsteryta.blit(matbild, matbit)

    # rita fönstret på skärmen
    pygame.display.update()
    huvudklocka.tick(40)
