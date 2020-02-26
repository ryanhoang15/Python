# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + "." + last + "@gmail.com"
#         self.pay = pay
#
#     def fullname(self):
#         return "{} {} ".format(self.first, self.last)
#
#
# emp_1 = Employee("sam", "black", 50000)
# emp_2 = Employee("jenn", "white", 70000)
#
# # print("{} {}".format(emp_2.first,emp_2.last))
# print(emp_1.email)
# print(emp_2.first)
# print(emp.fullname())
# # print(emp_1)
# # print(emp_2)
#
# # emp_1.first = "sam"
# # emp_1.last = "black"
# # emp_1.email = "sam.black@gmail.com"
# # emp_1.pay = 50000
# #
# # emp_2.first = "jenn"
# # emp_2.last = "white"
# # emp_2.email = "jean.white@gmail.com"
# # emp_2.pay = 70000
# #
# # # emp_3.first = "sam"
# # # emp_3.last = "black"
# # # emp_3.email = "sam.black@gmail.com"
# # # emp_3.pay = 50000
# #
# # print(emp_1.first)
# # print(emp_2.first)

#
class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + "." + last + "@gmail.com"
        Employee.num_of_emps += 1

    # def __init__(self, first, last, pay = 90000):
    #     self.first = first
    #     self.last = last
    #     self.pay = pay
    #     self.email = first + "." + last + "@gmail.com"
    #     Employee.num_of_emps += 1

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def set_raise(self):
        self.pay = self.pay + self.raise_amount


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lan):
        super().__init__(first, last, pay)
        self.prog_lan = prog_lan

    def get_salary(self):
        return self.pay