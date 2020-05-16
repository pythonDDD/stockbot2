

import requests



# bitflyer で取得
res = requests.get('https://api.bitflyer.jp/v1/ticker?product_code=FX_BTC_JPY')
jsonData = res.json()

price = "¥{:,.0f}".format(jsonData["ltp"])
