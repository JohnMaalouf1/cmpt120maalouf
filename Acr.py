# John Maalouf
# Professor Martensen
# Program that takes a sentence and turns it into an Acronym

def main():
    print("")
    word = input("Please Enter a Sentence: ")
    word = word.upper()
    splitWord = word.split()
# Takes word from user, converts it into lowercase, then splits it.
    acr = ""
    for i in range(len(splitWord)):
        acr = acr + splitWord[i][0]
# For loop that extracts first letter for every word.
    print("")
    print("The Acronym is: " +  (acr))
    print("")

print("")
print("Hello User, This is an Acronym Generator!")
main()
print("")
print("Thank you for Using our Software!")
input("Press the <Enter> Key to Exit: ")
print("")

