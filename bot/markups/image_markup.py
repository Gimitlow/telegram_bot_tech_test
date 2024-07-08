#импорт типов aiogram
from aiogram import types

class ImageButtons:

    #получить кнопки изображения
    async def get_image() -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton(text='Вернуться в меню', callback_data='get_main_menu')]
        ]

        keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards