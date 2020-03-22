a_str = input("Enter a string:\n ")
a_str = a_str.split()

print("Original list is", a_str)

final_list = []
for i in range(len(a_str)):
    if len(a_str[i]) >= 4:
        final_list.append(a_str[i])

print("Final list is", final_list)

