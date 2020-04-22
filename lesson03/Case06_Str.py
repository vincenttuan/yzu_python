s = "she sell sea shell on the sea shore"
print(s)
print("有 %s 個 s" % s.count('s'))
print("有 sea 這個字嗎 ? %d" % s.find('sea'))

# 是否都是a-zA-Z的英文字
# 技巧: 先利用 replace 去除空白
print(s.replace(' ', '').isalpha())


