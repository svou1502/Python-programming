def getIncomeTax(salary):
    personal_allowance = 11850
    tax_rate20pc = 34500
    tax_rate40pc = 150000

    if salary <= personal_allowance:
        return 0

    elif salary <=tax_rate20pc:
        taxed_20_amount = (salary - personal_allowance) * 0.2
        return taxed_20_amount

    elif salary <= tax_rate40pc:
        taxed_20_amount = (tax_rate20pc - personal_allowance) * 0.2
        taxed_40_amount = (salary - taxed_20_amount) * 0.4
        total_tax = taxed_20_amount + taxed_40_amount
        return total_tax

    elif salary > tax_rate40pc:
        taxed_20_amount = (salary - personal_allowance) * 0.2
        taxed_40_amount = (salary - taxed_20_amount) * 0.4
        taxed_45_amount = (salary - taxed_40_amount) * 0.45
        total_tax = taxed_20_amount + taxed_40_amount + taxed_45_amount
        return total_tax


# Main body of program - get salary

salary = float(input("Enter your salary "))
income_tax = getIncomeTax(salary)

print(f"Your income tax is: {income_tax:.2f} pounds")
