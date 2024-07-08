#импорт типов aiogram
from aiogram import types

#создание набора кнопок
class PaymentButtons:

    #кнопка с ссылкой на карты 
    async def get_payment(url: str) -> types.InlineKeyboardMarkup:
        buttons = [
            [types.InlineKeyboardButton(text='Оплатить', url=url)],
            [types.InlineKeyboardButton(text='Вернуться в меню', callback_data='get_main_menu')]
        ]

        keyboards = types.InlineKeyboardMarkup(inline_keyboard=buttons)
        return keyboards