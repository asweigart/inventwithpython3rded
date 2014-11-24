import pygame, sys
from pygame.locals import *

# menyiapkan pygame
pygame.init()

# menyiapkan jendela keluaran
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Halo Dunia!')

# menyiapkan warna yang dipakai
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# menyiapkan font yang dipakai
basicFont = pygame.font.SysFont(None, 48)

# menyiapkan teks
text = basicFont.render('Halo Dunia!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# menggambar latar belakang putih pada surface
windowSurface.fill(WHITE)

# menggambar segibanyak hijau pada surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# menggambar beberapa garis biru pada surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# menggambar lingkaran biru pada surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# menggambar elips merah pada surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# menggambar kotak latar belakang untuk teks pada surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# ambil array pixel dari surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# menggambar teks pada surface
windowSurface.blit(text, textRect)

# menggambar jendela pada layar
pygame.display.update()

# jalankan putaran game
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
