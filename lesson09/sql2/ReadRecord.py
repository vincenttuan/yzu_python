import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('company.db')

df = pd.read_sql_query("SELECT * FROM Employee", con=conn)
print(df)

# 繪圖
ma = df['SALARY'].rolling(window=2).mean()
#print(ma)
plt.plot(df.NAME.values, df.SALARY.values, 'r.')  # 畫紅點
plt.plot(df['NAME'], df['SALARY'])  # 畫折線
plt.plot(df.NAME.values, ma)
plt.xlabel('NAME')
plt.ylabel('SALARY')
plt.show()

conn.close()