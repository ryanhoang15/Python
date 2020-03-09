num1 = input("Enter the first set of integer values separated by space:\n ")
num2 = input("Enter the second set of integer values separated by space:\n ")
list1 = num1.split()
list2 = num2.split()
list1.sort()
list2.sort()

print("Checking if the two lists are the same :")
if num1 == num2:
    print("Yes, they are.")
else:
    print("They are not.")

print("Checking if the two lists contain the same elements:")

if list1 == list2:
    print("Yes, they are.")
else:
    print("They are not.")