# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
#John Maalouf

def main():
    print("Hello user, this program converts Celsius temperatures to Farenheit")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    print("Thank you for using our software")
    input("Press the <Enter> key to quit.")

main()
