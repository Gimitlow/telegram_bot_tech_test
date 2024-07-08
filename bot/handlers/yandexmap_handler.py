import logging

#импортируем роутер и фильтр хендлеров из основной библиотеки 
from aiogram import Router, F, types

#иморт кнопок
from bot.markups.yandexmap_markup import YandexMapButtons

#создание роутера(маршрута)
router = Router()

#подключение логгера
logging = logging.getLogger('app:bot:handlers:yandex_map')

class YandexMapHandler:

    #Получить ссылку на яндекс карты
    @router.callback_query(F.data == 'get_map_point')
    async def get_yandex_map_point(callback: types.CallbackQuery) -> None:
        await callback.message.delete()

        await callback.message.answer(text='Ваша точка на карте по ссылке.', reply_markup=await YandexMapButtons.get_yandex_map_point())