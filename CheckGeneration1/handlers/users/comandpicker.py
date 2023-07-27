from aiogram.types import ContentType, Message
from aiogram import  types
from keyboard.inline.mk_buttons import kb_menu, btnCan, log
from keyboard.inline.mk_inline import menu_inline
from loader import dp, bot
from db import DBase


db = DBase('data.db')


@dp.message_handler(commands=['start']) 
async def start(message: types.Message):
                  with open('baner.png', 'rb') as pho:
                    if (db.user_check_reg(user_id = message.from_user.id)):
                        await bot.send_message(chat_id= message.from_user.id, text=f"📖*Привет* {message.from_user.full_name}, *вы уже прошли тест, присоеденяйтесь в наш закрытый канал*", parse_mode="Markdown", reply_markup = menu_inline )
                        await bot.send_message(chat_id= message.from_user.id, text=f"*Присоединяйся !*", parse_mode="Markdown", reply_markup = log )
                    else: 
                       await bot.send_photo(chat_id= message.from_user.id, photo= pho, caption= f"*Приветствую  {message.from_user.first_name}*\n\n*Мы - команда лучших трейдеров, аналитиков, юристов, которые обучат арбитражу криптoвaлют каждого кто желает поднять свой месячный доход. Наша команда открыла программу обучения:*\n\n 💵 Большая рыночная компетенция\n 💵 Техническая поддержка 24/7\n 💵 Индиидуальный подход к обучению\n 💵 Удобный и простой инструментарий\n 💵 Безопасные операции без доступа к вашим счетам\n\n 🤩*Ознакомься, что бы понимать чему обучает наши профессионалы:*\n\n ✅ Что такое крипта и почему она так популярна\n ✅ Как выйти на реальный доход уже после просмотра урока\n ✅ Что такое арбитраж и как на нем делают деньги\n ✅ Актуальные связки на данный момент" , parse_mode="Markdown",reply_markup = kb_menu )
                       if not(db.user_check(message.from_user.id)):
                         db.add_user(user_id= message.from_user.id)