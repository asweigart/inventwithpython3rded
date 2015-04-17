import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('Jaki jest wynik ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2:
    print('Bardzo dobrze!')
else:
    print('Niestety! Prawidłowa odpowiedź to ' + str(number1 + number2))
