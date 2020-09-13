class rectangle:

    def __init__(self, h=1.0, w=1.0):
        self.height = h
        self.width = w

    # def setRect(self,h,w):
    #     self.height = h
    #     self.width = w

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return (2 * self.height) + (2 * self.width)


print("Stats of the Rectangle with no Arguments")
rect1 = rectangle()
print("Width: " + str(rect1.getWidth()))
print("Height: " + str(rect1.getHeight()))
print("Area: " + str(rect1.getArea()))
print("Perimeter: " + str(rect1.getPerimeter()))

print("\nStats of the Second Rectangle")
rect2 = rectangle(40, 4)
print("Width: " + str(rect2.getWidth()))
print("Height: " + str(rect2.getHeight()))
print("Area: " + str(format(rect2.getArea(), ".2f")))
print("Perimeter: " + str(rect2.getPerimeter()))

print("\nStats of the Third Rectangle")
rect3 = rectangle(35.9, 3.5)
print("Width: " + str(rect3.getWidth()))
print("Height: " + str(rect3.getHeight()))
print("Area: " + str(format(rect3.getArea(), ".2f")))
print("Perimeter: " + str(rect3.getPerimeter()))
