# John Maalouf
# Professor Martensen
# Calculates cost per square inch of pizza based on diameter and price

import math

def main():
   print("")
   diameter = float(input("Please Enter the Diameter of Pizza: "))
# takes diameter from user
   price = float(input("Please Enter the Price of the Pizza: "))
# takes price from user
   radius = diameter / 2
# calculates radius
   area = math.pi * (radius ** 2)
# calculates area
   finalPrice = price / area
# sets finalPrice value

   print("The Final Price is: $" + str(round(finalPrice, 2)))
   input("Press the <Enter> key to Exit: ")
   print("Thank you for using our software!")

# source of question python textbook/text
print("")
print("Hello User, This program will calculate the cost per square inch of a circular pizza, given its diameter and price.")

main()
