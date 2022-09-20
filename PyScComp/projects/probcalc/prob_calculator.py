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
    for item in list(data.keys()):
        for _ in list(data.values()):
            contents.append(item)

    print(contents)

funciton(black=6, red=4, green=3)

# hat = Hat(black=6, red=4, green=3)
# print(hat)
