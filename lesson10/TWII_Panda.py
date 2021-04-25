import requests
import datetime
import pandas as pd
from io import StringIO

date = datetime.datetime(2021, 4, 23)
datestr = date.strftime('%Y%m%d')
url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=' + datestr + '&selectType=ALL'
data = requests.get(url).text
# print(data)
# "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
# 將內容有「-」都取代成 「-1」
data = data.replace('"-"', '-1')

# 將內容有「"」都取代為「空」（若要轉為 pandas 則此行不要執行）
# data = data.replace('"', '')

# 將 column 數量小於等於 10 的行數都刪除
data = data.split('\n')
data = list(filter(lambda l: len(l.split(',')) > 7, data))
# print(type(data), data)  # 得到 list

# join 使用範例
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# 得到結果：John#Peter#Vicky

# 將list中的每一列再合並成一個字串，並用肉眼看不到的換行符號'\n'分開
data = "\n".join(data)

# print(data)

# 將content變成檔案：StringIO，並且用pd.read_csv將表格讀取進來
df = pd.read_csv(StringIO(data))

# 列出每一個欄位資料型態
print(df.dtypes)

# 將所有的表格元素都轉換成數字，error='coerce'的意思是說，假如無法轉成數字，則用 NaN 取代
df = df.apply(lambda s: pd.to_numeric(s, errors='coerce'))

# 刪除不必要的欄位
df = df[df.columns[df.isnull().all() == False]]

# 將爬取的日期存入 dataframe
df['date'] = pd.to_datetime(date)

# 將 「證券代號」設定成index
df = df.set_index('證券代號')
df = df.rename(columns={'殖利率(%)': '殖利率'})

mask1 = df["殖利率"] >= 10
mask2 = df["本益比"] <= 7
mask3 = df["股價淨值比"] < 1
df = df[mask1 & mask2 & mask3]
print(df)

