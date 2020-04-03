phone_number = input("Enter a 10 digit phone number:\n")
area_code = phone_number[0:3]
first_3_num = phone_number[3:6]
last_4_num = phone_number[-4:]
phone_num = "(" + area_code + ")" + first_3_num + '-' + last_4_num
print(phone_num)