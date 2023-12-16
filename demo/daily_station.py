import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
# 7 days past
url7 = "https://www.tmd.go.th/api/WeatherObservationDailyStation/weather-station-past7days?StationId=328201"
page7 = requests.get(url7)
print(page7.json()["items"][-1]['weatherObservationDailyStation']["note"])
res = dict()
for dict1 in page7.json()["items"]:
    for list in dict1["weatherObservationDailyStation"]:
        try:
            res[list].append(dict1["weatherObservationDailyStation"][list])
        except KeyError:
            res[list] = [dict1["weatherObservationDailyStation"][list]]
 
# printing result
df7 = pd.DataFrame(res)
print(df7)