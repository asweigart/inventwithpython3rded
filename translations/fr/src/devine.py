# Ceci est un jeu deviner un nombre
import random

tentative = 0

print('Bonjour ! Quel est votre nom ?')
monNom = input()

nombre = random.randint(1, 20)
print('Bien, ' + monNom + ', Je choisis un nombre entre 1 et 20.')

while tentative < 6:
    print('Faites votre choix.') # Il y a 4 espaces avant le print.
    choix = input()
    choix = int(choix)

    tentative = tentative + 1

    if choix < nombre:

        print('Votre choix est trop bas.') # There are eight spaces in front of print.

    if choix > nombre:
        print('Votre choix est trop haut.')

    if choix == nombre:
        break

if choix == nombre:
    tentative = str(tentative)
    print('Bien joué, ' + monNom + '! Vous avez devinez mon nombre en ' + tentative + ' tentatives !')

if choix != nombre:
    nombre = str(nombre)
    print('Raté. Le nombre que j''avais choisi était ' + nombre)
