day = "Sunday"
match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" :
        print ("Working Day")
    case _:
        print("Holiday")

days = ["MOnday", "Tuesday"]
prices = [10, 20]
for day, value in zip(days, prices):
    print (F"{day} : {value}")

for index, day in enumerate(days):
    print ({f"{index} : {day}"})