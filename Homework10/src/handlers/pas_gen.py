from aiogram.dispatcher.router import Router
from aiogram import types
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.types import ReplyKeyboardRemove

from random import choice
from string import ascii_uppercase, ascii_lowercase, digits

router = Router()


@router.message(Command(commands=["Password"]))
@router.message(Text(text="Сделать пароль"))
async def start_command(message: types.Message):
    await message.reply(text='Это генератор пароля! Задайте мне длину пароля от 6 до 40 и я придумаю его для вас!',
                        reply_markup=ReplyKeyboardRemove())

    @router.message()
    async def hard_gen_pass(message: types.Message):
        try:
            alphabet = ascii_lowercase
            alphabet += ascii_uppercase
            alphabet += digits
            password = ''
            length = int(message.text)
            if 6 <= int(length) <= 40:
                for i in range(length):
                    password += choice(alphabet)
            else:
                await message.reply('Задайте мне длину пароля от 6 до 40!')
                return

            await message.reply(f"Вот ваш пароль:")
            await message.answer(password)

        except:
            await message.reply('Задайте мне длину пароля от 6 до 40!')
