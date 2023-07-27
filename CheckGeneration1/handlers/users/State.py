from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ContentType, Message
from aiogram import  types
from keyboard.inline.mk_buttons import kb_menu, Canale, Que1, Que2, Que3, Hot, log
from keyboard.inline.mk_inline import menu_inline
from loader import dp, bot
from db import DBase

db = DBase('data.db')

temp = 0
class UseState(StatesGroup):
    Exp = State()
    money= State()
    timer = State()
    simple_time = State()

class Sender(StatesGroup):
    mess = State()

admins_id = []

@dp.message_handler(text = 'О нас📃')
async def qestion(message: types.Message): 
    if message.chat.type == 'private':
        with open('info.jpg', 'rb') as pho2:
                    if(db.user_check_reg(user_id=message.from_user.id)):
                       await bot.send_photo(chat_id= message.from_user.id,photo = pho2,caption=  f"📈Мы команда *P2P Army* - профессиональные криптоарбитражисты, специализирующиеся на высокоэффективной торговле и получении прибыли на финансовых рынках криптовалют.\n\nНаша основная цель извлечение выгоды из различий в ценах на криптовалюты на различных биржах.\n\nМы постоянно мониторим и анализируем рынки, ищем возможности для криптоарбитража и предсказываем изменения цен.\n\nКомплексный подход и использование передовых алгоритмов и технологий позволяют нам обнаруживать и реагировать на арбитражные возможности мгновенно, максимизируя прибыль и минимизируя риски.", reply_markup= menu_inline, parse_mode="Markdown")
                    else: 
                      await bot.send_photo(chat_id= message.from_user.id, photo = pho2 ,caption = f"📈Мы команда *P2P Army* - профессиональные криптоарбитражисты, специализирующиеся на высокоэффективной торговле и получении прибыли на финансовых рынках криптовалют.\n\nНаша основная цель извлечение выгоды из различий в ценах на криптовалюты на различных биржах.\n\nМы постоянно мониторим и анализируем рынки, ищем возможности для криптоарбитража и предсказываем изменения цен.\n\nКомплексный подход и использование передовых алгоритмов и технологий позволяют нам обнаруживать и реагировать на арбитражные возможности мгновенно, максимизируя прибыль и минимизируя риски.", reply_markup=kb_menu, parse_mode="Markdown")

#_____________Команды админв_____________#
@dp.message_handler(commands=['send'])
async def start(message: types.Message):
   
     if (message.from_user.id == 590129749 or 5896606791 or 5868342933):   #Тут надо прописать твой админ ID АДМИН ПАНЕЛЬ
        try:
            usersApp = message.text.split()
            userSend_id = usersApp[1]
            userSend_Text = (' '.join(usersApp[2:]))
            await bot.send_message(chat_id=userSend_id, text = str(userSend_Text))
        except:
            await bot.send_message(chat_id= -915803832, text = str("Не корректный ID, или ввод данных"))#chat_id ID в какой чат будт приходить реги и сообщения
                          

#Написать
@dp.message_handler(text = 'Написать✍️')
async def qestion(message: types.Message): 
    if message.chat.type == 'private': 
        if db.user_check_reg(message.from_user.id):     
                        await bot.send_message(chat_id=message.chat.id , text = str("*Пишите*"), reply_markup = Canale, parse_mode="Markdown")
                        await Sender.mess.set()
        else:
                        await bot.send_message(chat_id=message.chat.id , text = str("*Вы не прошли тест, пройдите его 😊*"), reply_markup = kb_menu, parse_mode="Markdown")

@dp.message_handler(state=Sender.mess)
async def send_sup(message: types.Message, state : FSMContext):
      if(message.text =="Отмена❌"):
        await bot.send_message(chat_id= message.chat.id , text= str("Отменено"), reply_markup = log)
        await state.finish()
        return 
      else:
        await bot.send_message(chat_id=message.chat.id , text = str(f"😊*Сообщение отправлино, ожидайте ответа, скоро вам напишет наш специалист*"),  reply_markup= log, parse_mode="Markdown")
        await bot.send_message(chat_id= -915803832, text= str(f"USERNAMe-> @{message.from_user.username}\nUSERID-> {message.from_user.id}\nMESTXT-> {message.text}"))
        await state.finish()
#----------------------------------------#

