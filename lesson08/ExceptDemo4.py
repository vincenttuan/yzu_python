x = 10
try:
    y = int(input('請輸入數字:'))
    z = x / y
except ZeroDivisionError as e:
    print('分母不可 = 0', e)
else:
    print(z)
finally:
    print('我一定要執行...')
