import re
problems = ["399 + 554", "43 + 102", "25 - 200"]

def arithmetic_arranger(problems, show_result = False):
    a = {}

    if len(problems) > 5:
        raise Exception("Error: Too many problems.")

    for problem in problems:
        problem = problem.replace(" ", "")
        if ("+" not in problem) and ("-" not in problem):
                raise Exception("Error: Operator must be \'+\' or \'-\'.")
        matches = re.search(r"^([0-9]+)([\+|\-])([0-9]+)$", problem)
        if bool(matches):
            number1, number2 = int(matches.group(1)), int(matches.group(3))
            operator = matches.group(2)
            if operator != "+" and operator != "-":
                raise Exception("Error: Operator must be \'+\' or \'-\'.")
            spaces1 = len(str(number1))
            spaces2 = len(str(number2))
            if spaces1 > 4 or spaces2 > 4:
                raise Exception("Error: Numbers cannot be more than four digits.")
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
        else:
            raise Exception("Error: Only Numbers")

    # for i in a:
    #     print((5 - a[i][0])*" ", a[i][1], 5*" ", end="")
    # print()
    # for i in a:
    #     print(a[i][2], (1 - a[i][3])*" ", a[i][4], 5*" ", end="")
    # print()
    # for i in a:
    #     print(2*max(a[i][0], a[i][3])*"-", 5*" ", end="")
    # print()
    # for i in a:
    #     if show_result == True:
    #         print((5 - a[i][5])*" ", a[i][6], 5*" ",  end="")
    # print()

    for i in a:
        print('{:>12}'.format(a[i][1]), end="")
    print()
    for i in a:
        print('{:>12}'.format(a[i][4]), end="")

def main():
    return arithmetic_arranger(problems, True)

if __name__ == "__main__":
    main()
