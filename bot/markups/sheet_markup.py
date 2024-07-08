#импорт типов aiogram
from aiogram import types

class GoogleSheetButtons:

    #вернуться в меню
    async def back_to_main_menu() -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton(text='Вернуться в меню', callback_data='get_main_menu')]
        ]

        keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards