import telebot


bot = telebot.TeleBot('6128004369:AAFfEhtaD9Cwl749ZIrGtBJBRgj7RRlzx1k')


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, message.text)
