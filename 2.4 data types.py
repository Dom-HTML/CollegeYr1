album1 = None

class albumClass():
    def __init__(self, title, artist, genre, numTracks, inStock, price):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.numTracks = numTracks
        self.inStock = inStock
        self.price = price

def main():
    getInputs()
    outputVars()

def getInputs():
    global album1
    
    title = str(input("what is the title of the album? :"))
    artist = str(input("Who is the artist? :"))
    genre = str(input("what is the genre? :"))
    numTracks = int(input("How many tracks on the album? :"))
    inStockQ = bool(input("is the album in stock? (yes/no):"))
    if inStockQ == "yes":
        inStock = True
    elif inStockQ == "no":
        inStock = False
    else:
        inStock = True
    price = float(input("How much is the album? :"))

    album1 = albumClass(title, artist, genre, numTracks, inStock, price)

def outputVars():
    print(album1.title)

main()
    
