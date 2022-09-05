import re

while True:
    problem = input("What\'s your problem dude?").replace(" ", "")
    matches = re.search(r"([0-9]+)(\+)([0-9]+)", problem)

    if matches:
        number1, number2 = matches.group(0), matches.group(2)
        operator = matches.group(1)
        # if operator == "+":
        #     print(number1 + number2)
        #     break
        # elif operator == "-":
        #     print(number1 - number2)
        #     break
        # else:
        #     continue
        print(number1, number2, operator)
        break


