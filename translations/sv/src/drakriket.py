import random
import time

def visaIntro():
    print('Du befinner dig i ett land fullt av drakar. Framför dig')
    print('ser du två grottor. I en av grottorna bor en snäll drake')
    print('som kommer att dela sin skatt med dig. Den andra draken')
    print('är girig och hungrig, och kommer att äta upp dig på fläcken.')
    print()

def väljGrotta():
    grotta = ''
    while grotta != '1' and grotta != '2':
        print('Vilken grotta går du in i? (1 eller 2)')
        grotta = input()

    return grotta

def kollaGrotta(valdGrotta):
    print('Du närmar dig grottan...')
    time.sleep(2)
    print('Det är mörkt och kusligt...')
    time.sleep(2)
    print('En stor drake hoppar ut framför dig! Han öppnar sina käftar och...')
    print()
    time.sleep(2)

    snällGrotta = random.randint(1, 2)

    if valdGrotta == str(snällGrotta):
         print('Ger dig sin skatt!')
    else:
         print('Slukar dig hel!')

spelaIgen = 'ja'
while spelaIgen == 'ja' or spelaIgen == 'j':

    visaIntro()

    grottnummer = väljGrotta()

    kollaGrotta(grottnummer)

    print('Vill du spela igen? (ja eller nej)')
    spelaIgen = input()
