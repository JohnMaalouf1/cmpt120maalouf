# John Maalouf
# Professor Martensen
# Calculates the Third side of a Triangle

import math


def main():
    
    print("")
    X1,Y1 = eval(input("Please Enter Length 1 'X1', 'Y1' separated by a ','\nX1, Y1: "))
    X2,Y2 = eval(input("Please Enter Length 2 'X2', 'Y2' separated by a ','\nX2, Y2: "))
    sideA = (X2 - X1)
    sideB = (Y2 - Y1)
# Takes input from user then calculate sides A,B    
    calcC = math.sqrt(sideA ** 2 + sideB ** 2)
# Calculates side C using Pythag theorm
    print("side A: " + str(sideA))
    print("side B: " + str(sideB))
    print("")    
    print("The length of the Side is: " + str(calcC))
    print("The Length of the Side rounded to the nearest whole number is: " + str(round(calcC)))
    print("THe Length of the Side rounded to the nearest decimal is: " + str(round(calcC, 1)))
    print("The Length of the Side rounded up to the nearest Integer is: " + str(math.ceil(calcC)))
    print("")
# Rounds items to specific places

print("")
print("Hello User, this program will calculate the length of the hypotenuse of a triangle")
main()
input("Press the <Enter> key to Exit.")
print("Thank You for using our software!")
print("")
