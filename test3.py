# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.05
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         Employee.num_of_emps += 1
#
#     def fullName(self):
#         return "{} {}".format(self.first, self.last)
#
#     def __repr__(self):
#         return "The first name is {}".format(self.first)
#
#     def __str__(self):
#         return "The last name is {}".format(self.last)
#
#     def apply_raise(self):
#         self.pay = self.pay * Employee.raise_amount
#
#
# emp1 = Employee("tom", "selleck", 5000)
# emp1.apply_raise()
# print(emp1.pay)
# emp2 = Employee("sam", "black", 3000)
# print(emp2.pay)
# print(emp2)


# class Transportation:
#     def move(self): # if the move function is called for the parent class but is not created and the subclass has it
#                     # than an error would appear b/c parent class can't inherit from sub class
#         return "My movement is not defined."
#
#     def __repr__(self):  # Over the print statement of print(x) to print hi instead of its memory location
#         return "hi"
#
#
# class Car(Transportation):
#     pass  # If pass was just in the class car than when the instance x = Car() is created
#            # and x.move() is called the print statement from the move method from the parent class is printed or returned
#
#     # def move(self):  # overrides the parent class move method
#     #     return "Press the accelerator on the car to move ahead"
#
#
# x = Car()
# print(x.move())
#
# # a = Transportation()
# # print(a.move())


# class Transportation(object):
#     def __init__(self, speed):
#         self.speed = speed
#
#
# class Car(Transportation):
#     def __init__(self, color, speed=55):
#         super().__init__(speed)
#         self.color = color
#
#     def __repr__(self):
#         return "A {} car with speed of {}".format(self.color, self.speed)
#
#
# my_car = Car("Blue", 65)
# print(my_car)


# class Transportation(object):
#     _how = "move"
#
#     def __init__(self, speed):
#         self._speed = speed
#
#     def getVelocity(self):
#         return "I can {} at {}".format(self._how, self._speed)
#
#
# class Bike(Transportation):
#     _how = "ride"  # override "_how”  in super class
#
#
# class Car(Transportation):
#     _how = "drive"  # override “_how”  in super class


# my_bike = Bike(75)
# print(my_bike._how)  # prints ride is the answer
# print(my_bike.getVelocity())  # answer I can ride at 75

# my_car = Car("65 mph")
# print(my_car.getVelocity())

# x = Transportation(20)
# print(x.getVelocity())


# def main():
#     i = 4
#     x = f1(i)
#     print(x+i)
#
# def f2(y):
#     n = 0
#     while n * n <= y:
#         n = n + 1
#     return n - 1
#
# def f1(a):
#     b = 0
#     for i in range(4):
#         i = f2(i)
#         print(i)
#         b = b + i
#     return b
#
# main()
#
# i = 10
# while i >= 5:
#     print("hi")
#     i = i - 1
#
# print("-")
#
# for i in range(10,-1,-2):
#     print("hi")

x = [3,2,4,3,5,6,7,8,9,0,1]
print(x[3:2])