import random
print('Je vais jouer à Pile ou Face, 1000 fois. Devinez combien de pile vont sortir (Appuyez sur Entrée pour commencer)')
input()
lances = 0
piles = 0
while lances < 1000:
    if random.randint(0, 1) == 1:
        piles = piles + 1
    lances = lances + 1

    if lances == 900:
        print('900 lancés et il y a eu ' + str(piles) + ' pile.')
    if lances == 100:
        print('A 100 lancés, pile est sorti ' + str(piles) + ' fois jusque là.')
    if lances == 500:
        print('Mi-parcours, et pile est sorti ' + str(piles) + ' fois.')

print()
print('Après 1000 lancés de pièces, pile est sorti ' + str(piles) + '  fois !')
print('Etiez-vous proche ?')
