import telebot

API_TOKEN = '7934037089:AAFubH4ZnLRnJMAsY4UH1H5_EI0qFmRJSmw'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    full_name = message.from_user.full_name

    bot.reply_to(message, f'🤖: Assalomu aleykum {full_name}, men tarjimon robotiman!\n'
                          f'sizga qanday yordam beroliyman?')


@bot.message_handler(commands=['help'])
def send_help(message):
    # text = message
    # print(text)
    bot.reply_to(message, '🤖: Yordam menusi')


@bot.message_handler()
def echo_message(message):
    text = message.text

    try:
        calc = eval(text)
        natija = f"<b>{text} = {calc}</b>"
        bot.reply_to(message, natija)

    except NameError:
        bot.reply_to(message, 'xisoblash amalga oshirilmadi!')

bot.infinity_polling()