import json
import requests

# 不合格米 url 位置
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'

# 合格米 url 位置
#url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceQualified.aspx'

r = requests.get(url)
#print(r.status_code)
#print(r.text)
bad_rices = json.loads(r.text)
for bad in bad_rices:
    if '月光' in bad.get('品名'):
        print(bad.get('品名'))
