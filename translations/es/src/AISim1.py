# Reversi

import random
import sys

def dibujarTablero(tablero):
    # Esta funcion dibuja el tablero pasado. Devuelve None
    LINEAH = '  +---+---+---+---+---+---+---+---+'
    LINEAV = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(LINEAH)
    for y in range(8):
        print(LINEAV)
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (tablero[x][y]), end=' ')
        print('|')
        print(LINEAV)
        print(LINEAH)


def blanquearTablero(tablero):
    # Blanquea el tablero pasado, excepto la posicion original.
    for x in range(8):
        for y in range(8):
            tablero[x][y] = ' '

    # Piezas que comienzan:
    tablero[3][3] = 'X'
    tablero[3][4] = 'O'
    tablero[4][3] = 'O'
    tablero[4][4] = 'X'


def obtenerNuevoTablero():
    # Crea un tablero nuevo, blanqueado.
    tablero = []
    for i in range(8):
        tablero.append([' '] * 8)

    return tablero


def esJugadaValida(tablero, baldosa, comienzox, comienzoy):
    # Si es una jugada válida, devuelve una lista de espacios al que el jugador se podría mover.
    if tablero[comienzox][comienzoy] != ' ' or not estaEnTablero(comienzox, comienzoy):
        return False

    tablero[comienzox][comienzoy] = baldosa # establece temporalmente la baldosa en el tablero.

    if baldosa == 'X':
        otraBaldosa = 'O'
    else:
        otraBaldosa = 'X'

    baldosasAGirar = []
    for direccionx, direcciony in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = comienzox, comienzoy
        x += direccionx # primer paso en la dirección
        y += direcciony # primer paso en la dirección
        if estaEnTablero(x, y) and tablero[x][y] == otraBaldosa:
            # Hay una piza perteneciente al otro jugador al lado de nustra pieza
            x += direccionx
            y += direcciony
            if not estaEnTablero(x, y):
                continue
            while tablero[x][y] == otraBaldosa:
                x += direccionx
                y += direcciony
                if not estaEnTablero(x, y): # rompe el ciclo while y continua en el ciclo for.
                    break
            if not estaEnTablero(x, y):
                continue
            if tablero[x][y] == baldosa:
                # Hay piezas a girar. Ve en aquella dirección hasta que lleguemos al espacio original, observando todas las baldosas.
                while True:
                    x -= direccionx
                    y -= direcciony
                    if x == comienzox and y == comienzoy:
                        break
                    baldosasAGirar.append([x, y])

    tablero[comienzox][comienzoy] = ' ' # Restaura el espacio vacio.
    if len(baldosasAGirar) == 0: # Si ninguna baldosa fue girada, no fue una jugada válida.
        return False
    return baldosasAGirar


def estaEnTablero(x, y):
    # Devuelve True si las coordenadas se encuentran dentro del tablero
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def obtenerTableroConJugadasValidas(tablero, baldosa):
    # Devuelve un nuevo tablero, marcando las jugadas válidas que el jugador puede realizar.
    dupTablero = obtenerCopiaTablero(tablero)

    for x, y in obtenerJugadasValidas(dupTablero, baldosa):
        dupTablero[x][y] = '.'
    return dupTablero


def obtenerJugadasValidas(tablero, baldosa):
    # Devuelve una lista de [x,y] listas de jugadas válidas para el jugador en el tablero dado.
    jugadasValidas = []

    for x in range(8):
        for y in range(8):
            if esJugadaValida(tablero, baldosa, x, y) != False:
                jugadasValidas.append([x, y])
    return jugadasValidas


def obtenerPuntajeTablero(tablero):
    # Determina el puntaje contando las baldosas. Devuelve un diccionario con las claves 'X' y 'O'.
    puntajex = 0
    puntajeo = 0
    for x in range(8):
        for y in range(8):
            if tablero[x][y] == 'X':
                puntajex += 1
            if tablero[x][y] == 'O':
                puntajeo += 1
    return {'X':puntajex, 'O':puntajeo}


def ingresarBalsodaJugador():
    # Permite al jugador elegir que baldosa desea ser.
    # Devuelve una lista con la baldosa del jugador como primer elemento y el de la computadora como segundo.
    baldosa = ''
    while not (baldosa == 'X' or baldosa == 'O'):
        print('¿Deseas ser X u O?')
        baldosa = input().upper()

    #  El primer elemento en la lista es la baldosa del juegador, la segunda la de la computadora.
    if baldosa == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def quienComienza():
    # Elije al azar que jugador comienza.
    if random.randint(0, 1) == 0:
        return 'computadora'
    else:
        return 'jugador'


def volverAJugar():
    # Esta funcion devuelve True si el jugador desea volver a jugar, de lo contrario False.
    print('¿Deseas volver a jugar? (si o no)')
    return input().lower().startswith('s')


