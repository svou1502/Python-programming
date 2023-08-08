min_value = 1
max_value = 100
attempts = 3

while attempts > 0:
    user_input = input(f"Enter an integer between {min_value} and {max_value}: ")

    if user_input.isdigit(): # You can use isdigit() to check that the number is not a string
        num = int(user_input)
        if min_value <= num <= max_value:
            print(f"You entered: {num}")
            break
        else:
            print("Value is outside the specified range.")
    else:
        print("Invalid input. Please enter an integer.")

    attempts -= 1

if attempts == 0:
    print("None")
