

from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='тут токен', parse_mode='html') 

faker = Faker() 


card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)

card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)




@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    
    bot.send_message(
        chat_id=message.chat.id, 
        text='Здравствуй! Я могу генерировать номера тестовых карт :)\nВыбери тип карты:',
        reply_markup=card_type_keybaord,
    )


@bot.message_handler()
def message_handler(message: types.Message):
   
    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'

    else:

        bot.send_message(
            chat_id=message.chat.id,
            text='Даже не знаю, что тебе сказать...',
            sti = open( 'sticker2.webp', 'rb')
            bot.send_sticker(message, chat.id, sti)
        )
        return

  
    card_number = faker.credit_card_number(card_type)
 
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\n<code>{card_number}</code>'
    )



def main():
  
    bot.infinity_polling()


if __name__ == '__main__':
    main()
