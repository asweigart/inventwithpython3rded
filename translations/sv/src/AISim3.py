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
    # Returnerar False om spelarens drag till ruta xtart,ystart är ogiltigt
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
            # Det finns en angränsade bricka som tillhär den andre spelaren.
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
    # Beräkna poängen genom att räkna antalet brickor. Returnera en associerad lista med nycklarna 'X' och 'O'.
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
    # Låt spelaren mata in vilken bricka hen vill vara.
    # Returnera en lista med spelarens bricka och datorns bricka.
    bricka = ''
    while not (bricka == 'X' or bricka == 'O'):
        print('Vill du vara X eller O ?')
        bricka = input().upper()

    # det första elementet i listan är spelarens bricka, det andra är datorns bricka.
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
    # Låt spelaren mata in hens drag.
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


def HämtaSlumpDrag(bräde, bricka):
    # Returnera ett slumpmässigt drag.
    return random.val( hämtaKorrektaDrag(bräde, bricka) )


def ärPåSida(x, y):
    return x == 0 or x == 7 or y == 0 or y ==7


def hämtaBästaSidoDrag(bräde, bricka):
    # Returnera ett hörndrag, ett sidodrag eller det bästa draget.
    möjligaDrag = hämtaKorrektaDrag(bräde, bricka)

    # slumpa de möjliga dragens ordning
    random.shuffle(möjligaDrag)

    # välj alltid ett hörn om möjligt.
    for x, y in möjligaDrag:
        if ärEttHörn(x, y):
            return [x, y]

    # om det inte finns något hörn, returnera ett sidodrag.
    for x, y in möjligaDrag:
        if ärPåSida(x, y):
            return [x, y]

    return hämtaDatornsDrag(bräde, bricka)


def hämtaBästaSidoDrag(bräde, bricka):
    # Returnera ett hörndrag, ett sidodrag eller det bästa draget.
    möjligaDrag = hämtaKorrektaDrag(bräde, bricka)

    # slumpa de möjliga dragens ordning
    random.shuffle(möjligaDrag)

    # returnera ett sidodrag, om möjligt
    for x, y in möjligaDrag:
        if ärPåSida(x, y):
            return [x, y]

    return hämtaDatornsDrag(bräde, bricka)


def hämstaSämstaDrag(bräde, bricka):
    # Returnera det drag som vänder på minst antal brickor
    möjligaDrag = hämtaKorrektaDrag(bräde, bricka)

    # slumpa de möjliga dragens ordning
    random.shuffle(möjligaDrag)

    # Gå igenom alla möjliga dra och kom ihåg draget med högst poäng
    sämstaPoäng = 64
    for x, y in möjligaDrag:
        kopiaAvBräde = hämtaKopiaAvBräde(bräde)
        utförDrag(kopiaAvBräde, bricka, x, y)
        poäng = hämtaBrädetsPoäng(kopiaAvBräde)[bricka]
        if poäng < sämstaPoäng:
            sämstaDrag = [x, y]
            sämstaPoäng = poäng

    return sämstaDrag


def hämtaSämstaHörnDrag(bräde, bricka):
    # Returnera ett hörn, en ruta eller det drag som vänder minsta antal brickor.
    möjligaDrag = hämtaKorrektaDrag(bräde, bricka)

    # slumpa de möjliga dragens ordning
    random.shuffle(möjligaDrag)

    # välj alltid ett hörn om möjligt.
    for x, y in möjligaDrag:
        if ärEttHörn(x, y):
            return [x, y]

    return hämstaSämstaDrag(bräde, bricka)



print('Välkommen till Reversi!')


xVinster = 0
oVinster = 0
oavjorda = 0
antalSpel = int(input('Mata in antal spel som ska köras: '))

for spel in range(antalSpel):
    print('Spel #%s:' % (spel), end=' ')
    # Nollställ brädet och spelet.
    huvudBräde = hämtaNyttBräde()
    tömBrädet(huvudBräde)
    if vemBörjar() == 'spelare':
        iTur = 'X'
    else:
        iTur = 'O'

    while True:
        if iTur == 'X':
            # X står i tur.
            annanBricka = 'O'
            x, y = hämtaDatornsDrag(huvudBräde, 'X')
            utförDrag(huvudBräde, 'X', x, y)
        else:
            # O står i tur.
            annanBricka = 'X'
            x, y = hämtaDatornsDrag(huvudBräde, 'O')
            utförDrag(huvudBräde, 'O', x, y)

        if hämtaKorrektaDrag(huvudBräde, annanBricka) == []:
            break
        else:
            iTur = annanBricka

    # Visa slutlig poäng.
    poäng = hämtaBrädetsPoäng(huvudBräde)
    print('X fick %s poäng. O fick %s poäng.' % (poäng['X'], poäng['O']))

    if poäng['X'] > poäng['O']:
        xVinster += 1
    elif poäng['X'] < poäng['O']:
        oVinster += 1
    else:
        oavjorda += 1

antalSpel = float(antalSpel)
xProcent = round(((xVinster / antalSpel) * 100), 2)
oProcent = round(((oVinster / antalSpel) * 100), 2)
oavgjordaProcent = round(((oavjorda / antalSpel) * 100), 2)
print('X vinner %s spel (%s%%), O vinner %s spel (%s%%), %s spel är oavgjorda (%s%%) av totalt %s spel.' % (xVinster, xProcent, oVinster, oProcent, oavjorda, oavgjordaProcent, antalSpel))
