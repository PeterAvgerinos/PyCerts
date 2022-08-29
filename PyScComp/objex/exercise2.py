class Poopster:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def __str__(self):
        if self.action == True:
            print('Mister is a big ol\'n Poopster')
        else:
            print('Mister ain\'t no Poopster')

    def poop(self):
        print('pritz')
        print('wowowoowoow')


x = input('Did you poop today?')
if x == 'yes':
    action = True
else:
    action = False

poop = Poopster('Peter', action)
print(poop)
poop.poop()
