import pygame, sys, time
from pygame.locals import *

# initiera pygame
pygame.init()

# initiera fönstret
FÖNSTER_BREDD = 400
FÖNSTER_HÖJD = 400
fönsterYta = pygame.display.set_mode((FÖNSTER_BREDD, FÖNSTER_HÖJD), 0, 32)
pygame.display.set_caption('Animering')

# skapa riktningskonstanter
NER_VÄNSTER = 1
NER_HÖGER = 3
UPP_VÄNSTER = 7
UPP_HÖGER = 9

HASTIGHET = 4

# skapa färgkonstanter
SVART = (0, 0, 0)
RÖD = (255, 0, 0)
GRÖN = (0, 255, 0)
BLÅ = (0, 0, 255)

# initiera blockets datastruktur
b1 = {'rektangel':pygame.Rect(300, 80, 50, 100), 'färg':RÖD, 'riktning':UPP_HÖGER}
b2 = {'rektangel':pygame.Rect(200, 200, 20, 20), 'färg':GRÖN, 'riktning':UPP_VÄNSTER}
b3 = {'rektangel':pygame.Rect(100, 150, 60, 60), 'färg':BLÅ, 'riktning':NER_VÄNSTER}
block = [b1, b2, b3]

# kör spelslingan
while True:
    # kontrollera om händelsen QUIT inträffat
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # rita svart bakgrund på ytan
    fönsterYta.fill(SVART)

    for b in block:
        # flytta blockets datastruktur
        if b['riktning'] == NER_VÄNSTER:
            b['rektangel'].left -= HASTIGHET
            b['rektangel'].top += HASTIGHET
        if b['riktning'] == NER_HÖGER:
            b['rektangel'].left += HASTIGHET
            b['rektangel'].top += HASTIGHET
        if b['riktning'] == UPP_VÄNSTER:
            b['rektangel'].left -= HASTIGHET
            b['rektangel'].top -= HASTIGHET
        if b['riktning'] == UPP_HÖGER:
            b['rektangel'].left += HASTIGHET
            b['rektangel'].top -= HASTIGHET

        # kontrollera om blocket har hamnat utanför fönstret
        if b['rektangel'].top < 0:
            # blocket har hamnat utanför ovansidan
            if b['riktning'] == UPP_VÄNSTER:
                b['riktning'] = NER_VÄNSTER
            if b['riktning'] == UPP_HÖGER:
                b['riktning'] = NER_HÖGER
        if b['rektangel'].bottom > FÖNSTER_HÖJD:
            # blocket har hamnat utanför undersidan
            if b['riktning'] == NER_VÄNSTER:
                b['riktning'] = UPP_VÄNSTER
            if b['riktning'] == NER_HÖGER:
                b['riktning'] = UPP_HÖGER
        if b['rektangel'].left < 0:
            # blocket har hamnat utanför vänster sida
            if b['riktning'] == NER_VÄNSTER:
                b['riktning'] = NER_HÖGER
            if b['riktning'] == UPP_VÄNSTER:
                b['riktning'] = UPP_HÖGER
        if b['rektangel'].right > FÖNSTER_BREDD:
            # blocket har hamnat utanför höger sida
            if b['riktning'] == NER_HÖGER:
                b['riktning'] = NER_VÄNSTER
            if b['riktning'] == UPP_HÖGER:
                b['riktning'] = UPP_VÄNSTER

        # rita blocket på ytan
        pygame.draw.rect(fönsterYta, b['färg'], b['rektangel'])

    # rita fönstret på skärmen
    pygame.display.update()
    time.sleep(0.02)
