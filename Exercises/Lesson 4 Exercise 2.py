age = int(input("Enter your age: "))
if age < 0 or age > 122: # The oldest person ever lived was 122 years old
    print("Invalid age")
else:
    if age < 18: # Check if the user is under 18
        print("Access denied: You must be 18 or older.")
    else:
        member = input("Are you a member? (yes or no): ")
        if age >= 18 and member == "yes":
            print("Access granted: You are a member.")
        elif age >= 18 and member == "no":
            print("Access granted: Please consider becoming a member.")