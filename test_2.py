# def steps_to_calories(steps):
#     print('FIXME: finish steps_to_calories')
#     return -1
#
# steps = int(input('Enter number of steps walked: '))
# # calories = steps_to_calories(steps)
# print(steps_to_calories(steps))
# # print('Calories:', calories)

# def hello ():
#     print("Hello there") # this would print the answer
#     return # this does nothing
#
# hello() # if it was print(hello()) the answer is Hello there
#                                                  None


# def hello (name):
#     print("Hello",  name)
#     return
#
# hello("Tim") # answer is Hello Tim
# "Tim" is the arg getting passed to the function hello parameter

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))

# def printNum(num):
#     print(num)
#
# a, b = 43, 21
# printNum(a), printNum(b)

# def cubeVolume(sideLength):
#     volume = sideLength** 3
#     # return volume  # return a value
#     return # return the value None as the answer
# print(cubeVolume(3))

# def cubeVolume(sideLength):
#     if(sideLength< 0):
#         return 0
#     volume = sideLength ** 3
#     return volume
#
# print(cubeVolume(-1)) # the answer is 0
# print(cubeVolume(3))  # the answer is 27
#
# def get_user_num():
#     print("FIXME: Finish get_user_num()")
#     return -1
# print(get_user_num())

# x = "global x"
# def test():
#     y = "local y"
#     print(y) # this prints local y as answer
# test()

# x = "global x"
# def test():
#     y = "local y"
#     print(x) # this prints global x
# test()

# x = "global x"
# def test():
#     x = "local x"
#     print(x) # this prints local x
#
# test()
# print(x) # this prints global x

# x = "global x"
# def test():
#     global x
#     x = "local x"
#     print(x) #this prints local x with or without the global statement
#
# test()
# print(x) #this now prints local x b/c the global statement is declare in the function

# # x = "global x"
# def test():
#     # global x
#     x= "local x"
#     print(x)
# test()
# print(x) # this gets an Error since there is no global variable

# def test(z):
#     x = "local x"
#     print(x) #this prints local x as the answer
#
# test('local z')
# print(z) # this gets an Error b/c z is not defined

# import builtins
# print(dir(builtins)) # give you the list of the attributes of given obj
# m = min([5, 6, 1, 3, 7])
# print(m)

# def min():
#     pass
# m = min([5, 6, 1, 3, 7])
# print(m) # "Type Error" b/c function def min takes 0 positional arguments but 1 was given

# def outer():
#     x = "outer x"
#     def inner():
#         x = "inner x"
#         print(x) #this prints inner x first
#     inner()
#     print(x) #this prints outer x second
# outer()

# def outer():
#     # x = "outer x“
#     def inner():
#         x = "inner x"
#         print(x)  # this gets the answer inner x
#
#     inner()
#     print(x)  # THIS WILL gets u an error since x is not defined and in this case it is commented out
#
# # Without the outer() function noting prints or execute

# def f1():
#  print('a', end='')
#  return 'b'
#
# def f2():
#  print('c', end='')
#  f3()
#  print('e', end='')
#
# def f3():
#  print('f', end='')
#  f1()
#  print('g', end='')
#
# f2() # the answer cfage

#
# def powerOf(x, p):
#     global power  # the global statement needs to be inside the function in order for it to work
#                   # if there is no global statement inside the function there needs to be a local variable declare
#                    # inside the function for it to work
#     power = x ** power
#     return power
#
#
# power = 3
# print(power)  # the answer is 3
# print(powerOf(10, 2))  # the answer is 1000
# print(power)  # the answer is 1000

# m = 0
# x = 0
# while x < 4:
#     y = 1
#     while y < 3:
#         m = y + m
#         y = y + 1
#         if x + y == 4:
#             continue
#         x = x + 1
# print(m) # the answer is 9

# m =0
# my_str = "Philadelphia"
# for char in my_str:
#     if char == 'h' or char == 'i':
#         continue
#     if char =='e':
#         break
#     m = m + 1
# print(m)  # 4 is the answer

# x = "university"
# print (x[0:4])   # univ is the answer
# print(x[5:0:-2]) # rvn is the answer

# age = int(input("Enter your age: "))
# if age < 10:
#     print("Child", end=',')
# if age < 30:
#     print("Adult", end=',')
# if age < 70:
#     print("Old", end=',')
# if age < 100:
#     print("Impressively Old", end=',') #the answer is old, Impressively old,


# x="Hi there, how are you?"
# if 'you' in x:
#     print('yes') #this is the answer
# else:
#     print('no')

# my_string="hello"
# if 10 % 5:  # has to == 0 in order for it to print the answer
#     print('true')
# elif "le" not in my_string:
#     print('false') # this is the answer
# else:
#     print('none')


