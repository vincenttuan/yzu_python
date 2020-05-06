import json
import requests

url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json'
data = json.loads(requests.get(url).text)
#print(data)
youbikes = data.get('result').get('records')
sbi = 30
bemp = 30
for youbike in youbikes:
    if int(youbike.get('sbi')) >= sbi and int(youbike.get('bemp')) >= bemp:
        print(youbike.get('sna'), youbike.get('sbi'), youbike.get('bemp'))

