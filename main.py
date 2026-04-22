import time
import random 

def dice():
    print("dice, brought to you by pyCasino")
    print("rolling the dice...")
    time.sleep(3)
    result = random.choice(["1", "2", "3", "4", "5", "6"])
    print(f"the dice rolled: {result}")
    print("thanks for playing! would you like to play some more games or play again?")
    print("1. play again")
    print("2. play more games")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        dice()
    elif choice == "2":
        casino()
    elif choice == "3":
        print("thanks for playing! goodbye!")
        exit()

def coinflip():
    print("coin flip, brought to you by pyCasino")
    print("flipping the coin...")
    time.sleep(3)
    result = random.choice(["heads", "tails"])
    print(f"the coin landed on: {result}")
    print("thanks for playing! would you like to play some more games or play again?")
    print("1. play again")
    print("2. play more games")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        coinflip()
    elif choice == "2":
        casino()
    elif choice == "3":
        print("thanks for playing! goodbye!")
        exit()

def slots():
    print("slots, brought to you by pyCasino")
    print("spinning the slots...")
    time.sleep(3)
    result = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar"])
    print(f"the slots landed on: {result}")
    print("thanks for playing! would you like to play some more games or play again?")
    print("1. play again")
    print("2. play more games")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        slots()
    elif choice == "2":
        casino()
    elif choice == "3":
        print("thanks for playing! goodbye!")
        exit()

def guessing():
    print("guessing game, brought to you by pyCasino")
    print("thinking of a number...")
    time.sleep(3)

    number = random.randint(1, 10)

    guess = int(input("i got it! now, try to guess a number between 1 and 10. "))

    if guess == number:
        print("congratulations! you guessed the number!")
    else:
        print(f"sorry, the number was: {number}")
    print("thanks for playing! would you like to play some more games or play again?")
    print("1. play again")
    print("2. play more games")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        guessing()
    elif choice == "2":
        casino()
    elif choice == "3":
        print("thanks for playing! goodbye!")
        exit()

def drawstraws():
    print("draw straws, brought to you by pyCasino")
    print("drawing straws...")
    time.sleep(3)
    straws = ["short", "long", "long", "long"]
    random.shuffle(straws)
    print("choose a straw (1-4): ")
    choice = int(input("> ")) - 1

    if straws[choice] == "short":
        print("sorry, you drew the short straw!")
    else:
        print("congrats, you drew a long straw!")

    print("thanks for playing! would you like to play some more games or play again?")
    print("1. play again")
    print("2. play more games")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        drawstraws()
    elif choice == "2":
        casino()
    elif choice == "3":
        print("thanks for playing! goodbye!")
        exit()

def casino():
    print("pyCasino, made by bitetheapple")
    print("welcome to pyCasino!")
    print("select what you want to do:")

    print("1. roll some dice")
    print("2. flip some coins")
    print("3. spin some slots")
    print("4. guess some numbers")
    print("5. draw straws")
    print("6. leave")

    choice = input("enter your choice: ")

    if choice == "1":
        dice()
    elif choice == "2":
        coinflip()
    elif choice == "3":
        slots()
    elif choice == "4":
        guessing()
    elif choice == "5":
        drawstraws()
    elif choice == "6":
        print("thanks for playing! goodbye!")
        exit()

casino()
