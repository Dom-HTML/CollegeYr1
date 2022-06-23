#plainText = "Hello World"
encrypted = ""
decrypted = ""

cache = []

shift = 10

def Main():
    word = input("Enter the word to encrypt and decrypt: ")
    Encrypt(word)
    Decrypt()
    Three()

def Encrypt(plainText):
    cache.clear()
    encrypted = ""
    for letter in plainText:
        cache.append(chr(ord(letter)+shift))
        
    for letter in cache:
        encrypted = encrypted + letter

    print(encrypted)

def Decrypt():
    global decrypted
    for letter in cache:
        decrypted = decrypted + chr(ord(letter)-shift)

    print(decrypted)

def Three():
    sent = input("enter a sentence >>")
    sent = (sent.replace(",","")).replace(" ","")

    alph = "abcdefghijklmnopqrstuvwxyz"
    revalph = "zyxwvutsrqponmlkgihgfedcba"
    alpha = []
    revalpha = []

    for letter in alph:
        alpha.append(letter)
    for letter in revalph:
        revalpha.append(letter)
        
Main()
