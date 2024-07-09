#импорт типов aiogram
from aiogram import types

class InputDateMarkup:

    #вернуться в меню
    async def back_to_main_menu() -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton(text='Вернуться в меню', callback_data='get_main_menu')]
        ]

        keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards
    
    #кнопки главного меню
    async def main_menu_markup() -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton(text='Яндекс карты', callback_data='get_map_point')],
            [types.InlineKeyboardButton(text='Оплатить 2р', callback_data='get_payment')],
            [types.InlineKeyboardButton(text='Получить картинку', callback_data='get_image')],
            [types.InlineKeyboardButton(text='Получить значение из Google Sheets', callback_data='get_google_sheets')],
            [types.InlineKeyboardButton(text='Валидатор даты', callback_data='get_date')]
        ]

        keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards