import math#importing math library

def main():
    swimmingPool()# calling functions
    roundPool()

def swimmingPool():
    poolLen = int(input("How long is the pool(m)?: "))#getting inputs
    poolWid = int(input("How wide is the pool(m)?: "))
    poolDep = int(input("How deep is the pool(m)?: "))

    poolPer = poolLen*2+poolWid*2#calculating and printing perimeter 
    print(poolPer)

    poolArea = poolWid*poolLen#calculating and printing poolVol
    poolVol = poolArea*poolDep
    print(poolVol)

def roundPool():
    diameter = float(input("What is the diameter of the pool(m)?: "))#getting input of diameter

    circm = 2 * math.pi * (diameter/2)#claculating circumfrence and printing it
    print(circm)

    area = math.pi * (diameter/2)**2#claculating area and printing
    print(area)

    print((diameter/2) % 1)#using the mod operation on the radius
    
main()#calling main function
