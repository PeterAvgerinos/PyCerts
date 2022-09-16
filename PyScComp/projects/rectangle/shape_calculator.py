class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.string = ""

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
        self.string = ""
        if self.height > 50 or self.width > 50:
            self.string = "Too big for picture."
            return self.string
        for _ in range(0, self.height):
            for _ in range(0, self.width):
                self.string += "*"
            self.string += "\n"
        return self.string

    def get_amount_inside(self, shape):
        numbers = self.get_area()//shape.get_area()
        return numbers

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        super().__init__(self.side, self.side)
