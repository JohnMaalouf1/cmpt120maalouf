
def main():
    terms = []
    classes = int(input("Please enter the amount of classes you take: "))
    for i in range(classes):
        grade = input("Please Enter your Letter Grade: ")
        if grade == "A" or grade == "a":
            FG = 4
        elif grade == "B+" or grade == "b+":
            FG = 3.5
        elif grade == "B" or grade == "b":
            FG = 3.0
        elif grade == "c+" or grade == "c+":
            FG = 2.5
        elif grade == "C" or grade == "c":
            FG = 2.0
        elif grade == "D" or grade == "d":
            FG = 1.0
        elif grade == "F" or grade == "f":
            FG = 0.0
        

        terms.append(FG)
    avg = sum(terms) / classes
    print(avg)
    input("Press the <Enter> Key to Exit:")

main()


