# 某數 n 是否是值數
n = 39
check = True
for i in range(2, n//2+1):
    print("%d / %d 餘數 %d" % (n, i, n % i))
    if n % i == 0:
        check = False
        break

print(n, check)
