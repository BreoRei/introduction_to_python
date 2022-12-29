from requests import get
from os import getenv
from sys import exit
from datetime import datetime
from src.config import open_weather_token


def get_weather(city):
    weather_token: str = open_weather_token
    if not weather_token:
        exit("Error: no token provided")

    code_to_smile = {"Clear": "Ясно \U00002600", "Clouds": "Облачно \U00002601", "Rain": "Дождь \U00002614",
                     "Show": "Снег \U0001F328"}
    try:
        respons = get(f"https://api.openweathermap.org/data/2.5/weather?q={city}"
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
        return (f"***{real_time.strftime('%d-%m-%Y %H:%M')}***\n"
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
        return 'Проверьте название города'
