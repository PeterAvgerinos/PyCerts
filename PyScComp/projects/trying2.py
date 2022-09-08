import re
problem = ["344 + 2", "434 + 222", "22 + 8", "52 - 22"]

def arithmetic_arranger(problems, show_result = False):
  a = {}
  lenbar = {}
  arithmetic_arranged = ""

  if len(problems) > 5:
      arithmetic_arranged = "Error: Too many problems."
      return arithmetic_arranged

  for problem in problems:
      problem = problem.replace(" ", "")
      if ("+" not in problem) and ("-" not in problem):
              arithmetic_arranged = "Error: Operator must be \'+\' or \'-\'."
              return arithmetic_arranged
      matches = re.search(r"^([0-9]+)([\+|\-])([0-9]+)$", problem)
      if bool(matches):
          number1, number2 = int(matches.group(1)), int(matches.group(3))
          operator = matches.group(2)
          spaces1 = len(str(number1))
          spaces2 = len(str(number2))
          if spaces1 > 4 or spaces2 > 4:
              arithmetic_arranged = "Error: Numbers cannot be more than four digits."
              return arithmetic_arranged
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
        arithmetic_arranged = "Error: Only Numbers"
        return arithmetic_arranged
  for i in a:
    if max(a[i][5], a[i][0], a[i][3]) <= 2:
      lenbar[i] = 4
    elif max(a[i][5], a[i][0], a[i][3]) <= 3:
      lenbar[i] = 5
    else:
      lenbar[i] = 6

  for i in a:
    arithmetic_arranged = arithmetic_arranged + (lenbar[i] - a[i][0])*" " + f'{a[i][1]}' + 4*" "
  arithmetic_arranged = arithmetic_arranged + '\n'
  for i in a:
    arithmetic_arranged = arithmetic_arranged + f'{a[i][2]}' + (lenbar[i] - a[i][3] - 1)*" " + f'{a[i][4]}' + 4*" "
  arithmetic_arranged = arithmetic_arranged + '\n'
  for i in a:
    arithmetic_arranged = arithmetic_arranged + lenbar[i]*"-" + 4*" "
  arithmetic_arranged = arithmetic_arranged + '\n'
  for i in a:
    if show_result == True:
      arithmetic_arranged = arithmetic_arranged + (lenbar[i] - a[i][5])*" " + f'{a[i][6]}' + 4*" "
  arithmetic_arranged = arithmetic_arranged + '\n'
  return arithmetic_arranged

def main():
    arithmetic_arranger(problem, True)

if __name__ == "__main__()":
    main()
