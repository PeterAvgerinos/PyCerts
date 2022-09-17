class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.spent = 0

    def __str__(self):
        spacesn = len(self.name)
        string = ("*"*((30-spacesn)//2) + self.name.title() + ((30-spacesn)//2)*"*") + "\n"
        for item in range(0, len(self.ledger)):
            if len(self.ledger[item]["description"]) > 23:
                string = string + self.ledger[item]["description"][0 : 23] + f'''{f'{float(self.ledger[item]["amount"]):.2f}':>7}''' + "\n"
            else:
                string = string + self.ledger[item]["description"] + " "*(30 -len(self.ledger[item]["description"]) - len(f'{float(self.ledger[item]["amount"]):.2f}')) + f'{float(self.ledger[item]["amount"]):.2f}' + "\n"
        string = string + ("Total: " + str(self.total))
        return string

    def deposit(self, amount, description = None):
        if description == None:
          self.ledger.append({"amount" : amount, "description" : ""})
        else:
          self.ledger.append({"amount" : amount, "description" : description})
        self.total += amount

    def withdraw(self, amount, description = None):
        if self.total > amount:
            self.total -= amount
            self.spent += amount
            if description == None:
              self.ledger.append({"amount" : -amount, "description" : ""})
            else:
              self.ledger.append({"amount" : -amount, "description" : description})
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
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.total < amount:
            return False
        else:
            return True

def create_spend_chart(categories):
    total_spent = 0
    catperc = []
    percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
    for item in categories:
        total_spent += item.spent
    for item in categories:
        catperc.append({"name" : item.name, "Percentage" : (item.spent/total_spent)*100, "listofos" : [], "listofls" : []})
    string = "Percentage spent by category\n"
    maximum = catperc[0]["name"]
    for k in range(0, len(catperc)):
        if len(catperc[k]["name"]) > len(maximum):
            maximum = catperc[k]["name"]

    for i in range(0, len(catperc)):
        for j in range(0, len(percentages)):
            if catperc[i]["Percentage"] > percentages[j]:
                catperc[i]["listofos"].append("o")
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
            string = string + " " + catperc[jitem]["listofos"][item] + " "
        string = string + " \n"
    string = string + "    ----------\n"

    for item in range(0, len(maximum)):
      string = string + "   "
      print(item)
      for jitem in range(0, len(catperc)):
          string = string + "  " + catperc[jitem]["listofls"][item]
      if item == len(maximum) - 1:
          string = string + "  "
      else:
          string = string + "  \n"
    return string
