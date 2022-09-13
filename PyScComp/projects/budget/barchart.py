string = "Percentage spent by category \n"
catperc = [{"name" : "Food", "Percentage" : 40, "listofos" : [' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0', '0', '0']},{"name" : "Auto", "Percentage" : 60, "listofos" : [' ', ' ', ' ', ' ', ' ', '0', '0', '0', '0', '0', '0']},{"name" : "Clothing", "Percentage" : 20, "listofos" : [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '0']}]
percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
for item in percentages:
    string = string + f"{item:>4}|"
for item in range(0,len(catperc)):
    for loco in range(0,11):
        print(catperc[item]["listofos"][loco])
    print("\n")
