import re
list = ["3 + 5", "4 + 10", "25 - 2"]

for item in list:
    problem = item.replace(" ", "")
    matches = re.search(r"([0-9]+)([\+|\-])([0-9]+)", problem)

    if matches:
        number1, number2 = int(matches.group(1)), int(matches.group(3))
        operator = matches.group(2)
        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        else:
            continue
        print(10*" ", number1)
        print(operator + (10)*" ", number2)
        print(10*"-")
        print((10)*" ", result)
