text = "半徑=10"
# 求圓面積
name, r = text.split("=")
print(type(name), type(r))
r = int(r)  # str 轉 int
print("%s 為 %d 的圓面積是 %.2f" % (name, r, r*r * 3.14))

