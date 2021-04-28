# 加入千分位
n = 123 * 99 * 1234 * 1.27
print(format(n, ','))

# 千分位 + 小數點
n = 123 * 99 * 1234 * 1.27432
print(format(float("%.2f" % n), ','))
print("{:,}".format(float("%.2f" % n)))

# 原始字串
s = r"C:\temp\nba.txt"
print(s)

#------------------------------------------------------
import random as r

n = r.randint(1, 10)
if n % 2 == 0:
    print('%d 偶數' % n)
else:
    print('%d 奇數' % n)

# 類三元運算子的寫法
print('%d %s' % (n, "偶數" if n % 2 == 0 else "奇數"))

# 建構是否是偶數的涵式 ?
def isOdd(n):
    return "偶數" if n % 2 == 0 else "奇數"

print('%d %s' % (n, isOdd(n)))


#------------------------------------------------------
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
#------------------------------------------------------
def foo():
    pass

def bar(n):
    if n < 60:
        return
    print('恭喜過關~')

foo()
bar(40)
#------------------------------------------------------
def mask(money) :
    x = money // 5
    size = "成人"
    return x, size

my_x, my_size = mask(100)
print(my_x, my_size)
#------------------------------------------------------
s = "she sell sea shell on the sea shore"
print(s)
print("有 %s 個 s" % s.count('s'))
print("有 sea 這個字嗎 ? %d" % s.find('sea'))

# 是否都是a-zA-Z的英文字
# 技巧: 先利用 replace 去除空白
print(s.replace(' ', '').isalpha())

print(s.swapcase())
#------------------------------------------------------
text = "半徑=10"
# 求圓面積
name, r = text.split("=")
print(type(name), type(r))
r = int(r)  # str 轉 int
print("%s 為 %d 的圓面積是 %.2f" % (name, r, r*r * 3.14))
#------------------------------------------------------
import random as r

while True:
    n = r.randint(1, 100)

    if n == 50:
        print(n)
        break

    if n % 3 != 0:
        continue

    print(n)
#------------------------------------------------------
for i in range(1, 5, 1):
    print(i, "Java")
#------------------------------------------------------
# 某數 n 是否是值數
n = 131
check = True
for i in range(2, n//2+1):
    # 印出 log
    print("%d / %d 餘數 %d" % (n, i, n % i))
    if n % i == 0:
        check = False
        break

print(n, check)
#------------------------------------------------------
def isPrime(n):
    check = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            check = False
            break
    return check

#------------------------------------------

for i in range(2, 101):
    print(i, "質數" if isPrime(i) else "")
#------------------------------------------------------
def add(x, y):
    sum = x + y
    return sum

sum = add(1, 2)
print(sum)
#------------------------------------------------------
# 遞迴求解 fib
def f(n):
    #print("n = %d" % n)
    if n == 0 or n == 1:
        return n
    return f(n-1) + f(n-2)

print(f(10))
#------------------------------------------------------
import random as r
ans = r.randint(1, 99)
min = 0
max = 100
count = 7

while count > 0:
    guess = int(input('(%d次數)請輸入數字 %d ~ %d :' % (count, min, max)))
    count -= 1  # count = count - 1
    # 先驗證數字是否在合法範圍 ?
    if guess <= min or guess >= max:
        print('數字範圍錯誤, 請重新輸入 !')
        continue

    # 進行遊戲比對
    if guess == ans:
        print('恭喜答對了')
        break;
    elif guess < ans:
        min = guess
    else:
        max = guess
