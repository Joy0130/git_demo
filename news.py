import requests
import pandas as pd
import datetime as dt
import json
data = []
url = "https://api.cnyes.com/media/api/v1/newslist/category/headline"
payload = {
    "page":1,
    "itCategoryHeadline":1,
    "limit":30,
    "startAt":int((dt.datetime.today()- dt.timedelta(days=11)).timestamp()),
    "endAt":int(dt.datetime.today().timestamp())
}
res = requests.get(url,params = payload)
jd = json.loads(res.text)
data.append(pd.DataFrame(jd['items']['data']))

for i in range(2,jd['items']['last_page'] +1):
    print("i = ", i)
    payload['page'] = i
    res = requests.get(url,params = payload)
    jd = json.loads(res.text)
    data.append(pd.DataFrame(jd['items']['data']))

df = pd.DataFrame(jd['items']['data'])
df = df[['newsId','title','summary']]
df['link'] = df['newsId'].apply(lambda x: 'https://m.cnyes.com/news/id/' + str(x))
df.to_csv('news.csv', encoding = 'utf-8-sig',index = False)
df.to_excel('news.xlsx',index = False)
print(df)
