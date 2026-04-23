import time
import random


money = 100


wait_enabled = True

loading_enabled = True

# psst, enter "2342" in the casino main menu for $100! don't tell anyone else though, it's a secret ;)

def atm():
    global money
    print(f"welcome to the pyCasino ATM! you currently have ${money}")
    print("what would you like to do?")
    print("1. deposit money")
    print("2. withdraw money")
    print("3. check balance")
    print("4. back to casino")

    choice = input("enter your choice: ")

    if choice == "1":
        try:
            amount = int(input("how much would you like to deposit? $"))
            if amount > 0:
                money += amount
                print(f"deposited ${amount}. new balance: ${money}")
            else:
                print("please enter a positive amount.")
        except ValueError:
            print("invalid amount. please enter a number.")
        atm()
    elif choice == "2":
        try:
            amount = int(input("how much would you like to withdraw? $"))
            if amount > 0 and amount <= money:
                money -= amount
                print(f"withdrew ${amount}. new balance: ${money}")
            elif amount > money:
                print("insufficient funds.")
            else:
                print("please enter a positive amount.")
        except ValueError:
            print("invalid amount. please enter a number.")
        atm()
    elif choice == "3":
        print(f"your current balance is: ${money}")
        atm()
    elif choice == "4":
        casino()
    else:
        print("invalid choice.")
        atm() 

def dice():
    print("dice, brought to you by pyCasino")
    print("rolling the dice...")
    if wait_enabled:
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
    if wait_enabled:
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
    global money
    print("slots, brought to you by pyCasino")
    print("spinning the slots...")
    if wait_enabled:
        time.sleep(3)
    result = random.choice(["cherry", "lemon", "orange", "plum", "bell", "bar"])
    print(f"the slots landed on: {result}")

    if result == "bar":
        winnings = 30
    elif result == "bell":
        winnings = 20
    elif result == "plum":
        winnings = 15
    elif result == "orange":
        winnings = 10
    elif result == "lemon":
        winnings = 5
    else:
        winnings = 0

    if winnings > 0:
        money += winnings
        print(f"you won ${winnings}! your new balance is: ${money}")
    else:
        print("no winnings this round. better luck next time!")

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

