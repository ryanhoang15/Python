a_str =input("Enter a string: \n").lower()

b_str = a_str[::-1]


if b_str == a_str:
    print("palindrome")
else:
    print("different word")