# Ekolod

import random
import sys

def ritaBräde(bräde):
    # Rita ut datastrukturen med spelbrädet.

    hrad = '    ' # inledande tomrum för siffrorna på vänstra sidan av brädet
    for i in range(1, 6):
        hrad += (' ' * 9) + str(i)

    # skriv ut siffrorna längs med överkanten
    print(hrad)
    print('   ' + ('0123456789' * 6))
    print()

    # skriv ut var och en av de 15 raderna
    for i in range(15):
        # ensiffriga tal måste fyllas ut med extra mellanrum
        if i < 10:
            mellanrum = ' '
        else:
            mellanrum = ''
        print('%s%s %s %s' % (mellanrum, i, hämtaRad(bräde, i), i))

    # skriv ut siffrorna längs med underkanten
    print()
    print('   ' + ('0123456789' * 6))
    print(hrad)


def hämtaRad(bräde, rad):
    # Returnera en sträng med en viss rad från datastrukturen med brädet.
    brädrad = ''
    for i in range(60):
        brädrad += bräde[i][rad]
    return brädrad

def hämtaNyttBräde():
    # Skapa en ny datastruktur för brädet med 60x15 element.
    bräde = []
    for x in range(60): # huvudlistan är en lista bestående av 60 listor
        bräde.append([])
        for y in range(15): # varje lista i huvudlistan innehåller 15 strängar med ett tecken i varje
            # använd olika tecken för havet för att göra det mer läsbart
            if random.randint(0, 1) == 0:
                bräde[x].append('~')
            else:
                bräde[x].append('`')
    return bräde

def slumpaFramKistor(antalKistor):
    # Skapa en lista med kistor (två heltal som representerar x- och y-koordinater)
    kistor = []
    for i in range(antalKistor):
        kistor.append([random.randint(0, 59), random.randint(0, 14)])
    return kistor

def ärTillåtetDrag(x, y):
    # Returnerar True om koordinaterna finns på brädet, annars False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def utförDrag(bräde, kistor, x, y):
    # Lägg till ett tecken för ekolodet på brädet. Ta bort skattkistor
    # från listan med kistor när de hittas. Returnera False om draget är otillåtet.
    # Annars, returnera en sträng med resultatet av draget.
    if not ärTillåtetDrag(x, y):
        return False

    minstaDistans = 100 # alla kistor ligger närmare än 100
    for cx, cy in kistor:
        if abs(cx - x) > abs(cy - y):
            distans = abs(cx - x)
        else:
            distans = abs(cy - y)

        if distans < minstaDistans: # vi vill ha den närmaste skattkistan
            minstaDistans = distans

    if minstaDistans == 0:
        # xy är direkt ovanför en skattkista!
        kistor.remove([x, y])
        return 'Du har hittat en sjunken skattkista!'
    else:
        if minstaDistans < 10:
            bräde[x][y] = str(minstaDistans)
            return 'Skatt upptäckt på en distans av %s från ekolodet.' % (minstaDistans)
        else:
            bräde[x][y] = 'O'
            return 'Ekolodet upptäckte ingenting. Alla skattkistor ligger utom räckhåll.'


def hämtaSpelardrag():
    # Låt spelaren mata in sitt drag. Returnera en lista med x- och y-koordinater.
    print('Var vill du släppa nästa ekolod? (0-59 0-14) (eller skriv sluta)')
    while True:
        drag = input()
        if drag.lower() == 'sluta':
            print('Tack för att du spelade!')
            sys.exit()

        drag = drag.split()
        if len(drag) == 2 and drag[0].isdigit() and drag[1].isdigit() and ärTillåtetDrag(int(drag[0]), int(drag[1])):
            return [int(drag[0]), int(drag[1])]
        print('Ange ett tal mellan 0 och 59, ett mellanrum, sedan ett tal mellan 0 och 14.')


def spelaIgen():
    # Den här funktionen returnerar True om spelaren vill spela igen, annars returnerar den False.
    print('Vill du spela igen? (ja eller nej)')
    return input().lower().startswith('j')


def visaInstruktioner():
    print('''Instruktioner:
Du är kapten på Simon, ett skattjägar-skepp. Ditt nuvarande uppdrag
är att hitta de tre sjunkna skattkistor som döljer sig i den del av 
havet där du befinner dig och samla in dem.

För att spela, ange koordinaterna för den plats i havet där du vill släppa ett
ekolod. Ekolodet kan räkna ut på vilket avstånd den närmaste kistan finns.
Ett exempel: Bokstaven e nedan visar var ekolodet har släppts, och tvåorna
representerar ett avstånd på 2 enheter från ekolodet. Fyrorna representerar
avstånd på 4 enheter från ekolodet.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 e 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
Tryck enter för att fortsätta...''')
    input()

    print('''Till exempel, här ligger en skattkista (markerad med s) på ett avstånd av 2 enheter
från ekolodet (markerat med e):

    22222
    s   2
    2 e 2
    2   2
    22222

Platsen där ekolodet släpptes kommer att markeras med en tvåa.

Skattkistorna flyttar sig inte. Ekoloden kan upptäcka skattkistor
på ett avstånd av upp till 9 enheter. Om alla kistor ligger utom räckhåll, så kommer platsen
att markeras med en nolla.

Om ett ekolod släpps rakt på en skattkista så kommer du att upptäcka
kistan och den kommer att samlas in. Ekolodet kommer att 
ligga kvar på platsen.

När du samlar in en kista kommer alla ekolod att uppdateras för att lokalisera
den kista som därefter ligger närmast.
Tryck enter för att fortsätta...''')
    input()
    print()


print('E K O L O D !')
print()
print('Vill du läsa instruktionerna? (ja/nej)')
if input().lower().startswith('j'):
    visaInstruktioner()

while True:
    # förbered spelet
    antalEkolod = 16
    brädet = hämtaNyttBräde()
    kistorna = slumpaFramKistor(3)
    ritaBräde(brädet)
    tidigareDrag = []

    while antalEkolod > 0:
        # Starten av en omgång:

        # visa status för antalet ekolod/kistor
        if antalEkolod > 1: ekolodändelse = '-enheter'
        else: ekolodändelse = '-enhet'
        if len(kistorna) > 1: kiständelse = 'or'
        else: kiständelse = 'a'
        print('Du har %s ekolod%s kvar. %s skattkist%s återstår.' % (antalEkolod, ekolodändelse, len(kistorna), kiständelse))

        x, y = hämtaSpelarDrag()
        tidigareDrag.append([x, y]) # vi måste spara alla drag så att ekoloden kan uppdateras

        resultatAvDrag = utförDrag(brädet, kistorna, x, y)
        if resultatAvDrag == False:
            continue
        else:
            if resultatAvDrag == 'Du har hittat en sjunken skattkista!':
                # uppdatera alla ekolod som för närvarande finns på kartan
                for x, y in tidigareDrag:
                    utförDrag(brädet, kistorna, x, y)
            ritaBräde(brädet)
            print(resultatAvDrag)

        if len(kistorna) == 0:
            print('Du har hittat alla sjunkna skattkistor! Grattis och bra spelat!')
            break

        antalEkolod -= 1

    if antalEkolod == 0:
        print('Vi har fått slut på ekolod! Nu måste vi vända skutan och ge oss av')
        print('hemåt trots att skattkistor ligger kvar i havet! Spelet är över.')
        print('    De återstående kistorna fanns här:')
        for x, y in kistorna:
            print('    %s, %s' % (x, y))

    if not spelaIgen():
        sys.exit()
