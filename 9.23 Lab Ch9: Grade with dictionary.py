dict = {}
while True:
    user = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit?\n ").lower()
    if user == "q":
        print("Goodbye!")
        break
    elif user == "a":
        name = input("Enter the name of the student: \n")
        if name in dict:
            print("Sorry, that student is already present.")
        else:
            grade = input("Enter the student's grade: \n")
            dict[name] = grade

    elif user == "r":
        remove = input("What student do you want to remove? \n")
        if remove not in dict:
            print("Sorry, that student doesn't exist and couldn't be removed. \n")
        else:
            del dict[remove]

    elif user == "m":
        modify = input("Enter the name of the student to modify:\n ")
        if modify not in dict:
            print("Sorry, that student doesn't exist and couldn't be modified.")
        else:
            print("The old grade is", dict[modify])
            new_grade = input("Enter the new grade:")
            dict[modify] = new_grade

    elif user == "p":
        if dict == {}:
            print("No record found!")
        else:
            for name in sorted(dict.keys()):
                print(name, dict[name])
    else:
        print("Sorry, that wasn't a valid choice.")
