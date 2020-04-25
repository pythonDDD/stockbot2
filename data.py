import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import requests
import argparse
import numpy as np
import seaborn as sns

#スタート日を決める
number = "2019-12-4" #@param {type:"string"}

#銘柄コード
start = number
end = datetime.date.today()
code1 = "BYND" #@param ["AAPL"] {allow-input: true}
code2 = "F" #@param ["AMD"] {allow-input: true}
code3 = "^GSPC" #@param ["MSFT"] {allow-input: true}
code4 = "XRX" #@param ["FB"] {allow-input: true}
code5 = "SPXS" #@param ["JNJ"] {allow-input: true}
code6 = "IBM" #@param ["JNJ"] {allow-input: true}
code7 = "BUD" #@param ["JNJ"] {allow-input: true}
codelist = [code1,code2,code3,code4,code5,code6,code7]
#終値取得(data2に終値を取り込み))
data2 = yf.download(codelist, start=start, end=end)["Adj Close"]
#取得単価
price1 =  98.02#@param {type:"number"}
price2 =  6.24#@param {type:"number"}
price3 =  0#@param {type:"number"}
price4 = 25 #@param {type:"number"}
price5 =  16.94#@param {type:"number"}
price6 = 0 #@param {type:"number"}
price7 =  45.01#@param {type:"number"}
#保有数量
code1stock =  280#@param {type:"number"}
code2stock =  21#@param {type:"number"}
code3stock =  0#@param {type:"number"}
code4stock =  3#@param {type:"number"}
code5stock =  600#@param {type:"number"}
code6stock =  0#@param {type:"number"}
code7stock =  28#@param {type:"number"}
#取得価額。保有数量×取得単価
mypf1 = code1stock * price1
mypf2 = code2stock * price2
mypf3 = code3stock * price3
mypf4 = code4stock * price4
mypf5 = code5stock * price5
mypf6 = code6stock * price6
mypf7 = code7stock * price7
mypf = mypf1 + mypf2 + mypf3 + mypf4 + mypf5 + mypf6 + mypf7
print(mypf)
#prに時価総額を格納 終値行列×保有数量
pr1 = data2[code1] * code1stock
pr2 = data2[code2] * code2stock
pr3 = data2[code3] * code3stock
pr4 = data2[code4] * code4stock
pr5 = data2[code5] * code5stock
pr6 = data2[code6] * code6stock
pr7 = data2[code7] * code7stock
pf = pr1 + pr2 + pr3 + pr4 + pr5 + pr6 +pr7
marketprice = pf.iloc[-1]
print(marketprice)
#損益状況
profit = marketprice - mypf
print(profit)
par = round(((1 - (marketprice / mypf)) * -100), 1)
#グラフの箱サイズ
pf.plot(label = "MY Portfolio", kind = 'area', alpha = 1, figsize = (8,6), fontsize = 16, stacked=True,cmap='summer',grid = True)
#ファイル保存
plt.savefig("test0.png")


#パーセント表示変形
df_all=((1+data2.pct_change()).cumprod())
#グラフの箱サイズ
df_all.plot(figsize=(8,6),fontsize=16)
#凡例の位置
plt.legend(loc = 'upper left', bbox_to_anchor=(0, 1), borderaxespad=0, fontsize=16)
plt.grid(True)
#ファイル保存
plt.savefig("test1.png")
#plt.show()　ファイルを保存する為には、プロットしない！！超重要！！！！

#終値とパーセント表示のヘッドを抽出
print(data2.head())
print(data2.iloc[-1])
print(df_all.iloc[-1])

# 株価を標準化
std = data2.apply(lambda x: (x-x.mean())/x.std(), axis=0).fillna(0)
std.plot(figsize=(8,6),fontsize=18)
plt.legend(loc = 'upper left', bbox_to_anchor=(0, 1), borderaxespad=0, fontsize=18)
plt.grid(True)
#標準化後のヘッド抽出
print(std.head())



#データを対前日比の株価変動率に変換しstdpctに格納
stdpct = data2.pct_change().dropna() * 100
#営業日ごとの株価変動率をプロット　
stdpct.plot(label = True ,figsize = (8,6),marker = 'o',fontsize = 16)
plt.legend(loc = 'upper left', bbox_to_anchor=(0, 1), borderaxespad=0, fontsize=16)
plt.grid(True)
#ファイル保存
plt.savefig("test3.png")

#株価変動率のヘッド抽出
print(stdpct.head())


#株価変動率の基本統計量を取得　
stastics = round(stdpct.describe(),2)
print(stastics)
#統計量をグラフ化
fig, ax = plt.subplots(figsize=(8,6))
ax.axis('off')
ax.axis('tight')
ax.table(cellText=stastics.values,
         colLabels=stastics.columns,
         rowLabels=stastics.index,
         loc='center',
         bbox=[0,0,1,1])
