income=float(input("Enter the income: \n"))
tax_amt = 0
if income <= 50000:
    tax_amt = income * .01

elif income > 50000 and income <= 75000:
    income = income - 50000
    tax_amt = 50000 * .01 + tax_amt
    tax_amt = income * .02 + tax_amt


elif income > 75000 and income <= 100000:
    income = income - 50000
    tax_amt = 50000 * .01 + tax_amt
    income = income - 25000
    tax_amt = 25000 * .02 + tax_amt
    tax_amt = income * .03 + tax_amt


elif income > 100000 and income <= 250000:
    income = income - 50000
    tax_amt = 50000 * .01 + tax_amt
    income = income - 25000
    tax_amt = 25000 * .02 + tax_amt
    income = income - 25000
    tax_amt = 25000 * .03 + tax_amt
    tax_amt = income * .04 + tax_amt

else:
    income = income - 50000
    tax_amt = 50000 * .01 + tax_amt
    income = income - 25000
    tax_amt = 25000 * .02 + tax_amt
    income = income - 25000
    tax_amt = 25000 * .03 + tax_amt
    income = income - 150000
    tax_amt = 25000 * .04 + tax_amt
    tax_amt = income * .05 + tax_amt

print(tax_amt)