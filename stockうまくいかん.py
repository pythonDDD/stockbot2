import data as dt
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
    result = dt.marketprice
    profit = dt.profit
    par = dt.par

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="現在の時価総額は、\n"  + str(result) + "\n ドルです。" + "\n 評価損益は、 \n" + str(profit) + "\n ドルです。" + str(par) + "%")
        )

@handler.add(MessageEvent, message=ImageMessage)👈魔術師様～～！！！画像ファイルが読み取れません。てゆーか、ヘロクに画像ファイルが保存されてません！！

def handle_image(event):👈魔術師様～～！！！画像ファイルが読み取れません。てゆーか、ヘロクに画像ファイルが保存されてません！！
    message_id = event.message.id👈魔術師様～～！！！画像ファイルが読み取れません。てゆーか、ヘロクに画像ファイルが保存されてません！！

    test1 = dt.test1.jpg👈魔術師様～～！！！画像ファイルが読み取れません。てゆーか、ヘロクに画像ファイルが保存されてません！！
    main_image_path = f"static/images/{message_id}_test1"👈魔術師様～～！！！画像ファイルが読み取れません。てゆーか、ヘロクに画像ファイルが保存されてません！！

    # 画像の送信👈魔術師様～～！！！画像ファイルが読み取れません。てゆーか、ヘロクに画像ファイルが保存されてません！！
    image_message = ImageSendMessage(
        original_content_url=f"https://stockbot2.herokuapp.com/{main_image_path}")

    app.logger.info(f"https://stockbot2.herokuapp.com/{main_image_path}")
    line_bot_api.reply_message(event.reply_token, image_message)
👈魔術師様～～！！！画像ファイルが読み取れません。てゆーか、ヘロクに画像ファイルが保存されてません！！






if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
