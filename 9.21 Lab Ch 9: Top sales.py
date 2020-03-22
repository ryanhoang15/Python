# customer = []
# amount = []
# maxi = 0
# while True:
#     name = input("What is the name of the customer?\n ")
#     if name == "":
#         break
#     customer.append(name)
#     money = input("What is the purchase amount (numbers only) ?\n ")
#     while not money.isdigit():
#         money = input("What is the purchase amount (numbers only) ?\n ")
#     amount.append(int(money))
# if name in customer:
#     for i in range(len(customer)):
#         if customer[i] == name:
#             amount[i] = amount[i] + money
#
#
# for i in range(len(amount)):
#     if amount[i] > maxi:
#         maxi = amount[i]
#         x = i
# print(maxi, customer[x])

customer = []
amount = []
maxi = 0
while True:
    name = input("What is the name of the customer?\n ")
    if name == "":
        break

    money = input("What is the purchase amount (numbers only) ?\n ")
    while not money.isdigit():
        money = input("What is the purchase amount (numbers only) ?\n ")
    amount.append(int(money))

    if name in customer:
        for i in range(len(customer)):
            if customer[i] == name:
                amount[i] = amount[i] + int(money)
                amount.append(amount[i])
    else:
        customer.append(name)

for i in range(len(amount)):
    if amount[i] > maxi:
        maxi = amount[i]
        x = i
print(customer[x],"spent $",maxi)