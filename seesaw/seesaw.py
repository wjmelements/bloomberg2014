import fileinput
comparisons = dict() # person person -> comp

def opposite(comp):
    if comp == "\\":
        return "/"
    elif comp == "/":
        return "\\"
    else:
        return "-"
kids = set()
for line in fileinput:
    one, comp, two = line.split()
    comparisons[(one,two)] = comp
    comparisons[(two,one)] = opposite(comp)
    
