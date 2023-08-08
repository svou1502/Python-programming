# Take input from the user

number = int(input("Enter any non negative number and I will give you it's factorial: "))

# Check if the input is negative
if number < 0:
    print("Factorial is not defined for negative numbers.")

else:
    factorial = 1 # This line ensures that the multiplication starts from 1 and builds up the factorial
    original_number = number # This stores the original number
    while number > 0:
        factorial = factorial * number
        number = number - 1

    print(f"The factorial of {original_number} is: {factorial}")
    # the 'f' in the above line creates an f-string, you can include anything including variables etc in the string


