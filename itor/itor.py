import fileinput
lines = fileinput.input()
n = int(lines[0])
out = ""
while n / 1000 > 0:
    out += "M"
    n -= 1000
if n >= 900:
    out += "CM"
    n -= 900
if n >= 500:
    out += "D"
    n -= 500
if n >= 400:
    out += "CD"
    n -= 400
while n / 100 > 0:
    out += "C"
    n -= 100
if n >= 90:
    out += "XC"
    n -= 90
if n >= 50:
    out += "L"
    n -= 50
if n >= 40:
    out += "XL"
    n -= 40
while n / 10 > 0:
    out += "X"
    n -= 10
if n == 9:
    out += "IX"
    n -= 9
if n >= 5:
    out += "V"
    n -= 5
if n == 4:
    out += "IV"
for i in range(n):
    out += "I"
print out
