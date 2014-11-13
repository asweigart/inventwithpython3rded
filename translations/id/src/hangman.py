import random
HANGMANPICS = ['''

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
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra semut babon musang kelelawar beruang unta kucing kerang kobra gagak anjing rusa bebek keledai elang musang rubah katak kambing angsa elang singa kadal monyet keledai tikus hiu kadal panda beo merpati piton kelinci tikus gagak badak salmon domba sigung kukang ular bangau angsa harimau kodok kalkun penyu musang paus serigala zebra'.split() # juga mengandung hewan dalam bahasa indonesia (satu suku kata)

def getRandomWord(wordList):
    # Fungsi ini mengembalikan satu string acak dari daftar string dalam list yang dilemparkan.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Huruf yang salah tebak:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # ganti garis dengan huruf yang ditebak dengan tepat
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # tampilkan kata rahasia dengan huruf-huruf yang dipisahkan satu spasi
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Mengembalikan huruf yang dimasukkan pemain. Fungsi ini memastika pemain memasukkan satu huruf, bukan string lainnya.
    while True:
        print('Tebak satu huruf.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Kamu sudah menebak huruf itu. Pilih lagi.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Masukkan huruf alfabet.')
        else:
            return guess

def playAgain():
    # Fungsi ini mengembalikan True jika pemain ingin bermain lagi, jika tidak maka False yang dikembalikan.
    print('Kamu mau main lagi? (ya or tidak)')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Ambil masukan satu huruf dari pemain.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Cek apakah pemain sudah menang
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Ya! Kata rahasia itu adalah "' + secretWord + '"! Kamu menang!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Cek apakah pemain sudah coba menebak terlalu banyak dan kalah
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('Kamu sudah tidak bisa menebak lagi!\nSetelah salah menebak ' + str(len(missedLetters)) + ' kali dan ' + str(len(correctLetters)) + ' tebakan yang tepat, kata itu adalah "' + secretWord + '"')
            gameIsDone = True

    # Tanya apakah pemain ingin main lagi (tapi, hanya jika game sudah selesai).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
