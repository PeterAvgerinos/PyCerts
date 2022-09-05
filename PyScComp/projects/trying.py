import re

while True:
    problem = input("What\'s your problem dude?").replace(" ", "")
    matches = re.search(r"([0-9]+)(\+)([0-9]+)", problem)

    if matches:
        number1, number2 = int(matches.group(1)), int(matches.group(3))
        operator = matches.group(2)
        if operator == "+":
            print(number1 + number2)
            break
        elif operator == "-":
            print(number1 - number2)
            break
        else:
            continue


