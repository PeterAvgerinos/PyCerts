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

r1 = Rectangle(10, 3)
print(r1)
print(r1.get_area())
print(r1.get_picture())

r1.set_height(4)
r1.set_width(4)
print(r1)

print(r1.get_diagonal())
print(r1.get_perimeter())
print(r1.get_picture())