def double_or_nothing():
    global money
    print("double or nothing, brought to you by pyCasino")
    print(f"your current balance is: ${money}")

    try:
        bet = int(input("how much would you like to bet? $"))
    except ValueError:
        print("invalid amount. please enter a number.")
        double_or_nothing()
        return

    if bet <= 0:
        print("please bet a positive amount.")
        double_or_nothing()
        return
    if bet > money:
        print("you don't have enough money for that bet.")
        double_or_nothing()
        return

    print("choose high or low:")
    print("1. high")
    print("2. low")
    choice = input("enter your choice: ")

    if choice == "1":
        bet_choice = "high"
    elif choice == "2":
        bet_choice = "low"
    else:
        print("invalid choice.")
        double_or_nothing()
        return

    result = random.choice(["higher", "lower"])
    print(f"the number is {result} than 50!")

    if bet_choice == result:
        money += bet
        print(f"you won ${bet}! your new balance is: ${money}")
    else:
        money -= bet
        print(f"you lost ${bet}. your new balance is: ${money}")

    print("what would you like to do next?")
    print("1. play again")
    print("2. go back to casino")
    print("3. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        double_or_nothing()
    elif choice == "2":
        casino()
    elif choice == "3":
        print("thanks for playing! goodbye!")
        exit()
    else:
        print("invalid choice. returning to casino.")
        casino()


def guessing():
    global money
    print("guessing game, brought to you by pyCasino")
    print("thinking of a number...")
    if wait_enabled:
        time.sleep(3)

    number = random.randint(1, 10)

    try:
        guess = int(input("i got it! now, try to guess a number between 1 and 10. "))
        
        if guess == number:
            winnings = 30
            money += winnings
            print(f"congratulations! you guessed the number and won ${winnings}!")
            print(f"your new balance is: ${money}")
        else:
            print(f"sorry, the number was: {number}")
    except ValueError:
        print("please enter a valid number!")
    
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
    if wait_enabled:
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

def bar():
    global money
    print(f"welcome to the pyCasino bar! you have ${money} to spend on drinks!")
    print("pick a drink:")
    print("1. water ($0)")
    print("2. beer ($5)")
    print("3. wine ($10)")
    print("4. whiskey ($15)")
    print("5. check balance")
    print("6. go to atm")
    print("7. back to casino")

    choice = input("enter your choice: ")

    if choice == "1":
        if money >= 0:
            money -= 0
            print("cheers! you bought water.")
            print(f"remaining balance: ${money}")
        else:
            print("sorry, you don't have enough money for water.")
    elif choice == "2":
        if money >= 5:
            money -= 5
            print("pouring you a cold one...")
            if wait_enabled:
                time.sleep(2)
            print("cheers! you bought beer.")
            print(f"remaining balance: ${money}")
        else:
            print("sorry, you don't have enough money for beer.")
    elif choice == "3":
        if money >= 10:
            money -= 10
            print("pouring you a glass...")
            if wait_enabled:
                time.sleep(2)
            print("sláinte! you bought wine.")
            print(f"remaining balance: ${money}")
        else:
            print("sorry, you don't have enough money for wine.")
    elif choice == "4":
        if money >= 15:
            money -= 15
            print("pouring you a shot...")
            if wait_enabled:
                time.sleep(1)
            print("bottoms up! you bought whiskey.")
            print(f"remaining balance: ${money}")
        else:
            print("sorry, you don't have enough money for whiskey.")
    elif choice == "5":
        print(f"your current balance is: ${money}")
    elif choice == "6":
        atm()
        return 
    elif choice == "7":
        casino()
        return 
    else:
        print("invalid choice.")

    bar()

def settings():
        print("settings, brought to you by pyCasino")
        print("1. disable wait() function on games")
        print("2. test money spending ($5)")
        print("3. fake loading screen on casino main menu")
        print("4. back to casino")

        choice = input("enter your choice: ")

        if choice == "1":
            global wait_enabled
            wait_enabled = not wait_enabled
            if wait_enabled:
                print("wait() function enabled! games will now have delays.")
            else:
                print("wait() function disabled! games like coin flipping will now answer instantly.")
            settings()
        elif choice == "2":
            global money
            if money >= 5:
                money -= 5
                print("test money spent successfully!")
                print(f"remaining balance: ${money}")
            else:
                print("sorry, you don't have enough money for test spending.")
            settings()
        elif choice == "3":
            global loading_enabled
            loading_enabled = not loading_enabled
            if loading_enabled:
                print("fake loading enabled! pyCasino will now have simulated loading times.")
            else:
                print("fake loading disabled! pyCasino will now load instantly.")
            settings()
        elif choice == "4":
            casino()
        else:
            print("invalid choice.")
            settings()

def casino():
    print("pyCasino, made by bitetheapple")
    time.sleep(1)
    print("loading digital casino...")
    if loading_enabled:
     time.sleep(3) # simulated loading, might delete or add a setting for it??? update: setting added
    print("welcome to pyCasino!")
    print("select what you want to do:")
    print("1. roll some dice")
    print("2. flip some coins")
    print("3. spin some slots")
    print("4. guess some numbers (money winner)")
    print("5. draw straws")
    print("6. pyCasino bar")
    print("7. atm")
    print("8. high or low (double or nothing)")
    print("9. settings")
    print("10. leave")

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
        bar()
    elif choice == "7":
        atm()
    elif choice == "8":
        double_or_nothing()
    elif choice == "9":
        settings()
    elif choice == "10":
        print("thanks for playing! goodbye!")
        exit()
    elif choice == "2342":
        global money
        money += 100
        print("you found a secret! thanks for checking the source code! +$100")
        print(f"remaining balance: ${money}")
        casino()
    else:
        print("invalid choice. please try again.")
        casino()

casino()
