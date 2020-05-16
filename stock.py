import wikipedia
wikipedia.set_lang("ja")
import dataakito as akito
import btcfx
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

    if word == "株価":
        text = "現在の時価総額は、"  + str(int(akito.marketprice)) + "ドルです。" + "評価損益は、" + str(int(akito.profit)) + "ドルです。" + str(akito.par) + "%"

    elif word == "btc":
        text = "bitFlyerFX価格:" + str(int(btcfx.price)) + "評価損益：" + btcfx.profit + '証拠金維持率：' + btcfx.ijiritu
    else:
        text = wikipedia.page(word).summary





    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text))






if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
