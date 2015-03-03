# Tic Tac Toe

import random

def zeichneSpielfeld(spielfeld):
    # Diese Funktion zeichnet das Spielfeld, das ihr übergeben wurde.

    # "spielfeld" ist eine Liste von 10 Zeichenketten, die das Spielfeld repräsentieren (Index 0 wird ignoriert)
    print('   |   |')
    print(' ' + spielfeld[7] + ' | ' + spielfeld[8] + ' | ' + spielfeld[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + spielfeld[4] + ' | ' + spielfeld[5] + ' | ' + spielfeld[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + spielfeld[1] + ' | ' + spielfeld[2] + ' | ' + spielfeld[3])
    print('   |   |')

def gibSpielersymbolEin():
    # Lässt den Spieler eingeben, ob er als X oder als O spielen will.
    # Gibt eine Liste zurück, die als erstes Element das Spielersymbol enthält und als zweites Element das Symbol für den Computergegner.
    buchstabe = ''
    while not (buchstabe == 'X' or buchstabe == 'O'):
        print('Möchtest du als X oder als O spielen?')
        buchstabe = input().upper()

    # Das erste Element in der Liste ist das Symbol des Spielers, das zweite ist das Symbol des Computergegners.
    if buchstabe == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def werFängtAn():
    # Wähle zufällig den Startspieler aus.
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Spieler'

def nochmalSpielen():
    # Diese Funktion gibt True zurück, wenn der Spieler nochmal spielen will. Wenn nicht, gibt sie False zurück.
    print('Möchtest du nochmal spielen? (ja oder nein)')
    return input().lower().startswith('j')

def macheEinenZug(spielfeld, symbol, zug):
    spielfeld[zug] = symbol

def hatGewonnen(feld, sym):
    # Diese Funktion überprüft, ob der Spieler mit dem übergebenen Symbol auf dem übergebenen Spielfeld gewonnen hat und gibt True zurück, falls das der Fall ist.
    # Wir benutzen feld statt spielfeld und sym statt symbol, damit wir nicht so viel tippen müssen.
    return ((feld[7] == sym and feld[8] == sym and feld[9] == sym) or # obere Zeile
    (feld[4] == sym and feld[5] == sym and feld[6] == sym) or # mittlere Zeile
    (feld[1] == sym and feld[2] == sym and feld[3] == sym) or # untere Zeile
    (feld[7] == sym and feld[4] == sym and feld[1] == sym) or # die linke Seite hinunter
    (feld[8] == sym and feld[5] == sym and feld[2] == sym) or # die Mitte hinunter
    (feld[9] == sym and feld[6] == sym and feld[3] == sym) or # die rechte Seite hinunter
    (feld[7] == sym and feld[5] == sym and feld[3] == sym) or # diagonal
    (feld[9] == sym and feld[5] == sym and feld[1] == sym)) # diagonal

def fertigeSpielfeldkopieAn(spielfeld):
    # Fertige eine Kopie des Spielfeldes an und gebe diese Kopie zurück.
    spielfeldKopie = []

    for i in spielfeld:
        spielfeldKopie.append(i)

    return spielfeldKopie

def istKästchenFrei(spielfeld, kästchen):
    # Gibt True zurück, wenn das angegebene Kästchen auf dem angegebenen Spielfeld noch frei ist.
    return spielfeld[kästchen] == ' '

def macheSpielerZug(spielfeld):
    # Lass den Spieler seinen Spielzug eingeben.
    zug = ' '
    while zug not in '1 2 3 4 5 6 7 8 9'.split() or not istKästchenFrei(spielfeld, int(zug)):
        print('Wohin möchtest du setzen? (1-9)')
        zug = input()
    return int(zug)

def wähleZufälligenZugAusListe(spielfeld, zugListe):
    # Wählt einen machbaren Zug für das mitgegebene Spielfeld aus der mitgegebenen Liste aus und gibt ihn zurück.
    # Gibt nichts (None) zurück, wenn es kein Zug gemacht werden kann.
    möglicheZüge = []
    for i in zugListe:
        if istKästchenFrei(spielfeld, i):
            möglicheZüge.append(i)

    if len(möglicheZüge) != 0:
        return random.choice(möglicheZüge)
    else:
        return None

def macheComputerZug(spielfeld, computerSymbol):
    # Ermittle für das mitgegebene Spielfeld einen Zug für den Computergegner und gebe diesen zurück.
    if computerSymbol == 'X':
        spielerSymbol = 'O'
    else:
        spielerSymbol = 'X'

    # Dies ist der Algorithmus für unsere Tic Tac Toe-KI:
    # Prüfe zu erst, ob das Spiel mit dem nächsten Zug gewonnen werden kann
    for i in range(1, 10):
        kopie = fertigeSpielfeldkopieAn(spielfeld)
        if istKästchenFrei(kopie, i):
            macheEinenZug(kopie, computerSymbol, i)
            if hatGewonnen(kopie, computerSymbol):
                return i

    # Prüfe ob der menschliche Spieler im nächsten Zug gewinnen könnte und blocke ihn.
    for i in range(1, 10):
        kopie = fertigeSpielfeldkopieAn(spielfeld)
        if istKästchenFrei(kopie, i):
            macheEinenZug(kopie, spielerSymbol, i)
            if hatGewonnen(kopie, spielerSymbol):
                return i

    # Versuche eine der Ecken zu übernehmen, falls diese noch frei sind.
    zug = wähleZufälligenZugAusListe(spielfeld, [1, 3, 7, 9])
    if zug != None:
        return zug

    # Setze auf das mittlere Feld, falls es noch frei ist.
    if istKästchenFrei(spielfeld, 5):
        return 5

    # Setze auf eines der Seitenfelder.
    return wähleZufälligenZugAusListe(spielfeld, [2, 4, 6, 8])

def istSpielfeldVoll(spielfeld):
    # Gibt True zurück, wenn alle Felder auf dem Spielfeld gesetzt wurden. Gibt False zurück, wenn dies nicht der Fall ist.
    for i in range(1, 10):
        if istKästchenFrei(spielfeld, i):
            return False
    return True


print('Willkommen bei Tic Tac Toe!')

while True:
    # Setze das Spielfeld zurück
    dasSpielfeld = [' '] * 10
    spielerSymbol, computerSymbol = gibSpielersymbolEin()
    amZug = werFängtAn()
    print('Der ' + amZug + ' fängt an.')
    spielLäuft = True

    while spielLäuft:
        if amZug == 'Spieler':
            # Der menschliche Spieler ist dran.
            zeichneSpielfeld(dasSpielfeld)
            zug = macheSpielerZug(dasSpielfeld)
            macheEinenZug(dasSpielfeld, spielerSymbol, zug)

            if hatGewonnen(dasSpielfeld, spielerSymbol):
                zeichneSpielfeld(dasSpielfeld)
                print('Hurra! Du hast das Spiel gewonnen!')
                spielLäuft = False
            else:
                if istSpielfeldVoll(dasSpielfeld):
                    zeichneSpielfeld(dasSpielfeld)
                    print('Das Spiel endet mit einem Unentschieden!')
                    break
                else:
                    amZug = 'Computer'

        else:
            # Der Computergegner ist dran.
            zug = macheComputerZug(dasSpielfeld, computerSymbol)
            macheEinenZug(dasSpielfeld, computerSymbol, zug)

            if hatGewonnen(dasSpielfeld, computerSymbol):
                zeichneSpielfeld(dasSpielfeld)
                print('Der Computergegner hat dich besiegt! Du hast verloren.')
                spielLäuft = False
            else:
                if istSpielfeldVoll(dasSpielfeld):
                    zeichneSpielfeld(dasSpielfeld)
                    print('Das Spiel endet mit einem Unentschieden!')
                    break
                else:
                    amZug = 'Spieler'

    if not nochmalSpielen():
        break
