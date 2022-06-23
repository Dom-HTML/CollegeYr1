#defines variables username, function
username = "bob"
password = "bob"

months = ["january","febuary",["march",""],"april","may","june","july","august","september","october","november","december"]
days = ["31","28","31","30","31","30","31","31","30","31","30","31"]

#defines main function
def main():
    #calls passwordf function
    #passwordf()
    #calls chooseMonth function
    chooseMonth()

#defines passwordf function
def passwordf():
    #takes users input and stors in userInput
    userInput = input("Enter your username :")
    #takes users input and stors in passInput
    passInput = input("Enter your password :")

    #checks if userInput is the same as username
    if userInput.strip() == username:
        #checks if passInput is the same as password
        if passInput.strip() == password:
            #prints string "welcome " then the username
            print("Welcome "+username)
        #checks if passInput is not the same as password
        else:
            #prints "password incorrect"
            print("password inncorrect")
    #checks if userInput is the same as username
    else:
        #prints "username incorrect"
        print("username incorrect")

def chooseMonth():
    curMonth = int(input("Enter the current month as a number :"))
    curMonthTex = ""

    for item in months:
        #print(str(int(months.index(item)) + 1) + " != " + str(curMonth))
        if int(months.index(item)) + 1 == curMonth:        
            print("The month is " + item)
            curMonthTex = item
            break  

    if (int(months.index(curMonthTex)) + 1) == 3 or (int(months.index(curMonthTex)) + 1) == 4 or (int(months.index(curMonthTex)) + 1) == 5:
        print("The season is spring")
    elif (int(months.index(curMonthTex)) + 1) == 6 or (int(months.index(curMonthTex)) + 1) == 7 or (int(months.index(curMonthTex)) + 1) == 8:
        print("The season is summer")
    elif (int(months.index(curMonthTex)) + 1) == 9 or (int(months.index(curMonthTex)) + 1) == 10 or (int(months.index(curMonthTex)) + 1) == 11:
        print("The season is autumn")
    elif (int(months.index(curMonthTex)) + 1) == 12 or (int(months.index(curMonthTex)) + 1) == 1 or (int(months.index(curMonthTex)) + 1) == 2:
        print("The season is winter")

    print(curMonthTex + " has " + days[months.index(curMonthTex)] + " days in it")

#calls main function
main()