@dp.message_handler(text = 'Пройти тест📝')
async def qestion(message: types.Message): 
    if message.chat.type == 'private': 
                    if not(db.user_check_reg(user_id = message.from_user.id)):
                      await bot.send_message(chat_id= message.from_user.id, text = str("👩‍🏫👨‍🏫 *Ответьте пожалуйста на несколько вопросов, что-бы наш менеджер подобрал для вас наилучшее предложение*"), reply_markup= Hot, parse_mode="Markdown" )
                    else:
                      await bot.send_message(chat_id= message.from_user.id, text = str("🤓 *Вы уже прошли тест, присоеденяйтесть к нашей группе*"), parse_mode="Markdown", reply_markup = menu_inline )

@dp.message_handler(text = '🔥Начать🔥')
async def qestion(message: types.Message): 
    if message.chat.type == 'private': 
                if not(db.user_check_reg(user_id = message.from_user.id)):
                    await bot.send_message(chat_id= message.from_user.id, text = str("🤓 *У вас есть опыт в Арбитраже криптовалют ?*"), parse_mode="Markdown", reply_markup = Que1 )
                    await UseState.Exp.set()
                else:
                       await bot.send_message(chat_id= message.from_user.id, text = str("🤓 *Вы уже прошли тест, присоеденяйтесть к нашей группе*"), parse_mode="Markdown", reply_markup = menu_inline )


@dp.message_handler(state=UseState.Exp)
async def trap_state(message: types.Message, state : FSMContext):
        if(message.text ==  "Отмена"):
                await bot.send_message(chat_id= message.from_user.id, text= str("Отменено"), reply_markup= kb_menu)
                await state.finish()
                return
        elif(message.text == str('Есть опыт📗') or message.text == str('Готов обучаться📒')):
                await state.update_data(Exp = message.text)       
                await bot.send_message(chat_id= message.from_user.id, text = str("🤑 *Сколько денег вы хотите зарабатывать в день* ?"), parse_mode="Markdown", reply_markup= Que2)
                await UseState.next()
        else:
               await bot.send_message(chat_id= message.from_user.id, text = str("Некорректные данные"))

        

@dp.message_handler(state=UseState.money)
async def trap_state(message: types.Message, state : FSMContext):
        if(message.text ==  "Отмена"):
                await bot.send_message( chat_id= message.from_user.id,text= str("Отменено"),reply_markup= kb_menu)
                await state.finish()
                return
        elif(message.text == str('150$ 💰') or message.text == str('500$ 💰') or message.text == str('1000$ 💰')):
                await state.update_data(money = message.text)       
                await bot.send_message(chat_id= message.from_user.id, text = str("👩‍🎓🧑‍🎓 *Сколько времени вы готовы уделять на обучение ?*"), reply_markup= Que3, parse_mode="Markdown")
                await UseState.next()
        else:
               await bot.send_message(chat_id= message.from_user.id, text = str("Некорректные данные"))

@dp.message_handler(state=UseState.timer)
async def trap_state(message: types.Message, state : FSMContext):
        if(message.text ==  "Отмена"):
                await bot.send_message(chat_id= message.from_user.id,text= str("Отменено"), reply_markup= kb_menu)
                await state.finish()
                return
        elif(message.text == str('🕐 1-2 часа') or message.text == str('🕐 3-4часа')):
                await state.update_data(simple_time = message.text)   
                res = message.text.split(":")
                data = await state.get_data()
                _Exp = data['Exp']
                _Money = data['money']
                _Timer = data['simple_time']
                db.add_reg_user(active= 1, user_id= message.from_user.id)
                        # db.add_reg_user(data['username'],data['numbers'], message.from_user.id)
                with open('logoEnd.jpg', 'rb') as pho:
                  await bot.send_photo( chat_id= message.from_user.id, photo = pho, caption = str("👨‍💻👩‍💼*Спасибо за оставленую заявку, наш менеджер свяжеться с вами, на протяжении дня, ожидайте сообщение или звонок* ✅\n😈 Наше закрытое комюнити:"), reply_markup= menu_inline, parse_mode="Markdown")    
                await bot.send_message(chat_id= message.from_user.id, text=f"*присоединяйся !*", parse_mode="Markdown", reply_markup = log )
                await bot.send_message(chat_id=-915803832, text = str(f"Новая регистрация\nUSERID-> {message.from_user.id}\nUSERNAME-> @{message.from_user.username}\nОпыт-> {data['Exp']}\nДеньги-> {data['money']}\nВремя->{data['simple_time']}"))
                await state.finish()
        else:
               await bot.send_message( chat_id= message.from_user.id,text = str("Некорректные данные"))
def isFloat(value):
        try:
                float(value)
                return True
        except ValueError:
                return False
          
        