def reverseString(a_str):
    a = a_str.split()
    new_list = []
    for i in range(len(a)):
        if int(i) % 2 != 0:
            x = a[i]
            new_list.append(x)

        else:
            x = a[i]
            y = x[::-1]
            new_list.append(y)

    return " ".join(new_list)


a_str = "Hello there, how are you"
print(reverseString(a_str))


# def reverseString(a_str):
#     a = a_str.split()
#     new_list = []
#     for i in range(len(a)):
#         if int(i) % 2 == 0:
#             x = a[i]
#             y = x[::-1]
#             new_list.append(y)
#
#         else:
#             x = a[i]
#             new_list.append(x)
#             # print(x)
#
#     return " ".join(new_list)
#
#
# a_str = "Hello there, how are you"
# print(reverseString(a_str))
