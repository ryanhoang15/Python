sentence = input("Enter a sentence: \n")
v=['a', 'i', 'o', 'u']
for b in v:
    sentence=sentence.replace(b, 'e')
V=['A', 'I', 'O', 'U']
for c in V:
    sentence=sentence.replace(c, 'E')
print(sentence)