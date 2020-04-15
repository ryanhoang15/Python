file_name = input("Enter the input file name:\n ")
in_file = open(file_name, "r")
ch = 0
words = 0
total = 0
for line in in_file:
    total = total + 1
    ch = ch + len(line)
    word = line.split()
    words = word + len(word)

print("The file contains", ch, "characters,", words, "words and", total, "lines")
