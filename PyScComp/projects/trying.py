import re
list = ["3 - 5", "4 + 10", "25 - 2"]

def arithmetic_arranger(problems):
    try:
        for item in problems:
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
                print(number1)
                print(operator, number2)
                print(10*"-")
                print(result)
                print()
    except:
        raise(ValueError)

def main():
    return arithmetic_arranger(list)

main()