#ファイル保存
plt.savefig("test4.png")
#ここで、重ね過ぎたfigファイルがダブって、グラフが二重になるのを防ぐため、clf()で削除。
plt.clf()



#seabornで箱ひげ図を作成　箱ひげ図は、ボックス内の線が平均値を表し、色がついたボックス内の値動きになる確率が50%であることを示しています。
#ボックスから突き出たヒゲの範囲まででほぼ100%の値動きを示していますが、髭の長さが箱の1.5倍を超えるようなデータは外れ値としてヒゲを突き抜けてプロットされています。
#ボックスが値0以上の場合、ほぼ値下がりがなく、上昇していることを意味する。
sns.boxplot(data = stdpct,fliersize = 6,width = 0.5)
sns.set_context("talk",font_scale = 1)
plt.grid(True)
#ファイル保存
plt.savefig("test5.png")
#ここで、重ね過ぎたfigファイルがダブって、グラフが二重になるのを防ぐため、clf()で削除。
plt.clf()



#ヒートマップにて相関関係を表示
stdpct1 = stdpct.dropna()
sns.set(style="white")
#三角形の上半分をマスクする
mask = np.zeros_like(stdpct1.corr(), dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

sns.heatmap(stdpct1.corr(),annot = True,mask = mask)
#ファイル保存
plt.savefig('test6.png')




#ここからはラインへ送信するコード。
#資産総額と損益状況
def lineNotify(message):
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

lineNotify("現在の時価総額は、\n" + str(marketprice) +"\n ドルです。" + "\n 評価損益は、 \n" + str(profit) + "\n ドルです。" + str(par) + "%"  )

#test0
def PythonNotify(message, *args):

    line_notify_api = 'https://notify-api.line.me/api/notify'
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    payload = {'message': message}

    if len(args) == 0:
        requests.post(line_notify_api, data=payload, headers=headers)
    else:

        files = {"imageFile": open(args[0], "rb")}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

#ファイル読み込み送信
if __name__=='__main__':
    PythonNotify("資産推移" , "test0.png")


#株価行列の最終行のみ抽出。
def lineNotify(message):
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

lineNotify("現在の株価。\n" + str([data2.iloc[-1]]) + "\n 株価は、 \n" + str(number) + "\n から、下記の倍数の状況です。\n" + str([df_all.iloc[-1]]))


#test1
def PythonNotify(message, *args):

    line_notify_api = 'https://notify-api.line.me/api/notify'
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    payload = {'message': message}

    if len(args) == 0:
        requests.post(line_notify_api, data=payload, headers=headers)
    else:

        files = {"imageFile": open(args[0], "rb")}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

#ファイル読み込み送信
if __name__=='__main__':
    PythonNotify("パーセントグラフ" , "test1.png")

#test3
def PythonNotify(message, *args):

    line_notify_api = 'https://notify-api.line.me/api/notify'
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    payload = {'message': message}

    if len(args) == 0:
        requests.post(line_notify_api, data=payload, headers=headers)
    else:

        files = {"imageFile": open(args[0], "rb")}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

#ファイル読み込み送信
if __name__=='__main__':
    PythonNotify('対前日比株価増減率',"test3.png")

#test4
def PythonNotify(message, *args):

    line_notify_api = 'https://notify-api.line.me/api/notify'
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    payload = {'message': message}

    if len(args) == 0:
        requests.post(line_notify_api, data=payload, headers=headers)
    else:

        files = {"imageFile": open(args[0], "rb")}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

#ファイル読み込み送信
if __name__=='__main__':
    PythonNotify('統計量',"test4.png")

#test5
def PythonNotify(message, *args):

    line_notify_api = 'https://notify-api.line.me/api/notify'
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    payload = {'message': message}

    if len(args) == 0:
        requests.post(line_notify_api, data=payload, headers=headers)
    else:

        files = {"imageFile": open(args[0], "rb")}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

#ファイル読み込み送信
if __name__=='__main__':
    PythonNotify('箱ひげ図',"test5.png")


#test6
def PythonNotify(message, *args):

    line_notify_api = 'https://notify-api.line.me/api/notify'
    line_notify_token = '7TSIKvVUMWFimJLZK9ERQg6Bdkk3pqNRrkGiGRqXHgJ'
    headers = {'Authorization': 'Bearer ' + line_notify_token}

    payload = {'message': message}

    if len(args) == 0:
        requests.post(line_notify_api, data=payload, headers=headers)
    else:

        files = {"imageFile": open(args[0], "rb")}
        requests.post(line_notify_api, data=payload, headers=headers, files=files)

#ファイル読み込み送信
if __name__=='__main__':
    PythonNotify('ヒートマップ',"test6.png")
