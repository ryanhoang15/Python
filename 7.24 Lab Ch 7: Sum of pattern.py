def sumOfPattern(num1,num2):
    total = 0
    value = ""
    for i in range(num2):
        value = value + str(num1)
        total = total + int(value)
    return total

