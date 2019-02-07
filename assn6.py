# John Maalouf
# Professor Martensen
# Assignment 6
# October 8, 2018


def createUsername():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    # Takes input, firstname and lastname
    
    uname = (firstName[0] + lastName[0:])
    # takes the first index of firstname and combines it with the lastname
    return uname
# returns uname back to main



def createPassword():
    
    userPassword = input("Please Enter a password: ")
    if len(userPassword) < 6:
        print("Invalid Password")
    #checks length of password to see if it is too short
    else:
        if checkFirstChar(userPassword):
            print("First Character is Valid")
        else:
            print("Invalid password")
        # Calls checkFirstChar and awaits a boolean value, True or False
        
        if checkRemaningChars(userPassword):
            print("Remaining Characters are Valid")
        else:
            print("Invalid password")

# Calls checkRemaningChars and awaits a boolean value, True or False


def checkFirstChar(userPassword):
    # Checks asscii value of userpassword after converting it to lowercase for asscii comparisons
    val = ord(userPassword[0].lower())
    if 97 < val < 122:
        return True
    else:
        return False


def checkRemaningChars(userPassword):
    # runs through each index of the password using [i] then check to see if it is equal to an invalid character
    i = 0
    while i < len(userPassword):
        if userPassword[i] == " " or userPassword[i] == "," or userPassword[i] == ".":
            return False
        i += 1
    else:
        return True

# return true or false

# main method calls other functions
def main():
    print("")
    print("This program creates a Username and a Password")
    print("")
    # sets variable username to the return value of createUsername()
    username = createUsername()
    print("Your username is ", username)
    # prints intro message and the username variable
    print("")
    password = createPassword()
# sets variable password to the return value of createPassword()

main()
print("")
input("Press the <Enter Key> to Exit")
