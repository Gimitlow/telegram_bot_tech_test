import logging
import os
import pandas

#импортируем метод для работы с гугл таблицами
from googleapiclient.discovery import build

#импортируем роутер и фильтр хендлеров из основной библиотеки 
from aiogram import Router, F, types

#иморт кнопок
from bot.markups.sheet_markup import GoogleSheetButtons

#библиотека для работы с виртуальным окружением
from dotenv import load_dotenv

GOOGLE_SHEET_KEY = os.getenv('GOOGLE_SHEET_KEY')
SHEET_ID = os.getenv('SHEET_ID')

#создание роутера(маршрута)
router = Router()

#подключение логгера
logging = logging.getLogger('app:bot:handlers:google_sheet')

class GoogleSheetsHandler:

    #получаем значение из гугл таблицы
    @router.callback_query(F.data == 'get_google_sheets')
    async def get_A2_from_table(callback: types.CallbackQuery) -> None:
        #определяем переменную результата по умолчанию
        value = None

        #удаляем предидущее сообщение
        await callback.message.delete()
        
        #формируем ссылку на получение доступа к таблице
        url = f'https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values?key={GOOGLE_SHEET_KEY}'

        #запрос к гугл таблицам
        try:
            service = build('sheets', 'v4', developerKey=GOOGLE_SHEET_KEY)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SHEET_ID, range='Лист1!A2').execute()
            value = result.get('values', [])[0][0]
        except Exception as e:
            logging.info(f'Ошибка при обращении к гугл таблице. {e}')
        
        #проверяем результат выполнения
        if value is not None:
            text=f'Ячейка А2 в таблице равно - {value}'    
        else:
            text=f'Пусто! В ячейке А2 в таблице'       

        #отвечаем с результатом
        await callback.message.answer(
            text=text,
            reply_markup=await GoogleSheetButtons.back_to_main_menu()
        )  

