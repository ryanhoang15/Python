#  Define constants.

##### Use the given variable "NAMES" as is, and DO NOT CHANGE its type, format and contents #######

NAMES = "January,  February March   April,  May      June     July     August   September October  November December        "

NAMES = NAMES.replace(","," ")
NAMES = NAMES.split()

num=int(input("Enter a number between 1 and 12: "))
if num < 1 or num >12:
    print("ERROR")
else:
    print(num,"is",NAMES[num-1])