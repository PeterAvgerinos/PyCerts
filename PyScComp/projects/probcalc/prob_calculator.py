import copy
import random

class Hat:
    def __init__(self, **data):
        self.contents = []
        self.datakeys = list(data.keys())
        self.datavalues = list(data.values())
        for item in range(0, len(self.datakeys)):
            for _ in range(0 ,self.datavalues[item]):
                self.contents.append(self.datakeys[item])

    def __str__(self):
        return str(self.contents)

    def draw(self, count):
        print(self.contents)
        for _ in range(0, count):
            randint = random.randint(0, len(self.contents))
            self.contents.pop(randint)
        print(self.contents)


hat = Hat(black=6, red=4, green=3)
print(hat)
hat.draw(3)
