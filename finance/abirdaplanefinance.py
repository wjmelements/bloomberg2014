import fileinput
for line in fileinput.input():
    company, exchange = line.split()
    result = ""
    if len(company) < 8:
        result += company
        for a in range(7 - len(company)):
            result += " "
    else:
        result += company[0:8]
    print result, exchange
