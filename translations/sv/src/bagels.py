import random
def hämtaHemligtTal(antalSiffror):
    # Returnerar en sträng som är antalSiffror lång och som består av unika, framslumpade siffror.
    siffror = list(range(10))
    random.shuffle(siffror)
    hemligtTal = ''
    for i in range(antalSiffror):
        hemligtTal += str(siffror[i])
    return hemligtTal

def hämtaLedtrådar(gissning, hemligtTal):
    # Returnerar en sträng med ledtrådar till användaren.
    if gissning == hemligtTal:
        return 'Du kom på det!'

    ledtråd = []

    for i in range(len(gissning)):
        if gissning[i] == hemligtTal[i]:
            ledtråd.append('Fermi')
        elif gissning[i] in hemligtTal:
            ledtråd.append('Pico')
    if len(ledtråd) == 0:
        return 'Bagels'

    ledtråd.sort()
    return ' '.join(ledtråd)

def ärBaraSiffror(tal):
    # Returnerar True om tal är en sträng som enbart består av siffror. Annars returneras False.
    if tal == '':
        return False

    for i in tal:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def spelaIgen():
    # Den här funktionen returnerar True om spelaren vill spela igen, annars returnerar den False.
    print('Vill du spela igen? (ja eller nej)')
    return input().lower().startswith('j')

ANTAL_SIFFROR = 3
MAX_ANTAL_GISSNINGAR = 10

print('Jag tänker på ett %s-siffrigt tal. Försök att gissa talet.' % (ANTAL_SIFFROR))
print('Här får du några ledtrådar:')
print('När jag säger:    Betyder det:')
print('  Pico            En siffra är korrekt men på fel position.')
print('  Fermi           En siffra är korrekt och på rätt position.')
print('  Bagels          Ingen siffra är korrekt.')

while True:
    hemligtTal = hämtaHemligtTal(ANTAL_SIFFROR)
    print('Jag har kommit på ett tal. Du får %s gissningar på dig för att räkna ut det.' % (MAX_ANTAL_GISSNINGAR))

    antalGissningar = 1
    while antalGissningar <= MAX_ANTAL_GISSNINGAR:
        gissning = ''
        while len(gissning) != ANTAL_SIFFROR or not ärBaraSiffror(gissning):
            print('Gissning #%s: ' % (antalGissningar))
            gissning = input()

        ledtråd = hämtaLedtrådar(gissning, hemligtTal)
        print(ledtråd)
        antalGissningar += 1

        if gissning == hemligtTal:
            break
        if antalGissningar > MAX_ANTAL_GISSNINGAR:
            print('Du fick slut på gissningar. Svaret var %s.' % (hemligtTal))

    if not spelaIgen():
        break
