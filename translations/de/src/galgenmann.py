import random
GALGENMANNBILDER = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
worte = 'aal adler alligator ameise amsel bär biber bussard chamäleon dachs delfin eichhörnchen eidechse elch elefant faultier fledermaus fuchs gans gepard gorilla hai hamster hase hirsch huhn igel jaguar kamel känguru koala leopard libelle marienkäfer maulwurf meerschweinchen möwe nachtigal nilpferd panda pfau qualle ratte regenwurm schaf schimpanse schwan schwein strauß tausendfüßer tintenfisch wachtel wal wolf zebra ziege'.split()

def zufallsWort(wortListe):
    # Diese Funktion gibt eine zufällige Zeichenkette aus der übergebenen Zeichenketten-Liste zurück.
    wortIndex = random.randint(0, len(wortListe) - 1)
    return wortListe[wortIndex]

def zeigeSpielbrettAn(GALGENMANNBILDER, falscheBuchstaben, richtigeBuchstaben, geheimWort):
    print(GALGENMANNBILDER[len(falscheBuchstaben)])
    print()

    print('Falsche Buchstaben:', end=' ')
    for buchstabe in falscheBuchstaben:
        print(buchstabe, end=' ')
    print()

    luecken = '_' * len(geheimWort)

    for i in range(len(geheimWort)): # Ersetze Lücken mit korrekt geratenen Buchstaben
        if geheimWort[i] in richtigeBuchstaben:
            luecken = luecken[:i] + geheimWort[i] + luecken[i+1:]

    for buchstabe in luecken: # Zeige das Geheimwort mit Leerzeichen zwischen den Buchstaben
        print(buchstabe, end=' ')
    print()

def rateBuchstabe(bereitsGeraten):
    # Stellt sicher, dass der Spieler nur einen einzelnen Buchstaben eintippt und gibt ihn zurück.
    while True:
        print('Rate einen Buchstaben.')
        eingabe = input()
        eingabe = eingabe.lower()
        if len(eingabe) != 1:
            print('Bitte gib einen einzelnen Buchstaben ein.')
        elif eingabe in bereitsGeraten:
            print('Du hast diesen Buchstaben bereits probiert. Rate noch einmal.')
        elif eingabe not in 'abcdefghijklmnopqrstuvwxyz':
            print('Bitte gib einen BUCHSTABEN ein.')
        else:
            return eingabe

def spieleNochEinmal():
    # Diese Funktion True zurück, falls der Spieler noch einmal spielen möchte, False sonst.
    print('Möchtest Du noch einmal spielen? (ja oder nein)')
    return input().lower().startswith('j')


print('G A L G E N M A N N')
falscheBuchstaben = ''
richtigeBuchstaben = ''
geheimWort = zufallsWort(worte)
spielIstBeendet = False

while True:
    zeigeSpielbrettAn(GALGENMANNBILDER, falscheBuchstaben, richtigeBuchstaben, geheimWort)

    # Lass den Spieler einen Buchhstaben eingeben.
    buchstabe = rateBuchstabe(falscheBuchstaben + richtigeBuchstaben)

    if buchstabe in geheimWort:
        richtigeBuchstaben = richtigeBuchstaben + buchstabe

        # Überprüfe, ob der Spieler gewonnen hat
        alleBuchstabenGeraten = True
        for i in range(len(geheimWort)):
            if geheimWort[i] not in richtigeBuchstaben:
                alleBuchstabenGeraten = False
                break
        if alleBuchstabenGeraten:
            print('Ja! Das geheime Wort ist "' + geheimWort + '"! Du hast gewonnen!')
            spielIstBeendet = True
    else:
        falscheBuchstaben = falscheBuchstaben + buchstabe

        # Überprüfe, ob der Spieler zu viele Rateversuche verbraucht und damit verloren hat
        if len(falscheBuchstaben) == len(GALGENMANNBILDER) - 1:
            zeigeSpielbrettAn(GALGENMANNBILDER, falscheBuchstaben, richtigeBuchstaben, geheimWort)
            print('Du hast zu viele Versuche gebraucht!\nNach ' + str(len(falscheBuchstaben)) + ' falsch und ' + str(len(richtigeBuchstaben)) + ' richtig geratenen Buchstaben lautet das Wort "' + geheimWort + '"')
            spielIstBeendet = True

    # Frage den Spieler, ob er noch einmal spielen möchte (aber nur, wenn das Spiel zu Ende ist).
    if spielIstBeendet:
        if spieleNochEinmal():
            falscheBuchstaben = ''
            richtigeBuchstaben = ''
            spielIstBeendet = False
            geheimWort = zufallsWort(worte)
        else:
            break
