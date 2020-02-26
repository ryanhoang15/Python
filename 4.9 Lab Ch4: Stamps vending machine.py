# Define the price of a stamp in pennies.
FIRST_CLASS_STAMP_PRICE = 44

# Compute and print the number of stamps to dispense.
dollars = float(input("Enter number of dollars: \n"))
stamps = dollars * 100 // FIRST_CLASS_STAMP_PRICE
change = dollars * 100 % FIRST_CLASS_STAMP_PRICE
print("First class stamps", int(stamps))


quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5
change = change % 5

print("Your change is:",'\n',
int(quarters),'quarters','\n',
int(dimes),'dimes','\n',
int(nickels),'nickels','\n',
int(change),'pennies')