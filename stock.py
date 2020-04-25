import datamiku as miku
import dataakito as akito
from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (ImageMessage, ImageSendMessage, MessageEvent,
                            TextMessage, TextSendMessage)


app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)



@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    word = event.message.text

    if word == "みく":
        result = miku.marketprice
        profit = miku.profit
        par = miku.par
    elif word == "あきと":
        result = akito.marketprice
        profit = akito.profit
        par = akito.par
    else:
        result = "とてもスライム"
        profit = "名前を平仮名で入れないと返信しない"
        par = "俺の可能性は∞"





    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="現在の時価総額は、\n"  + str(result) + "\n ドルです。" + "\n 評価損益は、 \n" + str(profit) + "\n ドルです。" + str(par) + "%")
        )






if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
