import random
print('Akan kulemparkan sebuah koin 1000 kali. Tebak berapa kali muncul kepala. (Tekan ENTER untuk memulai)')
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0, 1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print('900 lembaran dan sudah muncul kepala sebanyak ' + str(heads) + ' kali.')
    if flips == 100:
        print('Setelah lemparan 100, kepala muncul ' + str(heads) + ' kali.')
    if flips == 500:
        print('Baru setengah perjalanan dan kepala telah muncul ' + str(heads) + ' kali.')

print()
print('Setelah 1000 kali lemparan koin, kepala muncul ' + str(heads) + ' kali!')
print('Apa tebakanmu dekat?')


























