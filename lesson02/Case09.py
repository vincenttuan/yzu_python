# -*- coding:UTF-8 -*-
# BMI 資料運算
import math

h = float(input('請輸入身高:'))
w = float(input('請輸入體重:'))
#bmi = w / (h/100)**2
bmi = w / math.pow(h/100, 2)
result = 18 <= bmi < 23
print('身高: %.1f 體重: %.1f BMI: %.2f Result: %s' %
      (h, w, bmi, result))
