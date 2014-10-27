# Reversi

import random
import sys

def dibujarTablero(tablero):
    # This function prints out the board that it was passed. Returns None.
    LINEAHORIZONTAL = ' +--------+'
    print('  12345678')
    print(LINEAHORIZONTAL)
    for y in range(8):
        print('%s|' % (y+1), end='')
        for x in range(8):
            print(tablero[x][y], end='')
        print('|')
    print(LINEAHORIZONTAL)


def reiniciarTablero(tablero):
    # Deja en blanco el tablero recibido como argumento, excepto la posición inicial
    for x in range(8):
        for y in range(8):
            tablero[x][y] = ' '

    # Fichas iniciales:
    tablero[3][3] = 'X'
    tablero[3][4] = 'O'
    tablero[4][3] = 'O'
    tablero[4][4] = 'X'


def obtenerNuevoTablero():
    # Crea una estructura de datos de tablero completamente nueva y vacía.
    tablero = []
    for i in range(8):
        tablero.append([' '] * 8)

    return tablero


def esMovidaVálida(tablero, ficha, xinicio, yinicio):
    # Devuelve Falso si la movida del jugador en el casillero xinicio, yinicio is inválida.
    # Si es una movida válida, devuelve una lista de espacios que pasarían a ser del jugador si moviera aquí.
    if tablero[xinicio][yinicio] != ' ' or not perteneceAlTablero(xinicio, yinicio):
        return False

    tablero[xinicio][yinicio] = ficha # temporariamente colocar la ficha sobre el tablero.

    if ficha == 'X':
        otraFicha = 'O'
    else:
        otraFicha = 'X'

    fichasAVoltear = []
    for xdirección, ydirección in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xinicio, yinicio
        x += xdirección # primer paso en la dirección
        y += ydirección # primer paso en la dirección
        if perteneceAlTablero(x, y) and tablero[x][y] == otraFicha:
            # Hay una ficha perteneciente al otro jugador al lado de nuestra ficha.
            x += xdirección
            y += ydirección
            if not perteneceAlTablero(x, y):
                continue
            while tablero[x][y] == otraFicha:
                x += xdirección
                y += ydirección
                if not perteneceAlTablero(x, y): # salir del bucle while, luego continuar en el bucle for
                    break
            if not perteneceAlTablero(x, y):
                continue
            if tablero[x][y] == ficha:
                # Hay fichas para dar vuelta. Caminar en dirección opuesta hasta llegar al casillero original, registrando todas las posiciones en el camino.
                while True:
                    x -= xdirección
                    y -= ydirección
                    if x == xinicio and y == yinicio:
                        break
                    fichasAVoltear.append([x, y])

    tablero[xinicio][yinicio] = ' ' # restablecer el espacio vacío
    if len(fichasAVoltear) == 0: # Si no se volteó ninguna ficha, la movida no es válida.
        return False
    return fichasAVoltear


def perteneceAlTablero(x, y):
    # Devuelve True si las coordenadas pertenecen al tablero.
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def obtenerTableroConMovidasVálidas(tablero, ficha):
    # Devuelve un nuevo tablero con "." indicando las movidas válidos que el jugador tiene disponibles.
    réplicaTablero = obtenerCopiaTablero(tablero)

    for x, y in obtenerMovidasVálidas(réplicaTablero, ficha):
        réplicaTablero[x][y] = '.'
    return réplicaTablero


def obtenerMovidasVálidas(tablero, ficha):
    # Devuelve una lista de listas [x,y] de movidas válidas para el jugador dado en el tablero dado.
    movidasVálidas = []

    for x in range(8):
        for y in range(8):
            if esMovidaVálida(tablero, ficha, x, y) != False:
                movidasVálidas.append([x, y])
    return movidasVálidas


def obtenerPuntajeTablero(tablero):
    # Determina el puntaje contando las fichas. Devuelve un diccionario con claves 'X' y 'O'.
    xpuntaje = 0
    opuntaje = 0
    for x in range(8):
        for y in range(8):
            if tablero[x][y] == 'X':
                xpuntaje += 1
            if tablero[x][y] == 'O':
                opuntaje += 1
    return {'X':xpuntaje, 'O':opuntaje}


def ingresarFichaJugador():
    # Permite al jugador elegir qué ficha desea usar.
    # Devuelve una lista con la ficha del jugador como primer ítem, y la ficha de la computadora como segundo.
    ficha = ''
    while not (ficha == 'X' or ficha == 'O'):
        print('Do you want to be X or O?')
        ficha = input().upper()

    # el primer elemento en la lista es la ficha del jugador, el segundo es la ficha de la computadora.
    if ficha == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def quiénComienza():
    # Elige aleatoriamente qué jugador comienza.
    if random.randint(0, 1) == 0:
        return 'computadora'
    else:
        return 'jugador'


def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere jugar de nuevo, de lo contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')


def efectuarMovida(tablero, ficha, xinicio, yinicio):
    # Coloca la ficha sobre el tablero en xstart, ystart, y voltea cualquier ficha del oponente.
    # Devuelve False si la movida es inválida, True si es válida.
    fichasAVoltear = esMovidaVálida(tablero, ficha, xinicio, yinicio)

    if fichasAVoltear == False:
        return False

    tablero[xinicio][yinicio] = ficha
    for x, y in fichasAVoltear:
        tablero[x][y] = ficha
    return True


