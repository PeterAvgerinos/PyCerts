# class Hat:
#     def __init__(self, **data):
#         self.contents = []
#         for item in data:
#             i = 0
#             for _ in range(0, data[item]):
#                 self.contents.append(list(data.keys())[i])
#             i += 1
#         print(self.contents)
# hat = Hat(black=6, red=4, green=3)
# print(hat)

def funciton(**data):
    contents = []
    for item in data:
        i = 0
        for _ in range(0, data[item]):
            contents.append(list(data.keys()))
        i += 1
    print(contents)

funciton(black=6, red=4, green=3)
