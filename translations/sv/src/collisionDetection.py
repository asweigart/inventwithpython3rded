import pygame, sys, random
from pygame.locals import *

def överlapparRektanglar(rektangel1, rektangel2):
    for a, b in [(rektangel1, rektangel2), (rektangel2, rektangel1)]:
        # Kontrollera om a:s hörn är inuti b
        if ((ärPunktInutiRektangel(a.left, a.top, b)) or
            (ärPunktInutiRektangel(a.left, a.bottom, b)) or
            (ärPunktInutiRektangel(a.right, a.top, b)) or
            (ärPunktInutiRektangel(a.right, a.bottom, b))):
            return True

    return False

def ärPunktInutiRektangel(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


# initiera pygame
pygame.init()
huvudKlocka = pygame.time.Clock()

# initiera fönstret
FÖNSTER_BREDD = 400
FÖNSTER_HÖJD = 400
fönsterYta = pygame.display.set_mode((FÖNSTER_BREDD, FÖNSTER_HÖJD), 0, 32)
pygame.display.set_caption('Kollisionsdetektering')

# skapa riktningskonstanter
NER_VÄNSTER = 1
NER_HÖGER = 3
UPP_VÄNSTER = 7
UPP_HÖGER = 9

HASTIGHET = 4

# skapa färgkonstanter
SVART = (0, 0, 0)
GRÖN = (0, 255, 0)
VIT = (255, 255, 255)

# skapa studsbollen och matbitarnas datastruktur
matbitsRäknare = 0
NY_MATBIT = 40
MATBIT_STORLEK = 20
studsboll = {'rektangel':pygame.Rect(300, 100, 50, 50), 'riktning':UPP_VÄNSTER}
matbitar = []
for i in range(20):
    matbitar.append(pygame.Rect(random.randint(0, FÖNSTER_BREDD - MATBIT_STORLEK), random.randint(0, FÖNSTER_HÖJD - MATBIT_STORLEK), MATBIT_STORLEK, MATBIT_STORLEK))

# kör spelslingan
while True:
    # kontrollera om händelsen QUIT inträffat
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    matbitsRäknare += 1
    if matbitsRäknare >= NY_MATBIT:
        # addera mera matbitar
        matbitsRäknare = 0
        matbitar.append(pygame.Rect(random.randint(0, FÖNSTER_BREDD - MATBIT_STORLEK), random.randint(0, FÖNSTER_HÖJD - MATBIT_STORLEK), MATBIT_STORLEK, MATBIT_STORLEK))

    # rita svart bakgrund på ytan
    fönsterYta.fill(SVART)

    # flytta studsbollens datastruktur
    if studsboll['riktning'] == NER_VÄNSTER:
        studsboll['rektangel'].left -= HASTIGHET
        studsboll['rektangel'].top += HASTIGHET
    if studsboll['riktning'] == NER_HÖGER:
        studsboll['rektangel'].left += HASTIGHET
        studsboll['rektangel'].top += HASTIGHET
    if studsboll['riktning'] == UPP_VÄNSTER:
        studsboll['rektangel'].left -= HASTIGHET
        studsboll['rektangel'].top -= HASTIGHET
    if studsboll['riktning'] == UPP_HÖGER:
        studsboll['rektangel'].left += HASTIGHET
        studsboll['rektangel'].top -= HASTIGHET

    # kontrollera om studsbollen har hamnat utanför fönstret
    if studsboll['rektangel'].top < 0:
        # studsbollen har passerat ovansidan
        if studsboll['riktning'] == UPP_VÄNSTER:
            studsboll['riktning'] = NER_VÄNSTER
        if studsboll['riktning'] == UPP_HÖGER:
            studsboll['riktning'] = NER_HÖGER
    if studsboll['rektangel'].bottom > FÖNSTER_HÖJD:
        # studsbollen har passerat undersidan
        if studsboll['riktning'] == NER_VÄNSTER:
            studsboll['riktning'] = UPP_VÄNSTER
        if studsboll['riktning'] == NER_HÖGER:
            studsboll['riktning'] = UPP_HÖGER
    if studsboll['rektangel'].left < 0:
        # studsbollen har passerat vänster sida
        if studsboll['riktning'] == NER_VÄNSTER:
            studsboll['riktning'] = NER_HÖGER
        if studsboll['riktning'] == UPP_VÄNSTER:
            studsboll['riktning'] = UPP_HÖGER
    if studsboll['rektangel'].right > FÖNSTER_BREDD:
        # studsbollen har passerat höger sida
        if studsboll['riktning'] == NER_HÖGER:
            studsboll['riktning'] = NER_VÄNSTER
        if studsboll['riktning'] == UPP_HÖGER:
            studsboll['riktning'] = UPP_VÄNSTER

    # rita studsbollen på ytan
    pygame.draw.rect(fönsterYta, VIT, studsboll['rektangel'])

    # kontrollera om studsbollen korsar någon matbit
    for matbit in matbitar[:]:
        if överlapparRektanglar(studsboll['rektangel'], matbit):
            matbitar.remove(matbit)

    # rita matbitarna
    for i in range(len(matbitar)):
        pygame.draw.rect(fönsterYta, GRÖN, matbitar[i])

    # rita fönstret på skärmen
    pygame.display.update()
    huvudKlocka.tick(40)
