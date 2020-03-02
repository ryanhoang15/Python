price_chart = [[10, 10, 10, 10, 10],
               [20, 20, 20, 10, 10],
               [20, 20, 20, 10, 10],
               [20, 20, 20, 10, 10],
               [40, 30, 30, 20, 20]]

user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:\n ").lower()

while user_input != "q":
    if user_input == "s":
        row = int(input("Enter the row:\n "))-1
        col = int(input("Enter the column:\n "))-1
        if price_chart[col][row] != 0:
            print("Sold, for $", price_chart[col][row], "!")
            price_chart[col][row] = 0
        else:
            print("Sorry, that seat is not available.")

    elif user_input == "p":
        money = int(input("How much do you want to spend?\n "))
        found = False
        for x, col in enumerate(price_chart):
            for y, row in enumerate(col):
                if row == money and not found:
                    found = True
                    print("You can have seat", x+1, y+1)
                    price_chart[x][y] = 0
        if not found:
            print("Sorry, no tickets available at that price.")
    else:
        print("That wasn't a valid option.")
    user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:\n ").lower()
for x, row in enumerate(price_chart):
    for col in price_chart[x]:
        print(col, end=" ")
    print()





