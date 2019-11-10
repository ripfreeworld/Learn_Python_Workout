import random


def Guessnum(lBound, uBound):
    numUserStr = ""
    numUser = -1        # assign a number out of range to the default guess 
    attempt = 0
    number = random.randint(lBound, uBound)  

    while numUser != number:
        numUserStr = input("Enter your guess between {} and {}: \n".format(lBound, uBound))
        if numUserStr == "q":
            print("you gave up")
            break
        else:
            try:
                numUser = int(numUserStr)
                if numUser < number:
                    print("too low\n")
                elif numUser > number:
                    print("too high\n")
                else:
                    print("just right!\n")
                    break
                attempt += 1
            except ValueError:
                    print("invalid input")
            finally:
                if attempt >= limitChance:
                    print ("You didn't guess in time. Game Over.\n")
                    break


def GuessFruit(fruitNum):
    numUser = -1        # assign a number out of range to the default guess 
    attempt = 0

    while numUser != fruitNum:
        getInput = GetFruit()
        if type(getInput) == str:
            break
        else:
            numUser = getInput
            if numUser < fruitNum:
                print("Please choose a later word!\n")
            elif numUser > fruitNum:
                print("Please choose an earlier word!\n")
            else:
                print("just right!\n")
                break
            attempt += 1
            if attempt >= limitChance:
                print ("You didn't guess in time. Game Over.\n")
                break


def GetFruit():
    while True:
        userInput = input(f"please guess a fruit\n")
        if userInput == "q":
            return userInput
        else:
            try:
                fruitnum = textDict[userInput]
                return fruitnum
            except:
                print("This fruit is not recorded. Please guess another fruit.")
            finally:
                pass

## main()            
print("Guess Game starts\npress 'q' to quit\n")

limitChance = 5     # to define how many chances the user is able to guess
attempt = 0
print(f"You have {limitChance} chances to guess\n")

gamemode = input("guess a number (Press 1) or a fruit name in dictionary (Press 2)\n")

if gamemode == "1":
    print("number mode")
    lowerBound = 1
    upperBound = 100
    Guessnum(lowerBound, upperBound)

elif gamemode == "2":
    print("fruit mode")
    i = 1
    textArray = ["apple", "banana", "cherry", "grape", "orange", "pear", "pineapple", "strawberry", "watermelon"]
    textDict = {}
    for i in range(1, len(textArray)):
        textDict[textArray[i]] = i
    # textDict = {        # if some keys duplicate, the later one would substitute the former one
    #     "apple": 1,
    #     "banana": 2,
    #     "cherry": 3,
    #     "grape": 4, 
    #     "orange": 5,
    #     "pear": 6,
    #     "pineapple": 7,
    #     "strawberry": 8,
    #     "watermelon": 9
    # }
    lowerBound = 1
    upperBound = len(textDict)
    GuessFruit(random.randint(lowerBound, upperBound))
else:
    print("invalid choice!")

