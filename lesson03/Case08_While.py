import random as r

while True:
    n = r.randint(1, 100)

    if n == 50:
        print(n)
        break

    if n % 3 != 0:
        continue

    print(n)
