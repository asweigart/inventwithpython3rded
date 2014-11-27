import random
print('Jag kommer att singla slant 1000 gånger. Gissa hur många gånger det blir krona? (Tryck enter för att börja)')
input()
singlingar = 0
krona = 0
while singlingar < 1000:
    if random.randint(0, 1) == 1:
        krona = krona + 1
    singlingar = singlingar + 1

    if singlingar == 900:
        print('900 singlingar och det har blivit krona ' + str(krona) + ' gånger.')
    if singlingar == 100:
        print('Vid 100 singlingar så har det blivit krona ' + str(krona) + ' gånger.')
    if singlingar == 500:
        print('Halva jobbet gjort och det har blivit krona ' + str(krona) + ' gånger.')

print()
print('Av 1000 slantsinglingar så blev det krona ' + str(krona) + ' gånger!')
print('Var du nära?')



























