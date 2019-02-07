# John Maalouf
# Professor Martensen
# Username and Password generator
# September 28, 2018


# Gets firstname, lastname, and makes username
def main():
    firstName = input("Please Enter your First Name: ")
    lastName = input("Please Enter your Last Name: ")
    username = (firstName[0] + lastName[0:])
    username = username.lower()
    print("Your Username is: " + username)
    password()


# Gets password and check to see if its is long enough, and follows rules
def password():
    print("")
    userPassword = input("Please Enter a password: ")

    if len(userPassword) < 6:
        print("\nYour password is too short, Please Try again")
        password()

    val = ord(userPassword[0].lower())
    if 97 < val < 122:
        print("")
    else:
        print("\nYour password cannot begin with a non alphabetical character, Please Try again")
        password()

    i = 0
    while i < len(userPassword):
        if userPassword[i] == " " or userPassword[i] == "," or userPassword[i] == ".":
            print("You cannot have a space, comma, or period in your password, Please Try again")

            password()
        i += 1
    print("Your Password is:", userPassword)
    print("")
    input("Press the <Enter> key to Exit: ")
    print("")
    print("Thank you for using our software!")
    exit()


# Prints conclusion
print("")
print("Hello User this program will generate a username and a secure password")
print("")
main()
print("Thank you for using our software!")
print("")
