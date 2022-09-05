import re

problem = input("What\'s your problem dude?").replace(" ", "")
matches = re.search("[0-9]+", problem)

if matches:


