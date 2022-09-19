class Hat:
    def __init__(self, **data):
        self.contents = []
        for item in data:
            for _ in range(0, data[item]):
                self.contents.append(list(data.values()).index(_))
        print(self.contents)
hat = Hat(black=6, red=4, green=3)
print(hat)
