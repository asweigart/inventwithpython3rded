import pygame, random, sys
from pygame.locals import *

FÖNSTERBREDD = 600
FÖNSTERHÖJD = 600
TEXTFÄRG = (255, 255, 255)
BAKGRUNDSFÄRG = (0, 0, 0)
FPS = 40
SKURK_MIN_STORLEK = 10
SKURK_MAX_STORLEK = 40
SKURK_MIN_HASTIGHET = 1
SKURK_MAX_HASTIGHET = 8
NY_SKURK_NIVÅ = 6
SPELARHASTIGHET = 5

def avsluta():
    pygame.quit()
    sys.exit()

def väntaPåKnapptryckning():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                avsluta()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # ett tryck på escape avslutar spelet
                    avsluta()
                return

def spelareHarTräffatSkurk(spelarrektangel, skurkar):
    for s in skurkar:
        if spelarrektangel.colliderect(s['rektangel']):
            return True
    return False

def ritaText(text, font, yta, x, y):
    textobj = font.render(text, 1, TEXTFÄRG)
    textrektangel = textobj.get_rect()
    textrektangel.topleft = (x, y)
    yta.blit(textobj, textrektangel)

# förbered pygame, fönstret och muspekaren
pygame.init()
huvudklocka = pygame.time.Clock()
fönsteryta = pygame.display.set_mode((FÖNSTERBREDD, FÖNSTERHÖJD))
pygame.display.set_caption('Smitaren')
pygame.mouse.set_visible(False)

# förbered font
font = pygame.font.SysFont(None, 48)

# förbered ljud
speletÖverLjud = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mid')

# förbered bilder
spelarbild = pygame.image.load('player.png')
spelarrektangel = spelarbild.get_rect()
skurkbild = pygame.image.load('baddie.png')

# visa startskärmen
ritaText('Smitaren', font, fönsteryta, (FÖNSTERBREDD / 3), (FÖNSTERHÖJD / 3))
ritaText('Tryck på en tangent för att starta.', font, fönsteryta, (FÖNSTERBREDD / 3) - 160, (FÖNSTERHÖJD / 3) + 50)
pygame.display.update()
väntaPåKnapptryckning()


bästaPoäng = 0
while True:
    # förbered för start av spelet
    skurkar = []
    poäng = 0
    spelarrektangel.topleft = (FÖNSTERBREDD / 2, FÖNSTERHÖJD - 50)
    flyttaVänster = flyttaHöger = flyttaUpp = flyttaNer = False
    bakåtfusk = bromsfusk = False
    läggTillSkurkRäknare = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # spelloopen körs medan spelet pågår
        poäng += 1 # öka poängen

        for event in pygame.event.get():
            if event.type == QUIT:
                avsluta()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    bakåtfusk = True
                if event.key == ord('x'):
                    bromsfusk = True
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
                if event.key == ord('z'):
                    bakåtfusk = False
                    poäng = 0
                if event.key == ord('x'):
                    bromsfusk = False
                    poäng = 0
                if event.key == K_ESCAPE:
                        avsluta()

                if event.key == K_LEFT or event.key == ord('a'):
                    flyttaVänster = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    flyttaHöger = False
                if event.key == K_UP or event.key == ord('w'):
                    flyttaUpp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    flyttaNer = False

            if event.type == MOUSEMOTION:
                # Om muspekaren flyttas så ska spelaren följa med.
                spelarrektangel.move_ip(event.pos[0] - spelarrektangel.centerx, event.pos[1] - spelarrektangel.centery)

        # Lägg till nya skurkar längst upp på skärmen, om det behövs.
        if not bakåtfusk and not bromsfusk:
            läggTillSkurkRäknare += 1
        if läggTillSkurkRäknare == NY_SKURK_NIVÅ:
            läggTillSkurkRäknare = 0
            skurkstorlek = random.randint(SKURK_MIN_STORLEK, SKURK_MAX_STORLEK)
            nySkurk = {'rektangel': pygame.Rect(random.randint(0, FÖNSTERBREDD-skurkstorlek), 0 - skurkstorlek, skurkstorlek, skurkstorlek),
                        'hastighet': random.randint(SKURK_MIN_HASTIGHET, SKURK_MAX_HASTIGHET),
                        'yta':pygame.transform.scale(skurkbild, (skurkstorlek, skurkstorlek)),
                        }

            skurkar.append(nySkurk)

        # Flytta spelaren.
        if flyttaVänster and spelarrektangel.left > 0:
            spelarrektangel.move_ip(-1 * SPELARHASTIGHET, 0)
        if flyttaHöger and spelarrektangel.right < FÖNSTERBREDD:
            spelarrektangel.move_ip(SPELARHASTIGHET, 0)
        if flyttaUpp and spelarrektangel.top > 0:
            spelarrektangel.move_ip(0, -1 * SPELARHASTIGHET)
        if flyttaNer and spelarrektangel.bottom < FÖNSTERHÖJD:
            spelarrektangel.move_ip(0, SPELARHASTIGHET)

        # Flytta muspekaren till spelarens position.
        pygame.mouse.set_pos(spelarrektangel.centerx, spelarrektangel.centery)

        # Flytta skurkarna nedåt.
        for s in skurkar:
            if not bakåtfusk and not bromsfusk:
                s['rektangel'].move_ip(0, s['hastighet'])
            elif bakåtfusk:
                s['rektangel'].move_ip(0, -5)
            elif bromsfusk:
                s['rektangel'].move_ip(0, 1)

        # Radera skurkar som har försvunnit ur fönstret.
        for s in skurkar[:]:
            if s['rektangel'].top > FÖNSTERHÖJD:
                skurkar.remove(s)

        # Rita spelvärlden i fönstret.
        fönsteryta.fill(BAKGRUNDSFÄRG)

        # Skriv ut nuvarande poäng och bästa poängen.
        ritaText('Poäng: %s' % (poäng), font, fönsteryta, 10, 0)
        ritaText('Bästa poäng: %s' % (bästaPoäng), font, fönsteryta, 10, 40)

        # Rita spelarrektangeln.
        fönsteryta.blit(spelarbild, spelarrektangel)

        # Rita varje skurk.
        for s in skurkar:
            fönsteryta.blit(s['yta'], s['rektangel'])

        pygame.display.update()

        # Kolla om någon av skurkarna har träffat spelaren.
        if spelareHarTräffatSkurk(spelarrektangel, skurkar):
            if poäng > bästaPoäng:
                bästaPoäng = poäng # registrera ny topp-poäng
            break

        huvudklocka.tick(FPS)

    # Stoppa spelet och visa "Spelet över"-skärmen.
    pygame.mixer.music.stop()
    speletÖverLjud.play()

    ritaText('GAME OVER', font, fönsteryta, (FÖNSTERBREDD / 3), (FÖNSTERHÖJD / 3))
    ritaText('Tryck en tangent för att spela igen.', font, fönsteryta, (FÖNSTERBREDD / 3) - 180, (FÖNSTERHÖJD / 3) + 50)
    pygame.display.update()
    väntaPåKnapptryckning()

    speletÖverLjud.stop()
