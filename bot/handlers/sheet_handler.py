import logging
import os

#импортируем роутер и фильтр хендлеров из основной библиотеки 
from aiogram import Router, F, types

#иморт кнопок
from bot.markups.sheet_markup import GoogleSheetButtons

#создание роутера(маршрута)
router = Router()

#подключение логгера
logging = logging.getLogger('app:bot:handlers:google_sheet')

#импорт интеграции 
from bot.integrations.googlesheets import GoogleSheetsIntegration

class GoogleSheetsHandler:

    #получаем значение из гугл таблицы
    @router.callback_query(F.data == 'get_google_sheets')
    async def get_A2_from_table(callback: types.CallbackQuery) -> None:
        #удаляем предыдущуе сообщение
        await callback.message.delete()
        
        #получаем результат работы с таблицей
        result = await GoogleSheetsIntegration.get_A2()   

        #отвечаем с результатом
        await callback.message.answer(
            text=result,
            reply_markup=await GoogleSheetButtons.back_to_main_menu()
        )  

