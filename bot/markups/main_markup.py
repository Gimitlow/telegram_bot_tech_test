#импорт типов aiogram
from aiogram import types

#создание набора кнопок
class MainMenuButtons:
    #создание кнопок меню
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