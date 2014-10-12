import random
import time

def introdPantalla():
    print('Delante de usted, usted ve a dos cuevas. En una cueva,')
    print('usted ve a dos cuevas. En una cueva, el dragón es amable')
    print('y compartir su tesoro con usted. El otro dragón')
    print('es codicioso y hambriento, y te comer en la vista.')
    print()

def elijaCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('¿Qué cueva va a entrar en? (1 o 2)')
        cueva = input()

    return cueva

def examineCueva(cuevaSeleccionado):
    print('Usted acerca a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('Un gran dragón salta delante de usted! Él abre sus fauces y...')
    print()
    time.sleep(2)

    amableCueva = random.randint(1, 2)

    if cuevaSeleccionado == str(amableCueva):
         print('Él le da su tesoro!')
    else:
         print('Él te engulle en un bocado!')

jugarDeNuevo = 'sí'
while jugarDeNuevo == 'sí' or jugarDeNuevo == 's':

    introdPantalla()

    númeroCueva = elijaCueva()

    examineCueva(númeroCueva)

    print('¿Quieres jugar otra vez? (sí or no)')
    jugarDeNuevo = input()
