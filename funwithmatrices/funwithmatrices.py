import fileinput
lines = fileinput.input()
n = int(lines[0])
matrix = [[0 for x in range(n)] for y in range(n)]
for line in range(n):
    a = lines[1 + line]
    matrix[line] = map(int,a.split())
yes = True
for startx in range(1,n):
    starty = 0
    exp = matrix[startx][starty]
    while startx < n -1 and starty < n - 1:
        startx += 1
        starty += 1
        if matrix[startx][starty] != exp:
            yes = False
            break
for starty in range(0,n):
    startx = 0
    exp = matrix[startx][starty]
    while startx < n -1 and starty < n - 1:
        startx += 1
        starty += 1
        if matrix[startx][starty] != exp:
            yes = False
            break
if yes:
    print "Yes"
else:
    print "No"
