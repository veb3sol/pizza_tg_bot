import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token = "6604741800:AAHCbDi09tHUPhZzb3ogt7XKrzSaraugR8E")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')

# эхо бот
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())