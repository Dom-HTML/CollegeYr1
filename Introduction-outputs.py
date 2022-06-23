#defining strings
password = "password"
username = "username"

#creating array containing names
names = ["Ian","Jhon","Reni","Mani"]

#defining main function
def main():
    #outputs welcome
    print("Welcome")
    #gets users input and stores it in the variable user
    user = input("enter your username: ")

    #compares two variables and runs if they are the same
    if (user == username):
        #gets users input and stores it in the variable passInput
        passInput = input("Please enter your password: ")

        #compares two variables and runs if they are the same
        if (passInput == password):
            #prints welcome
            print("Welcome")

        #calls the function standardTasks
        standardTasks()


#defining standardTasks
def standardTasks():
    #prints hello world
    print("Hello World!")
    #prints the result of 9/3
    print(9/3)
    #prints the result of 9%3
    print(9%3)
    #defining new string variable which will store a concatonated string
    concat = ""
    #runs for every item in the array names
    for name in names:       
        #concatonates the the current array item to the string variable
        concat = concat + " " +name

    #outputs the varable concat
    print(concat)

    advancedTasks()

#defines function called advancedTasks
def advancedTasks():
    #defines variable called myName
    myName = "Dominic"
    #prints hello plus what is stored in the myName function
    print ("Hello "+myName)
    #outputs a hexidecimal value as a decimal value
    print(0XA5)
    #outputs a binary value as a decimal value
    print(0B1100011)
    """
    Block comment your code
    to get
    signed off 
    """

#calls the main function
main()
