# John Maalouf
# Professor Martensen
# Lab 8
# Shopping cart lab with class


from product import *

# Create an object for each product. Name each object product1, product2, etc.
product1 = Product("Ultrasonic range finder", 2.50, 4)

product2 = Product("Servo motor", 14.99, 10)

product3 = Product("Servo Controller", 44.95, 5)

product4 = Product("Microcontroller", 34.95, 7)

product5 = Product("Laser range finder", 149.99, 2)

product6 = Product("Lithium polymer battery", 8.99, 8)


# The following is a list containing each of the 6 product objects created above
products = [product1, product2, product3, product4, product5, product6]

def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
       # if the quantity for the product is  > 0:
            print(str(i)+")",products[i].name, "$", products[i].price)
            print()
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        prodId = int(vals[0])
        count = int(vals[1])

        if products[prodId].quantity >= count:
            if products[prodId].price * count:
                products[prodId].quantity -= count
                cash -= products[prodId].price * count
                print("You purchased", count, products[prodId].name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", products[prodId].name)

main()
