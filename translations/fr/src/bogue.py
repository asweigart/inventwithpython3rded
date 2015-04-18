import random
nombre1 = random.randint(1, 10)
nombre2 = random.randint(1, 10)
print('Combien fait ' + str(nombre1) + ' + ' + str(nombre2) + ' ?')
reponse = input()
if int(reponse) == nombre1 + nombre2:
    print('Correct!')
else:
    print('Raté ! La réponse est ' + str(nombre1 + nombre2))
