import asyncio
import logging
import os

#импорт роутеров
from bot.handlers import main_handler, yandexmap_handler, payment_handeler, image_handler, sheet_handler

#библиотека для работы с переменными среды 
from dotenv import load_dotenv

#импортируем объекты Aiogram
from aiogram import Bot, Dispatcher

#импорт переменных среды из .env
load_dotenv()

#импорт переменных из виртуального окружения
FILELOG = os.getenv('FILELOG')
FORMAT = os.getenv('FORMAT')
DATETIME = os.getenv('DATETIME')
TOKEN = os.getenv('TOKEN')

#подлючение логгера
file_log = logging.FileHandler(FILELOG)
console_out = logging.StreamHandler()

#конфиг для логгера
logging.basicConfig(
    handlers=(file_log, console_out),
    level=logging.INFO, 
    encoding='utf-8',
    format=FORMAT,
    datefmt=DATETIME
)

#создание логгера входной точки
logging = logging.getLogger("app")

#запусск/полинг бота
async def start():
    try:
        #создаем объект Бота
        bot = Bot(token=TOKEN)
        
        #создаем объект диспетчера для подключения обрабатываем хендлеров
        dispetcher = Dispatcher()

        #подключаем роутеры
        dispetcher.include_router(main_handler.router)
        dispetcher.include_router(yandexmap_handler.router)
        dispetcher.include_router(payment_handeler.router)
        dispetcher.include_router(image_handler.router)
        dispetcher.include_router(sheet_handler.router)
        
        #запускаем
        await dispetcher.start_polling(bot)
    except Exception as e:
        logging.exception('Ошибка при старте бота.')

#точка входа 
if __name__ == '__main__':
    asyncio.run(start())
