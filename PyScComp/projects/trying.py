import re
list = ["399 - 554", "43 + 102", "25 - 200"]
liste = []


def arithmetic_arranger(problems, show_result = False):
    a = {}

    for item in problems:
        i = 0
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
            # print((5 - spaces1)*" ",number1)
            # print(operator, (1 - spaces2)*" ", number2)
            # print(5*"-")
            # if show_result == True:
            #     print((5-spacesr)*" ", result)
            # print()
        i = i + 1

    for i in a:
        print((5 - a[i][0])*" ", a[i][1], end="")
    print()
    for i in a:
        print(a[i][2], (1 - a[i][3])*" ", a[i][4], end="")
    print()
    for i in a:
        print(5*"-", end="")
    print()
    for i in a:
        if show_result == True:
            print((5 - a[i][5])*" ", a[i][6], end="")
    print()

def main():
    return arithmetic_arranger(list, True)

main()
