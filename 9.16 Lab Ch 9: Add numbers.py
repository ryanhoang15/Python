# i = 0
# list1 = []
# while i < 5:
#     num = float(input("Please enter a floating point number:\n "))
#     if num in list1:
#         print("The number is already in the list!")
#         continue
#     else:
#         list1.append(num)
#     i = i + 1
#
# print("The numbers are:", list1)

i = 0
list1 = []
while i < 5:
    num = float(input("Please enter a floating point number:\n "))
    if num not in list1:
        list1.append(num)
    else:
        print("The number is already in the list!")
        continue
    i = i + 1

print("The numbers are:", list1)


list1 = []
while len(list1) < 5:
    num = float(input("Please enter a floating point number:\n "))
    if num not in list1:
        list1.append(num)
    else:
        print("The number is already in the list!")

print("The numbers are:", list1)