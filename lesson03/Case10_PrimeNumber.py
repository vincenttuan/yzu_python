# 某數 n 是否是值數
n = 37
check = True
for i in range(2, n//2+1):
    if n % i == 0:
        check = False
        break

print(n, check)
