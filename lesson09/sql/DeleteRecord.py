import sqlite3

sql = 'Delete From Lotto Where id=%d' % (1)

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()
cursor.execute(sql)
print("刪除成功", cursor.rowcount)
conn.commit()
conn.close()