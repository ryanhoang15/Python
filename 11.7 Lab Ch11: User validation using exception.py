total = 0
while True:
    try:
        total += float(input("Enter a number, or 2 non-numbers to quit:\n "))
    except Exception as r:
        try:
            total += float(input("Enter a number, or another non-number to quit:\n "))
        except Exception as r:
            break
print("The total is",total)

# total=[]
# while True:
# try:
#     num = input("Enter a number, or 2 non-numbers to quit:\n ")
#     while not num.isdigit():
#         again = input("Enter a number, or another non-number to quit:\n ")
#         while not again.isdigit and not num.isdigit():
#             break
#         else:
#             total.append(int(again))
#     else:
#         total.append(int(num))
#         print("The total is", sum(total))
#
# except ValueError:
#         print("sorry")


