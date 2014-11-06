# Das ist ein Zahlenratespiel.
import random

abgegebenTipps = 0

print('Hallo? Was ist dein Name')
meinName = input()

zahl = random.randint(1, 20)
print('Also, ' + meinName + ', ich denke an eine Zahl zwischen 1 und 20')

while abgegebenTipps < 6:
    print('Los, rate.') # Vor print sind vier Leerzeichen.
    tipp = input()
    tipp = int(tipp)

    abgegebenTipps = abgegebenTipps + 1

    if tipp < zahl:
        print('Dein Tipp ist zu niedrig.') # Hier sind acht Leerzeichen vor print.

    if tipp > zahl:
        print('Dein Tipp ist zu hoch.')

    if tipp == zahl:
        break

if tipp == zahl:
    abgegebenTipps = str(abgegebenTipps)
    print('Gut gemacht, ' + meinName + '! Du hast meine Zahl in ' + abgegebenTipps + ' Zügen erraten!')

if tipp != zahl:
    zahl = str(zahl)
    print('Nene. Die Nummer an die ich gedacht habe war ' + zahl)
