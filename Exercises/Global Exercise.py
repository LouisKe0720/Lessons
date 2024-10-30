global_var = "I am a global!"

#Function to print global and local variables
def print_variables():
    print(global_var)
    local_var = "I am a local!"
    print(local_var)

#Calling the function to print global and local variables
print_variables()

#Since this is a local variable, it cannot be accessed outside the function
print(local_var)