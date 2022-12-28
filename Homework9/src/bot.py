from requests import get
from datetime import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from os import getenv
from sys import exit

weather_token: str = getenv("open_weather_token")
if not weather_token:
    exit("Error: no token provided")

bot_token: str = getenv("tg_bot_token")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
db = Dispatcher(bot)


@db.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply('Приветствую, я погодный Бот!\nНапиши мне название города и я пришлю информацию о погоде!')


@db.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {"Clear": "Ясно \U00002600", "Clouds": "Облачно \U00002601", "Rain": "Дождь \U00002614",
        "Show": "Снег \U0001F328"}
    try:
        respons = get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}"
            f"&appid={weather_token}"
            f"&units=metric"
            f"&lang=ru")
        data = respons.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp
        real_time = datetime.now()
        wheather_description = data["weather"][0]["main"]
        if wheather_description in code_to_smile:
            wd = code_to_smile[wheather_description]
        else:
            wd = 'Не пойму что там за погода, посмотри в окно!'

        await message.reply(f"***{real_time.strftime('%d-%m-%Y %H:%M')}***\n"
                            f"Погода в городе: {city}\n"
                            f"Температура: {cur_weather}C {wd}\n"
                            f"Влажность: {humidity}%\n"
                            f"Давление: {pressure} мм.рт.ст\n"
                            f"Ветер: {wind} м/с\n"
                            f"Восход солнца: {sunrise_timestamp.strftime('%d-%m-%Y %H:%M')}\n"
                            f"Закат солнца: {sunset_timestamp.strftime('%d-%m-%Y %H:%M')}\n"
                            f"Продолжительность дня: {length_of_the_day}\n"
                            f"Я желаю вам хорошего дня!")
    except:
        await message.reply('Проверьте название города')


if __name__ == '__main__':
    print("Start")
    executor.start_polling(db)
