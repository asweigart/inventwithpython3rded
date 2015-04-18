import random
print('Rzucę monetą 1000 razy. Zgadnij ile razy wypadnie orzeł. (Naciśnij enter by rozpocząć)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('900 rzutów i orzeł wypadł ' + str(heads) + ' razy.')
    if flips == 100:
        print('Mamy 100 rzutów, jak na razie orzeł wypadł ' + str(heads) + ' razy.')
    if flips == 500:
        print('Połowa za nami, a orzeł wypadł ' + str(heads) + ' razy.')

print()
print('Na 1000 rzutów, orzeł wypadł ' + str(heads) + ' razy!')
print('Byłeś bliski?')
