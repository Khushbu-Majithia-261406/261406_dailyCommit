# get next day of given date using if-else

year = int(input("Input a year: "))


# check for leap year
if (year % 400 == 0):
    leap_year = 1
elif (year % 100 == 0):
    leap_year = 0
elif (year % 4 == 0):
    leap_year = 1
else:
    leap_year = 1

month = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
    if leap_year==1:
        month_length = 29
    else:
        month_length = 28
else:
    month_length = 30


day = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("The next date is [yyyy-mm-dd]  %d-%d-%d." % (year, month, day))