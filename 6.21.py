text = input("Enter a string: ")
uppercase = []
for i in text:
    if i.isupper():
        uppercase.append(i)
        x = "".join(uppercase)
print("Only uppercase letters in the string :", x)
second_letter = []
for i in range(len(text)):
    if i % 2 == 1:
        second_letter.append(text[i])
        x = "".join(second_letter)
print("Every second letter/number in the string:",x)
under_score = []
v = ['A',"E","I","O","U","a","e","i","o","u"]
for i in text:
    if i in v:
        under_score.append("_")
    else:
        under_score.append(i)
    x = "".join(under_score)
print("Replacing all the vowels with underscore:", x)
counter = 0
digit = []
for i in text:
    if i.isdigit():
        counter = counter + 1

print("The total number of digits in the string:", counter)
position = []
for i in range(len(text)):
    if text[i] in v:
        vowel = str(i)
        position.append(vowel)
        x = "".join(position)
print("The positions of all the vowels in the string:", x)
