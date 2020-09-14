#int functionName(int something, double somethingElse)

#def functionName(something,somethingElse)


# create a function that returns the larger number
# if the two numbers are equal, then return "equal"
'''
def maximum(num1,num2):
    if num1 > num2:
        return num1

    elif num2 > num1:
        return num2

    else:
        return "equal"

test1 = maximum(1,3)
print(test1, type(test1))

test2 = maximum(3,1)
print(test2, type(test2))

test3 = maximum(3,3)
print(test3, type(test3))
'''

class Peson:
    #constructor
    #def __init__
    def __init__(self,name,age):
        # self.name is the class's variable
        # name is a temporary use variable
        self.name = name
        self.age = age


    # Java toString()
    # c++ << operator overloading cout
    # returns the string that will print if using
    # the print function elsewhere
    def __str__(self):
        string = "name " + self.name
        string += "\nage: " + str(self.age)
        return string


p1 = Peson("Sam",20)
print(p1)


