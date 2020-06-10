import requests

url = 'http://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20200609&selectType=ALL'
data = requests.get(url).text
# print(data)
# "證券代號","證券名稱","殖利率(%)","股利年度","本益比","股價淨值比","財報年/季",
data = data.replace('"-"', '-1')
data = data.replace('"', '')
for d in data.split("\r\n"):
    list = d.split(",")
    if len(list) == 8 and list[0] != '證券代號':
        if float(list[2]) > 7.0 and \
           float(list[4]) < 10 and \
           float(list[5]) < 1:
            print(list, end=',')

