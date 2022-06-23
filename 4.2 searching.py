names = [] * 10
arLen = 100
binarray = [] * arLen

def main():
    global arLen
    #searchNames()
    arLen = len(binarray)
    binary()

def searchNames():
    for i in range(10):
        userInput = input("Enter a name>>")
        names.append(userInput)
    
    sv = input("What name to search for?>>")

    found = False
    for item in names:   
        if item == sv:
            print(f"name found at position {names.index(item)} in array")
            found = True
                
    if found == False:
        print("name not found")

def binary():
    for i in range(arLen):
        binarray.append(i*10)

    binarySearch(binarray, 350)

def binarySearch(sa, si):
    middle = lambda a : len(a)//2-1
    while True:
        if si > sa[middle(sa)]:
            newAr = []
            for i in range(middle(sa)):
                newAr.append(sa[i])
            sa = newAr
        elif si < sa[middle(sa)]:
            neg = middle(sa)
            newAr = []
            for i in range(middle(sa)):
                newAr.append(sa[i - neg])
            sa = newAr
            neg + 1
        elif si == sa[middle(sa)]:
            print(f"found at position {middle[sa]}")
    
main()

