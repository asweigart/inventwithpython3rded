import pygame, sys
from pygame.locals import *

# skapa pygame
pygame.init()

# skapa fönstret
fönsterYta = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hej Sverige!')

# skapa färgerna
SVART = (0, 0, 0)
VIT = (255, 255, 255)
RÖD = (255, 0, 0)
GRÖN = (0, 255, 0)
BLÅ = (0, 0, 255)

# skapa fonter
basFont = pygame.font.SysFont(None, 48)

# skapa texten
text = basFont.render('Hej Sverige!', True, VIT, BLÅ)
textRektangel = text.get_rect()
textRektangel.centerx = fönsterYta.get_rect().centerx
textRektangel.centery = fönsterYta.get_rect().centery

# rita den vita bakgrunden på ytan
fönsterYta.fill(VIT)

# rita en grön polygon på ytan
pygame.draw.polygon(fönsterYta, GRÖN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# rita några blå linjer på ytan
pygame.draw.line(fönsterYta, BLÅ, (60, 60), (120, 60), 4)
pygame.draw.line(fönsterYta, BLÅ, (120, 60), (60, 120))
pygame.draw.line(fönsterYta, BLÅ, (60, 120), (120, 120), 4)

# rita en blå cirkel på ytan
pygame.draw.circle(fönsterYta, BLÅ, (300, 50), 20, 0)

# rita en röd ellips på ytan
pygame.draw.ellipse(fönsterYta, RÖD, (300, 250, 40, 80), 1)

# rita textens bakgrundsrektangel på ytan
pygame.draw.rect(fönsterYta, RÖD, (textRektangel.left - 20, textRektangel.top - 20, textRektangel.width + 40, textRektangel.height + 40))

# hämta en pixelmatris från ytan
pixelMatris = pygame.PixelArray(fönsterYta)
pixelMatris[480][380] = SVART
del pixelMatris

# rita texten på ytan
fönsterYta.blit(text, textRektangel)

# rita fönstret på skärmen
pygame.display.update()

# kör spelslingan
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
