import os
import logging
import json

#импорт модуля для работы с датой
from datetime import datetime

#импортируем метод для работы с гугл таблицами
from googleapiclient.discovery import build

#библиотека для авторизации с гугл Auth
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials

#библиотека для работы с виртуальным окружением
from dotenv import load_dotenv

#получаем путь текущей папки
current_dir = os.path.dirname(os.path.abspath(__file__))

#импортируем переменные виртуальной среды
SERVICE_ACCOUNT_FILE = os.path.join(current_dir, '..', '..', os.getenv('GOOGLE_JSON_NAME')) 
SHEET_ID = os.getenv('SHEET_ID')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#формируем запрос на доступ к таблице
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4',credentials=credentials)

#подключение логгера
logging = logging.getLogger('app:bot:integrations:google_sheets')

class GoogleSheetsIntegration:

    #метод работы с гугл таблицей
    async def get_A2() -> None:
        #резурвируем переменную под результат
        value = None

        #запрос к гугл таблицам
        try:
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
    
    #функция для добавление значений даты в гугл таблицу
    async def input_in_B(date: str) -> bool:
        #запрос к таблице
        try:
            #проверяем соотвествие дате
            datetime.strptime(date, '%d.%m.%Y')

            sheet = service.spreadsheets()

            #запрашиваем необходимый диапазон в листе
            result = sheet.values().get(spreadsheetId=SHEET_ID, range='Лист1!B:B').execute()
            #получаем значения
            values = result.get('values', [])

            # Находим первую пустую ячейку
            empty_row = len(values) + 1

            # Отправляем данные в первую пустую ячейку столбца B
            update_result = service.spreadsheets().values().update(
                spreadsheetId=SHEET_ID, 
                range=f'Лист1!B{empty_row}', 
                valueInputOption='USER_ENTERED', 
                body={'values': [[date]]}
            ).execute()

            return True, f'Дата {date} была добавлена в exel таблицу.'
        except ValueError as e:
            return False, f'Неправильно введена дата {date}. Попробуйте еще раз, пример - 10.01.2024'