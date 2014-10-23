# Reversi

import random
import sys

def ritaBräde(bräde):
    # Denna funktion skriver ut brädet som skickats in. Returnerar inget.
    HRAD = '  +---+---+---+---+---+---+---+---+'
    VRAD = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HRAD)
    for y in range(8):
        print(VRAD)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (bräde[x][y]), end=' ')
        print('|')
        print(VRAD)
        print(HRAD)


def tömBrädet(bräde):
    # Tömmer brädet förutom de fyra utgångsbrickorna
    for x in range(8):
        for y in range(8):
            bräde[x][y] = ' '

    # Utgångsbrickor:
    bräde[3][3] = 'X'
    bräde[3][4] = 'O'
    bräde[4][3] = 'O'
    bräde[4][4] = 'X'


def hämtaNyttBräde():
    # Skapar ett nytt tomt bräde
    bräde = []
    for i in range(8):
        bräde.append([' '] * 8)

    return bräde


def ärKorrektDrag(bräde, bricka, xstart, ystart):
    # Returnerar False om spelarens drag till ruta xstart,ystart är ogiltigt
    # Om det är ett korrekt drag, returnera en lista med rutor
    if bräde[xstart][ystart] != ' ' or not inomBrädet(xstart, ystart):
        return False

    bräde[xstart][ystart] = bricka # Placera tillfälligt brickan på brädet.

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
            # Det finns en angränsade bricka som tillhör den andre spelaren.
            x += xriktning
            y += yriktning
            if not inomBrädet(x, y):
                continue
            while bräde[x][y] == annanBricka:
                x += xriktning
                y += yriktning
                if not inomBrädet(x, y): # lämna while-slingan, fortsätt med for-slingan
                    break
            if not inomBrädet(x, y):
                continue
            if bräde[x][y] == bricka:
                # Det finns brickor att vända. Gå i motsatt riktning till vi når den ursprungliga rutan. Kom ihåg brickorna längs vägen.
                while True:
                    x -= xriktning
                    y -= yriktning
                    if x == xstart and y == ystart:
                        break
                    brickorAttVända.append([x, y])

    bräde[xstart][ystart] = ' ' # återställ den tomma rutan
    if len(brickorAttVända) == 0: # Om inga brickor vändes, är detta inte ett tillåtet drag.
        return False
    return brickorAttVända


def inomBrädet(x, y):
    # Returnera True om koordinaterna finns på brädet.
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def hämtaBrädeMedTillåtnaDrag(bräde, bricka):
    # Returnerar ett nytt bräde med punkter markerande drag som spelaren kan utföra.
    kopiaAvBräde = hämtaKopiaAvBräde(bräde)

    for x, y in hämtaKorrektaDrag(kopiaAvBräde, bricka):
        kopiaAvBräde[x][y] = '.'
    return kopiaAvBräde


def hämtaKorrektaDrag(bräde, bricka):
    # Returnerar en lista med koordinater utgörande tillåtna drag för spelaren på aktuellt bräde.
    KorrektaDrag = []

    for x in range(8):
        for y in range(8):
            if ärKorrektDrag(bräde, bricka, x, y) != False:
                KorrektaDrag.append([x, y])
    return KorrektaDrag


def hämtaBrädetsPoäng(bräde):
    # Beräkna poängen genom att räkna antalet brickor. Returnera ett dictionary med nycklarna 'X' och 'O'.
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
    # Låt spelaren mata in vilken bricka han/hon vill vara.
    # Returnera en lista med spelarens bricka och datorns bricka.
    bricka = ''
    while not (bricka == 'X' or bricka == 'O'):
        print('Vill du vara X eller O ?')
        bricka = input().upper()

    # det första elementet i listan innehåller spelarens bricka, det andra innehåller datorns bricka.
    if bricka == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def vemBörjar():
    # Slumpa vilken spelare som ska börja.
    if random.randint(0, 1) == 0:
        return 'dator'
    else:
        return 'spelare'


def spelaIgen():
    # Denna funktion returnerar True om spelaren vill spela en gång till annars False.
    print('Vill du spela en gång till ? (ja eller nej)')
    return input().lower().startswith('j')


def utförDrag(bräde, bricka, xstart, ystart):
    # Placera bricka på brädet på ruta xstart,ystart, samt vänd på motståndarens brickor.
    # Returnera False om detta är ett ogiltigt drag annars True.
    brickorAttVända = ärKorrektDrag(bräde, bricka, xstart, ystart)

    if brickorAttVända == False:
        return False

    bräde[xstart][ystart] = bricka
    for x, y in brickorAttVända:
        bräde[x][y] = bricka
    return True


def hämtaKopiaAvBräde(bräde):
    # Skapa en kopia av brädet och returnera den.
    kopiaAvBräde = hämtaNyttBräde()

    for x in range(8):
        for y in range(8):
            kopiaAvBräde[x][y] = bräde[x][y]

    return kopiaAvBräde


def ärEttHörn(x, y):
    # Returnerar True om positionen är ett av de fyra hörnen.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def hämtaSpelarensDrag(bräde, spelarensBricka):
    # Låt spelaren mata in sitt drag.
    # Returnerar draget som [x, y] (eller en av strängarna 'ledtrådar' eller 'sluta')
    SIFFROR_1_8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Mata in ditt drag, eller sluta för att avsluta, eller ledtrådar för att slå av/på ledtrådar.')
        drag = input().lower()
        if drag == 'sluta':
            return 'sluta'
        if drag == 'ledtrådar':
            return 'ledtrådar'

        if len(drag) == 2 and drag[0] in SIFFROR_1_8 and drag[1] in SIFFROR_1_8:
            x = int(drag[0]) - 1
            y = int(drag[1]) - 1
            if ärKorrektDrag(bräde, spelarensBricka, x, y) == False:
                continue
            else:
                break
        else:
            print('Draget är inte tillåtet. Mata in siffran för x (1-8), därefter siffran för y (1-8).')
            print('Till exempel, 81 motsvarar övre högra hörnet.')

    return [x, y]


def hämtaDatornsDrag(bräde, datornsBricka):
    # Givet ett bräde och datorns bricka, avgör
    # dragen och returnera dem som en [x, y] lista.
    möjligaDrag = hämtaKorrektaDrag(bräde, datornsBricka)

    # slumpa de möjliga dragens ordning
    random.shuffle(möjligaDrag)

    # välj alltid ett hörn om möjligt.
    for x, y in möjligaDrag:
        if ärEttHörn(x, y):
            return [x, y]

    # Gå igenom alla möjliga dra och kom ihåg draget med högst poäng
    bästaPoäng = -1
    for x, y in möjligaDrag:
        kopiaAvBräde = hämtaKopiaAvBräde(bräde)
        utförDrag(kopiaAvBräde, datornsBricka, x, y)
        poäng = hämtaBrädetsPoäng(kopiaAvBräde)[datornsBricka]
        if poäng > bästaPoäng:
            bästaDrag = [x, y]
            bästaPoäng = poäng
    return bästaDrag


def visaPoäng(spelarensBricka, datornsBricka):
    # Skriv ut nuvarande poäng.
    poäng = hämtaBrädetsPoäng(huvudBräde)
    print('Du har %s poäng. Datorn har %s poäng.' % (poäng[spelarensBricka], poäng[datornsBricka]))



print('Välkommen till Reversi!')

while True:
    # Nollställ brädet och spelet.
    huvudBräde = hämtaNyttBräde()
    tömBrädet(huvudBräde)
    spelarensBricka, datornsBricka = mataInSpelarensBricka()
    visaLedtrådar = False
    iTur = vemBörjar()
    print('' + iTur + 'n börjar spela.')

    while True:
        if iTur == 'spelare':
            # Spelarens tur.
            if visaLedtrådar:
                korrektaDragBräde = hämtaBrädeMedTillåtnaDrag(huvudBräde, spelarensBricka)
                ritaBräde(korrektaDragBräde)
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
                utförDrag(huvudBräde, spelarensBricka, drag[0], drag[1])

            if hämtaKorrektaDrag(huvudBräde, datornsBricka) == []:
                break
            else:
                iTur = 'dator'

        else:
            # Datorns tur.
            ritaBräde(huvudBräde)
            visaPoäng(spelarensBricka, datornsBricka)
            input("Tryck på Retur för att se datorns drag.")
            x, y = hämtaDatornsDrag(huvudBräde, datornsBricka)
            utförDrag(huvudBräde, datornsBricka, x, y)

            if hämtaKorrektaDrag(huvudBräde, spelarensBricka) == []:
                break
            else:
                iTur = 'spelare'

    # Visa slutlig poäng.
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
