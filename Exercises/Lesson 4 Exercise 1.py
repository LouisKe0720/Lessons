grade = int(input("Enter a grade: "))
if 0 <= grade <= 100:
    if grade >= 90:
        print("You got an A")
    elif 89 >= grade >= 80:
        print("You got a B")
    elif 79 >= grade >= 70:
        print("You got a C")
    elif 69 >= grade >= 60:
        print("You got a D")
    elif grade < 60:
        print("You got an F")
else: 
    print("Invalid grade")
