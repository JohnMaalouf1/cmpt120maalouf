def main():
    round1 = []
    round2 = []
    userInput = input("Please Enter a String: ")
    userInput = userInput.lower()
    for i in range(len(userInput)):
        x = ord(userInput[i][0])
        round1.append(x)

        y = ("{0:>08b}".format(x))
        round2.append(y)
    print(round1)
    print(round2)


main()


