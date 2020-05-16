import pybitflyer
#環境変数取得
api_key = os.environ["api_key"]
api_secret = os.environ["api_secret"]


api = pybitflyer.API(api_key="api_key", api_secret="api_secret")

data = api.getcollateral();


import requests

# bitflyer で取得
res = requests.get('https://api.bitflyer.jp/v1/ticker?product_code=FX_BTC_JPY')
jsonData = res.json()

price = "¥{:,.0f}".format(jsonData["ltp"])
profit = str(data['open_position_pnl'])
sign = (data['open_position_pnl'])

judge = ()
if sign < -20000 :
    judge = ("神は死んだ。南無＼(゜ロ＼)ココハドコ? (／ロ゜)／アタシハダアレ?")
elif sign < -5000:
    judge = ("ヤッベーぜ。(´；ω；`)ｳｯ…")
elif sign > 1000:
    judge = ("ヨッシー。ピッカチュウ(#^.^#)")
else:
    judge = ("何とも言えない")

print('トレード状況:' + judge)
print('預入証拠金：' + str(data['collateral']))
print('純資産総額：' + str(data['collateral'] + data['open_position_pnl']))
ijiritu = str(data['keep_rate'] * 100) +"％"
