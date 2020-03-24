##
#  Print the first 3 letters of a string, followed by ..., followed by the  last 3 letters of a string.
##

word = input("Enter a word with longer than 8 letters: ")

### Your code goes here ###
first_3_letters=word[0:3]
last_3_letters=word[-3:]
print("The new word is {0}...{1}".format(first_3_letters, last_3_letters))