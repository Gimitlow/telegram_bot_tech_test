import asyncio
import logging
import os

#импортируем роутер и фильтр хендлеров из основной библиотеки 
from aiogram import Router, F, types

#импортируем фильтр состояний
from aiogram.filters import StateFilter
#импорт контекст состояния
from aiogram.fsm.context import FSMContext
#импортируем модель состояния контекста
from bot.states.states import DataFromUser

#иморт кнопок
from bot.markups.input_date_markup import InputDateMarkup

#импорт интеграции 
from bot.integrations.googlesheets import GoogleSheetsIntegration


#создание роутера(маршрута)
router = Router()

#подключение логгера
logging = logging.getLogger('app:bot:handlers:input_date')

class InputDateHandler:

    #выставляем стейт фильтр для обработки состояния, обзначая тем самым, что далее вводимые пользователем данные
    #нужно будет запомнить
    @router.callback_query(StateFilter(None), F.data == 'get_date')
    async def get_date(callback: types.Message, state: FSMContext) -> None:
        #удаляем предыдущуе сообщение
        await callback.message.delete()

        #просим ввести пользователя дату
        await callback.message.answer(
            text='Введите дату в формате день.месяц.год',
            reply_markup=await InputDateMarkup.back_to_main_menu()
        )

        #слушаем ввод пользователя
        await state.set_state(DataFromUser.date)

    #отлавливаем ввод пользователя с клавиатуры
    @router.message(DataFromUser.date, F.text)
    async def push_in_google_sheet(message: types.Message, state: FSMContext) -> None:
        #резервируем переменную под результат
        result = None
        
        #получаем ввод пользователя
        await state.update_data(date=message.text)
        
        #вытаскиваем массив переменных из объекта состояний state
        data = await state.get_data()

        #очищаем объект состояния
        await state.clear()

        #удаляем сообщения через генератор, чтобы не мазолили глаза
        [await message.bot.delete_message(chat_id= message.chat.id, message_id = message.message_id - i) for i in range(2)]

        #проверка на соответствие даты и добавление в таблицу
        result = await GoogleSheetsIntegration.input_in_B(data['date'])

        #возвращаем ответ 
        info = await message.answer(
            text=result[1]
        )

        await asyncio.sleep(3)
        await info.delete()

        await message.answer(
            text='Выберете действие',
            reply_markup= await InputDateMarkup.main_menu_markup()
        )