import os
import pybitflyer
import requests

#環境変数取得
api_key = os.environ["api_key"]
api_secret = os.environ["api_secret"]


api = pybitflyer.API(api_key="api_key", api_secret="api_secret")

data = api.getcollateral();


# bitflyer で取得
res = requests.get('https://api.bitflyer.jp/v1/ticker?product_code=FX_BTC_JPY')
jsonData = res.json()

price = "¥{:,.0f}".format(jsonData["ltp"])
profit = price - 1060000

if profit > 0:
    hoge = "セーフ"
else:
    hoge = "死亡"
