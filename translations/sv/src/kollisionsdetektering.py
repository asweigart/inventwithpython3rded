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
huvudklocka = pygame.time.Clock()

# initiera fönstret
FÖNSTERBREDD = 400
FÖNSTERHÖJD = 400
fönsteryta = pygame.display.set_mode((FÖNSTERBREDD, FÖNSTERHÖJD), 0, 32)
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
matbitsräknare = 0
NY_MATBIT = 40
MATBITSTORLEK = 20
studsboll = {'rektangel':pygame.Rect(300, 100, 50, 50), 'riktning':UPP_VÄNSTER}
matbitar = []
for i in range(20):
    matbitar.append(pygame.Rect(random.randint(0, FÖNSTERBREDD - MATBITSTORLEK), random.randint(0, FÖNSTERHÖJD - MATBITSTORLEK), MATBITSTORLEK, MATBITSTORLEK))

# kör spelslingan
while True:
    # kontrollera om händelsen QUIT inträffat
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    matbitsräknare += 1
    if matbitsräknare >= NY_MATBIT:
        # addera mera matbitar
        matbitsräknare = 0
        matbitar.append(pygame.Rect(random.randint(0, FÖNSTERBREDD - MATBITSTORLEK), random.randint(0, FÖNSTERHÖJD - MATBITSTORLEK), MATBITSTORLEK, MATBITSTORLEK))

    # rita svart bakgrund på ytan
    fönsteryta.fill(SVART)

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
    if studsboll['rektangel'].bottom > FÖNSTERHÖJD:
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
    if studsboll['rektangel'].right > FÖNSTERBREDD:
        # studsbollen har passerat höger sida
        if studsboll['riktning'] == NER_HÖGER:
            studsboll['riktning'] = NER_VÄNSTER
        if studsboll['riktning'] == UPP_HÖGER:
            studsboll['riktning'] = UPP_VÄNSTER

    # rita studsbollen på ytan
    pygame.draw.rect(fönsteryta, VIT, studsboll['rektangel'])

    # kontrollera om studsbollen korsar någon matbit
    for matbit in matbitar[:]:
        if överlapparRektanglar(studsboll['rektangel'], matbit):
            matbitar.remove(matbit)

    # rita matbitarna
    for i in range(len(matbitar)):
        pygame.draw.rect(fönsteryta, GRÖN, matbitar[i])

    # rita fönstret på skärmen
    pygame.display.update()
    huvudklocka.tick(40)
