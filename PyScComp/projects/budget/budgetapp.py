class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def __str__(self):
        spacesn = len(self.name)
        string = ("*"*((30-spacesn)//2) + self.name.title() + ((30-spacesn)//2)*"*") + "\n"
        for item in range(0, len(self.ledger)):
            string = string + (self.ledger[item]["description"][0 : 23] + " "*(30 -len(self.ledger[item]["description"]) - len(self.ledger[item]["amount"])) + (self.ledger[item]["amount"])) + "\n"
        string = string + ("Total: " + str(self.total))
        return string

    def deposit(self, amount, description):
        self.ledger.append({"amount" : str(amount), "description" : description})
        self.total = self.total + amount

    def withdraw(self, amount, description):
        if self.total > amount:
            self.total = self.total - amount
            self.ledger.append({"amount" : "-" + str(amount), "description" : description})
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def get_description(self, i):
        print(self.ledger[i]["description"])
        return self.ledger[i]["description"]

    def get_amount(self, i):
        print(self.ledger[i]["amount"])
        return self.ledger[i]["amount"]

    def transfer(self, amount, category):
        if self.total > amount:
            self.withdraw(amount, "transfer to [destination budget category]")
            category.deposit(amount, "transfer from [source budget category]")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.total < amount:
            return False
        else:
            return True

food = Category("food")
food.deposit(25, "poop")
food.deposit(30, "piss")
food.deposit(45, "ass")
food.deposit(73, "dicks")
food.withdraw(43, "pouch")
food.get_amount(1)
food.get_description(1)
print(food)


def create_spend_chart(categories):
    pass
