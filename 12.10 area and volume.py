import math


class SodaCan:

    def setHeight(self, h):  #In OOP the functions are called METHODS
        self.h = h  # In OOP the variables is called ATTRIBUTES

    def setRadius(self, r):
        self.r = r

    def getSurfaceArea(self):
        return (2 * math.pi * self.r * self.h) + (2 * math.pi * self.r ** 2)

    def getVolume(self):
        return math.pi * self.r ** 2 * self.h


coke = SodaCan() #This is a INSTANCE for for the Manifestation-(Embodies) of the class
coke.setHeight(5)
coke.setRadius(5)
print(coke.getVolume())