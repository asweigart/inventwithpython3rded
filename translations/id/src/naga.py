import random # Tolong namai game ini Alam Naga di chapter 6, jika sudah hapus komentar ini
import time

def displayIntro():
    print('Kamu ada di pulau yang dihuni banyak naga. Di depanmu,')
    print('kamu melihat dua gua. Di salah satu gua dihuni oleh naga ramah')
    print('dan mau berbagi harta karun bersamamu. Naga lain')
    print('tamak dan lapar. Kamu bisa dimakan olehnya jika terlihat')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Gua mana yang ingin kau jelajahi? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('Kamu memasuki gua...')
    time.sleep(2)
    print('Gua ini gelap dan menakutkan...')
    time.sleep(2)
    print('Naga besar lompat didepanmu! Dia membuka mulutnya dan...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
         print('Memberimu harta karunnya!')
    else:
         print('Mengunyahmu dalam satu gigitan!')

playAgain = 'ya'
while playAgain == 'ya' or playAgain == 'y':

    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Mau main lagi? (ya atau tidak)')
    playAgain = input()
