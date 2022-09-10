#AM before midday 1 - 12
#PM after midday 12 - 24
def add_time(start_time, duration, starting_day = None):
    weekdays = {"Sunday" : 0, "Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday": 4, "Friday" : 5, "Saturday" : 6}
    flag = "PM"

    start_time = start_time.strip(" ").upper()

    start_hour = int(start_time.split(":")[0])
    start_minutes = int(start_time.split(":")[1][:2])
    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    if flag in start_time:
        start_hour = start_hour + 12

    new_hour = start_hour + duration_hour
    new_minutes = start_minutes + duration_minutes

    new_hour = new_hour + new_minutes//60
    new_minutes = new_minutes%60

    days = new_hour//24
    new_hour = new_hour%24

    if starting_day:
        starting_day = starting_day.upper().title()
        ending_day_value = weekdays[starting_day] + days%6
        print(weekdays[f'{ending_day_value}'])

    if days == 0 :
        print(f"{new_hour}:{new_minutes}")
    elif days == 1:
        print(f"{new_hour}:{new_minutes} (next day)")
    else:
        print(f"{new_hour}:{new_minutes} ({days} days later)")

def main():
    # add_time("3:00 PM", "3:10")
    # print("Should output 6:10 PM")

    # add_time("11:30 AM", "2:32", "Monday")
    # print("Should output 2:02 PM, Monday")
    #
    # print(add_time("11:43 AM", "00:20"))
    # print("Should output 12:03 PM")
    #
    # print(add_time("10:10 PM", "3:30"))
    # print("Should output 1:40 AM (next day)")
    #
    print(add_time("11:43 PM", "24:20", "tueSday"))
    # print("Should output 12:03 AM, Thursday (2 days later)")
    #
    # add_time("6:30 PM", "205:12", "Monday")
    # print("Should output 7:42 AM (9 days later)")

if __name__ == "__main__":
    main()
