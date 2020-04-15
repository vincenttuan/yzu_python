import random

r = random.randrange(0, 2)  # 0 <= r < 2
print(r)

r = random.randint(0, 2)  # 0 <= r <= 2
print(r)

# 電腦選號四星彩
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print(n1, n2, n3, n4)

# 跳脫字元
print("\""); print("A\nB\tC")

a = 100 + 200\
    - 50 * 5 \
    / 10
print(a)
