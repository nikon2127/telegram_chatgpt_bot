import telegram_bot


def main():
    telegram_bot.bot.polling(none_stop=True, interval=0)


if __name__ == '__main__':
    main()
