word = input("Enter a word:\n ")
middle = len(word) // 2

if len(word) % 2 == 0:
    answer = word[middle-1] + word[middle]
else:
    answer = word[middle]

print("Middle:",answer)