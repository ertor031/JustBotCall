from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    resize_keyboard= True,

    keyboard=[
            [
        KeyboardButton('Пройти тест📝'),
        KeyboardButton('О нас📃')                                     
            ]   
        ])

Que1 = ReplyKeyboardMarkup(
    resize_keyboard= True,

    keyboard=[
            [
        KeyboardButton('Есть опыт📗'),
        KeyboardButton('Готов обучаться📒')                                     
            ]
        ])

Que2 = ReplyKeyboardMarkup(
    resize_keyboard= True,

    keyboard=[
            [
        KeyboardButton('150$ 💰'),
        KeyboardButton('500$ 💰'),
        KeyboardButton('1000$ 💰')                                         
            ]
        ])

Que3 = ReplyKeyboardMarkup(
    resize_keyboard= True,

    keyboard=[
            [
        KeyboardButton('🕐 1-2 часа'),
        KeyboardButton('🕐 3-4часа')                                     
            ]
        ])


Canale = ReplyKeyboardMarkup(
    resize_keyboard= True,

    keyboard=[
            [
        KeyboardButton('Отмена❌')                                    
            ]
        ])


Hot = ReplyKeyboardMarkup(
    resize_keyboard= True,

    keyboard=[
            [
        KeyboardButton('🔥Начать🔥')                                    
            ]
        ])

log = ReplyKeyboardMarkup(
    resize_keyboard= True,

    keyboard=[
             [
        KeyboardButton('О нас📃'),
        KeyboardButton('Написать✍️')                           
            ]
        ])


btnCanal = KeyboardButton('Отмена')
btnCan = ReplyKeyboardMarkup(resize_keyboard= True).add(btnCanal)

