def Main():

    print(gcd(91, 287))
    # print(gcd(17, 22))
    # print(gcd(36, 24))


def gcd(num1, num2):
    #formula a = bq + r
    # a = num1
    # b = num2
    # if num1 < num2:
    #     a = num2
    #     b = num1
    #
    # remainder = 0
    # while b > 0:
    #     remainder = a % b
    #     a = b
    #     b = remainder
    #
    # return a

    if num2 == 0:
        return num1
    else:
        a = num2
        b = num1 % num2
        return gcd(a, b)


Main()






