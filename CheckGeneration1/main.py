# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from PIL import Image, ImageFilter, ImageDraw, ImageFont
# from aiogram.types import ContentType, Message
# import logging
# import os
# import marcap as mar
# from Font.MyFont import myFonts

# storage = MemoryStorage()

# class UseState(StatesGroup):
#     Tokens = State()
#     procent= State()
#     buy_sell = State()
#     pleche = State()
#     price_open = State()
#     price_close = State()


# logging.basicConfig(level=logging.INFO)

# bot = Bot(token='5799476422:AAFyDnD-x4ay-dLORPPHymGooPzUv-UHWT4')
# dp = Dispatcher(bot, storage = storage)

# @dp.message_handler(commands=['start']) 
# async def start(message: types.Message):
#         if(message.chat.type == 'private'):
#               with open('photo_2023-06-07_19-15-13.jpg', 'rb') as pho:
#                 await bot.send_photo(chat_id= message.from_user.id, photo= pho, caption=f'*👁‍🗨Привет, {message.from_user.first_name}, давай начнем делать чеки ?*\n\n⚠️Бот предназначен только для использования в личных целях, чеки создаються для розыгрышей, разроботчик не несет никакой ответственности, за ваши действия, новостной канал -', parse_mode="Markdown",reply_markup= mar.kb_menu)

# @dp.message_handler()
# async def qestion(message: types.Message): 
#     if message.chat.type == 'private': 
#          if(message.text == 'OKL🟢'):
#                     await bot.send_message(chat_id=message.chat.id , text = str("Введите название токена->"), reply_markup= mar.btnCanal)
#                     await UseState.Tokens.set()


# @dp.message_handler(state=UseState.Tokens)
# async def trap_state(message: types.Message, state : FSMContext):
#         if(message.text ==  "Отмена"):
#                 await bot.send_message(chat_id= message.chat.id , text= str("Отменено"), reply_markup= mar.kb_menu)
#                 await state.finish()
#                 return
#         else: 
#                 await state.update_data(Tokens = message.text)       
#                 await bot.send_message(chat_id=message.chat.id , text = str("Процент"))
#                 await UseState.next()

# @dp.message_handler(state=UseState.procent)
# async def trap_state(message: types.Message, state : FSMContext):
#         if(message.text ==  "Отмена"):
#                 await bot.send_message(chat_id= message.chat.id , text= str("Отменено"))
#                 await state.finish()
#                 return
#         else: 
#                 await state.update_data(procent = message.text)       
#                 await bot.send_message(chat_id=message.chat.id , text = str("Buy/Sell"), reply_markup= mar.btnCan)
#                 await UseState.next()

# @dp.message_handler(state=UseState.buy_sell)
# async def trap_state(message: types.Message, state : FSMContext):
#         if(message.text ==  "Отмена"):
#                 await bot.send_message(chat_id= message.chat.id , text= str("Отменено"), reply_markup= mar.kb_menu)
#                 await state.finish()
#                 return
#         elif(message.text == "Buy"):
#                 await state.update_data(buy_sell = message.text)       
#                 await bot.send_message(chat_id=message.chat.id , text = str("Плече"))
#                 await UseState.next()

#         elif(message.text == "Sell"):
#                 await state.update_data(buy_sell = message.text)       
#                 await bot.send_message(chat_id=message.chat.id , text = str("Плече"))
#                 await UseState.next()
#         else:
#                await bot.send_message(chat_id=message.chat.id , text = str("Некорректные данные"))


# @dp.message_handler(state=UseState.pleche)
# async def trap_state(message: types.Message, state : FSMContext):
#         if(message.text ==  "Отмена"):
#                 await bot.send_message(chat_id= message.chat.id , text= str("Отменено"), reply_markup= mar.kb_menu)
#                 await state.finish()
#                 return
#         else:
#                 await state.update_data(pleche = message.text)       
#                 await bot.send_message(chat_id=message.chat.id , text = str("Цена открытия"))
#                 await UseState.next()


# @dp.message_handler(state=UseState.price_open)
# async def trap_state(message: types.Message, state : FSMContext):
        
#         if(message.text ==  "Отмена"):
#                 await bot.send_message(chat_id= message.chat.id , text= str("Отменено"), reply_markup= mar.kb_menu)
#                 await state.finish()
#                 return
#         else:
#                 await state.update_data(price_open = message.text)       
#                 await bot.send_message(chat_id=message.chat.id , text = str("Цена Закрытия"))
#                 await UseState.next()


# @dp.message_handler(state=UseState.price_close)
# async def trap_state(message: types.Message, state : FSMContext):
#         await state.update_data(price_close = message.text)       
#         if(message.text ==  "Отмена"):
#                 await bot.send_message(chat_id= message.chat.id , text= str("Отменено"), reply_markup= mar.kb_menu)
#                 await state.finish()
#                 return
#         else:
#                 data = await state.get_data()
#                 _Tokens = data['Tokens']
#                 _Procent = data['procent']
#                 _buy_sell = data['buy_sell']
#                 _pleche = data['pleche']
#                 _price_open = data['price_open']
#                 _price_close = data['price_close']  
   
#                 # db.add_reg_user(data['username'],data['numbers'], message.from_user.id)
#         Create(_Procent,_Tokens,_buy_sell,_pleche,_price_open,_price_close, message.from_user.id)
#         await bot.send_photo(chat_id= message.from_user.id, photo= open(f'temp/{message.from_user.id}.jpg', 'rb')  , reply_markup= mar.kb_menu)
#         await state.finish()



# def Create(procent,Tokens, buy_sell, pleche, price_open, price_close, id ):
#      img = Image.open('photo_2023-06-07_20-20-56.jpg')
#      idraw = ImageDraw.Draw(img)
#      idraw.text((55, 333), text= '+' + procent + '%',fill=(10,196,143,255),font = myFonts.okx_medium_text)
#      idraw.text((54, 145), text= Tokens.upper() + " Perpetual",fill='white', font= myFonts.okx_TOKEN_text)
#      if(buy_sell == "Sell"):
#         idraw.text((50, 208), text= 'Sell', fill=(176, 67, 75, 1), font=myFonts.okx_buy_sell)
#      else:
#          idraw.text((50, 208), text= 'Buy', fill=((40,168,127,255)), font=myFonts.okx_buy_sell)

#      idraw.text((137, 209), text= pleche + 'X', fill=(137,137,137,255), font=myFonts.okx_buy_sell)
#      idraw.text((72, 559), text= price_open, fill='white', font=myFonts.okx_price)
#      idraw.text((257, 559), text= price_close, fill='white', font=myFonts.okx_price)
#      img.save(f'temp/{id}.jpg')




# executor.start_polling(dp, skip_updates=True)  