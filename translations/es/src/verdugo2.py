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
palabras = {'Colores':'rojo naranja amarillo verde azul añil violeta blanco negro marrón'.split(),
'Formas':'cuadrado triángulo rectángulo círculo elipse rombo trapazoid galón pentágono hexágono heptágono octogon'.split(),
'Frutas':'manzana naranja limón pera sandía pomelo cereza cantalope plátano fresa tomate'.split(),
'Animales':'murciélago oso castor gato puma cangrejo ciervos perro burro pato águila peces ranas cabra sanguijuela león lagarto mono alces el ratón la nutria el búho panda pitón conejo rata tiburones ovejas mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

def obtenerPalabraAzar(diccionarioPalabra):
    # This function returns a random string from the passed dictionary of lists of strings, and the key also.
    # First, randomly select a key from the dictionary:
    palabrasClave = random.choice(list(diccionarioPalabra.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    índicePalabra = random.randint(0, len(diccionarioPalabra[palabrasClave]) - 1)

    return [diccionarioPalabra[palabrasClave][índicePalabra], palabrasClave]


def mostrarLaJunta(imágenesVerdugo, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(imágenesVerdugo[len(letrasIncorrectas)])
    print()

    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()

    espaciosVacíos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)): # Reemplace espaciosVacíos con letras adivinadas correctamente.
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + palabraSecreta[i] + espaciosVacíos[i+1:]

    for letra in espaciosVacíos: # Mostrar la palabra secreta con espacios entre cada letra.
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
    # Esta función devuelve True si el jugador quiere volver a jugar, de lo contrario, devuelve False.
    print('¿Quiere jugar otra vez? (sí o no)')
    return input().lower().startswith('s')


print('V E R D U G O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta, claveSecreta = obtenerPalabraAzar(palabras)
juegoTerminó = False

while True:
    print('La palabra secreta es en la categoría: ' + palabrasSecreta)
    mostrarLaJunta(imágenesVerdugo, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Dejar que el jugador escribe en una letra.
    conjetura = obtenerLaConjetura(letrasIncorrectas + letrasCorrectas)

    if conjetura in palabraSecreta:
        letrasCorrectas = letrasCorrectas + conjetura

        # Verificar si el jugador ha ganado.
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
        if encontradoTodasLasLetras:
            print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
            juegoTerminó = True
    else:
        letrasIncorrectas = letrasIncorrectas + conjetura

        # Comprobar si el jugador ha conjeturado demasiadas veces y perdido.
        if len(letrasIncorrectas) == len(imágenesVerdugo) - 1:
            mostrarLaJunta(imágenesVerdugo, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print('¡Usted ha quedado sin conjeturas!\nDespués de ' + str(len(letrasIncorrectas)) + ' conjeturas perdidas y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
            juegoTerminó = True

    # Preguntar al jugador si quieren volver a jugar (pero sólo si se realiza el juego).
    if juegoTerminó:
        if juegueOtraVez():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminó = False
            palabraSecreta = obtenerPalabraAzar(words)
        else:
            break
