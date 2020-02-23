letter=input("Enter a letter grade:\n ").upper()


my_dict = {'A': 4, 'B': 3, 'C': 2,'D':1,'F':0}

if letter in my_dict:
    print("The numeric value is",float(my_dict[letter]))
if len(letter)==2:
    if letter[0]=="A" or letter[0]=="F":
        my_dict[letter[0]]
    else:
        if letter[1]=="+":
            my_dict[letter[0]] += .3
        else:
            my_dict[letter[0]] -= .3
    print("The numeric value is", float(my_dict[letter[0]]))