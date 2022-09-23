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
        drawn = []
        if count > len(self.contents):
            return self.contents
        else:
            for _ in range(0, count):
                randint = random.randint(0, len(self.contents) - 1)
                drawn.append(self.contents[randint])
            return drawn

    def contains(self, other):
        j = 0
        temp = self
        for i in range(0, len(other.contents)):
            if other.contents[i] in temp.contents:
                temp.contents.remove(other.contents[i])
                j += 1
        return j == len(other.contents)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    hat2 = Hat(**expected_balls)
    for _ in range(0, num_experiments):
        drawn = hat.draw(num_balls_drawn)
        if drawn.contains(hat2):
            m += 1
    probability = m/num_experiments
    return probability

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
exp = {"red":2, "green":1}
hat3 = Hat(**exp)
print(hat3)

