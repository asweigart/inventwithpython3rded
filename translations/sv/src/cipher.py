# Caesar Cipher

MAX_NYCKEL_STORLEK = 58

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

    alfabet = 'abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ'

    for tecken in meddelande:
        if tecken.isalpha():
            nummer = alfabet.index(tecken)
            nummer += nyckel
            nummer = nummer % len(alfabet)
            tecken = alfabet[nummer]
        översatt += tecken
    return översatt
            

riktning = hämtaRiktning()
meddelande = hämtaMeddelande()
nyckel = hämtaNyckel()

print('Din översatta text är:')
print(hämtaÖversattMeddelande(riktning, meddelande, nyckel))
