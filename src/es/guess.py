# Esta es una conjetura el juego número.
import random

conjeturasTomadas = 0

print('¡Hola! Cuál es tu nombre?')
miNombre = input()

número = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while conjeturasTomadas < 6:
    print('Tome una conjetura.') # There are four spaces in front of print.
    conjetura = input()
    conjetura = int(conjetura)

    conjeturasTomadas = conjeturasTomadas + 1

    if conjetura < número:
        print('Su conjetura es demasiado bajo.') # There are eight spaces in front of print.

    if conjetura > número:
        print('Su conjetura es demasiado alto.')

    if conjetura == número:
        break

if conjetura == número:
    conjeturasTomadas = str(conjeturasTomadas)
    print('Buen trabajo, ' + miNombre + '! Lo has adivinado mi número enn ' + conjeturasTomadas + ' conjeturas!')

if conjetura != número:
    número = str(número)
    print('Nop. El número que estaba pensando era ' + número)
