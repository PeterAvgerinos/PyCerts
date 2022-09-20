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
    datakeys = list(data.keys())
    datavalues = list(data.values())
    for item in range(0, len(list(data.keys()))):
        for _ in range(0 ,datavalues[item]):
            contents.append(datakeys[item])
    print(contents)

funciton(black=6, red=4, green=3)

# hat = Hat(black=6, red=4, green=3)
# print(hat)
