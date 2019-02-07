# Jack Maalouf
# Jackson O'Sullivan
# Nick Ruiz

greeting = input("Hello, possible pirate! What's the password?")
if greeting == ("Arrr!"):
	print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")

'''
No ending quote on line 1
Line 2 if greeting in instead of '==='
change elif to else with colon
Add indent to else statement

'''
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889" }

for author, date in authors.items():
    print(author, " died in " + date)
'''
Change Authors name
add ending bracket
In for loop preperly call function .items()
Change formatting of print statement
Broken print statement

'''

# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).




year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")

'''
proper declaration of year
add parantheses in print statement
proper int input
added colon after year
change single quote to double quotes
change && to and
change elif to else
'''


# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == grade is "F":
    print("Student is failing.")
else:
    print("Student is passing.")

'''
    Change all inputs to int
    rename exam_3 to exam_three
    seperate by ',' in list
    change grade to grades in for loop
    fix quotes for C
    add : to elif
    change elif to else
    add parantheses to print statements


'''
