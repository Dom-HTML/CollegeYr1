import random

def main():
    #randomDice()
    blackJack()
    #examGrade()

def randomNum(minRan, maxRan):
    randomNum = random.randint(minRan, maxRan)
    return randomNum

def randomDice():
    print("dice roll:" + str(randomNum(0,6)))

    total = 0

    for x in range(4):
        randNum = randomNum(0,6)
        print("dice roll"+str(x)+":"+str(randNum))
        total = total + randNum

    print(total)

def blackJack():
    print("----------BlackJack----------")
    card1 = randomNum(1,11)
    card2 = randomNum(1,11)
    total = card1 + card2

    dCard1 = randomNum(1,11)
    dCard2 = randomNum(1,11)
    dTotal = card1 + card2

    print("card one:" + str(card1))
    print("card one:" + str(card2))
    print("Total :"+str(total))

    desision = input("Twist or stick(1/0): ")

    if desision == 1:
        newCard = randomNum(1, 11)
        total = total + newCard
        print("new card :"+newCard)
        print("Total:"+total)

    if dTotal < 6:
        dNewCard = randomNum(1, 11)
        dTotal = dTotal + dNewCard

    if dTotal <= 21:
        if dTotal > total:
            print("Dealer Wins")
        elif total <= 21:
            if total > dTotal:
                print("You Win")
    elif total < 21 and total > dTotal:
        print("You Win")
    elif total > 21 and dTotal > 21:
        print("No one wins")
    elif total < 21 and total <= 21 and dTotal > 21:
        print("You Win")
    elif total == dTotal:
        print("Draw")
    else:
        print("Scenario not predicted")

    print("-------Scoreboard-------")
    print("dealer:"+str(dTotal))
    print("player:"+str(total))
    print("-------End-------")

    playAgain = input("press enter to play again...(0 if not): ")
    if playAgain == 0:
        exit()
    else:
        blackJack()

def examGrade():
    score = int(input("Enter you exam score(0-100): "))

    if score > 100:
        print("Dont be silly")
    elif score < 0:
        print("That bad huh")
    elif score <= 100 and score >= 90:
        print("A*")
    elif score <= 89 and score >= 80:
        print("A")
    elif score <= 79 and score >= 70:
        print("B")
    elif score <= 69 and score >= 60:
        print("C")
    elif score <= 59 and score >= 50:
        print("D")
    elif score <= 49 and score >= 40:
        print("E")
    elif score < 40:
        print("U")
    else:
        print("Either you broke the system or you tyed in a word")

main()
