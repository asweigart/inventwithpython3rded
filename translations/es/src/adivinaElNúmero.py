# Este es el juego de adivinar el número.
import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

número = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar.') # Hay cuatro espacios delante de print.
    estimación = input()
    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:
        print('Tu estimación es muy baja.') # Hay ocho espacios delante de print.

    if estimación > número:
        print('Tu estimación es muy alta.')

    if estimación == número:
        break

if estimación == número:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado mi número en ' + intentosRealizados + ' intentos!')

if estimación != número:
    número = str(número)
    print('Pues no. El número que estaba pensando era ' + número)
