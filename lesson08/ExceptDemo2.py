x = 10
try:
    y = int(input('請輸入數字:'))
    z = x / y
except ZeroDivisionError as e:
    print('分母不可 = 0', e)
except ValueError as e:
    print('輸入資料錯誤.', e)
else:
    print(z)