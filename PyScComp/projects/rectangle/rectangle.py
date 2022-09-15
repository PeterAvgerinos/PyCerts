class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.heigth = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_area(self):
        return self.width*self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)** .5)

    def get_picture(self):
        string = ""
        for _ in range(0, self.height):
            for _ in range(0, self.width):
                string += "*"
            string += "\n"
        return string


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        super().__init__(side, side)

r1 = Square(10)
print(r1)
print(r1.get_picture())
print(r1.get_perimeter())
print(r1.get_diagonal())
print(r1.get_area())
r1.set_side(2)
print(r1)
print(r1.get_picture())
print(r1.get_perimeter())
print(r1.get_diagonal())
print(r1.get_area())
