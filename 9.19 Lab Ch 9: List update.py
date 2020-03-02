def main():
    print("This program requires a list with a minimum of 4 items.")
    new_list = []
    while True:
        item = input("Enter the item of the list, or 'Q' to quit:\n ").lower()
        if item == "q":
            break
        new_list.append(item)

    if len(new_list) < 4:
        print("Not enough items in the list - goodbye.")
    else:
        word = input("Enter a string:\n ")
        print(updateList(new_list, word))

def updateList(list1, wd):
    for i in range(1, 4):
        list1[i] = wd
    return list1

main()