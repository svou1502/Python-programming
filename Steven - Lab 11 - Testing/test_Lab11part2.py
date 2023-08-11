def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

# Main function for user input/output - this needs to be defined
# otherwise pytest tries to test for input/output
def main():
    user_input = int(input("Enter a number: "))
    result = fact(user_input)
    print(f"The factorial is: {result}")

# Test the factorial function
def test_factorial():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(4) == 24