def hacerJugada(tablero, baldosa, comienzox, comienzoy):
    # Posiciona la baldosa en el tablero en comienzox, comienzoy y gira cualquiera de las pizas del oponente.
    # Returns False if this is an invalid jugada, True if it is valid.
    baldosasAGirar = esJugadaValida(tablero, baldosa, comienzox, comienzoy)

    if baldosasAGirar == False:
        return False

    tablero[comienzox][comienzoy] = baldosa
    for x, y in baldosasAGirar:
        tablero[x][y] = baldosa
    return True


def obtenerCopiaTablero(tablero):
    # Duplica la lista del tablero y devuelve el duplicado.
    dupTablero = obtenerNuevoTablero()

    for x in range(8):
        for y in range(8):
            dupTablero[x][y] = tablero[x][y]

    return dupTablero


def esEsquina(x, y):
    # Devuelve True si la posicion es una de las esquinas.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def obtenerJugadaJugador(tablero, baldosaJugador):
    # Permite al jugador tipear su jugada.
    # Revuelve una jugada como [x,y] (o devuelve las palabras 'pistas' o 'quitar')
    DIGITOS1A8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingresa tu jugada, quitar para terminar el juego, o pistas para activar/desactivar pistas.')
        jugada = input().lower()
        if jugada == 'quitar':
            return 'quitar'
        if jugada == 'pistas':
            return 'pistas'

        if len(jugada) == 2 and jugada[0] in DIGITOS1A8 and jugada[1] in DIGITOS1A8:
            x = int(jugada[0]) - 1
            y = int(jugada[1]) - 1
            if esJugadaValida(tablero, baldosaJugador, x, y) == False:
                continue
            else:
                break
        else:
            print('Esta no es una jugada válida. Presiona el digito x (1-8), luego el digoto y (1-8).')
            print('Por ejemplo, 81 será la esquina superior derecha.')

    return [x, y]


def obtenerJugadaComputadora(tablero, baldosaComputadora):
    # Dado un tablero y la bandosa de la computadora, determinar donde
    # realizar la jugada y devuelve esa jugada como una lista [x,y].
    jugadasPosibles = obtenerJugadasValidas(tablero, baldosaComputadora)

    # ordena al azar el orden de las jugadas posibles
    random.shuffle(jugadasPosibles)

    # siempre elegir una esquina de estar disponible.
    for x, y in jugadasPosibles:
        if esEsquina(x, y):
            return [x, y]

    # Recorrer todas las jugadas posibles y elegir la de mejor puntaje.
    puntajeMaximo = -1
    for x, y in jugadasPosibles:
        dupTablero = obtenerCopiaTablero(tablero)
        hacerJugada(dupTablero, baldosaComputadora, x, y)
        puntaje = obtenerPuntajeTablero(dupTablero)[baldosaComputadora]
        if puntaje > puntajeMaximo:
            mejorJugada = [x, y]
            puntajeMaximo = puntaje
    return mejorJugada


def mostrarPuntajes(baldosaJugador, baldosaComputadora):
    # Imprime en pantalla el mejor puntaje.
    puntajes = obtenerPuntajeTablero(tableroPrincipal)
    print('Tienes %s puntos. La computadora tiene %s puntos.' % (puntajes[baldosaJugador], puntajes[baldosaComputadora]))



print('¡Bienvenido a Reversi!')

while True:
    # Resetea el tablero y el juego.
    tableroPrincipal = obtenerNuevoTablero()
    blanquearTablero(tableroPrincipal)
    if quienComienza() == 'player':
        turno = 'X'
    else:
         turno = 'O'
    print("La" + turno + ' irá primero.')

    while True:
         dibujarTablero(tableroPrincipal)
         puntajes = obtenerPuntajeTablero(tableroPrincipal)
         print('X tiene %s puntos. O tiene %s puntos' % (puntajes['X'], puntajes['O']))
         input('Presiona Enter para continuar.')

         if turno == 'X':
              # Turno de X.
              otraBaldosa = 'O'
              x, y = obtenerJugadaComputadora(tableroPrincipal, 'X')
              hacerJugada(tableroPrincipal, 'X', x, y)
         else:
              # Turno de O.
              otraBaldosa = 'X'
              x, y = obtenerJugadaComputadora(tableroPrincipal, 'O')
              hacerJugada(tableroPrincipal, 'O', x, y)

         if obtenerJugadasValidas(tableroPrincipal, otraBaldosa) == []:
              break
         else:
              turno = otraBaldosa

    # Muestra el puntaje final.
    dibujarTablero(tableroPrincipal)
    puntajes = obtenerPuntajeTablero(tableroPrincipal)
    print('X obtuvo %s puntos. O obtuvo %s puntos.' % (puntajes['X'], puntajes['O']))

    if not volverAJugar():
         sys.exit()
