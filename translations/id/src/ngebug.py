import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('Berapa ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if answer == number1 + number2:
    print('Tepat!')
else:
    print('Bukan! Jawabannya adalah ' + str(number1 + number2))
