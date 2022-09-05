import re
list = ["399 - 554", "43 + 102", "25 - 200"]

def arithmetic_arranger(problems):
    for item in problems:
        problem = item.replace(" ", "")
        matches = re.search(r"([0-9]+)([\+|\-])([0-9]+)", problem)

        if matches:
            number1, number2 = int(matches.group(1)), int(matches.group(3))
            operator = matches.group(2)
            spaces1 = len(str(number1))
            spaces2 = len(str(number2))
            if operator == "+":
                result = number1 + number2
                spacesr = len(str(result))
            elif operator == "-":
                result = number1 - number2
                spacesr = len(str(result))
            else:
                continue
            print((10 - spaces1)*" ",number1)
            print(operator, (8 - spaces2)*" ", number2)
            print(10*"-")
            print((10-spacesr)*" ", result)
            print()

def main():
    return arithmetic_arranger(list)

main()
