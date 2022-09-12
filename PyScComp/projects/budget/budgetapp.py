class Category:
    def __init__(self, name, ledger ):
        self.name = name
        self.ledger = ledger
        total = 0

    def deposit(self, amount, description):
        self.ledger.append({"amount" : amount, "description" : description})

    def withdraw(self, amount, description):
        for item in self.ledger:
            self.total = self.total + self.ledger[item]
            if self.total > abs(amount):
                self.ledger.append({"amount" : amount, "description" : description})
                return True
            else:
                return False






def create_spend_chart(categories):
    pass
