string = "Percentage spent by category \n"
catperc = [{"name" : "Food", "Percentage" : 45, "listofos" : [], "listofls" : []},{"name" : "Auto", "Percentage" : 60, "listofos" : [], "listofls" : []},{"name" : "Clothing", "Percentage" : 20, "listofos" : [], "listofls" : []}]
percentages = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

maximum = catperc[0]["name"]
for k in range(0, len(catperc)):
    if len(catperc[k]["name"]) > len(maximum):
        maximum = catperc[k]["name"]

print(maximum)

for i in range(0, len(catperc)):
    for j in range(0, len(percentages)):
        if catperc[i]["Percentage"] > percentages[j]:
            catperc[i]["listofos"].append("0")
        else:
            catperc[i]["listofos"].append(" ")

for item in range(0, len(percentages)):
    string = string + f"{percentages[item]:>3}|"
    for jitem in range(0, len(catperc)):
        string = string + " " + catperc[jitem]["listofos"][item]
    string = string + "\n"
string = string + "    ----------"

print(string)

