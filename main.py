from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from token_1 import TOKEN


bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

author_name = 'Егор'


@dp.message_handler(commands=['start'])
async def hello_func(message: Message):
    print(message.message_id, message.text)
    await message.answer(text=f'Привет, {message.chat.username}\nТы можешь ознакомиться с личным сайтом {author_name}а по ссылке')

executor.start_polling(dispatcher=dp)
