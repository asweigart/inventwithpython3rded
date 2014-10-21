# Reversi

import random
import sys

def ritaBräde(bräde):
    # Denna funktion skriver ut brädet som skickats in. Returnerar inget.
    HRAD = '  +---+---+---+---+---+---+---+---+'
    # VRAD = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HRAD)
    for y in range(8):
        # print(VRAD)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (bräde[x][y]), end=' ')
        print('|')
        # print(VRAD)
        print(HRAD)


def tömBräde(bräde):
    # Tömmer brädet som skickats in och återställer startbrickorna.
    for x in range(8):
        for y in range(8):
            bräde[x][y] = ' '

    # Startbrickor:
    bräde[3][3] = 'X'
    bräde[3][4] = 'O'
    bräde[4][3] = 'O'
    bräde[4][4] = 'X'


def hämtaNyttBräde():
    # Skapar ett nytt tomt bräde.
    bräde = []
    for i in range(8):
        bräde.append([' '] * 8)

    return bräde


def ärTillåtetDrag(bräde, bricka, xstart, ystart):
    # Returnerar False om spelaren inte får lägga på rutan xstart,ystart.
    # Om det är ett korrekt drag, returnera en lista med brickor som blir spelarens om draget utförs.
    if bräde[xstart][ystart] != ' ' or not inomBrädet(xstart, ystart):
        return False

    bräde[xstart][ystart] = bricka # placera brickan tillfälligt på rutan.

    if bricka == 'X':
        annanBricka = 'O'
    else:
        annanBricka = 'X'

    brickorAttVända = []
    for xriktning, yriktning in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xriktning # första steget i riktningen
        y += yriktning # första steget i riktningen
        if inomBrädet(x, y) and bräde[x][y] == annanBricka:
            # En bricka som tillhör motståndaren är granne.
            x += xriktning
            y += yriktning
            if not inomBrädet(x, y):
                continue
            while bräde[x][y] == annanBricka:
                x += xriktning
                y += yriktning
                if not inomBrädet(x, y): # hoppa ut ur while-slingan, fortsätt därefter med for-slingan
                    break
            if not inomBrädet(x, y):
                continue
            if bräde[x][y] == bricka:
                # Det finns brickor att vända. Gå i motsatt riktning tills vi når den ursprungliga rutan, kom ihåg rutorna längs vägen.
                while True:
                    x -= xriktning
                    y -= yriktning
                    if x == xstart and y == ystart:
                        break
                    brickorAttVända.append([x, y])

    bräde[xstart][ystart] = ' ' # Återställ den tomma rutan.
    if len(brickorAttVända) == 0: # Om inga brickor har vänts, är draget inte tillåtet.
        return False
    return brickorAttVända


def inomBrädet(x, y):
    # Returnera True om koordinaterna finns på brädet
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def hämtaBrädeMedKorrektaDrag(bräde, bricka):
    # Returnerar ett nytt bräde med punkter som markerar de drag spelaren kan utföra.
    kopiaAvBräde = hämtaKopiaAvBräde(bräde)

    for x, y in hämtaKorrektaDrag(kopiaAvBräde, bricka):
        kopiaAvBräde[x][y] = '.'
    return kopiaAvBräde


def hämtaKorrektaDrag(bräde, bricka):
    # Returnerar en lista med korrekta drag för spelaren på det givna brädet.
    korrektaDrag = []

    for x in range(8):
        for y in range(8):
            if ärTillåtetDrag(bräde, bricka, x, y) != False:
                korrektaDrag.append([x, y])
    return korrektaDrag


def hämtaBrädetsPoäng(bräde):
    # Bestäm poängen genom att räkna brickorna. Returnerar en associerad lista med nycklarna 'X' och 'O'.
    xPoäng = 0
    oPoäng = 0
    for x in range(8):
        for y in range(8):
            if bräde[x][y] == 'X':
                xPoäng += 1
            if bräde[x][y] == 'O':
                oPoäng += 1
    return {'X':xPoäng, 'O':oPoäng}


def mataInSpelarensBricka():
    # Låt spelaren ange vilken bricka hen vill ha.
    # Returnerar en lista med spelarens bricka som första element och datorns bricka som andra.
    bricka = ''
    while not (bricka == 'X' or bricka == 'O'):
        print('Do you want to be X or O?')
        bricka = input().upper()

    # det första elementet i listan är spelarens bricka, det andra är datorns bricka.
    if bricka == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def vemBörjarSpela():
    # Låt slumpen avgöra vilken spelare som börjar.
    if random.randint(0, 1) == 0:
        return 'dator'
    else:
        return 'spelare'


def spelaIgen():
    # Denna funktion returnerar True om spelaren vill spela en gång till, annars False.
    print('Vill du spela igen? (ja eller nej)')
    return input().lower().startswith('j')


def skapaBräde(bräde, bricka, xstart, ystart):
    # Placera brickan på brädet på rutan xstart,ystart. Vänd på motståndarens brickor.
    # Returnerar False om draget inte är tillåtet, True om det är tillåtet.
    brickorAttVända = ärTillåtetDrag(bräde, bricka, xstart, ystart)

    if brickorAttVända == False:
        return False

    bräde[xstart][ystart] = bricka
    for x, y in brickorAttVända:
        bräde[x][y] = bricka
    return True


