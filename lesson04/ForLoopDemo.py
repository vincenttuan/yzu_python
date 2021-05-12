# 數組 list(可重複), Set(不可重複), Dict(Key-Value)
scores = [100, 90, 80]
scores.append(70)
print(scores)  # 列印數組
print(scores[0])  # 取得維度=0的內容
print(len(scores))  # 取得數組長度(有幾筆資料)
print(scores.index(100))  # 取得內容=100的維度(index)值
for x in scores:
    print(scores.index(x), x)

for (i, x) in enumerate(scores):
    print(i, x)
    
# List 串列
# Tuple 元祖 (唯讀)
# Dict 字典 (key = value)

# 建立串列
# len、min、max
print('1.--- len、min、max ---')
a = [20, 30, 10]
print('a = {}'.format(a))
print('len(a) = {}'.format(len(a)))
print('max(a) = {}'.format(max(a)))
print('min(a) = {}'.format(min(a)))

# append、insert、extend
print('2.--- append、insert、extend ---')
a = [20, 30, 10]
print('a = {}'.format(a))

a.append(90)
print('a = {}'.format(a))

a.append([40, 80])
print('a = {}'.format(a))

a.extend([60, 50])
print('a = {}'.format(a))

a.insert(0, 100)
print('a = {}'.format(a))

# index、remove、pop
print('\n--- index、remove、pop ---')
a = [20, 30, 10, 90, [40, 80], 60, 50]
print('a = {}'.format(a))
print('a[0] = {}'.format(a[0]))
print('a[4] = {}'.format(a[4]))
print('a[4][0] = {}'.format(a[4][0]))
print('a[4][1] = {}'.format(a[4][1]))
print('a.index(90) = {}'.format(a.index(90)))
a.remove(90)
print('remove 90, a = {}'.format(a))

value = a.pop(0)  # 得到 20 並移除 20
print('pop a.pop(0) 得到 {}, a = {}'.format(value, a))

# reverse、sort
print('\n--- reverse、sort ---')
a = [20, 30, 10, 90, 40, 80, 60, 50]
print('a = {}'.format(a))
a.sort()
print('a.sort(), a = {}'.format(a))
a.reverse()
print('a.reverse(), a = {}'.format(a))

# count
print('\n--- count ---')
a = 'she sell sea shell on the sea shore'
print('a = {}'.format(a))
print('s 有幾個 ? {}'.format(a.count('s')))
print('sea 有幾個 ? {}'.format(a.count('sea')))

# 數列與元祖
a = [1, 2, 3, 4, 5]  # 可修改
b = (1, 2, 3, 4, 5)  # 不可修改
# a[0] = 99
# print(a)
# b[0] = 99
# print(b)

# 轉換
# b = list(b)  # tuple 轉 list
# # b[0] = 99
# # print(b)

a = tuple(a)  # list 轉 tuple
# a[0] = 99

