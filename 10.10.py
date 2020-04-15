file_name = input("Enter the input file name: ")
in_file = open(file_name, "r")
other_file = open("100-most-common-words.txt","r")

other_file = other_file.readlines()


list_1 = []
for line in in_file:
    line = line.strip()
    line = line.split()
    for word in line:
        counter = 0
        for common in other_file:
            common = common.strip()
            if word != common:
                counter = counter + 1
        if counter == 100:
            list_1.append(word)

print("The following words are not in the 100 most common word list:")
for i in list_1:
    print(i)

# Another way to print it out

# print("The following words are not in the 100 most common word list:")
# for line in in_file:
#     line = line.strip()
#     line = line.split()
#     for word in line:
#         counter = 0
#         for common in other_file:
#             common = common.strip()
#             if word != common:
#                 counter = counter + 1
#         if counter == 100:
#             print(word)