def hämtaKopiaAvBräde(bräde):
    # Skapa en kopia av brädet och returnera kopian.
    kopiaAvBräde = hämtaNyttBräde()

    for x in range(8):
        for y in range(8):
            kopiaAvBräde[x][y] = bräde[x][y]

    return kopiaAvBräde


def ärEttHörn(x, y):
    # Returnerar True om positionen är ett av de fyra hörnen.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def hämtaSpelarensDrag(bräde, spelarensBricka):
    # Låt spelaren skriva in sitt drag.
    # Returnerar draget som [x,y] (eller strängarna 'ledtrådar' eller 'sluta')
    SIFFROR_1_8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Mata in ditt drag, eller mata in sluta för att avsluta spelet, eller ledtrådar för att slå av/på ledtrådar.')
        drag = input().lower()
        if drag == 'sluta':
            return 'sluta'
        if drag == 'ledtrådar':
            return 'ledtrådar'

        if len(drag) == 2 and drag[0] in SIFFROR_1_8 and drag[1] in SIFFROR_1_8:
            x = int(drag[0]) - 1
            y = int(drag[1]) - 1
            if ärTillåtetDrag(bräde, spelarensBricka, x, y) == False:
                continue
            else:
                break
        else:
            print('Draget är inte tillåtet. Skriv en siffra för kolumn (1-8), därefter en siffra för rad (1-8).')
            print('Till exempel anger 81 övre högra hörnet.')

    return [x, y]


def hämtaDatornsDrag(bräde, datornsBricka):
    # Givet ett bräde och datorns bricka, bestäm
    # draget och returnera draget som en [x,y] lista.
    möjligaDrag = hämtaKorrektaDrag(bräde, datornsBricka)

    # slumpa de mjöliga dragen
    random.shuffle(möjligaDrag)

    # välj alltid ett hörn om det är möjligt.
    for x, y in möjligaDrag:
        if ärEttHörn(x, y):
            return [x, y]

    # Gå igenom alla möjliga drag och kom ihåg det med högst poäng.
    högstaPoäng = -1
    for x, y in möjligaDrag:
        kopiaAvBräde = hämtaKopiaAvBräde(bräde)
        skapaBräde(kopiaAvBräde, datornsBricka, x, y)
        poäng = hämtaBrädetsPoäng(kopiaAvBräde)[datornsBricka]
        if poäng > högstaPoäng:
            bästaDrag = [x, y]
            högstaPoäng = poäng
    return bästaDrag


def visaPoäng(spelarensBricka, datornsBricka):
    # Skriv ut nuvarande poäng.
    poäng = hämtaBrädetsPoäng(huvudBräde)
    print('Du har %s poäng. Datorn har %s poäng.' % (poäng[spelarensBricka], poäng[datornsBricka]))



print('Välkommen till Reversi!')

while True:
    # Nollställ brädet och spelet.
    huvudBräde = hämtaNyttBräde()
    tömBräde(huvudBräde)
    spelarensBricka, datornsBricka = mataInSpelarensBricka()
    visaLedtrådar = False
    itur = vemBörjarSpela()
    print(itur + 'n börjar spela.')

    while True:
        if itur == 'spelare':
            # Spelarens drag.
            if visaLedtrådar:
                brädeMedKorrektaDrag = hämtaBrädeMedKorrektaDrag(huvudBräde, spelarensBricka)
                ritaBräde(brädeMedKorrektaDrag)
            else:
                ritaBräde(huvudBräde)
            visaPoäng(spelarensBricka, datornsBricka)
            drag = hämtaSpelarensDrag(huvudBräde, spelarensBricka)
            if drag == 'sluta':
                print('Tack för spelet!')
                sys.exit() # avsluta programmet
            elif drag == 'ledtrådar':
                visaLedtrådar = not visaLedtrådar
                continue
            else:
                skapaBräde(huvudBräde, spelarensBricka, drag[0], drag[1])

            if hämtaKorrektaDrag(huvudBräde, datornsBricka) == []:
                break
            else:
                itur = 'dator'

        else:
            # Datorns drag.
            ritaBräde(huvudBräde)
            visaPoäng(spelarensBricka, datornsBricka)
            input('Tryck på Retur-tangenten för att se datorns drag.')
            x, y = hämtaDatornsDrag(huvudBräde, datornsBricka)
            skapaBräde(huvudBräde, datornsBricka, x, y)

            if hämtaKorrektaDrag(huvudBräde, spelarensBricka) == []:
                break
            else:
                itur = 'spelare'

    # Visa den slutliga poängen.
    ritaBräde(huvudBräde)
    poäng = hämtaBrädetsPoäng(huvudBräde)
    print('X fick %s poäng. O fick %s poäng.' % (poäng['X'], poäng['O']))
    if poäng[spelarensBricka] > poäng[datornsBricka]:
        print('Du slog datorn med %s poäng! Gratulerar!' % (poäng[spelarensBricka] - poäng[datornsBricka]))
    elif poäng[spelarensBricka] < poäng[datornsBricka]:
        print('Du förlorade. Datorn slog dig med %s poäng.' % (poäng[datornsBricka] - poäng[spelarensBricka]))
    else:
        print('Spelet blev oavgjort!')

    if not spelaIgen():
        break