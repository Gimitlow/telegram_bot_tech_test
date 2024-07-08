import logging

#импортируем роутер и фильтр хендлеров из основной библиотеки 
from aiogram import Router, F, types
#импорт фильтра по командам
from aiogram.filters import Command

#иморт кнопок
from bot.markups.main_markup import MainMenuButtons

#создание роутера(маршрута)
router = Router()

#подключение логгера
logging = logging.getLogger('app:bot:handlers:main_handler')

class MainMenuHandler:
    
    #функция старта
    @router.message(Command('start'))
    async def start(message: types.Message):

        #вывод меню        
        await message.answer(
            text='Выберете действие',
            reply_markup=await MainMenuButtons.main_menu_markup()
        )
    
    #обработка возврата в главное меню
    @router.callback_query(F.data == 'get_main_menu')
    async def start(callback: types.CallbackQuery):
        #удаляем предидущее сообщение
        await callback.message.delete()

        #вывод меню        
        await callback.message.answer(
            text='Выберете действие',
            reply_markup=await MainMenuButtons.main_menu_markup()
        )  
