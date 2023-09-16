from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hai bosku {message.from_user.full_name}")
    await message.answer("Ada yang bisa admin bantu?")
    db.add_user(message.from_user.id, message.from_user.full_name)

