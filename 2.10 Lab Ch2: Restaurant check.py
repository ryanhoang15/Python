price=float(input('Enter the charge for food:\n', ))
tax=.07
tip=.18
tip_amt = (price * tip)
tax_amt = (price * tax)
total=price+tip_amt+tax_amt
print('Tax: $',format(tax_amt,'.2f'),',','Tip: $',format(tip_amt,'.2f'),',','Total: $',format(total,'.2f'))