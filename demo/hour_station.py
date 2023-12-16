import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
# 24 hrs past
url24 = "https://www.tmd.go.th/api/Weather3Hour/weather-past-24hours-station?StationId=328201&Culture=th-TH"
page24 = requests.get(url24)
for i in range(page24.json()["totalCount"]):
    cloud_text = page24.json()["items"][i]["cloudText"]
    latest_timestamp = page24.json()["items"][i]["dateTime"]
    date_,time_ = latest_timestamp.split("T")
    print(f"{date_}  {time_}  {cloud_text}")

res = dict()
for dict1 in page24.json()["items"]:
    for list in dict1:
        try:
            res[list].append(dict1[list])
        except KeyError:
            res[list] = [dict1[list]]
 
# printing result
df24 = pd.DataFrame(res)
print(df24)