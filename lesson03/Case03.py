# 涵式(有回傳值)
def add(x, y):
    sum = (x + y) * 1.03
    return sum

# 涵式(無回傳值)
def addAndPrint(x, y):
    sum = (x + y) * 1.03
    print(sum)

print((1+2) * 1.03)
print((5+2) * 1.03)
print(add(1, 2))
print(add(5, 2))
addAndPrint(1, 2)
addAndPrint(5, 2)
