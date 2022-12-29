from aiogram import types
from aiogram.dispatcher.router import Router
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.types import ReplyKeyboardRemove

from src.parsing.openweathermap import get_weather

router = Router()


@router.message(Command(commands=["whether"]))
@router.message(Text(text="Погода"))
async def start_command(message: types.Message):
    await message.reply(text='Приветствую, я погодный Бот!\nНапиши мне название города и я пришлю информацию о погоде!',
                        reply_markup=ReplyKeyboardRemove())

    @router.message()
    async def weather(message: types.Message):
        await message.reply(get_weather(message.text))
