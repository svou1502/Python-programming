# Take input from the user

initial_investment = float(input("Enter the initial investment in pounds: "))
target_value = float(input("Enter the target value in pounds: "))
interest_rate = float(input("Enter the interest rate in percentage: "))

# Convert the interest rate to a decimal
interest_rate /= 100

# Calculate the number of years it will take
years = 0
while initial_investment < target_value:
    initial_investment = initial_investment * (1 + interest_rate)
    years = years + 1

print(f"It will take {years} years for the investment to reach the target value.")
    

    