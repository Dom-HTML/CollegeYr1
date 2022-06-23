import time#imports time library
import random

class safe():
    def __innit__(self, code, numTrys, hints):
        self.code = code
        self.numTrys = numTrys
        self.hints = hints

safeSafe = safe()
safeSafe.code = "123"
safeSafe.numTrys = 5
        
def main():
    safeCrackerMenu()
    #name()
    #bottles()

def name():
    name = input("Enter your name: ")

    for char in name:
        if not char.isnumeric():
            print(char)
        else:
            continue

def bottles():
    s = "s"
    rang = 100
    for item in range(rang):
        if rang - item == 1:
            s = ""
        print(f"{rang - item} bottle{s} left on the wall")
        time.sleep(0.2)

def safeCrackerMenu():
    safeSafe.hints = True
    print("""----Menu----
1.set safe code
2.generate random safe code
3.set max number of guesses
4.turn hints off
5.guess the code
---------
Enter your option (enter the number)
---------""")

    option = int(input("option >>").strip())

    if option == 1:
        setCode()
    if option == 2:
        genCode()
    if option == 3:
        setNumTrys()
    if option == 4:
        hintsToggle()
    if option == 5:
        guessf()
    else:
        print("Try again")
        safeCrackerMenu()

    print("""---------
Loading...
---------""")
    time.sleep(2)

def setCode():
    print("Set a 3 digit code for the safe")
    code = input("code >>")
    safeSafe.code = code
    safeCrackerMenu()

def genCode():
    print("Loading...")
    code = None
    for i in range(3):
        random.randint(0,9)
    time.sleep(1)
    print("Done")
    safeCrackerMenu()

def setNumTrys():
    print("Enter the max number of guesses")
    maxNum = input("max >>")
    safeSafe.maxTrys = maxNum
    print("Done")
    safeCrackerMenu()

def hintsToggle():
    safeSafe.hints = not safeSafe.hints
    print(f"Hints:{safeSafe.hints}")
    safeCrackerMenu()

def guessf():
    numTrys = safeSafe.numTrys
    for i in range(numTrys):
        guess = ""
        s = "tries"
        if safeSafe.numTrys == 1:
            s = "try"
        print(f"Enter your guess (you have {safeSafe.numTrys} {s} left)")
        while not guess.isnumeric():
            guess = input("guess >>")
        if guess == safeSafe.code:
            print("Safe open")
            break
        else:
            print(f"{anylise(guess)} is/are in the right position")
            continue

    if safeSafe.numTrys <= 0:
        print("The safe makes a large clunk, it is locked forever")
        print("Tryagain")

def anylise(guess):
    correct = []
    for i in range(int(len(guess))):
        if safeSafe.code[i] == len(guess)[i]:
            correct.append(guess[i])
    concatStr  = ""
    for item in correct:
        if concatStr == "":
            concatStr = concatStr + correct[correct.index(item)]
            continue
        else:
            concatStr = concatStr + " and " + correct[correct.index(item)]
        return concatStr
        
main()