# my_str = "university"
# count = 0
# for char in my_str:
#     if char == "i":
#         continue
#     else:
#         count += 3
# print(count) # the answer is 24

# x = 'e'
# y = 3
# if x in 'computer science':
#     y = y + 5
# else:
#     y = y + 10
# if "x" in 'computer science':
#     y = y + 20
# else:
#     y = y + 40
#
# print(y)  # the answer is 48

# m = 0
# my_str1 = 'cat'
# my_str2 = 'pet'
# for char1 in my_str1:
#     for char2 in my_str2:
#         if char1 != char2:
#             m = m + 1
# print(m)  # the answer is 8


# def square(x):
#     y = x * x
#     return y
#
#
# def sumOfSquares(x, y, z):
#     a = square(x)
#     b = square(y)
#     c = square(z)
#     return a + b + c
#
#
# def main():
#     a = -5
#     b = 2
#     c = 10
#     result = sumOfSquares(a, b, c)
#     print(result) # answer is 129
#
#
# main()

# x = "university"
# print(x[:-1]) # answer is universit
# print(x[::-1]) # answer is ytisrevinu b/c [::-1] prints it backs wards


# earthquake = 7.5
# if earthquake>= 8.0 :
#     print("Most structures fall")
# if earthquake >= 7.0 :
#     print("Many buildings destroyed") # this is the answer
# if earthquake >= 6.0 :
#     print("Many buildings damaged, some collapse") # this is the answer
# if earthquake >= 4.5 :
#     print("Damage to poorly constructed buildings") # this is the answer

# age = int(input("Enter your age: "))
# if age < 10:
#     print("Child", end=',')
# if age < 30:
#     print("Adult", end=',')
# if age < 70:
#     print("Old", end=',')
# if age < 100:
#     print("Impressively Old", end=',')

# x="Hi there, how are you?"
# if 'you' in x:
#     print('yes')
# else:
#     print('no')

# def hello():
#     # print("hello")
#     x = "hello"
#     return "hi"
#
# print(hello())

# scores = [10, 9, 7, 4, 5]
# values = scores
# print(values)
# print(scores)

# my_list= [[5, 13], [50, 75, 100]]
# print(my_list[0])
# print(my_list[1])


# num_guesses = int(input())
# user_guesses = []
# for i in range(num_guesses):
#     num = int(input())
#     user_guesses.append(num)
#
# print('user_guesses:', user_guesses)


# user_input = input()
# test_grades = list(map(int, user_input.split())) # contains test scores
# sum_extra = -999 # Initialize 0 before your loop
# sum_extra = 0
# for i in range(len(test_grades)):
#     if test_grades[i] > 100:
#         sum_extra = sum_extra + test_grades[i] - 100
#
# print('Sum extra:', sum_extra)


# user_input = input()
# hourly_temperature = user_input.split()
#
# temp = []
# for i in range(len(hourly_temperature)):
#     if i == len(hourly_temperature)-1:
#         x = hourly_temperature[i] + " "
#         temp.append(x)
#     else:
#         temp.append(hourly_temperature[i])
#
# print(" -> ".join(temp))


# # squars=[]
# # for i in range(1, 101):
# #     squars.append(i**2)
# # print(squars)
# squars_2 =[i**2 for i in range(1, 101)]
# print(squars_2)


# user_input= input()
# lines = user_input.split(',')
# # # This line uses a construct called a list comprehension, introduced elsewhere,
# # # to convert the input string into a two-dimensional list.
# # # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
# #
# mult_table = [[int(num) for num in line.split()] for line in lines]
#
# for row in mult_table:
#     # print(" | ".join([str(col) for col in row]))
#     for col in row:
#         x = str(col)
#         print(' | '.join(x))


# currency = [[1.00, 5.00, 10.0],[0.75, 3.77, 7.53],[0.65, 3.25, 6.50]]
#
# for row in currency:
#     for cell in row:
#         print(cell, end=' ')
#     print()


# my_list = [[5, 10, 15], [2, 3, 16], [100]]
# sum_list  = sum([sum(row) for row in my_list])
# print(sum_list)


school = {}
school['John'] = {'Math':'A','Chemistry' : 'A'}
school['Jim'] = {'Math':'B','English': 'B'}
#
# for name, info in school.items():
#     print(name + ":")
#     for subject, grade in info.items():
#         print('\t', subject, grade)
#       # answer is John:
#     # 	                Math A
#     # 	                Chemistry A
#     #             Jim:
#     # 	                Math B
#     # 	                English B
#     #            b/c there is not end=" "

# for name, info in school.items():
#     print(name, info)   # answer is John {'Math': 'A', 'Chemistry': 'A'}
                                  # Jim {'Math': 'B', 'English': 'B'}

