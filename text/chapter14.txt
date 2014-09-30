Chapter 14 - Caesar Cipher

Topics Covered In This Chapter:

Cryptography and ciphers
Encrypting and decrypting
Ciphertext, plaintext, keys, and symbols
The Caesar Cipher
ASCII ordinal values
The chr() and ord() functions
The isalpha() string method
The isupper() and islower() string methods
Cryptanalysis
The brute force technique
The program in this chapter is not really a game, but it is fun to play with nonetheless. Our program will convert normal English into a secret code, and also convert secret codes back into regular English again. Only someone who is knowledgeable about secret codes will be able to understand our secret messages.

Because this program manipulates text in order to convert it into secret messages, we will learn several new functions and methods that come with Python for manipulating strings. We will also learn how programs can do math with text strings just as it can with numbers.

About Cryptography

The science of writing secret codes is called cryptography. Cryptography has been used for thousands of years to send secret messages that only the recipient could understand, even if someone captured the messenger and read the coded message. A secret code system is called a cipher. There are thousands of different ciphers that have been used, each using different techniques to keep the messages a secret.

In cryptography, we call the message that we want to be secret the plaintext. The plaintext could look something like this:

Hello there! The keys to the house are hidden under the reddish flower pot.

When we convert the plaintext into the encoded message, we call this encrypting the plaintext. The plaintext is encrypted into the ciphertext. The ciphertext looks like random letters (also called garbage data), and we cannot understand what the original plaintext was by just looking at the ciphertext. Here is an example of some ciphertext:

Ckkz fkx kj becqnejc kqp pdeo oaynap iaoowca!

But if we know about the cipher used to encrypt the message, we can decrypt the ciphertext back to the plaintext. (Decryption is the opposite of encryption.)

Many ciphers also use keys. Keys are secret values that let you decrypt ciphertext that was encrypted using a specific cipher. Think of the cipher as being like a door lock. Although all the door locks of the same type are built the same, but a particular lock will only unlock if you have the key made for that lock.

The Caesar Cipher


Figure 14-1: Shifting over letters by three spaces. Here, B becomes E.
When we encrypt a message using a cipher, we will choose the key that is used to encrypt and decrypt this message. The key for our Caesar Cipher will be a number from 1 to 26. Unless you know the key (that is, know the number), you will not be able to decrypt the encrypted message.

The Caesar Cipher was one of the earliest ciphers ever invented. In this cipher, you encrypt a message by taking each letter in the message (in cryptography, these letters are called symbols because they can be letters, numbers, or any other sign) and replacing it with a "shifted" letter. If you shift the letter A by one space, you get the letter B. If you shift the letter A by two spaces, you get the letter C. Figure 14-1 is a picture of some letters shifted over by 3 spaces.

To get each shifted letter, draw out a row of boxes with each letter of the alphabet. Then draw a second row of boxes under it, but start a certain number of spaces over. When you get to the leftover letters at the end, wrap around back to the start of the boxes. Here is an example with the letters shifted by three spaces:


Figure 14-2: The entire alphabet shifted by three spaces.

The number of spaces we shift is the key in the Caesar Cipher. The example above shows the letter translations for the key 3.

Using a key of 3, if we encrypt the plaintext "Howdy", then the "H" becomes "K". The letter "o" becomes "r". The letter "w" becomes "z". The letter "d" becomes "g". And the letter "y" becomes "b". The ciphertext of "Hello" with key 3 becomes "Krzgb".

We will keep any non-letter characters the same. In order to decrypt "Krzgb" with the key 3, we just go from the bottom boxes back to the top. The letter "K" becomes "H", the letter "r" becomes "o", the letter "z" becomes "w", the letter "g" becomes "d", and the letter "b" becomes "y" to form "Howdy".

You can find out more about the Caesar Cipher from Wikipedia at http://en.wikipedia.org/wiki/Caesar_cipher

ASCII, and Using Numbers for Letters

How do we implement this shifting of the letters in our program? We can do this by representing each letter as a number (called an ordinal), and then adding or subtracting from this number to form a new number (and a new letter). ASCII (pronounced "ask-ee" and stands for American Standard Code for Information Interchange) is a code that connects each character to a number between 32 and 127. The numbers less than 32 refer to "unprintable" characters, so we will not be using them.

