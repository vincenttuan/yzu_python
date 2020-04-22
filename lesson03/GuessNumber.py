import random as r
ans = r.randint(1, 99)
min = 0
max = 100

while True:
    guess = int(input('請輸入數字 %d ~ %d :' % (min, max)))
    if guess == ans:
        print('恭喜答對了')
        break;
    elif guess < ans:
        min = guess
    else:
        max = guess
