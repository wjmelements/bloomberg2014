import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)
n = int(lines[0])
sentence = lines[1]
print "Left -"
pos = 0
line = ""
leftlines = []
for word in sentence.split():
    if pos > 0:
        pos += 1
    if pos + len(word) > n:
        pos = 0
        leftlines.append(line)
        print line
        line = ""
    if pos > 0:
        line += " "
    line += word
    pos += len(word)
print line
leftlines.append(line)
print
print "Centered -"
pos = 0
line = ""
for line in leftlines:
    words = line.split()
    total = 0
    for word in words:
        total += len(word)
    extraspace = n  - total
    if len(words) - 1 > 0:
        allspacing = extraspace / (len(words) - 1)
        remaining = extraspace % (len(words) - 1)
    else:
        allspacing = 0
        remaining = 0
    out = ""
    for index, word in enumerate(words):
        out += word
        if index != len(words) - 1:
            for s in range(allspacing):
                out += " "
        if remaining > 0:
            remaining -= 1
            out += " "
    print out
print
print "Fib -"
line = ""
fib1 = 0
fib2 = 1
for word in sentence.split():
    if pos > 0:
        pos += fib2
    if pos + len(word) > n:
        pos = 0
        fib1 = 0
        fib2 = 1
        print line
        line = ""
    if pos > 0:
        for s in range(fib2):
            line += " "
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    line += word
    pos += len(word)
print line
