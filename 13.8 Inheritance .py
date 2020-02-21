class Shoes:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def getType(self):
        return "shoe"

    def describe(self):
        return "{} {}: size {}".format(self.color, self.getType(), self.size)


class Boots(Shoes):
    def __init__(self, color, size, height):
        super().__init__(color, size)
        self._height = str(height)

    def getType(self):
        return "boots"

    def describe(self):
        return super().describe() + " height: " + self._height


class Sneakers(Boots):
    def __init__(self, color, size, height, lace_color):
        super().__init__(color, size, height)
        self._lace_color = lace_color

    def getType(self):
        return "sneakers"

    def describe(self):
        return super().describe() + " lace color: " + self._lace_color

x = Sneakers("Yellow", 7, 7, "blue")
print(x.describe())