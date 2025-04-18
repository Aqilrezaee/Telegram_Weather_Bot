from flask import Flask, request
import telegram

TOKEN = "8177696418:AAF1p0Z4hM7RIz35FYi9qge5lHoXbmiYIWU"
bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route(f'/{TOKEN}', methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    bot.send_message(chat_id=chat_id, text="سلام! من زنده‌ام 🌟")
    return 'ok'

@app.route('/')
def index():
    return 'ربات فعال است 🟢'

if __name__ == '__main__':
    app.run(port=5000)
