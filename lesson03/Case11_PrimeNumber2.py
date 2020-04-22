def isPrime(n):
    check = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            check = False
            break
    return check

for i in range(2, 101):
    print(i, "質數" if isPrime(i) else "")
