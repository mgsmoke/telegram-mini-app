import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.token import TokenValidationError
from dotenv import load_dotenv
import asyncio

# Загружаем токен из .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Проверяем корректность токена
try:
    bot = Bot(token=TOKEN)
except TokenValidationError:
    print("Ошибка: некорректный токен! Проверь .env")
    exit()

dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url="https://mgsmoke.github.io/telegram-mini-app/"))]
        ]
    )
    await message.answer("Нажмите кнопку ниже, чтобы открыть приложение:", reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())