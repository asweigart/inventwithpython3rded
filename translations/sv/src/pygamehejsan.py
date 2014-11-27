import pygame, sys
from pygame.locals import *

# skapa pygame
pygame.init()

# skapa fönstret
fönsteryta = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hej Sverige!')

# skapa färgerna
SVART = (0, 0, 0)
VIT = (255, 255, 255)
RÖD = (255, 0, 0)
GRÖN = (0, 255, 0)
BLÅ = (0, 0, 255)

# skapa fonter
basfont = pygame.font.SysFont(None, 48)

# skapa texten
text = basfont.render('Hej Sverige!', True, VIT, BLÅ)
textrektangel = text.get_rect()
textrektangel.centerx = fönsteryta.get_rect().centerx
textrektangel.centery = fönsteryta.get_rect().centery

# rita den vita bakgrunden på ytan
fönsteryta.fill(VIT)

# rita en grön polygon på ytan
pygame.draw.polygon(fönsteryta, GRÖN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# rita några blå linjer på ytan
pygame.draw.line(fönsteryta, BLÅ, (60, 60), (120, 60), 4)
pygame.draw.line(fönsteryta, BLÅ, (120, 60), (60, 120))
pygame.draw.line(fönsteryta, BLÅ, (60, 120), (120, 120), 4)

# rita en blå cirkel på ytan
pygame.draw.circle(fönsteryta, BLÅ, (300, 50), 20, 0)

# rita en röd ellips på ytan
pygame.draw.ellipse(fönsteryta, RÖD, (300, 250, 40, 80), 1)

# rita textens bakgrundsrektangel på ytan
pygame.draw.rect(fönsteryta, RÖD, (textrektangel.left - 20, textrektangel.top - 20, textrektangel.width + 40, textrektangel.height + 40))

# hämta en pixelmatris från ytan
pixelmatris = pygame.PixelArray(fönsteryta)
pixelmatris[480][380] = SVART
del pixelmatris

# rita texten på ytan
fönsteryta.blit(text, textrektangel)

# rita fönstret på skärmen
pygame.display.update()

# kör spelslingan
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
