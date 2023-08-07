# Input two float numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print the input numbers
print("You entered:", num1, "and", num2)

# Display calculator menu
print("This is your Calculator Menu:")
print("1. Add            +")
print("2. Subtract      -")
print("3. Multiply      *")
print("4. Divide         /")
print("5. Square       s")

# Ask the user to choose an operation
operation = input("Choose a mathematical operation (1/2/3/4/5): ")

# Perform the selected operation
if operation == '1':
    result = num1 + num2
    print("Adding these two numbers equals:", result)
elif operation == '2':
    result = num1 - num2
    print("Subtracting these two numbers equals:", result)
elif operation == '3':
    result = num1 * num2
    print("Multiplying these two numbers equals:", result)
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print("Deviding these two numbers equals:", result)
    else:
        print("Cannot divide by zero.")
elif operation == '5':
    result1 = num1 * num1
    result2 = num2 * num2
    print("The square of the first number equals:", result1)
    print("The squre of the second number equals:", result2)
else:
    print("Invalid choice. Please choose a valid operation.")
