class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def __str__(self):
        spacesn = len(self.name)
        string = ("*"*((30-spacesn)//2) + self.name.title() + ((30-spacesn)//2)*"*") + "\n"
        for item in range(0, len(self.ledger)):
            if len(self.ledger[item]["description"]) > 23:
                string = string + (self.ledger[item]["description"][0 : 23] + " "*(7 - len(self.ledger[item]["amount"])) + self.ledger[item]["amount"]) + "\n"
            else:
                string = string + (self.ledger[item]["description"][0 : 23] + " "*(30 -len(self.ledger[item]["description"]) - len(self.ledger[item]["amount"])) + (self.ledger[item]["amount"])) + "\n"
        string = string + ("Total: " + str(self.total)) + "\n"
        return string

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount" : str(amount), "description" : description})
        self.total = self.total + amount

    def withdraw(self, amount, description = ""):
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

def create_spend_chart(categories):
    total = 0
    catperc = []
    percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    for item in categories:
        total = total + item.total
    for item in categories:
        catperc.append({"name" : item.name, "Percentage" : (item.total/total)*100, "listofos" : [], "listofls" : []})
    string = "Percentage spent by category \n"
    maximum = catperc[0]["name"]
    for k in range(0, len(catperc)):
        if len(catperc[k]["name"]) > len(maximum):
            maximum = catperc[k]["name"]

    for i in range(0, len(catperc)):
        for j in range(0, len(percentages)):
            if catperc[i]["Percentage"] > percentages[j]:
                catperc[i]["listofos"].append("0")
            else:
                catperc[i]["listofos"].append(" ")
            for k in range(0, len(maximum)):
                try:
                    catperc[i]["listofls"].append(catperc[i]["name"][k])
                except IndexError:
                    catperc[i]["listofls"].append(" ")

    for item in range(0, len(percentages)):
        string = string + f"{percentages[item]:>3}|"
        for jitem in range(0, len(catperc)):
            string = string + " " + catperc[jitem]["listofos"][item]
        string = string + "\n"
    string = string + "    ---------- \n"

    for item in range(0, len(maximum)):
        string = string + "    "
        for jitem in range(0, len(catperc)):
            string = string + " " + catperc[jitem]["listofls"][item]
        string = string + "\n"
    return string

