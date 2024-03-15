from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from token_1 import TOKEN
from aiogram.types.web_app_info import WebAppInfo


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_web_app(message: Message):
    await message.answer(text=f'Привет, {message.chat.username}\nТы можешь ознакомиться с личным сайтом автора по ссылке')
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(
        text='Открыть страницу cайта', web_app=WebAppInfo(url='https://egorskvor.github.io')))
    await message.answer(text='Жми кнопку', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp)
