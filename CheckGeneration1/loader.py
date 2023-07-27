from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import config
import logging

storage = MemoryStorage()

bot = Bot(token= config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage = storage)
logging.basicConfig(level=logging.INFO)