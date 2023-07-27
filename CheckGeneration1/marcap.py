from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    resize_keyboard= True,
    keyboard=[
            [
        KeyboardButton('OKX🟢'),
        KeyboardButton('Binance(Скоро)🔶')                                     
            ],
            [
                KeyboardButton('Информация') 
            ]
        ])

btnCanal = KeyboardButton('Отмена')
btnCan = ReplyKeyboardMarkup(resize_keyboard= True).add(btnCanal)

