# To jest gra w zgadywanie liczby
import random

probyZgadniecia = 0

print('Cześć! Jak masz na imię?')
mojeImie = input()

tajemnaLiczba = random.randint(1, 20)
print('Dobrze ' + mojeImie + ', myślę sobie o liczbie między 1 i 20.')

while probyZgadniecia < 6:
    print('Spróbuj ją zgadnąć.') # Na początku linii są cztery spacje.
    podanaLiczba = input()
    podanaLiczba = int(podanaLiczba)

    probyZgadniecia = probyZgadniecia + 1

    if podanaLiczba < tajemnaLiczba:
        print('Podałeś za małą liczbę.') # Na początku linii jest osiem spacji.

    if podanaLiczba > tajemnaLiczba:
        print('Podałeś zbyt dużą liczbę.')

    if podanaLiczba == tajemnaLiczba:
        break

if podanaLiczba == tajemnaLiczba:
    probyZgadniecia = str(probyZgadniecia)
    print('Gratuluję ' + mojeImie + '! Zgadłeś moją liczbę w ' + probyZgadniecia + ' próbach!')

if podanaLiczba != tajemnaLiczba:
    tajemnaLiczba = str(tajemnaLiczba)
    print('Niestety. Numer o jakim myślałem to ' + tajemnaLiczba)
