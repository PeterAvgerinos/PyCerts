def add_time(a, b, c = None):
    pass

def main():
    print(add_time("3:00 PM", "3:10"))
    print("Should output 6:10 PM")

    print(add_time("11:30 PM", "2:30", "Monday"))
    print("Should output 2:02 PM, Monday")

    print(add_time("11:43 AM", "00:20"))
    print("Should output 12:03 PM")

    print(add_time("10:10 PM", "3:30"))
    print("Should output 1:40 AM (next day)")

    print(add_time("11:43 PM", "24:20", "tueSday"))
    print("Should output 12:03 AM, Thursday (2 days later)")

    print(add_time("6:30 PM", "205:12"))
    print("Should output 7:42 AM (9 days later)")

