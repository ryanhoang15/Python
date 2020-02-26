a_string=input("Enter a string consisting of alphabetic characters with \"$\": \n")
'''
for i in range (len(a_string)-1,-1,-1):
    if a_string[i]=="$":
        if i==0:
           a_string = string[:i]
            break
    else:
        a_string = a_string[:i+1]
        break
print(a_string)
'''

# for i in range (len(a_string)-1,-1,-1):
#     if a_string[i]!="$":
#         print(a_string[:i+1])
#         break

while a_string.endswith("$"):
    a_string = a_string[:len(a_string)-1]
print(a_string)

