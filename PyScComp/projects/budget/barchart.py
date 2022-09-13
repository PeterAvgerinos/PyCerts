string = "Percentage spent by category \n"
catperc = [{"name" : "Food", "Percentage" : 40, "listofos" : [' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0', '0', '0']},{"name" : "Auto", "Percentage" : 60, "listofos" : [' ', ' ', ' ', ' ', ' ', '0', '0', '0', '0', '0', '0']},{"name" : "Clothing", "Percentage" : 20, "listofos" : [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0']}]
percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
for item in percentages:
    string = string + f"{item:>4}|"
    for loco in range(0,11):
        string = string + catperc[0]["listofos"][loco] + catperc[1]["listofos"][loco] + catperc[2]["listofos"][loco] + "\n"
print(string)
