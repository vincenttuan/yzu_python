n = 83  # 隻
f = 240  # 總腳數

c = 0  # 雞的個數
r = 0  # 兔子的個數

# block of code ...
r = (f - (n * 2)) // 2
c = n - r

print("雞有 %d 隻, 兔子有 %d 隻" % (c, r))
print("雞有 " + str(c) + " 隻, 兔子有 " + str(r) + " 隻")

