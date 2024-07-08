import logging

#импортируем роутер и фильтр хендлеров из основной библиотеки 
from aiogram import Router, F, types

#иморт кнопок
from bot.markups.payment_markup import PaymentButtons

#импорт платежной системы
from bot.integrations.yomoney_payment import YooMoneyIntegration

#создание роутера(маршрута)
router = Router()

#подключение логгера
logging = logging.getLogger('app:bot:handlers:payment')

class PaymentHandler:

    #вывод кнопок оплаты
    @router.callback_query(F.data == 'get_payment')
    async def get_payment(callback: types.CallbackQuery) -> None:
        #удаляем предидущее сообщение
        await callback.message.delete()
        
        #формирование ссылки на оплату с Yomoney
        payment = await YooMoneyIntegration.get_order()

        #отвечаем вмесете с сылкой
        await callback.message.answer(
            text=f'Прошу вас оплатить сумму в {payment[1]} рубля',
            reply_markup=await PaymentButtons.get_payment(payment[0])
        )