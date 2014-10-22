# Det här spelet går ut på att gissa rätt tal.
import random

antalGissningar = 0

print('Hej! Vad heter du?')
namn = input()

tal = random.randint(1, 20)
print('Okej, ' + namn + ', jag tänker på ett tal mellan 1 och 20.')

while antalGissningar < 6:
    print('Gör en gissning.') # Det är fyra mellanslag före print.
    gissning = input()
    gissning = int(gissning)

    antalGissningar = antalGissningar + 1

    if gissning < tal:
        print('Du gissade på ett för lågt tal.') # Det är åtta mellanslag före print.

    if gissning > tal:
        print('Du gissade på ett för högt tal.')

    if gissning == tal:
        break

if gissning == tal:
    antalGissningar = str(antalGissningar)
    print('Bra jobbat, ' + namn + '! Du gissade rätt på ' + antalGissningar + ' gissningar!')

if gissning != tal:
    tal = str(tal)
    print('Nix. Talet jag tänkte på var ' + tal)
