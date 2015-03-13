import random
print('Ich simuliere 1000 Münzenwürfe. Rate, wie oft das Ergebnis Zahl ist. (Drücke Enter, um zu beginnen)')
input()
wuerfe = 0
kopf = 0
while wuerfe < 1000:
	if random.randint(0, 1) == 1
		kopf = kopf + 1
	wuerfe = wuerfe + 1

	if wuerfe == 900:
    	print('900 Münzenwürfe, und Kopf kam ' + str(kopf) + ' mal vor.')
    if wuerfe == 100:
	    print('100 Münzenwürfe, Kopf kam bisher ' + str(kopf) + ' mal vor.')
	if wuerfe == 500:
		print('Halbzeit, und Kopf kam ' + str(kopf) + ' mal vor.')

print()
print('Von 1000 Münzwürfen hatten ' + str(kopf) + ' das Ergebnis Kopf!')
print('Warst du nahe dran?')