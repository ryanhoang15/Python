def Main():
    while True:
        binary = input("Enter a binary: ")
        print(binary2Dec(binary))
        print("Would you like to enter again (Y/N): ", end="")
        answer = input().lower()
        if answer == "n":
            print("Bye Bye")
            break



def power(base, pow):
    if pow == 0:
        return 1

    elif pow == 1:
        return base

    else:
        return power(base, pow - 1) * base


def binary2Dec(binary):
    length = len(binary)
    pow = 0
    decimal = 0
    base = 2
    for i in range(length -1,-1,-1):
        if binary[i] == "1":
            decimal = decimal + power(base,pow)
            pow = pow + 1
            length = length - 1

        else:
            pow = pow + 1

    return decimal

Main()

