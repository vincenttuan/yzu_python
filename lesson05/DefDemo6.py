def add(x):
    return x + 1

def sub(x):
    return x - 1

def operate(func, x):
    return func(x)

x = 10
x = operate(add, x)
print(x)
x = operate(sub, x)
print(x)

z = [add, sub]  # 函式陣列
