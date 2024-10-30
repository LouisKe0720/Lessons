def greet_user(name):
    """
    Prints a greeting message to the user.
    
    Parameters:
    name (str): The name of the user to greet.
    
    Returns:
    None
    """
    print(f"Hello, {name}!")

# Example usage
name = input("What is your name? ")

greet_user(name)

#Task 2

def square(number):
    """
    Returns the square of a number.
    
    Parameters:
    number (int or float): The number to square.
    
    Returns:
    int or float: The square of the input number.
    """
    return number ** 2

# Example usage

number = float(input("Enter a number: "))

result = square(number)

print(f"The square of {number} is {result}.")
