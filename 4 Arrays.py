#declaring lists
days: list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
numArray: list = []

#declaring main function
def main():
    #calling recurese function passing in the days list
    recurse(days)
    numArrayf()

#declaring recure function
def recurse(array):
    #loops through passed array and prints every output
    for item in array:
        print(item) 

#declaring numArrayf function
def numArrayf():
    s: str = "a "#declare a local varialbe called s
    for i in range(5):#loop runs 5 times
        intCast: bool = False#declaring a bool, set as false
        if i > 0:#if runs if it is not the first loop 
            s = "another "
        while intCast == False:#runs until inCast is true
            print("--------------")
            userInput: int = input(f"Enter {s}number >>")#gets input form user
            try:
                userInput = int(userInput)#casts to an int
                numArray.append(userInput)#appends userinput to numArray
                intCast = True#set intCast to true, will break for dloop
            except:#runs if error in try block
                print("the input could not be cast to an integer")
                print("please enter a number not a word")
                print("--------------")
                continue#progresses for loop by one   
    
    recurse(numArray)#calls recurese function passing in numArray

main()#callin main function
