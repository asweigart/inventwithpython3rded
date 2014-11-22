import random
HANGMANBILDER = ['''

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
ord = {'Färger':'röd orange gul grön blå indigo violett vit svart brun'.split(),
'Former':'kvadrat triangel rektangel cirkel ellips romb trapets pentagon hexagon heptagon oktogon'.split(),
'Frukter':'äpple apelsin citron lime päron vattenmelon vindruva grapefrukt körsbär banan nätmelon mango jordgubbe tomat'.split(),
'Djur':'anka apa björn bläckfisk bäver fisk fladdermus igel lejon get groda haj hund får katt kalkon kanin krabba mus puma panda pytonorm rådjur råtta skunk sköldpadda tiger uggla utter vessla val varg vombat zebra älg åsna ödla örn'.split()}

def slumpaOrd(ordbok):
    # Den här funktionen returnerar en slumpmässigt vald sträng från den "uppslagsbok" med ord som skickats in. Även nyckeln returneras.
    # Först slumpas en av nycklarna fram:
    ordnyckel = random.choice(list(ordbok.keys()))

    # Sedan väljs ett av orden ur uppslagsbokens lista för nyckeln:
    ordindex = random.randint(0, len(ordbok[ordnyckel]) - 1)

    return [ordbok[ordnyckel][ordindex], ordnyckel]


def visaBräde(HANGMANBILDER, missar, träffar, hemligtOrd):
    print(HANGMANBILDER[len(missar)])
    print()

    print('Felaktiga bokstäver:', end=' ')
    for bokstav in missar:
        print(bokstav, end=' ')
    print()

    tomrum = '_' * len(hemligtOrd)

    for i in range(len(hemligtOrd)): # ersätt tomrum med korrekt gissade bokstäver
        if hemligtOrd[i] in träffar:
            tomrum = tomrum[:i] + hemligtOrd[i] + tomrum[i+1:]

    for bokstav in tomrum: # visa det hemliga ordet med mellanrum mellan varje bokstav
        print(bokstav, end=' ')
    print()

def hämtaGissning(tidigareGissningar):
    # Returnerar bokstaven som spelaren har matat in. Den här funktionen kontrollerar att spelaren bara har matat in en enda bokstav.
    while True:
        print('Gissa en bokstav.')
        gissning = input()
        gissning = gissning.lower()
        if len(gissning) != 1:
            print('Var snäll och mata in en enda bokstav.')
        elif gissning in tidigareGissningar:
            print('Du har redan gissat på den bokstaven. Gissa igen.')
        elif gissning not in 'abcdefghijklmnopqrstuvwxyzåäö':
            print('Var snäll och mata in en BOKSTAV.')
        else:
            return gissning

def spelaIgen():
    # Den här funktionen returnerar True om spelaren vill spela igen, annars returnerar den False.
    print('Vill du spela igen? (ja eller nej)')
    return input().lower().startswith('j')


print('H A N G M A N')
missar = ''
träffar = ''
hemligtOrd, hemligNyckel = slumpaOrd(ord) 
speletSlut = False

while True:
    print('Det hemliga ordet finns i kategorin: ' + hemligNyckel)
    visaBräde(HANGMANBILDER, missar, träffar, hemligtOrd)

    # Låt spelaren skriva in en bokstav.
    gissning = hämtaGissning(missar + träffar)

    if gissning in hemligtOrd:
        träffar = träffar + gissning

        # Kolla om spelaren har vunnit
        hittatAllaBokstäver = True
        for i in range(len(hemligtOrd)):
            if hemligtOrd[i] not in träffar:
                hittatAllaBokstäver = False
                break
        if hittatAllaBokstäver:
            print('Ja! Det hemliga ordet var "' + hemligtOrd + '"! Du har vunnit!')
            speletSlut = True
    else:
        missar = missar + gissning

        # Kolla om spelaren har gissat för många gånger och förlorat
        if len(missar) == len(HANGMANBILDER) - 1:
            visaBräde(HANGMANBILDER, missar, träffar, hemligtOrd)
            print('Du har slut på gissningar!\nEfter ' + str(len(missar)) + ' felaktiga gissningar och ' + str(len(träffar)) + ' korrekta gissningar, kan jag avslöja att ordet var "' + hemligtOrd + '"')
            speletSlut = True

    # Fråga om spelaren vill spela igen (men bara om spelet är slut).
    if speletSlut:
        if spelaIgen():
            missar = ''
            träffar = ''
            speletSlut = False
            hemligtOrd, hemligNyckel = slumpaOrd(ord)
        else:
            break
