amountOfTomatoes = 0.0
boilingSpeed = 0.0
volumeOfCan = 0.0

def isPositive(num):
    if num > 0:
        return True
    else:
        return False

def getInputs():
    try:      
        amountOfTomatoes = float(input("Please enter the amount of tomatoes (in kg) that you have: "))
        boilingSpeed = float(input("Please enter boiling speed (rate at which a kg of tomato boiled in a second (kg/sec)): "))
        volumeOfCan = float(input("Please enter the volume of a can: "))
        print(type(amountOfTomatoes))
        print(type(boilingSpeed))
        print(type(volumeOfCan))
    except:
        print("Wrong type!! Please type digit!!")


getInputs()