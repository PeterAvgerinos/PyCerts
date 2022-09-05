import re

while True:
    problem = input("What\'s your problem dude?").replace(" ", "")
    matches = re.search(r"[0-9]+|\+|[0-9]+", problem)

    if matches:
        number1, number2 = int(matches[0]), int(matches[2])
        operator = matches[1]
        if operator == "+":
            print(number1 + number2)
            break
        elif operator == "-":
            print(number1 - number2)
            break
        else:
            continue


