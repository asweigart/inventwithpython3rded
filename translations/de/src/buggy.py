import random
nummer1 = random.randint(1, 10)
nummer2 = random.randint(1, 10)
print('Wieviel ist ' + str(nummer1) + ' + ' + str(nummer2) + '?')
antwort = input()
if antwort == nummer1 + nummer2:
	print('Richtig!')
else:
	print('Nein! Die Antwort ist ' + str(nummer1 + nummer2))