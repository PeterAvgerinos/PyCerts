def add_time(start_time, duration, starting_day = None):
    weekdays = {"Sunday" : 0, "Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, "Thursday": 4, "Friday" : 5, "Saturday" : 6}
    lw = list(weekdays.keys())

    start_time = start_time.strip(" ").upper()
    flag = start_time.split(":")[1][-2:]
    start_hour = int(start_time.split(":")[0])
    start_minutes = int(start_time.split(":")[1][:2])
    duration_hour = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])
    new_time = ""

    if flag == "PM":
        start_hour = start_hour + 12

    new_hour = start_hour + duration_hour
    new_minutes = start_minutes + duration_minutes

    new_hour = new_hour + new_minutes//60
    new_minutes = new_minutes%60

    days = new_hour//24
    new_hour = new_hour%24

    if new_hour >= 13:
        new_hour = new_hour - 12
        flag = "PM"
    else:
        flag = "AM"
        if new_hour == 0:
            new_hour = 12

    ending_day_value = 0
    if starting_day:
        starting_day = starting_day.lower().title()
        ending_day_value = weekdays[starting_day] + days%6
        ending_day_value = ending_day_value%6

    if days == 0 :
        if starting_day:
            new_time = (f"{new_hour}:{new_minutes:02} {flag}, {lw[ending_day_value]}")
        else:
            new_time = (f"{new_hour}:{new_minutes:02} {flag}")
    elif days == 1:
        if starting_day:
            new_time = (f"{new_hour}:{new_minutes:02} {flag}, {lw[ending_day_value]} (next day)")
        else:
            new_time = (f"{new_hour}:{new_minutes:02} {flag} (next day)")
    else:
        if starting_day:
            new_time = (f"{new_hour}:{new_minutes:02} {flag}, {lw[ending_day_value]} ({days} days later)")
        else:
            new_time = (f"{new_hour}:{new_minutes:02} {flag} ({days} days later)")
    return new_time

print(add_time("2:59 AM", "24:00", "saturDay"))
