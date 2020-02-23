string = input("Enter a string:\n ")
print("The new string: ", end=" ")

for i in range(len(string), 0, -1):
    if string[i-1] != " ":
        print(string[i-1], end="")

