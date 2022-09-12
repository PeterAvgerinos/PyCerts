class Category:
    def __init__(self, name, ledger ):
        self.name = name
        self.ledger = ledger
        self.total = 0

    def deposit(self, amount, description):
        self.ledger.append({"amount" : amount, "description" : description})
        self.total = self.total + amount

    def withdraw(self, amount, description):
        if self.total > amount:
            self.total = self.total - amount
            self.ledger.append({"amount" : amount, "description" : description})
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






def create_spend_chart(categories):
    pass
