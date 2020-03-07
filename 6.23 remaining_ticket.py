# tickets = 20
# buyer = 0
# while tickets > 0:
#     print("There are currently",tickets,"tickets remaining.")
#     purchase = int(input("How many tickets would you like to purchase?\n "))
#     while purchase > 4 or purchase > tickets:
#         print("Sorry, you can't buy that many.")
#         break
#     else:
#         tickets = tickets - purchase
#         buyer = buyer + 1
#
#         print("The total number of buyers was", buyer)


# This is the correct way to do it
tickets = 20
remaining_ticket = tickets
total_buyer = 0

while remaining_ticket > 0:
    print("There are currently", remaining_ticket, "tickets remaining.")
    purchase = int(input("How many tickets would you like to purchase?\n "))

    while purchase > 4 or purchase > remaining_ticket or purchase < 1:
        print("Sorry, you can't buy that many.")
        purchase = int(input("How many tickets would you like to purchase?\n "))
    remaining_ticket = remaining_ticket - purchase
    total_buyer = total_buyer + 1


print("The total number of buyers was", total_buyer)
