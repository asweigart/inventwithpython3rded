import random
tal1 = random.randint(1, 10)
tal2 = random.randint(1, 10)
print('Vad blir ' + str(tal1) + ' + ' + str(tal2) + '?')
svar = input()
if svar == tal1 + tal2:
    print('Rätt!')
else:
    print('Nix! Svaret är ' + str(tal1 + tal2))
