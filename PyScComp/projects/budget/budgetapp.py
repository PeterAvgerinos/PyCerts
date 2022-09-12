class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = {}
        self.total = 0

    def __str__(self):
        spacesn = len(self.name)
        print("*"*((30-spacesn)//2) + self.name + ((30-spacesn)//2)*"*")
        for item in self.ledger:
            print(self.ledger[item]["description"][0 : 23] + " "*(7 - len(self.ledger[item]["amount"])) + (self.ledger[item]["amount"]))
        print("Total: " + str(self.total))

    def deposit(self, amount, description):
        self.ledger.update({"amount" : amount, "description" : description})
        self.total = self.total + amount

    def withdraw(self, amount, description):
        if self.total > amount:
            self.total = self.total - amount
            self.ledger.update({"amount" : "-" + amount, "description" : description})
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, Category):
        if self.total > amount:
            self.withdraw(amount, "Transfer to [Destination Budget Category]")
            Category.deposit(amount, "Transfer from [Source Budget Category]")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.total < amount:
            return False
        else:
            return True

food = Category("Food")
food.deposit(25, "poop")
food.deposit(30, "piss")
food.deposit(45, "ass")
food.deposit(73, "dicks")
food.withdraw(43, "pouch")
print(food)


def create_spend_chart(categories):
    pass
