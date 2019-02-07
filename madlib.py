# madlib.py
# program that Simulates madlib game
# John Maalouf
# September 8, 2018

def main():
    # Takes 4 inputs from the user, Name, Animal, Place, Adjective.
    print("")
    name = input("Please Enter a Name: ")
    animal = input("Please Enter an Animal: ")
    place = input("Please Enter a Place: ")
    adjective = input("Please Enter an Adjective: ")
    print("")
    
    # Puts inputs into a string.
    result = (name + " and his " + animal + " went to the " + place + " to get " + adjective + " food!")
    print(result)
    
    print("")
    recall()


def recall():
    # Method that will replay the game if the user responds True.
    answer = (input("Would you like to play again? (True/False): "))
    if answer == "True":
        main()
    elif answer == "False":
        print("Thank you for playing!")
        input("Press the <Enter> Key to Exit.")


print("Hello User, Welcome to Madlibs. This Program will emulate a Madlibs Game!")
main()





