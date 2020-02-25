user_response = input("Enter a positive integer between 1 and 7: ")
number = int(user_response)
days = ['MONDAY', 'TUESDAY', 'WENSDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

if number < 1 or number > 7:
    print("ERROR")
else:
    print(days[number - 1])

