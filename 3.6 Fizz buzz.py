count = []
b = 0
f = 0
fb = 0

def main():
    upto = int(inputf("Enter the number to count to >>"))
    fn =  int(inputf("Enter the fizz number >>"))
    bn = int(inputf("Enter the buzz number >>"))
    fbn = int(inputf("Enter the fizzbuzz number >>"))
    
    fizzBuzz(upto, fn, bn, fbn)

    count = ["FizzBuzz: " + str(fb),"Fizz: " + str(f),"Buzz" + str(b)]
    
    for item in count:
        printf(item)

def fizzBuzz(upto, fn, bn, fbn):
    for i in range(1, upto):
        if i%15 == 0:
            printf("FizzBuzz")
            keepCount("fb")
        elif i%5 == 0:
            printf("Buzz")
            keepCount("b")
        elif i%3 == 0:
            printf("Fizz")
            keepCount("f")
        else:
            printf(i)

def printf(string):
    print(string)

def inputf(caption):
    inp = input(caption)
    return inp

def keepCount(data):
    global count, f, b , fb
    if data == "f":
        f += 1
    elif data == "b":
        b += 1
    elif data == "fb":
        fb += 1
        
main()
