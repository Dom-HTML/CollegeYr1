import random

ROW_SIZE = 5
COLUMN_SIZE = 5

board = [[0]*ROW_SIZE]*COLUMN_SIZE

mineX = 0
mineY = 0

def Main():
    CreateBoard()
    OutputBoard()
    Guess()

def CreateBoard():
    global mineX, mineY
    #this loops is pretty usless but i had to do it
    for i in range(ROW_SIZE):
        for j in range(COLUMN_SIZE):
            board[i][j] = 0

    randX = random.randint(0,4)
    randY = random.randint(0,4)

    mineX = randX
    mineY = randY

    #testing
    board[mineX][mineY] = 1

def OutputBoard():
    for i in range(ROW_SIZE):
        print(f"{board[i]}")

def Guess():
    print("\nEnter your guess e.g. 1 2 (row 1, column 2)")
    guess = input("guess >>")

    row = (guess.split( )[0]).strip()
    column = (guess.split( )[1]).strip()
    
    if row == mineX:
        if column == mineY:
            print("Well Done You Guessed Correctly")
    else:
        print("NiceTry")
        board[int(row)][int(column)] = 1
    
Main()

#This script does not work 0.0
    
