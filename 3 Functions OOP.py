newDogVar = None

def newDog():
    coat = input("Enter the dogs coat colour: ")
    eye = input("Enter the dogs eye colour: ")
    leng = input("Enter the dogs length: ")
    weig = input("Enter the dogs weight: ")
    price = input("Enter the price of the dog: ")

    newDogVar = dog(coat, eye, leng, weig, price)

class dog:
    def __innit__(self, coat, eye, leng, weig, price):
        self.coat = coat
        self.eye = eye
        self.leng = leng
        self.weig = weig
        self.price = price

newDog()
