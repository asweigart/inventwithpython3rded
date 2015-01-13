import random
def obtenerNumSecreto(digitosNum):
    # Devuelve un numero de largo digotosNUm, compuesto de dígitos únicos al azar.
    numeros = list(range(10))
    random.shuffle(numeros)
    numSecreto = ''
    for i in range(digitosNum):
        numSecreto += str(numeros[i])
    return numSecreto

def obtenerPistas(conjetura, numSecreto):
    # Devuelve una palabra con las pistas Panecillos Pico y Fermi en ella.
    if conjetura == numSecreto:
        return '¡Lo has adivinado!'

    pista = []

    for i in range(len(conjetura)):
        if conjetura[i] == numSecreto[i]:
            pista.append('Fermi')
        elif conjetura[i] in numSecreto:
            pista.append('Pico')
    if len(pista) == 0:
        return 'Panecillos'

    pista.sort()
    return ' '.join(pista)

def esSoloDigitos(num):
    # Devuelve True si el número se compone sólo de dígitos. De lo contrario Falso.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def jugarDeNuevo():
    # Esta funcion devuelve True si el jugador desea vovler a jugar, de lo contrario Falso.
    print('¿Deseas volver a jugar? (sí o no)')
    return input().lower().startswith('s')

digitosNum = 3
MAXADIVINANZAS = 10

print('Estoy pensando en un número de %s dígitos. Intenta adivinar cuál es.' % (digitosNum))
print('Aquí hay algunas pistas:')
print('Cuando digo:    Eso significa:')
print('  Pico          Un dígito es correcto pero en la posición incorrecta.')
print('  Fermi         Un dígito es correcto y en la posición correcta.')
print('  Panecillos    Ningún dígito es correcto.')

while True:
    numSecreto = obtenerNumSecreto(digitosNum)
    print('He pensado un número. Tienes %s intentos para adivinarlo.' % (MAXADIVINANZAS))

    numIntentos = 1
    while numIntentos <= MAXADIVINANZAS:
        conjetura = ''
        while len(conjetura) != digitosNum or not esSoloDigitos(conjetura):
            print('Conjetura #%s: ' % (numIntentos))
            conjetura = input()

        pista = obtenerPistas(conjetura, numSecreto)
        print(pista)
        numIntentos += 1

        if conjetura == numSecreto:
            break
        if numIntentos > MAXADIVINANZAS:
            print('Te has quedado sin intentos. La respuesta era %s.' % (numSecreto))

    if not jugarDeNuevo():
        break
