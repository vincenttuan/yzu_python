import sqlite3

sql = 'Insert into Lotto(n1, n2, n3, n4, n5, n6) ' \
      'Values (%d, %d, %d, %d, %d, %d)' % (31, 32, 33, 34, 35, 36)

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.execute(sql)
id = cursor.lastrowid
print('新增一筆資料成功 id=', id)
conn.commit()
conn.close()