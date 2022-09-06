import re
list = ["399 - 554", "43 + 102", "25 - 200"]
liste = []


def arithmetic_arranger(problems, show_result = False):
    a = {}

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
            new_value = {problem: [spaces1, number1, operator, spaces2, number2, spacesr, result]}
            a.update(new_value)

    for i in a:
        print((5 - a[i][0])*" ", a[i][1], 5*" ", end="")
    print()
    for i in a:
        print(a[i][2], (1 - a[i][3])*" ", a[i][4], 5*" ", end="")
    print()
    for i in a:
        print(2*max(a[i][0], a[i][3])*"-", 5*" ", end="")
    print()
    for i in a:
        if show_result == True:
            print((5 - a[i][5])*" ", a[i][6], 5*" ",  end="")
    print()

def main():
    return arithmetic_arranger(list, True)

main()
