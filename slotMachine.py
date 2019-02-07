import random

def main(money):
    if money <= 0:
        print("You are out of money, Sorry")
    else:
        spin(money)

def spin(money):
        reelResult1 = (random.choice(slot))
        reelResult2 = (random.choice(slot))
        reelResult3 = (random.choice(slot))
        money = money - 1
        checkResults(reelResult1, reelResult2, reelResult3, money)

def checkResults(reel1, reel2, reel3, money):
    print("")
    print("-----------------------------")
    print(reel1, "|", reel2, "|", reel3)
    if reel1 == reel2 and reel2 == reel3:
        print("You won the Jackpot!!! You received $50!")
        money = money + 50
    elif reel1 == reel2 or reel2 == reel3:
        print("Aww so close... How about another?")
    else:
        print("Better luck next time...")
    print("Your balance is: $" + str(money))
    print("-----------------------------")
    replay(money)

def replay(money):
    while money > 0:
        answer = input("\nPlay again? (true/false): ")
        answer = answer.lower()
        if answer == "true" or answer == "t":
            spin(money)
        elif answer == "false" or answer == "f":
            print("Your final Balance is $" + str(money))
                input("Press the <Enter> Key to Exit: ")
                    print("Thank you for using our Software!")
        else:
            print("Invalid input")
            replay(money)


slot = ['Watermelon', 'Cherry', 'Orange', 'Gold Bar', 'Diamond', '7']
money = eval(input("\nTry your luck today! How much money would you like to start with?: $"))
print("You've got $" + str(money) + " and as many tries... ")

main(money)
print("")
