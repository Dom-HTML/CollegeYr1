#code, in my opion this code is scuffed as hell
coat = "d"
eye = "d"
length = "d"
weight = "d"
price = "d"

def main():
    name = input("Enter your name: ")
    print(name)
    
    coatf()
    eyeColourf()
    lengthf()
    weightf()
    pricef()

    menu()

def coatf():
    global coat
    coat = input("what colour is the coat: ")
def eyeColourf():
    global eye
    eye = input("what colour is the eyes: ")
def lengthf():
    global length
    length = input("what lenght is dog: ")
def weightf():
    global weight
    weight = input("what weight is dog: ")
def pricef():
    global price
    price = input("what much money in pence is dog: ")

def powerComplexf():
    command = input("in command ghere: ")
    print("Dog "+command+"s")

def dogAttributesf():
    print(f"{coat}, {eye}, {length}, {weight}, {price}")

def menu():
    print("""what to change
1.coat colour
2.eye colour
3.length
4.weight
5.price
enter the number of the option""")

    option = int(input("enter an option: "))
    if option == 1:
         coatf()
    elif option == 2:
        eyeColourf()
    elif option == 3:
        lengthf()
    elif option == 4:
        weightf()
    elif option == 5:
        pricef()
    else:
        print("enter an acctuall option")
        

main()
powerComplexf()
dogAttributesf()
