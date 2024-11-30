import time
from datetime import datetime

print("Date1:", end="")
str_date1 = input("")
year1 = int(str_date1[0] + str_date1[1] + str_date1[2] + str_date1[3])
month1 = int(str_date1[5] + str_date1[6])
day1 = int(str_date1[8] + str_date1[9])


print("Date2:", end="")
str_date2 = input("")

year2 = int(str_date2[0] + str_date2[1] + str_date2[2] + str_date2[3])
month2 = int(str_date2[5] + str_date2[6])
day2 = int(str_date2[8] + str_date2[9])


a = datetime(year2,month2,day2,0,0,0)
b = datetime(year1,month1,day1,0,0,0)
print("Number of days between dates=", end="")
print("{:.1f}". format((a-b).days))
