def main():

    #Initalizes Score
    score = 0
    
    #The following comments pertain to all questions
    
    #Question 1
    question1 = input("\nWho was the First president of the United States: ")
    #Takes input
    question1 = question1.lower()
    #Converts question answer to all lower case
    if question1 == "george washington":
        #Compares user response to Answer
        score = score + 1
        #increments score if user input is equal to answer
        print("Correct")
    else:
        print("Incorrect")
    #prints "Incorrect" and continues on to next question

    print("---------------------------------------------------")

    question2 = input("\nWho was the Second President of the United States: ")
    question2 = question2.lower()
    if question2 == "john adams":
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

    print("---------------------------------------------------")

    question3 = input("\nWho was the Third President of the United States: ")
    question3 = question3.lower()
    if question3 == "thomas jefferson":
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

    print("---------------------------------------------------")

    question4 = input("\nWho was the Forth President of the United States: ")
    question4 = question4.lower()
    if question4 == "james madison":
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

    print("---------------------------------------------------")

    question5 = input("\nWho was the Fifth President of the United States: ")
    question5 = question5.lower()
    if question5 == "james monroe":
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")

    print("---------------------------------------------------")

    #Prints Score messaged based on value of 'score'
    print("\nYour score was", score, "Out of 5")
    if score < 3:
        print("\nBetter luck next time.")
    elif score < 5:
        print("\nNot bad. Try again soon!")
    elif score == 5:
        print('\nAwesome! You rock!')
    input("Press the <Enter> key to Exit")

#Intro and Main Method
print("\nHello User! Welcome to your Presidents Quiz!")
main()
