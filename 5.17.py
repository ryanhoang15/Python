first_time = input("Enter the first time as hours:minutes in 24 hour format:\n ")
second_time = input("Enter the second time as hours:minutes in 24 hour format:\n ")

a = first_time.split(":")
b = second_time.split(":")

# hour_1 = first_time[0:2]
# hour_2 = second_time[0:2]
# minute_1 = first_time[3:5]
# minute_2 = second_time[3:5]

if a[0] < b[0]:

    print("time1 comes first")

elif a[0] == b[0]:

    if a[1] < b[1]:
        print("time1 comes first")

    elif a[1] == b[1]:
        print("time1 and time2 are the same")

else:
    print("time2 comes first!")
