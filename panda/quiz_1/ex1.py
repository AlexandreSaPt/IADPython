import calendar

year = int(input(""))
month = int(input(""))

print(f"Year:{year}", end="")
print(f"Month:{month}")


month_weeks = list(calendar.monthcalendar(year, month))

for i in range(len(month_weeks)):
    
    if month_weeks[i][0] != 0:
        print(month_weeks[i][0])