def obtenerCopiaTablero(tablero):
    # Crea una réplica de la lista asociada al tablero y devuelve la réplica.
    réplicaTablero = obtenerNuevoTablero()

    for x in range(8):
        for y in range(8):
            réplicaTablero[x][y] = tablero[x][y]

    return réplicaTablero


def esUnaEsquina(x, y):
    # Devuelve True si la posición coincide con una de las cuatro esquinas.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def obtenerMovidaJugador(tablero, fichaJugador):
    # Permite al jugador efectuar su movida.
    # Devuelve la movida como [x, y] (o devuelve las cadenas 'pistas' o 'salir')
    CIFRAS1A8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingresa tu movida, o teclea salir para terminar el juego, o pistas para activar/desactivar las pistas.')
        jugada = input().lower()
        if jugada == 'salir':
            return 'salir'
        if jugada == 'pistas':
            return 'pistas'

        if len(jugada) == 2 and jugada[0] in CIFRAS1A8 and jugada[1] in CIFRAS1A8:
            x = int(jugada[0]) - 1
            y = int(jugada[1]) - 1
            if esMovidaVálida(tablero, fichaJugador, x, y) == False:
                continue
            else:
                break
        else:
            print('Esa movida no es válida. Ingresa la coordenada x (1-8), luego la coordenada y (1-8).')
            print('Por ejemplo, 81 corresponde a la esquina superior derecha.')

    return [x, y]


def obtenerMovidaComputadora(tablero, fichaComputadora):
    # Dado un tablero y la ficha de la computadora, determinar dónde
    # mover y devolver esa movida como una lista [x, y].
    movidasPosibles = obtenerMovidasVálidas(tablero, fichaComputadora)

    # ordenar aleatoriamente las movidas posibles
    random.shuffle(movidasPosibles)

    # siempre jugar en una esquina si está disponible.
    for x, y in movidasPosibles:
        if esUnaEsquina(x, y):
            return [x, y]

    # Recorrer la lista de movidas posibles y recordar la movida que da el mejor puntaje
    mejorPuntaje = -1
    for x, y in movidasPosibles:
        réplicaTablero = obtenerCopiaTablero(tablero)
        efectuarMovida(réplicaTablero, fichaComputadora, x, y)
        puntaje = obtenerPuntajeTablero(réplicaTablero)[fichaComputadora]
        if puntaje > mejorPuntaje:
            mejorMovida = [x, y]
            mejorPuntaje = puntaje
    return mejorMovida


def mostrarPuntaje(fichaJugador, fichaComputadora):
    # Imprime el puntaje actual.
    puntajes = obtenerPuntajeTablero(tableroPrincipal)
    print('Tienes %s puntos. La computadora tiene %s puntos.' % (puntajes[fichaJugador], puntajes[fichaComputadora]))



print('¡Bienvenido a Reversi!')

while True:
    # Reiniciar el tablero y el juego.
    tableroPrincipal = obtenerNuevoTablero()
    reiniciarTablero(tableroPrincipal)
    fichaJugador, fichaComputadora = ingresarFichaJugador()
    mostrarPistas = False
    turno = quiénComienza()
    print('The ' + turno + ' will go first.')

    while True:
        if turno == 'jugador':
            # Turno del jugador.
            if mostrarPistas:
                TableroConMovidasVálidas = obtenerTableroConMovidasVálidas(tableroPrincipal, fichaJugador)
                dibujarTablero(TableroConMovidasVálidas)
            else:
                dibujarTablero(tableroPrincipal)
            mostrarPuntaje(fichaJugador, fichaComputadora)
            movida = obtenerMovidaJugador(tableroPrincipal, fichaJugador)
            if movida == 'salir':
                print('¡Gracias por jugar!')
                sys.exit() # salir del programa
            elif movida == 'pistas':
                mostrarPistas = not mostrarPistas
                continue
            else:
                efectuarMovida(tableroPrincipal, fichaJugador, movida[0], movida[1])

            if obtenerMovidasVálidas(tableroPrincipal, fichaComputadora) == []:
                break
            else:
                turno = 'computadora'

        else:
            # Turno de la computadora.
            dibujarTablero(tableroPrincipal)
            mostrarPuntaje(fichaJugador, fichaComputadora)
            input('Teclea Enter para ver la movida de la computadora.')
            x, y = obtenerMovidaComputadora(tableroPrincipal, fichaComputadora)
            efectuarMovida(tableroPrincipal, fichaComputadora, x, y)

            if obtenerMovidasVálidas(tableroPrincipal, fichaJugador) == []:
                break
            else:
                turno = 'jugador'

    # Visualizar el puntaje final.
    dibujarTablero(tableroPrincipal)
    puntajes = obtenerPuntajeTablero(tableroPrincipal)
    print('X ha marcado %s puntos. O ha marcado %s puntos.' % (puntajes['X'], puntajes['O']))
    if puntajes[fichaJugador] > puntajes[fichaComputadora]:
        print('¡Has vencido a la computadora por %s puntos! ¡Felicitaciones!' % (puntajes[fichaJugador] - puntajes[fichaComputadora]))
    elif puntajes[fichaJugador] < puntajes[fichaComputadora]:
        print('Has perdido. La computadora te ha vencido por %s puntos.' % (puntajes[fichaComputadora] - puntajes[fichaJugador]))
    else:
        print('¡Ha sido un empate!')

    if not jugarDeNuevo():
        break
