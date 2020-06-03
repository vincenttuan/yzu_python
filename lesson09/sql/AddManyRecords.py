import sqlite3
import random

sql = 'Insert into Lotto(n1, n2, n3, n4, n5, n6) ' \
      'Values (?, ?, ?, ?, ?, ?)'

lottos = []
for i in range(100):
      # 取出1~46 不重複的數字六個
      nums = set()
      while len(nums) < 6:
            nums.add(random.randint(1, 46))
      lottos.append(tuple(nums)) # 要轉元組

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.executemany(sql, lottos)
print('新增資料成功')
conn.commit()
conn.close()