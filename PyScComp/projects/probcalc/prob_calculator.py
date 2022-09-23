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
        if count > len(self.contents):
            return self.contents
        else:
            for _ in range(0, count):
                randint = random.randint(0, len(self.contents) - 1)
                self.contents.pop(randint)
            return self.contents

hat = Hat(black=6, red=4, green=3)
print(hat)
hat.draw(4)
print(hat)
