#defines function called main
def main():
    #calls the conversation fuction
    conversation()
    mixedRainbow()

#defines the conversation function
def conversation():
    #gets user input and stores it in the name variable
    name = input("What is your name? : ")
    #prints the variable name after hello
    print("hello " + name)
    #prints the string "how are you today, " and concatenates the variable name
    print("how was your day today, " + name)
    #gives the user a stupid nickname
    print("I'll give you a really dumb nickname, oh yeah it'll be " + name[:3] + "gsy")

#defines the function mixedRainbow
def mixedRainbow():
    #array that holds a finished list of colours
    colourNames = ["red","orange","yellow","green","blue","indigo","violet"]
    #empty array to store user inputs
    colours = []
    #empty array that will store the colours after changing the cases
    newCases = []

    #if the colours array is empty it runs
    if len(colours) == 0:
        #appends user input to the colours array
        colours.append(input("Enter the the fist colour in the rainbow: "))

    #runs for the length of the colourNames array
    for item in range(len(colourNames)-1):
        #appends the users input to the array colours
        colours.append(input("Enter the the next colour in the rainbow: "))

    #boolean that switches which dictates what case the colour will be converted to
    upper = False

    #runs for every items in the colours array
    for item in colours:
        #runs if the upper boolean is true
        if upper == True:
            #converts string to upper case and appends it to the newCases array
            newCases.append(item.upper())
            #swaps the upper boolean to false
            upper = False
        #runs if the boolean upper is false
        elif upper == False:
            #converts string to lower case and appends it to the newCases array
            newCases.append(item.lower())
            #swaps the upper boolean to true
            upper = True

    #runs for every item in the new cases array
    for item in newCases:
        #swaps every e with an a then prints the item
        item = item.replace("e", "a")
        item = item.replace("E", "A")
        print(item)

#calls main
main()
