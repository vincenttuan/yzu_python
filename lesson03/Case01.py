# 加入千分位
n = 123 * 99 * 1234 * 1.27
print(format(n, ','))

# 千分位 + 小數點
n = 123 * 99 * 1234 * 1.27432
print(format(float("%.2f" % n), ','))
print("{:,}".format(float("%.2f" % n)))

# 原始字串
s = r"C:\temp\nba.txt"
print(s)
