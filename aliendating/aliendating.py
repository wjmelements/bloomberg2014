import fileinput
import re
lines = fileinput.input()
form = lines[0]
q, b, k, u = map(int,re.split("\\.|/", form))
base = 9 + 16 * 10 + 20 * 10 * 23 + 100 * 20 * 10 * 1452 # December 7th 1952
date = q * 100 * 20 * 10 + b * 20 * 10 + k * 10 + u - base # days since base
month = 11
day = 7
year = 1952
leapyears = date / (365 * 4)
if date < 0:
    leapyears += 1
date -= leapyears
changeyears = date / 365
if date < 0:
    changeyears += 1
year += changeyears
if date < 0:
    date %= 365
    date = date - 365
else:
    date %= 365
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year % 4 == 0:
    monthdays[1] = 29
while monthdays[month] < date:
    date -= monthdays[month]
    month += 1
    if month > 11:
        month = 0
        year += 1
        if year % 4 == 0:
            monthdays[1] = 29
        else:
            monthdays[1] = 28
while monthdays[(month + 11) % 12] < -date:
    month -= 1
    if month < 1:
        month = 11
        year -= 1
        if year % 4 == 0:
            monthdays[1] = 29
        else:
            monthdays[1] = 28
    date += monthdays[month]
while date > 0:
    day += 1
    if day > monthdays[month]:
        month += 1
        if month > 11:
            month = 0
            year += 1
            if year % 4 == 0:
                monthdays[1] = 29
            else:
                monthdays[1] = 28
        day = 1
    date -= 1
while date < 0:
    date += 1
    day -= 1
    if day < 1:
        month -= 1
        if month < 0:
            month = 11
            year -= 1 
            if year % 4 == 0:
                monthdays[1] = 29
            else:
                monthdays[1] = 28
        day = monthdays[month]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print months[month] + " " + str(day) + ", " + str(year)
