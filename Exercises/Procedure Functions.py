#Joke Telling

def joke1():
    print("Why did the scarecrow win an award? Because he was outstanding in his field.")

def joke2():
    print("What is a computer's first sign of old age? Loss of memory.")

def joke3():
    print("What do computers snack on? Microchips.")

#Main Program
def main():

    joke = input("Enter a number between 1 and 3 to choose a joke: ")
    if joke == "1":
        joke1()
        print("Would you like to hear another joke? (yes/no)")
        answer = input().lower()
        if answer == "yes":
            main()
        elif answer == "no":
            print("Goodbye!")
        else:
            while answer!= "yes" and answer!= "no":
                print("Invalid input. Please enter 'yes' or 'no'.")
                answer = input().lower()
    elif joke == "2":
        joke2()
        print("Would you like to hear another joke? (yes/no)")
        answer = input().lower()
        if answer == "yes":
            main()
        elif answer == "no":
            print("Goodbye!")
        else:
            while answer!= "yes" and answer!= "no":
                print("Invalid input. Please enter 'yes' or 'no'.")
                answer = input().lower()
    elif joke == "3":
        joke3()
        print("Would you like to hear another joke? (yes/no)")
        answer = input().lower()
        if answer == "yes":
            main()
        elif answer == "no":
            print("Goodbye!")
        else:
            while answer!= "yes" and answer!= "no":
                print("Invalid input. Please enter 'yes' or 'no'.")
                answer = input().lower()
    else:
        while joke != "1" and joke != "2" and joke != "3":
            print("Invalid input. Please enter a number between 1 and 3.")
            joke = input("Enter a number between 1 and 3 to choose a joke: ")
            if joke == "1":
                joke1()
                print("Would you like to hear another joke? (yes/no)")
                answer = input().lower()
                if answer == "yes":
                    main()
                elif answer == "no":
                    print("Goodbye!")
                else:
                    while answer!= "yes" and answer!= "no":
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        answer = input().lower()
            elif joke == "2":
                joke2()
                print("Would you like to hear another joke? (yes/no)")
                answer = input().lower()
                if answer == "yes":
                    main()
                elif answer == "no":
                    print("Goodbye!")
                else:
                    while answer!= "yes" and answer!= "no":
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        answer = input().lower()
            elif joke == "3":
                joke3()
                print("Would you like to hear another joke? (yes/no)")
                answer = input().lower()
                if answer == "yes":
                    main()
                elif answer == "no":
                    print("Goodbye!")
                else:
                    while answer!= "yes" and answer!= "no":
                        answer = input("Invalid input. Please enter 'yes' or 'no'.")
                        answer = input().lower()


main()

# Parameter Passing is when passing input parameters into a function and and receiving the results back. Parameters are the things between the "()" in a function. Ex. def add_numbers(num1, num2):. num1 and num2 are the parameters. Arguments are the values that are passed into the parameters. Ex. add_numbers(5, 10). 5 and 10 are the arguments.

number = input("Enter a number from 1 - 10: ")
if number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6" and number != "7" and number != "8" and number != "9" and number != "10":
    while number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6" and number != "7" and number != "8" and number != "9" and number != "10":
        print("Invalid input. Please enter a number from 1 - 10.")
        number = input("Enter a number from 1 - 10: ")
def multiplication_table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

multiplication_table(int(number))