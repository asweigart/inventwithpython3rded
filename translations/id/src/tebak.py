# Ini adalah game tebak angka.
import random

guessesTaken = 0

print('Halo! Siapa namamu?')
myName = input()

number = random.randint(1, 20)
print('Eh, ' + myName + ', Aku lagi berpikir angka antara 1 dan 20.')

while guessesTaken < 6:
    print('Coba tebak.') # Ada empat spasi di depan print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Tebakanmu terlalu rendah.') # Ada delapan spasi didepan print.

    if guess > number:
        print('Tebakanmu terlalu tinggi.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Hebat, ' + myName + '! Kamu menebak angkaku dalam ' + guessesTaken + ' tebakan!')

if guess != number:
    number = str(number)
    print('Sayang sekali. Angka yang aku pikirkan adalah ' + number)
