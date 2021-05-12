import statistics as stat
import matplotlib.pyplot as plt
import matplotlib as mpl
# python -m pip install -U pip
# python -m pip install -U matplotlib

list = [1, 2, 3, 4, 4]

# 算術平均
print(stat.mean(list))

# 中位數
print(stat.median([1, 3, 5]))
print(stat.median([1, 3, 5, 7]))
print(stat.median_grouped([1, 3, 5, 7]))

print(stat.stdev([1, 3, 5]))

print(stat.median([1, 2, 3, 3, 3]))
print(stat.median_grouped([1, 2, 3, 3, 3]))

# 標準差

# 變異係數是一種相對差異量數，用以比較單位不同或單位相
# 同但資料差異甚大的資料分散情形。
# 變異係數越大表示分散程度越大
# 公式 : cv = s(標準差)/m(平均)
# 調查五位學生之身高及體重如下，試比較其分散程度。
# 身高：172、168、164、170、176(公分)
# 體重：62、57、58、64、64(公斤)
no = [1, 2, 3, 4, 5]
h = [172, 168, 164, 170, 176]
w = [62, 57, 58, 64, 64]
print(stat.stdev(h) / stat.mean(h))
print(stat.stdev(w) / stat.mean(w))

#font = mpl.font_manager.FontProperties(fname='SimHei.ttf')
font = mpl.font_manager.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
#plt.rc('axes', unicode_minus=False)  #（解決座標軸負數的負號顯示問題）
plt.plot(h)
plt.title("身高統計表", fontproperties=font) # title
plt.ylabel("公分", fontproperties=font) # y label
plt.xlabel("編號", fontproperties=font) # x labe
plt.show()

plt.plot(h, '-', color=(1, 0, 0), marker = "o") # 255/255, 0/255, 0/255
plt.plot(w, '--', color=(0, 0, 1), marker = "o")
plt.grid(True)
plt.show()

lines = plt.plot(no,h,no,w)
plt.grid(True)
plt.setp(lines, marker = "o")
plt.show()


# 某公司有18位員工，其中10位在去年投資股票，一年的獲
# 利率如下(單位：%)：
#   7.6 3.9 15.6 28.3 1.2 10.8 35.3 45.6 10.2 0.5
# 另外8位員工投資買公債一年內獲利率如下(單位：%)
#   6.8 7.2 6.8 7.5 6.9 7.9 7.9 7.1 7.2
# 試分別求此公司的員工投資股票與公債的獲利率變異係數。
#
# 解答：投資股票的獲利率變異係數 C.V. = 0.969
#      投資買公債的獲利率變異係數 C.V. = 0.059
