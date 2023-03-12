#!usr/bin/env python3
import telebot
import openai

# Установить API-ключ OpenAI
openai.api_key = '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'

# Установить модель OpenAI и параметры генерации
engine = "text-davinci-003"
max_tokens = 4000
temperature = 0.7

# Установить TOKEN telegram
bot = telebot.TeleBot('6128004369:AAFfEhtaD9Cwl749ZIrGtBJBRgj7RRlzx1k')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет я ИИ задай мне любой вопрос.")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    # print(message)
    # Сгенерировать ответ с помощью OpenAI API
    response = openai.Completion.create(
        engine=engine,
        prompt=message.text,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    bot.send_message(message.from_user.id, response.choices[0].text)


def main():
    # bot.polling(none_stop=True, interval=0)
    bot.infinity_polling()


if __name__ == '__main__':
    main()
