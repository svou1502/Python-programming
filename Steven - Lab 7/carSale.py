companies = []
sales = []

file_path = "C:/Users/Admin/Source/Repos/svou1502/Python-programming/Steven - Lab 7/carSale.csv"

with open(file_path, "r") as file:
    lines = file.readlines()

# Need to skip the header line

for x in range(1, len(lines), 2):
    company_line = lines[x - 1].strip()
    data_line = lines[x].strip()

    companies.append(company_line)

    data = data_line.split(',')[1:] # Skip the first field (Manufacturer)

    sales.append(list(map(int, data)))

# Print the extracted companies and sales

for i in range(len(companies)):
    print("Company", companies[i])
    print("Sales:", sales[i])
    print()


# Calculate sum of cars sold in each month


monthly_sum = sum(sales)

print("Monthly sales", monthly_sum)
