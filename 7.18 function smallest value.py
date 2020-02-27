def smallest(x, y, z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    else:
        return z


def average(x, y, z):
    return (x + y + z) / 3


# print(smallest(10, 20, 30))
#
# print(smallest(17, 5, 11))
#
# print(smallest(23, 27, 4))
#
# print(average(10,20,30))
#
# print(average(17,5,11))
#
# print(average(23,27,4))
