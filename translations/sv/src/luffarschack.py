# Luffarschack

import random

def ritaBräde(bräde):
    # Den här funktionen skriver ut det spelbräde som har skickats in.

    # "bräde" är en lista med 10 strängar som representerar spelbrädet (ignorera index 0)
    print('   |   |')
    print(' ' + bräde[7] + ' | ' + bräde[8] + ' | ' + bräde[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bräde[4] + ' | ' + bräde[5] + ' | ' + bräde[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + bräde[1] + ' | ' + bräde[2] + ' | ' + bräde[3])
    print('   |   |')

def väljBokstav():
    # Låter spelaren välja vilken bokstav den ska vara.
    # Returnerar en lista med spelarens bokstav i det första elementet och datorns bokstav i det andra.
    bokstav = ''
    while not (bokstav == 'X' or bokstav == 'O'):
        print('Vill du vara X eller O?')
        bokstav = input().upper()

    # första elementet i listan är spelarens bokstav, det andra är datorns bokstav
    if bokstav == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def vemBörjar():
    # Avgör med hjälp av slumpen vilken spelare som ska börja.
    if random.randint(0, 1) == 0:
        return 'datorn'
    else:
        return 'spelaren'

def spelaIgen():
    # Den här funktionen returnerar True om spelaren vill spela igen, annars returnerar den False.
    print('Vill du spela igen? (ja eller nej)')
    return input().lower().startswith('j')

def görDrag(bräde, bokstav, drag):
    bräde[drag] = bokstav

def ärVinnare(br, bo):
    # Får in spelbrädet och spelarens bokstav och returnerar True om spelaren har vunnit.
    # Vi använder br i stället för bräde och bo i stället för bokstav så vi inte behöver skriva så mycket.
    return ((br[7] == bo and br[8] == bo and br[9] == bo) or # vågrätt längst upp
    (br[4] == bo and br[5] == bo and br[6] == bo) or # vågrätt i mitten
    (br[1] == bo and br[2] == bo and br[3] == bo) or # vågrätt längst ner
    (br[7] == bo and br[4] == bo and br[1] == bo) or # lodrätt till vänster
    (br[8] == bo and br[5] == bo and br[2] == bo) or # lodrätt i mitten
    (br[9] == bo and br[6] == bo and br[3] == bo) or # lodrätt till höger
    (br[7] == bo and br[5] == bo and br[3] == bo) or # ena diagonalen
    (br[9] == bo and br[5] == bo and br[1] == bo)) # andra diagonalen

def kopieraBräde(bräde):
    # Gör en kopia av listan med spelbrädet och returnerar kopian.
    brädkopia = []

    for i in bräde:
        brädkopia.append(i)

    return brädkopia

def finnsPlats(bräde, drag):
    # Returnerar True om det finns plats på den position som spelaren vill flytta till.
    return bräde[drag] == ' '

def hämtaSpelardrag(bräde):
    # Låter spelaren skriva in sitt drag.
    drag = ' '
    while drag not in '1 2 3 4 5 6 7 8 9'.split() or not finnsPlats(bräde, int(drag)):
        print('Vilket är ditt nästa drag? (1-9)')
        drag = input()
    return int(drag)

def slumpaDragFrånLista(bräde, draglista):
    # Returnerar ett giltigt drag från den lista över drag som skickats in.
    # Returnerar None om det inte finns något giltigt drag.
    möjligaDrag = []
    for i in draglista:
        if finnsPlats(bräde, i):
            möjligaDrag.append(i)

    if len(möjligaDrag) != 0:
        return random.choice(möjligaDrag)
    else:
        return None

def hämtaDatordrag(bräde, datorbokstav):
    # Givet spelbrädet och datorns bokstav, avgör vart datorn ska flytta och returnera draget.
    if datorbokstav == 'X':
        spelarbokstav = 'O'
    else:
        spelarbokstav = 'X'

    # Här är vår algoritm för luffarschackets AI:
    # Först kollar vi om vi kan vinna genom nästa drag
    for i in range(1, 10):
        kopia = kopieraBräde(bräde)
        if finnsPlats(kopia, i):
            görDrag(kopia, datorbokstav, i)
            if ärVinnare(kopia, datorbokstav):
                return i

    # Kolla ifall spelaren kan vinna genom nästa drag och blockera i så fall positionen.
    for i in range(1, 10):
        kopia = kopieraBräde(bräde)
        if finnsPlats(kopia, i):
            görDrag(kopia, spelarbokstav, i)
            if ärVinnare(kopia, spelarbokstav):
                return i

    # Försök att ta ett av hörnen, om det finns ett ledigt.
    drag = slumpaDragFrånLista(bräde, [1, 3, 7, 9])
    if drag != None:
        return drag

    # Försök att ta mittenpositionen, om den är ledig.
    if finnsPlats(bräde, 5):
        return 5

    # Flytta till en av sidorna.
    return slumpaDragFrånLista(bräde, [2, 4, 6, 8])

def brädetFullt(bräde):
    # Returnera True om varje position på spelbrädet är upptagen. Annars returnera False.
    for i in range(1, 10):
        if finnsPlats(bräde, i):
            return False
    return True


print('Välkommen till Luffarschack!')

while True:
    # Nollställ spelbrädet
    spelbrädet = [' '] * 10
    spelarbokstav, datorbokstav = väljBokstav()
    nästPåTur = vemBörjar()
    print('Det är ' + nästPåTur + ' som börjar.')
    speletPågår = True

    while speletPågår:
        if nästPåTur == 'spelaren':
            # Det är spelarens tur.
            ritaBräde(spelbrädet)
            drag = hämtaSpelardrag(spelbrädet)
            görDrag(spelbrädet, spelarbokstav, drag)

            if ärVinnare(spelbrädet, spelarbokstav):
                ritaBräde(spelbrädet)
                print('Hurra! Du har vunnit partiet!')
                speletPågår = False
            else:
                if brädetFullt(spelbrädet):
                    ritaBräde(spelbrädet)
                    print('Partiet blev oavgjort!')
                    break
                else:
                    nästPåTur = 'datorn'

        else:
            # Det är datorns tur.
            drag = hämtaDatordrag(spelbrädet, datorbokstav)
            görDrag(spelbrädet, datorbokstav, drag)

            if ärVinnare(spelbrädet, datorbokstav):
                ritaBräde(spelbrädet)
                print('Datorn har slagit dig! Du har förlorat.')
                speletPågår = False
            else:
                if brädetFullt(spelbrädet):
                    ritaBräde(spelbrädet)
                    print('Partiet blev oavgjort!')
                    break
                else:
                    nästPåTur = 'spelaren'

    if not spelaIgen():
        break
