def validate(x):
    if x[0] in grades:
        if len(x) == 2:
            if x[1] == "+" or x[1] == "-":
                return True
        elif len(x) == 1:
                return True
    return False

grades = ["a","b","c","d","f"]
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
            try:
                grade = input("Enter the student's grade: \n").lower()
                if not validate(grade):
                    raise ValueError("Invalid grade, did not add record. Valid grades are 'A','B','C','D','F' !")
                dict[name] = grade
            except ValueError as e:
                print(e)

    elif user == "r":
        try:
            remove = input("What student do you want to remove? \n")
            if remove not in dict:
                raise ValueError("Sorry, that student doesn't exist and couldn't be removed. \n")
            else:
                del dict[remove]
        except ValueError as e:
            print(e)

    elif user == "m":
        modify = input("Enter the name of the student to modify:\n ")
        try:
            if modify not in dict:
                raise ValueError("Sorry, that student doesn't exist and couldn't be modified.")
            else:
                print("The old grade is", dict[modify])
                new_grade = input("Enter the new grade:").lower()
                if not validate(new_grade):
                    raise ValueError("Invalid grade, did not modify record. Valid grades are 'A','B','C','D','F' !")
                dict[modify] = new_grade
        except ValueError as e:
            print(e)

    elif user == "p":
        if len(dict) >= 1:
            for name in sorted(dict.keys()):
                print(name, dict[name])
    else:
        print("Sorry, that wasn't a valid choice.")


