from asyncio import run
from config import tg_bot_token
from src.handlers import weather, pas_gen
from src.keyboards.simple_row import make_row_keyboard

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Bot, types, Dispatcher
from aiogram.filters.command import Command
from aiogram.filters.text import Text

bot_token: str = tg_bot_token
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
db = Dispatcher()


async def main():
    db.include_router(weather.router)
    db.include_router(pas_gen.router)
    await db.start_polling(bot, allowed_updates=db.resolve_used_update_types())


@db.message(Command(commands="start"))
@db.message(Text(text="старт", ignore_case=True))
async def cmd_start(message: types.Message):
    menu = ["Погода", "Сделать пароль"]
    await message.answer(text="Приветствую, я бот.\nВот что я умею!",
                         reply_markup=make_row_keyboard(menu))


@db.message(Command(commands=["cancel"]))
@db.message(Text(text=("отмена", "стоп"), ignore_case=True))
async def cmd_cancel(message: Message):
    await message.answer(text="Действие отменено",
                         reply_markup=ReplyKeyboardRemove())


if __name__ == "__main__":
    print("Start")
    run(main())
