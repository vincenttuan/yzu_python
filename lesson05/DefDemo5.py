x = 0  # global var
y = 0  # global var
def changeX(n):
    x = n # local var

def changeY(n):
    global y
    y = n

print("x=", x)
changeX(100)
print("x=", x)

print("y=", y)
changeY(100)
print("y=", y)