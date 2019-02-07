
def main():
    #Initalizes Score
    score = 20

    # The following comments pertain to all questions
    # Ask's user question and stores answer as input
    question1 = input("\nWho was the First president of the United States: ")
    # Converts the answer into all lowercase to ensure answer is properly checked
    question1 = question1.lower()
    # while the anser is incorrect it will repeat the question.
    # The loop is broken if the user enters 'skip'
    while question1 != "george washington" and question1 != "skip":
        print("|Incorrect, Please try again|")
        question1 = input("\nWho was the First president of the United States: ")
    
    print("---------------------------------------------------")
	
    question2 = input("\nWho was the Second President of the United States: ")
    question2 = question2.lower()
    while question2 != "john adams"and question2 != "skip":
        print("|Incorrect, Please try again|")
        question2 = input("\nWho was the Second President of the United States: ")
    
    print("---------------------------------------------------")

    question3 = input("\nWho was the Third President of the United States: ")
    question3 = question3.lower()
    while question3 != "thomas jefferson" and question3 != "skip":
        print("|Incorrect, Please try again|")
        question3 = input("\nWho was the Third President of the United States: ")
    
    print("---------------------------------------------------")

    question4 = input("\nWho was the Forth President of the United States: ")
    question4 = question4.lower()
    while question4 != "james madison" and question4 != "skip":
        print("|Incorrect, Please try again|")
        question4 = input("\nWho was the Forth President of the United States: ")
    
    print("---------------------------------------------------")

    question5 = input("\nWho was the Fifth President of the United States: ")
    question5 = question5.lower()
    while question5 != "james monroe" and question5 != "skip":
        print("|Incorrect, Please try again|")
        question5 = input("\nWho was the Fifth President of the United States: ")
    
    print("---------------------------------------------------")

    print('\nThe Quiz is Over')
    recall()

# Intro and Main Method
print("\nHello User! Welcome to your Presidents Quiz!")
print("Input the correct answer or enter <skip> to proceed to the next question")


def recall():
    # Method that will replay the game if the user responds True.
    answer = (input("Would you like to play again? (True/False): "))
    answer = answer.lower()
    if answer == "true":
        main()
    elif answer == "false":
        print("Thank you for playing!")
        input("Press the <Enter> Key to Exit.")
main()

