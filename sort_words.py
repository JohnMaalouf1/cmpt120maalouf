usr_string = input("Enter a string: ")

text = usr_string.split()

text.sort()


print(("They words: ") + (usr_string) + (" in alphabetical order are: "))
for text in text:
    print(text)
print("\nThe program has ended, have a great day!")
