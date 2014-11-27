# Sandi Caesar

MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('Apa kamu ingin mengenkripsi atau mendekripsi suatu pesan?')
        mode = input().lower()
        if mode in 'enkripsi e dekripsi d'.split():
            return mode
        else:
            print('Masukkan "enkripsi" atau "e" atau "dekripsi" atau "d".')

def getMessage():
    print('Masukkan pesanmu:')
    return input()

def getKey():
    key = 0
    while True:
        print('Masukkan bilangan kunci (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

mode = getMode()
message = getMessage()
key = getKey()

print('Pesan hasil pergeserannya adalah:')
print(getTranslatedMessage(mode, message, key))
