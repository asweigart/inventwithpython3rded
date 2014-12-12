import random
import time

def zeigeEinfuehrungAn():
    print('Du bist ein einem Land voller Drachen. Vor Dir')
    print('siehst Du zwei Höhlen. In einer Höhle haust ein freundlicher Drache,')
    print('der seine Schätze mit Dir teilt. Der andere Drache')
    print('ist gierig und hungrig, und wird Dich bei Sichtkontakt auffressen.')
    print()

def sucheHoehleAus():
    hoehle = ''
    while hoehle != '1' and hoehle != '2':
        print('In welche Höhle wirst Du gehen? (1 oder 2)')
        hoehle = input()

    return hoehle

def ueberpruefeHoehle(ausgewaehlteHoehle):
    print('Du näherst Dich der Höhle...')
    time.sleep(2)
    print('Es ist dunkel und gruselig...')
    time.sleep(2)
    print('Ein großer Drache spring vor Deine Füße! Er öffnet sein Maul und...')
    print()
    time.sleep(2)

    freundlicheHoehle = random.randint(1, 2)

    if ausgewaehlteHoehle == str(freundlicheHoehle):
         print('Gibt Dir seinen Schatz!')
    else:
         print('Verschlingt Dich in einem Mal!')

spieleNochEinmal = 'ja'
while spieleNochEinmal == 'ja' or spieleNochEinmal == 'j':

    zeigeEinfuehrungAn()

    hoehlenNummer = sucheHoehleAus()

    ueberpruefeHoehle(hoehlenNummer)

    print('Möchtest Du noch einmal spielen? (ja oder nein)')
    spieleNochEinmal = input()
