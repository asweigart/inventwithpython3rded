import random
imágenesVerdugo = ['''

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
words = 'hormiga babuino tejón murciélago oso castor camello gato almeja cobra puma coyote cuervo ciervo perro burro pato águila hurón zorro rana cabra ganso halcón león lagarto llama topo mono alce ratón mula tritón nutria búho panda loro paloma pitón conejo carnero rata cuervo rinoceronte salmón sello tiburón oveja mofeta pereza serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

def obtenerPalabraAzar(wordList):
    # This function returns a random string from the passed list of strings.
    índicePalabra = random.randint(0, len(wordList) - 1)
    return wordList[índicePalabra]

def mostrarLaJunta(imágenesVerdugo, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(imágenesVerdugo[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): # replace espaciosVacíos with correctly guessed letters
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos: # show the secret word with spaces in between each letter
        print(letra, end=' ')
    print()

def obtenerLaConjetura(alreadyGuessed):
    # Devuelve la carta el jugador entró. Esta función hace que el jugador entró en una sola letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Por favor, introduzca una sola letra.')
        elif guess in alreadyGuessed:
            print('Ya has adivinado que letra. Volver a elegir.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor entre en una LETRA.')
        else:
            return guess

def juegueOtraVez():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('¿Quiere jugar otra vez? (sí o no)')
    return input().lower().startswith('s')


print('V E R D U G O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(words)
juegoTerminó = False

while True:
    mostrarLaJunta(imágenesVerdugo, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Dejar que el jugador escribe en una letra.
    guess = obtenerLaConjetura(letrasIncorrectas + letrasCorrectas)

    if guess in palabraSecreta:
        letrasCorrectas = letrasCorrectas + guess

        # Verificar si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('Yes! The secret word is "' + palabraSecreta + '"! You have won!')
            juegoTerminó = True
    else:
        letrasIncorrectas = letrasIncorrectas + guess

        # Comprobar si el jugador ha conjeturado demasiadas veces y perdido.
        if len(letrasIncorrectas) == len(imágenesVerdugo) - 1:
            mostrarLaJunta(imágenesVerdugo, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('You have run out of guesses!\nAfter ' + str(len(letrasIncorrectas)) + ' missed guesses and ' + str(len(letrasCorrectas)) + ' correct guesses, the word was "' + palabraSecreta + '"')
            juegoTerminó = True

    # Preguntar al jugador si quieren volver a jugar (pero sólo si se realiza el juego).
    if juegoTerminó:
        if juegueOtraVez():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminó = False
            palabraSecreta = obtenerPalabraAlAzar(words)
        else:
            break
