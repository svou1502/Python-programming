number = 1

while number <= 100:
    square = number * number
    print(f"Number: {number}, Square: {square}")
    
    if square > 2000:
        break
    
    number = number + 1

