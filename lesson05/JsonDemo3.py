import json
import requests
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2): # 經度1，緯度1，經度2，緯度2）
    # 轉弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # 半正矢 haversine 公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # 地球平均半徑(公里)
    return c * r * 1000 # 單位公尺

url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json'
data = json.loads(requests.get(url).text)
#print(data)
youbikes = data.get('result').get('records')
sbi = 1 # 可借數量
bemp = 1 # 可還數量
m = 500
for youbike in youbikes:
    lat = float(youbike.get('lat'))
    lng = float(youbike.get('lng'))
    mm = haversine(121.268160, 24.970612, lng, lat)
    if int(youbike.get('sbi')) >= sbi and int(youbike.get('bemp')) >= bemp and mm < m:
        print(youbike.get('sna'), youbike.get('sbi'), youbike.get('bemp'), mm , "m")

