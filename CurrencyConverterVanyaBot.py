import telebot
from config import keys,TOKEN
from  Exeption import ConversionExeption, CryptoConverter


bot = telebot.TeleBot(TOKEN)





@bot.message_handler(commands=['start'])
def start(message:telebot.types.Message):
    text = 'Привет, я бот который конвертирует валюты \n' \
           'Команды : \n'\
           '/values \n'\
           '/help \n'
    bot.reply_to(message,text)


@bot.message_handler(commands=['help','start'])
def help(message:telebot.types.Message):
    text = 'Что бы начать работу , введите следующее : \n' \
           '< Название валюты >  \n' \
           '< В какую валюту перевести >\n' \
           '< Kоличество переводимой валюты >\n' \
           '< Например: USD BYN 1 >\n' \
           '<Доступные валюты > : /values'
    bot.reply_to(message,text)


@bot.message_handler(commands=['values'])
def values(message:telebot.types.Message):
    dict_new = list(keys.values())
    for i in dict_new:
        bot.reply_to(message,i)




@bot.message_handler(content_types=['text', ])
def convert(message:telebot.types.Message):
    try:
        bot.reply_to(message, text='Конвертирую')
        values = message.text.split(' ')
        quote, base, amount = values



        if len(values) != 3:
            raise ConversionExeption('Слишком много параметров.')

        total_base = CryptoConverter.convert(quote, base, amount)
    except ConversionExeption as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')

    except Exception as e:
        bot.reply_to(message,text=f'Не удалось обработать команду. \n{e}')
    else:



        total_base_fl = float(total_base)
        amount_fl = float(amount)

        text = f'Цена  {amount} {quote} в {base} - {total_base_fl * amount_fl}'
        text_2 = f' Курс {quote} в {base} - {total_base} '
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id,text_2)




bot.polling()

