import random
import time

def displayIntro():
    print('Jesteś w krainie pełnej smoków. Przed sobą widzisz')
    print('dwie jasinie. W jednej mieszka przyjacielski smok,')
    print('który podzieli sie z tobą skarbem. Drugi smok jest')
    print('chciwy i głodny, i zje cię na miejscu.')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Do której jaskini chcesz wejść? (1 lub 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('Zbliżasz się do jaskini...')
    time.sleep(2)
    print('Jest ciemna i straszna...')
    time.sleep(2)
    print('Wielki smok wyskakuje prosto na ciebie! Otwiera swą paszczę i ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
         print('Daje ci swój skarb!')
    else:
         print('Pożera cie jednym kłapnięciem paszczy!')

playAgain = 'tak'
while playAgain == 'tak' or playAgain == 't':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Chcesz zagrać ponownie? (tak lub nie)')
    playAgain = input()
