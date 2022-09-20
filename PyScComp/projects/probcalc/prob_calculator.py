# class Hat:
#     def __init__(self, **data):
#         self.contents = []
#         for item in list(data.keys()):
#             for _ in list(data.values()):
#                 self.contents.append(item)
#
#     def __str__(self):
#         return str(self.contents)

def funciton(**data):
    contents = []
    i = 0
    for item in list(data.keys()):
        i = 0
        for _ in list(data.values())[i]:
            contents.append(item)

    print(contents)

funciton(black=6, red=4, green=3)

# hat = Hat(black=6, red=4, green=3)
# print(hat)
