#импорт типов aiogram
from aiogram import types

#создание набора кнопок
class YandexMapButtons:

    #кнопка с ссылкой на карты 
    async def get_yandex_map_point() -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton(text='Посмотреть', url='https://yandex.ru/maps/-/CDG7IMJl')],
            [types.InlineKeyboardButton(text='Вернуться в меню', callback_data='get_main_menu')]
        ]

        keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards