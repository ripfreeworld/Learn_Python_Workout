import random

lowerBound = 1
upperBound = 10

number = random.randint(lowerBound, upperBound)
numUserStr = ""
numUser = lowerBound - 1
print("Guess Game starts\npress 'q' to quit\n")

while numUser != number:
    numUserStr = input("Enter your guess between {0} and {1}: \n".format(lowerBound, upperBound))
    try:
        numUser = int(numUserStr)
        if numUser < number:
            print("too low\n")
        elif numUser > number:
            print("too high\n")
        else:
            print("just right!\n")
            break
    except ValueError:
        if numUserStr == "q":
            print("you gave up")
            break
        else:
            print("invalid input")
    

