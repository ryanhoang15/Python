num_1=input("Enter the first number:\n ")
num_2=input("Enter the second number:\n ")
num_3=input("Enter the third number:\n ")

if num_1 == num_2 and num_2 == num_3:
    print("all the same")
elif num_1 != num_2 and num_2 != num_3:
    print("all different")
else:
    print("neither")