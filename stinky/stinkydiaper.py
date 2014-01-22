import fileinput
for line in fileinput.input():
    unique = True
    found = set()
    duplicate = set()
    for a in line:
        if a != " " and a != "\n":
            if a in found:
                unique = False
                if a not in duplicate:
                    duplicate.add(a)
            else:
                found.add(a)
    if unique:
        result = "W"
        for a in range(len(found)):
            result += "A"
        print result
    else:
        result = "G"
        for a in range(len(duplicate)):
            result += "A"
        print result
