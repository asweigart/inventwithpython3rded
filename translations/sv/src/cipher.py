# Caesar Cipher

MAX_NYCKEL_STORLEK = 26

def hämtaRiktning():
    while True:
        print('Vill du kryptera eller dekryptera ett meddelande?')
        riktning = input().lower()
        if riktning in 'kryptera k dekryptera d'.split():
            return riktning
        else:
            print('Mata in antingen "kryptera", "k", "dekryptera" eller "d"')

def hämtaMeddelande():
    print('Mata in ditt meddelande:')
    return input()

def hämtaNyckel():
    nyckel = 0
    while True:
        print('Mata in nyckel (1-%s)' % (MAX_NYCKEL_STORLEK))
        nyckel = int(input())
        if (nyckel >= 1 and nyckel <= MAX_NYCKEL_STORLEK):
            return nyckel

def hämtaÖversattMeddelande(riktning, meddelande, nyckel):
    if riktning[0] == 'd':
        nyckel = -nyckel
    översatt = ''

    for tecken in meddelande:
        if tecken.isalpha():
            nummer = ord(tecken)
            nummer += nyckel

            if tecken.isupper():
                if nummer > ord('Z'):
                    nummer -= 26
                elif nummer < ord('A'):
                    nummer += 26
            elif tecken.islower():
                if nummer > ord('z'):
                    nummer -= 26
                elif nummer < ord('a'):
                    nummer += 26

            översatt += chr(nummer)
        else:
            översatt += tecken
    return översatt

riktning = hämtaRiktning()
meddelande = hämtaMeddelande()
nyckel = hämtaNyckel()

print('Din översatta text är:')
print(hämtaÖversattMeddelande(riktning, meddelande, nyckel))
