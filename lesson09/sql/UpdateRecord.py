import sqlite3

sql = 'Update Lotto Set n1=%d, n2=%d Where id=%d' % (99, 98, 1)

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.execute(sql)
print("修改成功", cursor.rowcount)
conn.commit()
conn.close()