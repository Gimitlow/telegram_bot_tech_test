import os
import logging

#импортируем метод для работы с гугл таблицами
from googleapiclient.discovery import build

#библиотека для работы с виртуальным окружением
from dotenv import load_dotenv

#импортируем переменные виртуальной среды
GOOGLE_SHEET_KEY = os.getenv('GOOGLE_SHEET_KEY')
SHEET_ID = os.getenv('SHEET_ID')

#подключение логгера
logging = logging.getLogger('app:bot:integrations:google_sheets')

class GoogleSheetsIntegration:

    #метод работы с гугл таблицей
    async def get_A2() -> None:
        #резурвируем переменную под результат
        value = None

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
        
        return text