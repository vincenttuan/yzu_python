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