# my_dict = {'Ahmad': 1, 'Jane': 42}
# number = my_dict.get("Chad", 411)
# print(my_dict.get('Jane', 411))
# print(number)


# list_1 = [1, 2, 3, 4]
# list_2 = ["Apple", 23, "po"]
# list_2[0] = 14
# print(list_1 + list_2) # answer is [1, 2, 3, 4, 14, 23, 'po']
# list_2[len(list_2):] = [9] # adds it to the end of list 2
# del list_2[1]
# print(list_2) #answer is [14, 'po', 9]

#
# friends = ["Harry", "Emily", "Bob", "Cari", "Emily"]
#
# n = friends.index("Emily")
# n2 = friends.index("Emily",n+1)
# print(n) # answer is 1
# print(n2) # answer is 4


# x = ["Apple"]
# print(x*12)  # answer is ['Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple', 'Apple']
#
# a = ["pie"]*12
# print(a)

# contacts = { "Fred": 7235591, "Mary": 3841212, "Bob": 3841212, "Sarah": 2213278 }
# # print(contacts)
#
# new_contacts = dict(contacts)
# # new_contacts["Fred"] = 0 # answer is {'Fred': 0, 'Mary': 3841212, 'Bob': 3841212, 'Sarah': 2213278}
#                         #  if new_contacts is changed
# contacts["Fred"] = 0
# print(new_contacts) # answer is {'Fred': 7235591, 'Mary': 3841212, 'Bob': 3841212, 'Sarah': 2213278}
                     # since contacts is being change and u print out new_contacts
# num = contacts.pop("Fred")
# print(num)

# entries = { "rocky road" : [6700.10,5012.45,7056.50] ,
#             "strawberry" : [9285.15,8276.10,8705.00]  }
# for key,value in entries.items():
#     print(key,value)

# n = {12:12,122:"ryan"}
# a = {24:"black"}
# n.update(a) # combines dict a with dict n
# print(n) # {12: 12, 122: 'ryan', 24: 'black'}

# a_str = "CECS174CLASS"
# print(a_str[7:1:-2])  # answer is C7S
#

# values = [1, 2, 3, 4, 5]
# moreValues = values
# moreValues[3] = 6
# print(values) # if moreValues or values is updated than both get the new list [1, 2, 3, 6, 5]

# states = ["Alaska", "Hawaii", "Florida", "Maine", "Ohio", "Florida"]
# states.pop()
# print(states)

# my_list = []
# for x in range(2, 11, 3):
#     my_list.append(x)
# print(my_list)  # ANSWER IS [2, 5, 8]

# fruit = {"Apple": "Green", "Banana": "Yellow"}
# fruit["Plum"] = "Purple" # adds it the the fruit list
# print(fruit)  # answer is {'Apple': 'Green', 'Banana': 'Yellow', 'Plum': 'Purple'}

# days = {}
# days["February"] = [28, 29]
# print(days) # answer is {'February': [28, 29]}

# a_list = [81,82,83]
# b_list = [81,82,83]
# print(a_list == b_list, a_list is b_list)
# b_list = a_list # this has to be here in order for print(b_list) to get answer [5, 82, 83]
#                #  if not there than answer would be [81, 82, 83]
# print(a_list == b_list, a_list is b_list) # is is memory location
# a_list[0] = 5
# print(b_list)

# a = [[1,2,3], [7, 8]]
# for row in a:
#     for col in row:
#         print(row, col)  # answer is [1, 2, 3] 1
#                                  #  [1, 2, 3] 2
#                                  #  [1, 2, 3] 3
#                                  #  [7, 8] 7
#                                  #  [7, 8] 8

# values = [1,2,3,4,5]
# moreValues = values
# moreValues[3] = 6
# print(values)

# a = ["sam"]
# x = a
# print(a == x, a is x)


# try:
#     x = int(input("Enter the numerator "))
#     y = int(input("Enter the denominator "))
#     print("The result is ", x/y)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError as x:
#     print("Need to enter a number: ",x)
# else:
#     print("Good job")
# finally:
#     print("Thanks for playing")

# try:
#     l = int(input("Enter the length of the box "))
#     if l <= 0:
#         raise ValueError("Length must be a positive integer")
#     w = int(input("Enter the width of the box "))
#     if w <= 0:
#         raise ValueError("Width must be a positive integer")
#     area = l * w
#     print ("Area is ",area)
# except ValueError as e:
#     print("Value Error:",e)

# infile = open("io_text.txt", "r")
# for sentence in infile :
#    print(sentence)
# infile.close()
# infile= open("io_text.txt", "r")
# for x in infile :
#    print(x)
