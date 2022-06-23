import random

option = 4
options = ["Rock", "Paper", "Scissors"]
comp = 4

matchCode = 0#1=win#2=loss#3=draw

playerCount = 0
compCount = 0

def main():
    optionF()
    compChoice()
    compare()
    winner()
    again()

def optionF():
    global option
    option = 4
    
    print("""Enter an option
1.Rock
2.Paper
3.Scissors
(Enter the number)""")

    while True:
        option = int(input("Please enter an option: "))

        if option > 3 or option < 1:
            print("Please enter a valid option")
        else:
            break

def compChoice():
    global comp
    comp = 4
    
    while comp == 4:
        comp = random.randint(1,3)

def compare():
    global comp
    global option
    global matchCode

    if option == 1:#rock
        if comp == 1:
            matchCode = 3#draw
        elif comp == 2:
            matchCode = 2#loss
        elif comp == 3:
            matchCode = 1#win
    elif option == 2:#paper
        if comp == 1:
            matchCode = 1#win
        elif comp == 2:
            matchCode = 3#draw
        elif comp == 3:
            matchCode = 2#loss
    elif option == 3:#scissors
        if comp == 1:
            matchCode = 2#loss
        elif comp == 2:
            matchCode = 1#win
        elif comp == 3:
            matchCode = 3#draw
    else:
        print("Error With Comparing")

def winner():  
    global matchCode
    
    global option
    global comp
    global options
    
    global playerCount
    global compCount

    match = ""

    if matchCode == 1:
        match = "Win"
        playerCount = playerCount + 1
    elif matchCode == 2:
        match = "Loss"
        compCount = compCount + 1
    elif matchCode == 3:
        match = "Draw"

    print(f"""~~~\n{match}
~
you: {options[option - 1]}
computer: {options[comp - 1]}
~~~
Scoreboard
~
you: {playerCount}
computer: {compCount}""")

def again():
    playA = 3
    
    print("""~~~\nPlay Again
1.Yes
2.No
(Enter the number)""")

    while True:
        playA = int(input("Please enter an option: "))

        if playA == 3:
            print("Please enter a valid option")
        elif playA == 1:
            print("-----------------")
            main()
            break
        elif playA == 2:
            exit() 

main()
