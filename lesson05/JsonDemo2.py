import json
import requests

url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
r = requests.get(url)
#print(r.status_code)
#print(r.text)
bad_rices = json.loads(r.text)
for bad in bad_rices:
    print(bad.get('品名'))
