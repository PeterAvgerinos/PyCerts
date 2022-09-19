class Hat:
    def __init__(self, **data):
        self.contents = []
        for _ in data:
            self.contents.append(list(data.keys()))
        print(self.contents)
hat = Hat(black=6, red=4, green=3)
print(hat)
