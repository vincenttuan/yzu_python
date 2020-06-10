# https://blog.csdn.net/zhaohansk/article/details/50505636
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

site = "https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?period1=0&period2=1549258857&interval=1d&events=history&=hP2rOschxO0"
response = requests.get(site)

data = json.loads(response.text)
df = pd.DataFrame(data['chart']['result'][0]['indicators']['quote'][0], index=pd.to_datetime(np.array(data['chart']['result'][0]['timestamp'])*1000*1000*1000))

print(df.head())

df.close.plot()
plt.show()
