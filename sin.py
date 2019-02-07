
import math

def main():

    print("Hello User, This program will calculate the length of a ladder based on the Height and Angle.")
    print("")
    height = int(input("Please Enter the Height: "))
# Takes height input from user
    angle = int(input("Please Enter the Angle: "))
# Takes angle input from user
    radian = math.pi/180 * angle
# Calculates Radian from user
    ladder_length = height / math.sin(radian)
# Calculates ladder_length
    rounded_length = round(ladder_length, 2)
# Rounds lader_length and stores in new variable, rounded_length
    print("The length of the ladder is: " + str((rounded_length)))
    print("Thank you for using our software!")

main()