The capital letters "A" through "Z" have the ASCII numbers 65 through 90. The lowercase letters "a" through "z" have the ASCII numbers 97 through 122. The numeric digits "0" through "9" have the ASCII numbers 48 through 57.


Table 14-1: The ASCII Table
32  (space) 48  0   64  @   80  P   96  `   112 p
33  !   49  1   65  A   81  Q   97  a   113 q
34  "   50  2   66  B   82  R   98  b   114 r
35  #   51  3   67  C   83  S   99  c   115 s
36  $   52  4   68  D   84  T   100 d   116 t
37  %   53  5   69  E   85  U   101 e   117 u
38  &   54  6   70  F   86  V   102 f   118 v
39  '   55  7   71  G   87  W   103 g   119 w
40  (   56  8   72  H   88  X   104 h   120 x
41  )   57  9   73  I   89  Y   105 i   121 y
42  *   58  :   74  J   90  Z   106 j   122 z
43  +   59  ;   75  K   91  [   107 k   123 {
44  ,   60  <   76  L   92  \   108 l   124 |
45  -   61  =   77  M   93  ]   109 m   125 }
46  .   62  >   78  N   94  ^   110 n   126 ~
47  /   63  ?   79  O   95  _   111 o
So if we wanted to shift "A" by three spaces, we first convert it to a number (65). Then we add 3 to 65, to get 68. Then we convert the number 68 back to a letter ("D"). We will use the chr() and ord() functions to convert between letters and numbers.

For example, the letter "A" is represented by the number 65. The letter "m" is represented by the number 109. A table of all the ASCII characters from 32 to 12 is in Table 14-1.

The chr() and ord() Functions

The chr() function (pronounced "char", short for "character") takes an integer ASCII number for the parameter and returns the single-character string. The ord() function (short for "ordinal") takes a single-character string for the parameter, and returns the integer ASCII value for that character. Try typing the following into the interactive shell:

>>> chr(65)
'A'
>>> ord('A')
65
>>> chr(65+8)
'I'
>>> chr(52)
'4'
>>> chr(ord('F'))
'F'
>>> ord(chr(68))
68
>>>
On the third line, chr(65+8) evaluates to chr(73). If you look at the ASCII table, you can see that 73 is the ordinal for the capital letter "I". On the fifth line, chr(ord('F')) evaluates to chr(70) which evaluates to 'F'. Feeding the result of ord() to chr() will evaluate to the same as the original argument. The same goes for feeding the result of chr() to ord(), as shown by the sixth line.

Using chr() and ord() will come in handy for our Caesar Cipher program. They are also helpful when we need to convert strings to numbers and numbers to strings.

Sample Run of Caesar Cipher

Here is a sample run of the Caesar Cipher program, encrypting a message:

Do you wish to encrypt or decrypt a message?
encrypt
Enter your message:
The sky above the port was the color of television, tuned to a dead channel.
Enter the key number (1-26)
13
Your translated text is:
Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
Now we will run the program and decrypt the text that we just encrypted.

Do you wish to encrypt or decrypt a message?
decrypt
Enter your message:
Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
Enter the key number (1-26)
13
Your translated text is:
The sky above the port was the color of television, tuned to a dead channel.
On this run we will try to decrypt the text that was encrypted, but we will use the wrong key. Remember that if you do not know the correct key, the decrypted text will just be garbage data.

Do you wish to encrypt or decrypt a message?
decrypt
Enter your message:
Gur fxl nobir gur cbeg jnf gur pbybe bs gryrivfvba, gharq gb n qrnq punaary.
Enter the key number (1-26)
15
Your translated text is:
Rfc qiw yzmtc rfc nmpr uyq rfc amjmp md rcjctgqgml, rslcb rm y bcyb afyllcj.
Caesar Cipher's Source Code

Here is the source code for the Caesar Cipher program. If you don't want to type all of this code in, you can visit this book's website at the URL http://inventwithpython.com/chapter14 and follow the instructions to download the source code. After you type this code in, save the file as cipher.py

cipher.py
This code can be downloaded from http://inventwithpython.com/cipher.py
If you get errors after typing this code in, compare it to the book's code with the online diff tool at http://inventwithpython.com/diff or email the author at al@inventwithpython.com
# Caesar Cipher
MAX_KEY_SIZE = 26
def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
def getMessage():
    print('Enter your message:')
    return input()
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
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
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
How the Code Works: Lines 1 to 34

This code is much shorter compared to our other games. The encryption and decryption processes are the just the reverse of the other, and even then they still share much of the same code. Let's look at how each line works.

# Caesar Cipher
MAX_KEY_SIZE = 26
The first line is simply a comment. The Caesar Cipher is one cipher of a type of ciphers called simple substitution ciphers. Simple substitution ciphers are ciphers that replace one symbol in the plaintext with one (and only one) symbol in the ciphertext. So if a "G" was substituted with "Z" in the cipher, every single "G" in the plaintext would be replaced with (and only with) a "Z".

MAX_KEY_SIZE is a variable that stores the integer 26 in it. MAX_KEY_SIZE reminds us that in this program, the key used in our cipher should be between 1 and 26.

Deciding to Encrypt or Decrypt

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')
The getMode() function will let the user type in if they want to encrypt or decrypt the message. The return value of input() (which then has the lower() method called on it, which returns the lowercase version of the string) is stored in mode. The if statement's condition checks if the string stored in mode exists in the list returned by 'encrypt e decrypt d'.split(). This list is ['encrypt', 'e', 'decrypt', 'd'], but it is easier for the programmer to just type in 'encrypt e decrypt d'.split() and not type in all those quotes and commas. But you can use whatever is easiest for you; they both evaluate to the same list value.

This function will return the first character in mode as long as mode is equal to 'encrypt', 'e', 'decrypt', or 'd'. This means that getMode() will return the string 'e' or the string 'd'.

Getting the Message from the Player

def getMessage():
    print('Enter your message:')
    return input()
The getMessage() function simply gets the message to encrypt or decrypt from the user and uses this string as its return value.

Getting the Key from the Player

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key
The getKey() function lets the player type in key they will use to encrypt or decrypt the message. The while loop ensures that the function only returns a valid key. A valid key here is one that is between the integer values 1 and 26 (remember that MAX_KEY_SIZE will only have the value 26 because it is constant). It then returns this key. Remember that on line 22 that key was set to the integer version of what the user typed in, and so getKey() returns an integer.

Encrypt or Decrypt the Message with the Given Key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
getTranslatedMessage() is the function that does the encrypting and decrypting in our program. It has three parameters. mode sets the function to encryption mode or decryption mode. message is the plaintext (or ciphertext) to be encrypted (or decrypted). key is the key that is used in this cipher.

The first line in the getTranslatedMessage() function determines if we are in encryption mode or decryption mode. If the first letter in the mode variable is the string 'd', then we are in decryption mode. The only difference between the two modes is that in decryption mode, the key is set to the negative version of itself. If key was the integer 22, then in decryption mode we set it to -22. The reason for this will be explained later.

translated is the string that will hold the end result: either the ciphertext (if we are encrypting) or the plaintext (if we are decrypting). We will only be concatenating strings to this variable, so we first store the blank string in translated. (A variable must be defined with some string value first before a string can be concatenated to it.)

The isalpha() String Method

The isalpha() string method will return True if the string is an uppercase or lowercase letter from A to Z. If the string contains any non-letter characters, then isalpha() will return False. Try typing the following into the interactive shell:

>>> 'Hello'.isalpha()
True
>>> 'Forty two'.isalpha()
False
>>> 'Fortytwo'.isalpha()
True
>>> '42'.isalpha()
False
>>> ''.isalpha()
False
>>>
As you can see, 'Forty two'.isalpha() will return False because 'Forty two' has a space in it, which is a non-letter character. 'Fortytwo'.isalpha() returns True because it does not have this space. '42'.isalpha() returns False because both '4' and '2' are non-letter characters. And ''.isalpha() is False because isalpha() only returns True if the string has only letter characters and is not blank.

We will use the isalpha() method in our program in the next few lines.

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
Line 31's for loop iterates over each letter (remember in cryptography they are called symbols) in the message string. In a for loop, strings are treated just like lists of single-character strings. If message had the string 'Hello', then for symbol in 'Hello' would be the same as for symbol in ['H', 'e', 'l', 'l', 'o']. On each iteration through this loop, symbol will have the value of a letter in message.

The reason we have the if statement on line 32 is because we will only encrypt/decrypt letters in the message. Numbers, signs, punctuation marks, and everything else will stay in their untranslated form. The num variable will hold the integer ordinal value of the letter stored in symbol. Line 34 then "shifts" the value in num by the value in key.

The isupper() and islower() String Methods

The isupper() and islower() string methods (which are on line 36 and 41) work in a way that is very similar to the isdigit() and isalpha() methods. isupper() will return True if the string it is called on contains at least one uppercase letter and no lowercase letters. islower() returns True if the string it is called on contains at least one lowercase letter and no uppercase letters. Otherwise these methods return False. The existence of non-letter characters like numbers and spaces does not affect the outcome. Although strings that do not have any letters, including blank strings, will also return False. Try typing the following into the interactive shell:

>>> 'HELLO'.isupper()
True
>>> 'hello'.isupper()
False
>>> 'hello'.islower()
True
>>> 'Hello'.islower()
False
>>> 'LOOK OUT BEHIND YOU!'.isupper()
True
>>> '42'.isupper()
False
>>> '42'.islower()
False
>>> ''.isupper()
False
>>> ''.islower()
False
>>>
How the Code Works: Lines 36 to 57

The process of encrypting (or decrypting) each letter is fairly simple. We want to apply the same Python code to every letter character in the string, which is what the next several lines of code do.

Encrypting or Decrypting Each Letter

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
This code checks if the symbol is an uppercase letter. If so, there are two special cases we need to worry about. What if symbol was 'Z' and key was 4? If that were the case, the value of num here would be the character '^' (The ordinal of '^' is 94). But ^ isn't a letter at all. We wanted the ciphertext to "wrap around" to the beginning of the alphabet.

The way we can do this is to check if key has a value larger than the largest possible letter's ASCII value (which is a capital "Z"). If so, then we want to subtract 26 (because there are 26 letters in total) from num. After doing this, the value of num is 68, which is the ASCII value for 'D'.

            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
If the symbol is a lowercase letter, the program runs code that is very similar to lines 36 through 40. The only difference is that we use ord('z') and ord('a') instead of ord('Z') and ord('A').

If we were in decrypting mode, then key would be negative. Then we would have the special case where num -= 26 might be less than the smallest possible value (which is ord('A'), that is, 65). If this is the case, we want to add 26 to num to have it "wrap around".

            translated += chr(num)
        else:
            translated += symbol
The translated string will be appended with the encrypted/decrypted character. If the symbol was not an uppercase or lowercase letter, then the else-block on line 48 would have executed instead. All the code in the else-block does is append the original, untranslated symbol to the translated string. This means that spaces, numbers, punctuation marks, and other characters will not be encrypted or decrypted.

    return translated
The last line in the getTranslatedMessage() function returns the translated string.

The Start of the Program

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
This is the main part of our program. We call each of the three functions we have defined above in turn to get the mode, message, and key that the user wants to use. We then pass these three values as arguments to getTranslatedMessage(), whose return value (the translated string) is printed to the user.

Brute Force

That's the entire Caesar Cipher. However, while this cipher may fool some people who don't understand cryptography, it won't keep a message secret from someone who knows cryptanalysis. While cryptography is the science of making codes, cryptanalysis is the science of breaking codes.

Do you wish to encrypt or decrypt a message?
encrypt
Enter your message:
Doubts may not be pleasant, but certainty is absurd.
Enter the key number (1-26)
8
Your translated text is:
Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
The whole point of cryptography is that so if someone else gets their hands on the encrypted message, they cannot figure out the original unencrypted message from it. Let's pretend we are the code breaker and all we have is the encrypted text:

Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.

One method of cryptanalysis is called brute force. Brute force is the technique of trying every single possible key. If the cryptanalyst knows the cipher that the message uses (or at least guesses it), they can just go through every possible key. Because there are only 26 possible keys, it would be easy for a cryptanalyst to write a program than prints the decrypted ciphertext of every possible key and see if any of the outputs make sense. Let's add a brute force feature to our program.

Adding the Brute Force Mode to Our Program

First, change lines 7, 9, and 12 (which are in the getMode() function) to look like the following (the changes are in bold):

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt or brute force a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode[0]
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b".')
This will let us select "brute force" as a mode for our program. Then modify and add the following changes to the main part of the program:

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Your translated text is:')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
These changes make our program ask the user for a key if they are not in "brute force" mode. If they are not in "brute force" mode, then the original getTranslatedMessage() call is made and the translated string is printed.

However, otherwise we are in "brute force" mode, and we run a getTranslatedMessage() loop that iterates from 1 all the way up to MAX_KEY_SIZE (which is 26). Remember that when the range() function returns a list of integers up to but not including the second parameter, which is why we have + 1. This program will print out every possible translation of the message (including the key number used in the translation). Here is a sample run of this modified program:

Do you wish to encrypt or decrypt or brute force a message?
brute
Enter your message:
Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
Your translated text is:
1 Kvbiaz thf uva il wslhzhua, iba jlyahpuaf pz hizbyk.
2 Juahzy sge tuz hk vrkgygtz, haz ikxzgotze oy ghyaxj.
3 Itzgyx rfd sty gj uqjfxfsy, gzy hjwyfnsyd nx fgxzwi.
4 Hsyfxw qec rsx fi tpiewerx, fyx givxemrxc mw efwyvh.
5 Grxewv pdb qrw eh sohdvdqw, exw fhuwdlqwb lv devxug.
6 Fqwdvu oca pqv dg rngcucpv, dwv egtvckpva ku cduwtf.
7 Epvcut nbz opu cf qmfbtbou, cvu dfsubjouz jt bctvse.
8 Doubts may not be pleasant, but certainty is absurd.
9 Cntasr lzx mns ad okdzrzms, ats bdqszhmsx hr zartqc.
10 Bmszrq kyw lmr zc njcyqylr, zsr acpryglrw gq yzqspb.
11 Alryqp jxv klq yb mibxpxkq, yrq zboqxfkqv fp xyproa.
12 Zkqxpo iwu jkp xa lhawowjp, xqp yanpwejpu eo wxoqnz.
13 Yjpwon hvt ijo wz kgzvnvio, wpo xzmovdiot dn vwnpmy.
14 Xiovnm gus hin vy jfyumuhn, von wylnuchns cm uvmolx.
15 Whnuml ftr ghm ux iextltgm, unm vxkmtbgmr bl tulnkw.
16 Vgmtlk esq fgl tw hdwsksfl, tml uwjlsaflq ak stkmjv.
17 Uflskj drp efk sv gcvrjrek, slk tvikrzekp zj rsjliu.
18 Tekrji cqo dej ru fbuqiqdj, rkj suhjqydjo yi qrikht.
19 Sdjqih bpn cdi qt eatphpci, qji rtgipxcin xh pqhjgs.
20 Rciphg aom bch ps dzsogobh, pih qsfhowbhm wg opgifr.
21 Qbhogf znl abg or cyrnfnag, ohg pregnvagl vf nofheq.
22 Pagnfe ymk zaf nq bxqmemzf, ngf oqdfmuzfk ue mnegdp.
23 Ozfmed xlj yze mp awpldlye, mfe npceltyej td lmdfco.
24 Nyeldc wki xyd lo zvokckxd, led mobdksxdi sc klcebn.
25 Mxdkcb vjh wxc kn yunjbjwc, kdc lnacjrwch rb jkbdam.
26 Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
After looking over each row, you can see that the 8th message is not garbage, but plain English! The cryptanalyst can deduce that the original key for this encrypted text must have been 8. This brute force would have been difficult to do back in the days of Caesars and the Roman Empire, but today we have computers that can quickly go through millions or even billions of keys in a short time. You can even write a program that can recognize when it has found a message in English, so you don't have read through all the garbage text.

Summary: Reviewing Our Caesar Cipher Program

Computers are very good at doing mathematics. When we create a system to translate some piece of information into numbers (such as we do with text and ASCII or with space and coordinate systems), computer programs can process these numbers very quickly and efficiently.

But while our Caesar cipher program here can encrypt messages that will keep them secret from people who have to figure it out with pencil and paper, it won't keep it secret from people who know how to get computers to process information for them. (Our brute force mode proves this.) And there are other cryptographic ciphers that are so advanced that nobody knows how to decrypt the secret messages they make. (Except for the people with the key of course!)

A large part of figuring out how to write a program is figuring out how to represent the information you want to manipulate as numbers. I hope this chapter has especially shown you how this can be done. The next chapter will present our final game, Reversi (also known as Othello). The AI that plays this game will be much more advanced than the AI that played Tic Tac Toe in chapter 9. In fact, the AI is so good, that you'll find that most of the time you will be unable to beat it!
